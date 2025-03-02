# Product Requirements Document (PRD)

## **Project Name:** AI Agent for YouTube Review Analysis

## **Overview**
This AI Agent is designed to analyze YouTube review videos for a given product and classify user comments to help users make informed purchasing decisions. The project is implemented using **SmolAgent** and leverages **LLM** for classification and **YouTube API** for data extraction.

## **Objectives**
- Automate the process of collecting and analyzing YouTube review comments.
- Provide structured insights into user opinions.
- Allow users to input a natural language prompt to analyze a product.
- Enable future AI integration for deeper analysis and recommendation.

## **Features & Functionalities**

### ✅ **Completed Features**
1. **Prompt Processing**: The agent accepts a natural language query (e.g., "Should I buy an iPhone 15 for work?").
2. **Product Detection**: Extracts the mentioned product from the prompt using an LLM.
3. **YouTube Search Integration**: Searches YouTube for related review videos using keywords like "review" and "comparison."
4. **Video Ranking Mechanism**: Filters and ranks videos based on engagement metrics (views, likes, comments, etc.).
5. **Video ID Extraction**: Retrieves video IDs from the top-ranked videos **without opening them**, using the YouTube API.

### 🔲 **Pending Features**
1. **YouTube Comments Extraction**
   - Retrieve comments from selected videos.
   - Handle pagination for large comment sections.
2. **Comment Sentiment Classification**
   - Use LLM to classify comments into categories:
     - Positive
     - Negative
     - Pros
     - Cons
3. **Result Formatting & Reporting**
   - Structure the output for better readability.
   - Provide a summary of user sentiment.
4. **User-Defined Product Evaluation (Optional)**
   - Allow users to set criteria (e.g., durability, performance, battery life) and evaluate based on classified comments.
5. **Error Handling & Improvements**
   - Implement logging and error handling.
   - Optimize API usage and performance.

## **Technology Stack**
- **AI Agent Framework**: SmolAgent
- **LLM**: Hugging Face Model
- **Backend**: Python (FastAPI / Flask)
- **Data Extraction**: YouTube API v3
- **Storage & Processing**: Pandas / SQLite (for caching results if needed)
- **Deployment**: Docker

## **Next Steps**
- Implement **YouTube comment extraction**
- Develop **comment classification logic**
- Design **result formatting and evaluation criteria**
- Integrate error handling and optimizations

## **Final Goal**
- A working AI Agent capable of analyzing YouTube review comments, providing structured insights, and helping users make better purchasing decisions.

---
This PRD will be updated as new features are completed.

