from fastapi import FastAPI
import json
from extract import extract_data  # extract işlemi için
from transform import transform_data  # transform işlemi için
from load import save_to_json, save_to_csv, save_to_postgresql


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


# ✅ Load işlemi için PostgreSQL bağlantı bilgileri
db_config = {
    "dbname": "etl_db",
    "user": "etl_user",
    "password": "etl_password",
    "host": "localhost",
    "port": "5432"
}

@app.get("/load")
def load_endpoint():
    """Extract edilmiş ve transform edilmiş veriyi JSON, CSV ve PostgreSQL'e kaydeder."""
    try:
        with open("transformed_data.json", "r", encoding="utf-8") as f:
            transformed_data = json.load(f)
        
        # ✅ JSON ve CSV olarak kaydetme
        save_to_json(transformed_data)
        save_to_csv(transformed_data)

        # ✅ PostgreSQL'e kaydetme
        save_to_postgresql(transformed_data, db_config)

        return {"message": "Load işlemi başarılı! Veri JSON, CSV ve PostgreSQL'e kaydedildi."}

    except FileNotFoundError:
        return {"error": "❌ 'transformed_data.json' bulunamadı. Lütfen önce /transform çalıştırın."}

    except Exception as e:
        return {"error": str(e)}


# FastAPI sunucusunu başlatmak için terminalde çalıştır:
# uvicorn main:app --reload
