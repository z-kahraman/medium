import json

def transform_data(raw_data):
    """Extracted JSON verisini temizler ve dönüştürür."""
    
    transformed_data = []
    
    for country in raw_data:
        try:
            # 1️⃣ Gereksiz alanları temizleme
            name = country.get("name", {}).get("common", "Unknown")
            official_name = country.get("name", {}).get("official", "Unknown")
            region = country.get("region", "Unknown")
            population = country.get("population", 0)
            currencies = country.get("currencies", {})

            # 2️⃣ Para birimi dönüşümü
            currency_list = ", ".join(currencies.keys()) if currencies else "Unknown"

            # 3️⃣ Eksik veri yönetimi (Nüfus bilgisi eksikse 0 olarak ata)
            population = max(population, 0)  

            # 4️⃣ Yeni hesaplanmış alan (Nüfus Yoğunluğu)
            area = country.get("area", 1)  # Alan 1'den küçük olamaz
            population_density = round(population / area, 2)

            # 5️⃣ Dönüştürülmüş veriyi ekleme
            transformed_data.append({
                "name": name,
                "official_name": official_name,
                "region": region,
                "population": population,
                "currencies": currency_list,
                "population_density": population_density
            })

        except Exception as e:
            print(f"❌ Veri dönüştürme hatası: {e}")

    return transformed_data

# Örnek test
if __name__ == "__main__":
    try:
        with open("extracted_data.json", "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        
        clean_data = transform_data(raw_data)
        
        with open("transformed_data.json", "w", encoding="utf-8") as f:
            json.dump(clean_data, f, indent=4, ensure_ascii=False)

        print("✅ Transform işlemi tamamlandı! 'transformed_data.json' dosyası oluşturuldu.")

    except FileNotFoundError:
        print("❌ Hata: 'extracted_data.json' dosyası bulunamadı!")
