import requests
import pandas as pd
import os
import json
import time
import csv
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")

if not API_KEY:
    raise ValueError("ERROR: API key not found! Please check your .env file.")

# Get a unique timestamp with seconds and milliseconds
current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')  # Ensures uniqueness
current_date = datetime.now().strftime('%Y-%m-%d')

# Define output folders
output_folder = "data/"
log_folder = "execution_logs/"  # New folder for logs

# Ensure directories exist
os.makedirs(output_folder, exist_ok=True)
os.makedirs(log_folder, exist_ok=True)  # Create execution_logs folder if not exists

# Define log file paths inside execution_logs/
log_file_csv = os.path.join(log_folder, "execution_log.csv")
log_file_json = os.path.join(log_folder, "execution_log.json")

# Define output file paths for news data
output_txt_path = os.path.join(output_folder, f"news_api_response_{current_time}.txt")
output_excel_path = os.path.join(output_folder, f"news_data_{current_time}.xlsx")

# Start tracking time
start_time = time.time()

# ✅ 1️⃣ Measure API Request Time
api_start = time.time()
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
response = requests.get(url)
api_end = time.time()
api_time = round(api_end - api_start, 4)
print(f"⏱ API Request Time: {api_time} seconds")

# ✅ 2️⃣ Measure JSON Processing Time
json_start = time.time()
if response.status_code == 200:
    data = response.json()
else:
    print(f"❌ API request failed! Status: {response.status_code}")
    exit()
json_end = time.time()
json_time = round(json_end - json_start, 4)
print(f"⏱ JSON Processing Time: {json_time} seconds")

# ✅ 3️⃣ Measure Saving Raw Data to TXT Time
txt_start = time.time()
with open(output_txt_path, "w", encoding="utf-8") as txt_file:
    json.dump(data, txt_file, indent=4, ensure_ascii=False)
txt_end = time.time()
txt_time = round(txt_end - txt_start, 4)
print(f"⏱ TXT File Writing Time: {txt_time} seconds")

# ✅ 4️⃣ Measure DataFrame Creation Time
df_start = time.time()
articles = data.get("articles", [])
df = pd.DataFrame(articles)
df_end = time.time()
df_time = round(df_end - df_start, 4)
print(f"⏱ DataFrame Creation Time: {df_time} seconds")

# ✅ 5️⃣ Measure Processing & Saving to Excel Time
excel_start = time.time()
if not df.empty:
    df = df[["source", "author", "title", "description", "url", "publishedAt"]]
    df["source"] = df["source"].apply(lambda x: x["name"] if isinstance(x, dict) else x)
    df.to_excel(output_excel_path, index=False)
excel_end = time.time()
excel_time = round(excel_end - excel_start, 4)
print(f"⏱ Excel File Writing Time: {excel_time} seconds")

# ✅ Total Execution Time
end_time = time.time()
total_time = round(end_time - start_time, 4)
print(f"🚀 Total Execution Time: {total_time} seconds")

# ✅ Log Data for BI Tool with Unique Timestamp
log_data = {
    "date": current_date,
    "timestamp": current_time,  # Now includes seconds & milliseconds
    "api_time": api_time,
    "json_time": json_time,
    "txt_time": txt_time,
    "df_time": df_time,
    "excel_time": excel_time,
    "total_time": total_time
}

# ✅ 6️⃣ Save Logs to CSV Inside `execution_logs/`
csv_headers = ["date", "timestamp", "api_time", "json_time", "txt_time", "df_time", "excel_time", "total_time"]
file_exists = os.path.isfile(log_file_csv)

with open(log_file_csv, mode="a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=csv_headers)
    if not file_exists:
        writer.writeheader()
    writer.writerow(log_data)

print(f"✅ Execution log saved to {log_file_csv}")

# ✅ 7️⃣ Save Logs to JSON Inside `execution_logs/`
if os.path.exists(log_file_json):
    with open(log_file_json, "r", encoding="utf-8") as json_file:
        existing_data = json.load(json_file)
else:
    existing_data = []

existing_data.append(log_data)

with open(log_file_json, "w", encoding="utf-8") as json_file:
    json.dump(existing_data, json_file, indent=4)

print(f"✅ Execution log saved to {log_file_json}")
