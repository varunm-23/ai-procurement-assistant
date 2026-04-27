# ai-procurement-assistant
AI-powered procurement assistant that uses TinyLlama, FastAPI, MongoDB, and a chat interface to answer natural language questions from California State purchasing data.

# AI Procurement Assistant

An AI-powered conversational assistant that answers procurement-related questions using the California State Purchasing Dataset.

## 🚀 Features

- Natural language chat interface
- Converts user questions into MongoDB queries
- Retrieves real procurement insights
- Uses local free LLM (TinyLlama via Ollama)
- FastAPI backend + HTML/CSS/JS frontend

## 🛠 Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: FastAPI (Python)
- Database: MongoDB
- AI Model: TinyLlama (Ollama)

---

## 📂 Project Structure

project/
├── backend/
├── frontend/
├── data/
├── README.md
├── .gitignore

---

## ⚙️ Setup Instructions

### 1. Clone Repository

- git clone <your-github-link>
- cd project


### 2. Backend Setup 
- cd backend
- pip install -r requirements.txt
- uvicorn main:app --reload

Backend runs at:
http://127.0.0.1:8000

Swagger API Docs:
http://127.0.0.1:8000/docs


### 3. Frontend Setup

Open:
frontend/index.html

---

## Dataset Setup

The dataset file is not included in this repository because it exceeds GitHub file size limits.

Please download the California Procurement Dataset from the Kaggle link provided below :
https://www.kaggle.com/datasets/sohier/large-purchases-by-the-state-of-ca
---
### Steps

1. Download the CSV dataset from Kaggle.
2. Rename the file to:

PURCHASE_ORDER_DATA.csv

3. Create a `data` folder in the project root..
4. Place the file inside:

project/data/PURCHASE_ORDER_DATA.csv


### Load Dataset into MongoDB

After placing the dataset file, run:

- cd backend
- python load_data.py
- python clean_data.py


### Final Structure
- project/
- ├── backend/
- ├── frontend/
- ├── data/
- │   └── PURCHASE_ORDER_DATA.csv
- ├── README.md
- ├── .gitignore

Supported Queries
1. What is total spending?
2. Which supplier has the highest spending?
3. Top 5 suppliers by spending
4. Which department spent the most?
5. Lowest spending supplier
6. Total records count
7. Show top departments

# The workflow is:
User Question → FastAPI API → Agent Module → MongoDB Query Generation → Query Execution → Response Formatter → Frontend Display
``` bash


