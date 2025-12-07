# SQL Injection Detection with Machine Learning

This project focuses on detecting **SQL Injection attacks** using **Machine Learning** techniques. It identifies malicious SQL queries and prevents database manipulation by classifying queries as legitimate or suspicious. This project uses several machine learning models and tools to achieve high detection accuracy.

---
## 🚀 Features

- **Data Preprocessing**: Extracts features from SQL queries using various techniques.
- **Model Training**: Trains machine learning models on a labeled dataset to detect SQL Injection attempts.
- **Evaluation**: Evaluate models' performance using metrics like accuracy, precision, recall, and F1-score.
- **Detection**: Classifies SQL queries as legitimate or as SQL injection attempts.
- **Web Interface**: A simple interface to input queries and get predictions.

## 🛠️ Technologies Used

- **Python**
- **Scikit-learn** for machine learning models
- **NumPy**, **Pandas** for data manipulation
- **Regex** for SQL query feature extraction
- **Jupyter Notebooks** for model training and evaluation
- **Pickle** for saving and loading trained models

## 📂 Project Structure

- **/sql_injection_Mehdi/**  
  Contains the project files for training and testing the model.
  - `code.ipynb`: Jupyter notebook containing the full code for training and testing the SQL injection detection model.
  - `nmap.ipynb`: Jupyter notebook for additional analysis and data processing related to network security and SQL injection detection.
  - `test.py`: Python script for testing the trained model and making predictions on SQL queries.
  - `trained_model.pkl`: The trained machine learning model for SQL injection detection (saved using `pickle`).
  - `vectorized.pkl`: TF-IDF vectorizer for transforming SQL queries into numerical features.

## 📈 Model Evaluation

- **Accuracy**: ~87%
- **Precision, Recall, F1-Score**: Model performance evaluated using classification metrics.
- **Algorithms Used**: Logistic Regression.
## 🛡️ Security Considerations

While machine learning detection models are valuable tools, they should be used in conjunction with **best practices** for SQL injection prevention, such as **parameterized queries** and **input validation**.
