from fastapi import FastAPI
import json
from extract import extract_data  # extract işlemi için
from transform import transform_data  # transform işlemi için

app = FastAPI()

@app.get("/extract")
def extract_endpoint():
    """API'den veriyi çeker ve dosyaya kaydeder."""
    try:
        extracted_result = extract_data()
        extracted_data = extracted_result.get("data", [])

        if not extracted_data:
            return {"message": "Extract işlemi başarısız", "error": extracted_result.get("error")}

        with open("extracted_data.json", "w", encoding="utf-8") as f:
            json.dump(extracted_data, f, indent=4, ensure_ascii=False)

        return {"message": "Extract işlemi başarılı", "data": extracted_data}
    
    except Exception as e:
        return {"error": str(e)}

@app.get("/transform")
def transform_endpoint():
    """Extract edilmiş veriyi alır, dönüştürür ve döndürür."""
    try:
        with open("extracted_data.json", "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        
        transformed_data = transform_data(raw_data)

        with open("transformed_data.json", "w", encoding="utf-8") as f:
            json.dump(transformed_data, f, indent=4, ensure_ascii=False)

        return {"message": "Transform işlemi başarılı", "data": transformed_data}
    
    except FileNotFoundError:
        return {"error": "❌ 'extracted_data.json' bulunamadı! Önce /extract endpointini çağırın."}
    
    except Exception as e:
        return {"error": str(e)}

# FastAPI sunucusunu başlatmak için terminalde çalıştır:
# uvicorn main:app --reload
