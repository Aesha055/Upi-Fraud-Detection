# Upi-Fraud-Detection
# UPI Fraud Detection System

## Overview
This project is an ML-based UPI fraud detection system that identifies fraudulent transactions using supervised learning. 
It analyzes transaction behavior patterns and predicts whether a transaction is legitimate or fraudulent.

## Features
- Supervised machine learning model for fraud detection
- Behavioral feature analysis (amount, frequency, receiver patterns, etc.)
- Real-time prediction using Streamlit
- User-friendly web interface

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Kaggle dataset

## Machine Learning Model
- Algorithm used: Random Forest Classifier
- Data preprocessing and feature selection applied
- Model trained on labeled transaction data(80/20) rule 

## How It Works
1. User enters transaction details
2. Data is processed and scaled
3. ML model predicts fraud probability
4. Result is displayed in real-time

## Installation & Usage
```bash
pip install -r requirements.txt
streamlit run app.py
