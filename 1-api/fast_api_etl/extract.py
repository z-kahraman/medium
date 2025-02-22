import requests
import json

API_URL = "https://restcountries.com/v3.1/independent?status=true"

def extract_data():
    """API'den veriyi çeker ve JSON olarak döndürür."""
    try:
        response = requests.get(API_URL, timeout=10)  # Timeout ekledik
        response.raise_for_status()  # HTTP hata yönetimi ekledik

        data = response.json()
        
        with open("extracted_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        return {"message": "Extract işlemi başarılı", "data": data}  # İlk 5 ülkeyi göster

    except requests.exceptions.RequestException as e:
        return {"message": "Failed to extract data", "error": str(e)}

# Örnek test
if __name__ == "__main__":
    result = extract_data()
    print(result)
