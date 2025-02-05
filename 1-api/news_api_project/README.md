# News API Project 📰

This project is a Python application that **fetches news from NewsAPI** and saves them to an Excel file.  
It also **logs execution times** for performance analysis and BI tools.

## 🚀 Usage

### 1️⃣ Install Dependencies
Run the following command to install required packages:

```bash
pip install -r requirements.txt
```

### 2️⃣ Add API Key to `.env` File
Create a `.env` file in the project directory and add your **NewsAPI key**:

```ini
NEWS_API_KEY=your_api_key_here
```

### 3️⃣ Run the Script to Fetch News
To retrieve the latest news and save them to an Excel file, run:

```bash
python fetch_news.py
```

---

## 📂 Project Structure
```md
news_api_project/
│── data/                      # Stores fetched news data
│   ├── news_api_response_YYYY-MM-DD_HH-MM-SS-ffffff.txt
│   ├── news_data_YYYY-MM-DD_HH-MM-SS-ffffff.xlsx
│── execution_logs/             # Stores execution time logs
│   ├── execution_log.csv
│   ├── execution_log.json
│── fetch_news.py               # Python script to fetch news and save to Excel
│── requirements.txt            # Dependencies list
│── .env                        # API key configuration file (excluded from Git)
│── README.md                   # Project documentation
```

---

## ⚙️ Features
✔ Fetches real-time news from **NewsAPI**  
✔ Saves news articles in an **Excel (.xlsx) file**  
✔ Stores the raw API response in a **.txt file**  
✔ Uses a **`.env` file** to secure API credentials  
✔ **Logs execution times** to `execution_logs/` for analysis  

---

## 📊 Execution Logs for BI Tools
- Every script run is **logged with precise timestamps** including seconds and milliseconds.
- Logs are saved in:
  - **CSV format** (`execution_logs/execution_log.csv`) for easy import into BI tools like **Power BI, Tableau, or Excel**.
  - **JSON format** (`execution_logs/execution_log.json`) for structured analysis.

---

## 📝 Notes
- Make sure to **get a free API key** from [NewsAPI](https://newsapi.org/register) before running the script.
- The **Excel and text files are automatically named with timestamps** to avoid overwriting previous data.
- **`.gitignore` is set up** to exclude `.env` and `data/` folder from Git tracking.

---

## 📌 License
This project is open-source and available under the **MIT License**.
