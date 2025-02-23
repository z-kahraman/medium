# 🚀 FastAPI ETL Pipeline

## 📖 Introduction
This repository contains a complete **ETL (Extract, Transform, Load) pipeline** built with **FastAPI, PostgreSQL, and Docker**. The project demonstrates how to:

✅ **Extract** data from an external API.  
✅ **Transform** raw data into a structured format.  
✅ **Load** the transformed data into PostgreSQL.  
✅ **Deploy the ETL pipeline using Docker.**

This ETL pipeline is ideal for **data engineering, API integration, and backend development**.

---

## 📂 Project Structure
```
📦 fast_api_etl
 ┣ 📜 docker-compose.yml  # Docker configuration for PostgreSQL
 ┣ 📜 extract.py           # Extracts raw data from an external API
 ┣ 📜 load.py              # Saves transformed data to JSON, CSV, and PostgreSQL
 ┣ 📜 main.py              # FastAPI application with ETL endpoints
 ┣ 📜 transform.py         # Cleans and transforms the extracted data
 ┣ 📜 extracted_data.json  # Raw extracted data file
 ┣ 📜 transformed_data.csv # Transformed data in CSV format
 ┣ 📜 transformed_data.json # Transformed data in JSON format
 ┣ 📜 README.md            # Project documentation (this file)
```

---

## 🚀 Installation & Setup
### 🔹 1. Clone the Repository
```bash
git clone https://github.com/z-kahraman/medium.git
cd medium/1-api/fast_api_etl
```

### 🔹 2. Create a Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scriptsctivate
pip install -r requirements.txt
```

### 🔹 3. Run FastAPI Locally
```bash
uvicorn main:app --reload
```
FastAPI will be available at: **`http://127.0.0.1:8000/docs`**

---

## 🐳 Running with Docker
### 🔹 1. Start PostgreSQL in Docker
```bash
docker-compose up -d
```

### 🔹 2. Verify Running Containers
```bash
docker ps
```

### 🔹 3. Run FastAPI with Docker
```bash
docker build -t fastapi-etl .
docker run -p 8000:8000 fastapi-etl
```

---

## ⚡ FastAPI Endpoints
### 📌 Extract Data
**Fetch raw data from an API and save as JSON.**
```http
GET /extract
```

### 📌 Transform Data
**Clean and process extracted data.**
```http
GET /transform
```

### 📌 Load Data
**Save transformed data to PostgreSQL.**
```http
GET /load
```

---

## 🎯 Future Improvements
🔹 Add real-time **Kafka streaming** for data ingestion.  
🔹 Implement **cloud storage integration** for scalability.  
🔹 Optimize **database indexing and query performance**.  

---

## 📜 License
This project is licensed under the MIT License. Feel free to use and contribute!

---

## 📢 Author
**Zafer Kahraman**  
💼 [LinkedIn](https://linkedin.com/in/zafer-kahraman)  
📄 [Medium Blog](https://medium.com/@zafer_kahraman)  
🐙 [GitHub](https://github.com/z-kahraman)  

🚀 Follow me for more **Data Engineering & FastAPI projects!**
