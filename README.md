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

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone <your-github-link>
cd project

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

### Final Structure

project/
├── backend/
├── frontend/
├── data/
│   └── PURCHASE_ORDER_DATA.csv

---

### Load Dataset into MongoDB

After placing the dataset file, run:

```bash
cd backend
python load_data.py
python clean_data.py
