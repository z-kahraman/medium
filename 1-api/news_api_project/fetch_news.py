import requests
import pandas as pd
import os
from dotenv import load_dotenv
import json
from datetime import datetime

# .env dosyasını yükle / Load environment variables from .env file
load_dotenv()

# API anahtarını al / Get API Key
API_KEY = os.getenv("NEWS_API_KEY")

# API anahtarı yoksa hata ver / Raise an error if API Key is missing
if not API_KEY:
    raise ValueError("ERROR: API anahtarı bulunamadı! Lütfen .env dosyanı kontrol et. / API key not found! Please check your .env file.")

# Günün tarih ve saat bilgisini al / Get current date and time (YYYY-MM-DD_HH-MM format)
current_time = datetime.now().strftime('%Y-%m-%d_%H-%M')

# Kaydedilecek klasör / Folder to store the data
output_folder = "data/"
os.makedirs(output_folder, exist_ok=True)  # Klasör yoksa oluştur / Create folder if it doesn't exist

# Dosya isimleri (Tarih + Saat + Dakika) / File names (Date + Hour + Minute)
output_txt_path = os.path.join(output_folder, f"news_api_response_{current_time}.txt")
output_excel_path = os.path.join(output_folder, f"news_data_{current_time}.xlsx")

# NewsAPI URL'si (En son haberleri çekiyoruz) / API URL to fetch latest news
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

# API isteğini yap / Make API request
response = requests.get(url)

if response.status_code == 200:
    # API'den gelen JSON verisini al / Get JSON data from API response
    data = response.json()

    # ✅ 1️⃣ JSON yanıtını dosyaya kaydet / Save raw JSON response to a text file
    with open(output_txt_path, "w", encoding="utf-8") as txt_file:
        json.dump(data, txt_file, indent=4, ensure_ascii=False)
    
    print(f"✅ API yanıtı '{output_txt_path}' dosyasına kaydedildi. \n✅ API response saved to '{output_txt_path}'.")

    # ✅ 2️⃣ Haberleri işle ve Excel'e kaydet / Process news data and save to Excel
    articles = data.get("articles", [])

    # DataFrame oluştur / Create DataFrame
    df = pd.DataFrame(articles)

    # Eğer hiç haber yoksa çıkış yap / Exit if no news found
    if df.empty:
        print("⚠️ API başarılı çalıştı ama haber bulunamadı! \n⚠️  API request was successful but no news found!")
        exit()

    # Gerekli sütunları seç / Select relevant columns
    df = df[["source", "author", "title", "description", "url", "publishedAt"]]

    # 'source' sütunu içindeki 'name' değerini çıkar / Extract 'name' field from 'source' column
    df["source"] = df["source"].apply(lambda x: x["name"] if isinstance(x, dict) else x)

    # ✅ 3️⃣ Excel dosyasına kaydet / Save to Excel file
    df.to_excel(output_excel_path, index=False)

    print(f"✅ Veri başarıyla '{output_excel_path}' dosyasına kaydedildi! Toplam haber sayısı: {len(df)} \n✅ Data successfully saved to '{output_excel_path}'! Total news articles: {len(df)}")

else:
    print(f"❌ API isteği başarısız! Status: {response.status_code} \n API request failed! Status: {response.status_code}")
