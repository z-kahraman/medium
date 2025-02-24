from kafka import KafkaConsumer
import json
import psycopg2

# PostgreSQL bağlantısını oluştur
conn = psycopg2.connect(
    dbname="etl_db",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Kafka Consumer
consumer = KafkaConsumer(
    'etl_pipeline',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='etl_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Kafka Consumer Başlatıldı. Mesajlar dinleniyor...")

# Mesajları dinle ve PostgreSQL'e kaydet
for message in consumer:
    data = message.value
    print(f"Alınan Mesaj: {data}")

    # Veriyi PostgreSQL'e ekle
    cursor.execute(
        "INSERT INTO countries (name, population) VALUES (%s, %s)",
        (data["country"], data["population"])
    )
    conn.commit()

print("Veriler başarıyla PostgreSQL'e kaydedildi!")
