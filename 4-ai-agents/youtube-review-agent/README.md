# AI Agent for YouTube Review Analysis

## 📌 Overview
This AI Agent analyzes YouTube review videos for a given product and classifies user comments into categories like positive, negative, pros, and cons. The goal is to help users make informed purchasing decisions by structuring and summarizing YouTube comments using AI.

## 🚀 Features
### ✅ Completed Features
- **Prompt Processing**: Accepts natural language queries (e.g., "Should I buy an iPhone 15 for work?").
- **Product Detection**: Extracts product names from user queries using an LLM.
- **YouTube Search**: Searches for related review videos on YouTube.
- **Video Ranking**: Sorts videos based on engagement metrics (views, likes, comments, etc.).
- **Video ID Extraction**: Retrieves the top-ranked video IDs using the YouTube API.

### 🔲 Upcoming Features
- **YouTube Comment Extraction**: Retrieve and process comments from top-ranked videos.
- **Comment Classification**: Use LLM to categorize comments into sentiment groups.
- **Result Formatting**: Structure the output for clarity and user insights.
- **User-Defined Product Evaluation (Optional)**: Allow users to specify criteria for analysis.
- **Error Handling & Optimization**: Improve API efficiency and logging.

## 🛠️ Tech Stack
- **AI Agent Framework**: SmolAgent
- **LLM**: Hugging Face Model
- **Backend**: Python (FastAPI / Flask)
- **Data Extraction**: YouTube API v3
- **Processing**: Pandas / SQLite (optional caching)
- **Deployment**: Docker

## 🏗️ Installation & Setup
### 🔹 Prerequisites
- Python 3.9+
- YouTube API Key
- Docker (optional for containerized deployment)

### 🔹 Clone the Repository
```sh
git clone https://github.com/your-username/ai-agent-youtube-review.git
cd ai-agent-youtube-review
```

### 🔹 Install Dependencies
```sh
pip install -r requirements.txt
```

### 🔹 Set up Environment Variables
Create a `.env` file and add your YouTube API key:
```
YOUTUBE_API_KEY=your_api_key_here
```

### 🔹 Run the Application
```sh
python main.py
```
Or, if using Docker:
```sh
docker-compose up --build
```

## 📝 Usage
1. Run the application.
2. Input a product-related question (e.g., "Is the MacBook Air M2 worth it?").
3. The AI Agent will:
   - Detect the product.
   - Search for relevant YouTube reviews.
   - Extract video IDs.
   - (Upcoming) Retrieve and classify comments.
4. View structured insights about user opinions.

## 🤝 Contributing
1. Fork the repository.
2. Create a new branch (`feature-branch-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push the branch (`git push origin feature-branch-name`).
5. Create a Pull Request.

## 📜 License
This project is licensed under the MIT License.

## 📬 Contact
For questions or contributions, reach out via [GitHub Issues](https://github.com/your-username/ai-agent-youtube-review/issues).