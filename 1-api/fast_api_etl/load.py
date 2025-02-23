import json
import csv
import psycopg2
from psycopg2 import sql

# ✅ Load verisini JSON olarak kaydetme
def save_to_json(data, filename="transformed_data.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"✅ Data successfully saved to {filename}")

# ✅ Load verisini CSV olarak kaydetme
def save_to_csv(data, filename="transformed_data.csv"):
    if not data:
        print("❌ No data to save!")
        return

    keys = data[0].keys()
    with open(filename, "w", encoding="utf-8", newline="") as f:
        dict_writer = csv.DictWriter(f, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    
    print(f"✅ Data successfully saved to {filename}")

# ✅ PostgreSQL veritabanına veri yükleme
def save_to_postgresql(data, db_config):
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # Tablo oluştur (Eğer yoksa)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS country_data (
                id SERIAL PRIMARY KEY,
                name TEXT,
                official_name TEXT,
                region TEXT,
                population INTEGER,
                currencies TEXT,
                population_density FLOAT
            )
        """)

        # Veriyi ekleme
        insert_query = sql.SQL("""
            INSERT INTO country_data (name, official_name, region, population, currencies, population_density)
            VALUES (%s, %s, %s, %s, %s, %s)
        """)
        
        for country in data:
            cursor.execute(insert_query, (
                country["name"],
                country["official_name"],
                country["region"],
                country["population"],
                country["currencies"],
                country["population_density"]
            ))
        
        conn.commit()
        print("✅ Data successfully saved to PostgreSQL!")
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"❌ Error saving to PostgreSQL: {e}")
