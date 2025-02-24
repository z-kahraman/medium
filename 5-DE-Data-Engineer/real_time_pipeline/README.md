# 🚀 Real-Time Data Processing Pipeline

## 📖 Introduction
This repository contains a **Real-Time Data Processing Pipeline** built using **Kafka, FastAPI, PostgreSQL, and Docker**. The project demonstrates how to:

✅ **Produce real-time data streams using Kafka**  
✅ **Consume and store processed data in PostgreSQL**  
✅ **Implement a scalable microservices architecture with Docker**  
✅ **Enable future real-time analytics with Spark Streaming**  

This project is ideal for **data engineers, backend developers, and real-time system enthusiasts**.

---

## 📂 Project Structure
```
📦 real_time_pipeline
 ┣ 📂 api
 ┃ ┣ 📜 producer.py      # Kafka Producer - Sends data to Kafka
 ┃ ┣ 📜 consumer.py      # Kafka Consumer - Reads data from Kafka and stores in PostgreSQL
 ┃ ┣ 📜 main.py          # FastAPI entry point
 ┣ 📂 database
 ┃ ┣ 📜 db_connector.py  # PostgreSQL connection setup (Planned)
 ┃ ┣ 📜 models.py        # ORM models for database tables (Planned)
 ┣ 📂 processing
 ┃ ┣ 📜 transform.py     # Data transformation functions (Planned)
 ┃ ┣ 📜 spark_stream.py  # Spark Streaming integration (Planned)
 ┣ 📜 docker-compose.yml # Manages Kafka, PostgreSQL services
 ┣ 📜 requirements.txt   # Python dependencies
 ┗ 📜 README.md          # Documentation
```

---

## 🚀 Installation & Setup
### 🔹 1. Clone the Repository
```bash
git clone https://github.com/z-kahraman/real_time_pipeline.git
cd real_time_pipeline
```

### 🔹 2. Create a Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 🔹 3. Run FastAPI Locally
```bash
uvicorn api.main:app --reload
```
FastAPI will be available at: **`http://127.0.0.1:8000/docs`**

---

## 🐳 Running with Docker
### 🔹 1. Start Kafka & PostgreSQL in Docker
```bash
docker-compose up -d
```

### 🔹 2. Verify Running Containers
```bash
docker ps
```

### 🔹 3. Run FastAPI with Docker
```bash
docker build -t real-time-pipeline .
docker run -p 8000:8000 real-time-pipeline
```

---

## ⚡ Kafka Streaming Process
### 📌 Produce Data
**Send data to Kafka**
```http
POST /produce/
```
Example Request:
```json
{
    "country": "Germany",
    "population": 83000000
}
```

### 📌 Consume Data
**Read from Kafka and store in PostgreSQL**
```bash
python api/consumer.py
```

---

## 🎯 Future Improvements
🔹 Add **real-time analytics with Spark Streaming**  
🔹 Implement **WebSocket for real-time dashboards**  
🔹 Optimize **PostgreSQL with ORM & indexing**  

---

## 📜 License
This project is licensed under the MIT License.

---

## 📢 Author
**Zafer Kahraman**  
💼 [LinkedIn](https://linkedin.com/in/zafer-kahraman)  
📄 [Medium Blog](https://medium.com/@zafer_kahraman)  
🐙 [GitHub](https://github.com/z-kahraman)  

🚀 Follow for more **data engineering projects!**

