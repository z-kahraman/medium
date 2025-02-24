from fastapi import FastAPI
from kafka import KafkaProducer
import json

app = FastAPI()

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

@app.post("/produce/")
def send_to_kafka(message: dict):
    producer.send("etl_pipeline", message)
    return {"message": "Data sent to Kafka!", "data": message}