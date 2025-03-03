import os
import logging
import time
import json
from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import ollama
import requests
from api.youtube_search import search_youtube_videos


# 📌 Ollama modellerini listeleme
def list_ollama_models():
    """Ollama içinde mevcut olan modelleri listeler."""
    try:
        models = ollama.list()
        return [model["name"] for model in models["models"]]
    except Exception as e:
        return f"❌ Ollama Model Listesi Çekilemedi: {str(e)}"


# 📌 data klasörünü oluştur (eğer yoksa)
log_directory = "data"
os.makedirs(log_directory, exist_ok=True)

# 📌 Log dosyasını `data` klasörüne kaydet
log_file_path = os.path.join(log_directory, "api_requests.log")
comments_file_path = os.path.join(log_directory, "raw_comments.json")

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

app = FastAPI()

class PromptRequest(BaseModel):
    query: str
    model: str = "llama3.2:1b"  # Varsayılan model
    language: str = "tr"  # Varsayılan dil Türkçe 🇹🇷
    region: str = "TR"    # Varsayılan bölge Türkiye 🇹🇷


def extract_product_name(query, model):
    """Extract only the product name using Ollama. If the model is not found, return available models and log the error."""
    prompt = f"Extract only the product name from the following query. Do not provide any additional information. Query: '{query}'\n\nProduct name:"
    
    try:
        response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
        product_name = response["message"]["content"].strip()

        # 📌 Log success if the request was successful
        logging.info(f"Ollama API Success | Model: {model} | Query: {query} | Extracted Product: {product_name}")
        return JSONResponse(content=json.loads(json.dumps({"product": product_name})))
        # return product_name

    except ollama.ResponseError as e:
        error_message = str(e)  # Capture error message
        
        # 📌 Check if the error message contains "not found" (indicating a missing model)
        if "not found" in error_message.lower():
            missing_model = error_message.split('"')[1] if '"' in error_message else model
            
            try:
                # Retrieve available models
                available_models = [m.model for m in ollama.list()["models"]]
                formatted_models = "\n".join([f"✅ {m}" for m in available_models])

                logging.error(f"OLLAMA Model Not Found | Requested Model: {missing_model} | Available Models: {available_models}")

                return {
                    "error": f"❌ Model '{missing_model}' not found.",
                    "message": "Please select a valid model. Available models are:",
                    "available_models": available_models,
                    "formatted_models": formatted_models
                }
            



            except Exception as model_list_error:
                logging.error(f"OLLAMA Model List Retrieval Error | Error: {str(model_list_error)}")
                return {
                    "error": f"❌ Model '{missing_model}' not found and available models could not be retrieved.",
                    "detail": str(model_list_error)
                }

        # 📌 Log general OLLAMA API errors
        logging.error(f"Ollama API Error | Model: {model} | Query: {query} | Error: {error_message}")
        return {"error": f"OLLAMA error: {error_message}"}

    except Exception as e:
        logging.error(f"Unexpected Error in extract_product_name | Query: {query} | Model: {model} | Error: {str(e)}")
        return {"error": f"An unexpected error occurred: {str(e)}"}


def classify_sentiment(text, model):
    """Ollama ile sentiment analizi yap ve yanıtı logla."""
    prompt = f"Classify the sentiment of the following text as 'positive', 'negative', or 'neutral':\n\n{text}\n\nSentiment:"
    
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    sentiment = response["message"]["content"].strip().lower()

    if sentiment not in ["positive", "negative", "neutral"]:
        sentiment = "neutral"

    # 📌 Ollama API Yanıtını Logla
    logging.info(
        f"Ollama Sentiment Analysis | Model: {model} | Text: {text[:50]}... | Sentiment: {sentiment} | Full Response: {response}"
    )

    return sentiment


def save_comments_to_json(product_name, video_id, comments):
    """Ürüne göre yorumları `data/raw_comments.json` içine kaydeder."""
    if os.path.exists(comments_file_path):
        with open(comments_file_path, "r", encoding="utf-8") as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                existing_data = {}
    else:
        existing_data = {}

    # 📌 Ürün bazında organize et
    if product_name not in existing_data:
        existing_data[product_name] = {}

    existing_data[product_name][video_id] = comments

    with open(comments_file_path, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=4)

@app.post("/analyze")
async def analyze_product(request: PromptRequest):
    request_time = datetime.utcnow().isoformat()
    start_time = time.time()
    model = request.model

    # 1️⃣ Ürün Algılama (Eğer model hatalıysa, işlemi sonlandır)
    product_result = extract_product_name(request.query, model)

    # Eğer product_result bir hata mesajı içeriyorsa, işlemi durdur
    if isinstance(product_result, dict) and "error" in product_result:
        logging.error(f"Model hatası: {product_result}")  # Log kaydı
        return product_result  # Hata mesajını API yanıtı olarak gönder

    product_name = product_result  # Model doğruysa devam et

    # 2️⃣ YouTube API ile Video Arama (Eğer video yoksa, işlemi sonlandır)
    videos = search_youtube_videos(product_name, max_results=10, language=request.language, region=request.region)

    if not videos:
        execution_time = time.time() - start_time
        log_data = {
            "timestamp": request_time,
            "model": model,
            "query": request.query,
            "product": product_name,
            "videos_found": 0,
            "execution_time": f"{execution_time:.2f}s",
            "response": {"error": "No relevant YouTube videos found."}
        }
        logging.info(log_data)
        return {"error": "No relevant YouTube videos found."}

    # 3️⃣ Yorumları JSON'a Kaydetme ve Loglama
    analyzed_comments = {}
    youtube_api_key = os.getenv("YOUTUBE_API_KEY")

    for video in videos:
        video_id = video["id"]
        comment_url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={youtube_api_key}"
        comments = requests.get(comment_url).json().get("items", [])[:10]

        video_comments = []
        for comment in comments:
            text = comment["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            sentiment = classify_sentiment(text, model)
            video_comments.append({"text": text, "sentiment": sentiment})

        # 📌 JSON'a kaydet
        save_comments_to_json(product_name, video_id, video_comments)
        analyzed_comments[video_id] = video_comments

    execution_time = time.time() - start_time

    log_data = {
        "timestamp": request_time,
        "model": model,
        "query": request.query,
        "product": product_name,
        "videos_found": len(videos),
        "comments_analyzed": sum(len(v) for v in analyzed_comments.values()),
        "execution_time": f"{execution_time:.2f}s",
    }
    logging.info(log_data)

    return {
        "product": product_name,
        "videos": [{"title": video["title"], "video_id": video["id"], "channel": video["channel"]} for video in videos],
        "analyzed_comments": analyzed_comments
    }
