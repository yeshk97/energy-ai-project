🚀 Energy AI Forecasting System
📌 Overview

This project is an end-to-end AI pipeline that collects real-time weather data, stores it in a database, trains a machine learning model, and serves predictions through APIs and an interactive dashboard.

🧠 What This Project Does
Collects real-time weather data from an external API
Stores data in a SQLite database
Preprocesses data for machine learning
Trains a regression model to predict energy demand
Exposes predictions via FastAPI endpoints
Provides a Streamlit dashboard for visualization and interaction
🏗️ Architecture
Weather API
     ↓
Data Collector (Python)
     ↓
SQLite Database
     ↓
Preprocessing Pipeline
     ↓
ML Model (Linear Regression)
     ↓
FastAPI (Prediction API)
     ↓
Streamlit Dashboard (Frontend)
⚙️ Tech Stack
Python
Pandas
Scikit-learn
SQLite
FastAPI
Streamlit
Requests
🔌 API Endpoints
1. Manual Prediction
/predict

Provide inputs manually:

temperature
hour
day_of_week
is_weekend
2. Live Prediction
/predict-live
Fetches real-time weather data
Generates prediction instantly
3. Database Prediction
/predict-from-db
Uses latest stored data from database
Provides stable prediction
💻 Dashboard Features
📊 View stored weather data
📈 Temperature trend visualization
🔁 Select prediction mode:
Live Prediction
Database Prediction
Manual Prediction
▶️ How to Run
1. Activate virtual environment
.\.venv\Scripts\Activate
2. Start API server
uvicorn api.app:app --reload
3. Start dashboard
streamlit run app/dashboard.py
4. Open in browser
API Docs:
http://127.0.0.1:8000/docs
Dashboard:
http://localhost:8501
📊 Sample Workflow
Run data collector → stores weather data in DB
Train model using stored data
Use API or dashboard to get predictions
🎯 Key Learnings
Built a complete ML pipeline
Integrated real-time data ingestion
Designed database-driven architecture
Developed API-based model serving
Created interactive frontend dashboard
🚀 Future Improvements
Replace SQLite with PostgreSQL (cloud)
Add automated data pipelines (scheduler)
Improve model with advanced ML algorithms
Deploy using Docker + Cloud (AWS/Azure)
👨‍💻 Author

Yeswanth Kumar Lekkala
