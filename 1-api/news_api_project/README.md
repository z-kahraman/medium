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

## ⚙️ Automating with Cron Job

### 📌 What is a Cron Job?
A **cron job** is a scheduled task in Unix-based systems that runs automatically at specified intervals. In this project, we use a cron job to **fetch news data periodically** without manual execution.

### 🔹 How the Cron Job Works
- The script `fetch_news.py` fetches the latest news from the API.
- The cron job **automatically runs this script** at scheduled intervals.
- The output is saved to `execution_logs/cron_log.txt` for debugging and tracking.

### 🛠 Setting up the Cron Job
To automate the script execution, follow these steps:

1️⃣ **Open the cron job editor:**
```bash
crontab -e
```

2️⃣ **Add the following line to schedule the script:**
```bash
0 * * * * /usr/bin/python3 /path/to/news_api_project/fetch_news.py >> /path/to/execution_logs/cron_log.txt 2>&1
```
### **📌 Explanation of the Cron Schedule:**
| Field         | Value | Meaning |
|--------------|-------|---------|
| Minute       | `0`   | Runs at the start of every hour |
| Hour         | `*`   | Runs every hour |
| Day of Month | `*`   | Runs every day of the month |
| Month        | `*`   | Runs every month |
| Day of Week  | `*`   | Runs on all days of the week |

### 🔄 Running the Cron Job Manually
If you want to test it immediately without waiting, run:
```bash
python fetch_news.py
```

### 🛠 Checking if the Cron Job is Running
To see active cron jobs, use:
```bash
crontab -l
```

To check logs for errors:
```bash
cat /path/to/execution_logs/cron_log.txt
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
