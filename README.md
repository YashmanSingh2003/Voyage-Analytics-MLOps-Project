# ✈️ Voyage Analytics

## End-to-End Machine Learning Travel Analytics Platform

Voyage Analytics is an end-to-end machine learning project that combines predictive analytics, recommendation systems, deployment, and MLOps concepts into a unified travel analytics platform. The project consists of three machine learning models: Flight Price Prediction, Gender Classification, and Hotel Recommendation System. These models are integrated into an interactive Streamlit dashboard and supported by Flask APIs, MLflow experiment tracking, Docker containerization, Kubernetes deployment, Airflow workflow automation, and Jenkins CI/CD pipelines.

---

# Project Overview

This project includes:

* Flight Price Prediction using Random Forest Regressor
* Gender Classification using Random Forest Classifier
* Hotel Recommendation System using Collaborative Filtering
* Flask API Integration
* Streamlit Dashboard
* MLflow Experiment Tracking
* Docker Containerization
* Kubernetes Deployment
* Apache Airflow Workflow Automation
* Jenkins CI/CD Pipeline

---

# Project Structure

```text
Voyage_Analytics
│
├── streamlit_app.py
├── app.py
├── requirements.txt
├── README.md
├── flight_price_model.pkl
├── gender_model.pkl
├── hotel_recommender.pkl
├── Dockerfile
├── deployment.yaml
├── travel_pipeline_dag.py
├── mlflow_tracking.py
├── Jenkinsfile
│
├── notebooks
│     ├── 01_Flight_Price_Prediction_Regression.ipynb
│     ├── 02_Gender_Classification_Model.ipynb
│     └── 03_Hotel_Recommendation_System.ipynb
│
└── images
```

---

# Dataset Information

The project uses travel-related datasets containing information about:

### Flight Dataset

Features:

* Departure city
* Destination city
* Flight type
* Travel time
* Distance
* Airline agency
* Date information

Target:

* Flight Price

### User Dataset

Features:

* Company
* Name
* Age

Target:

* Gender

### Hotel Dataset

Features:

* User ID
* Hotel Name
* Destination
* Booking Amount

Target:

* Hotel Recommendations

---

# Machine Learning Models

## Flight Price Prediction

### Algorithm

Random Forest Regressor

### Evaluation Metrics

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

---

## Gender Classification

### Algorithm

Random Forest Classifier

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score

---

## Hotel Recommendation System

### Approach

User-Based Collaborative Filtering

### Similarity Measure

Cosine Similarity

---

# Streamlit Dashboard

The project provides an interactive Streamlit application where users can:

* Predict flight prices
* Predict gender from user details
* Generate hotel recommendations

---

# Flask API

Flask APIs are used to serve machine learning models and provide prediction endpoints.

---

# MLflow Tracking

MLflow is used for:

* Experiment tracking
* Metric logging
* Parameter tracking
* Model management

---

# Docker Containerization

Docker is used to package the application and ensure reproducibility across environments.

---

# Kubernetes Deployment

Kubernetes deployment files are included to demonstrate container orchestration and scalability.

---

# Apache Airflow

Airflow DAGs are used to automate workflows and manage pipeline execution.

---

# Jenkins CI/CD

Jenkins pipelines are included to demonstrate Continuous Integration and Continuous Deployment concepts.

---

# Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Voyage_Analytics.git
```

Move into the project directory:

```bash
cd Voyage_Analytics
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Run Streamlit Application

```bash
streamlit run streamlit_app.py
```

---

# Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-learn
* Joblib
* Flask
* Streamlit
* MLflow

### MLOps Tools

* Docker
* Kubernetes
* Apache Airflow
* Jenkins

---

# Future Improvements

* Cloud Deployment
* User Authentication
* Database Integration
* Real-Time Predictions
* Advanced Recommendation Models

---

# Author

Yashman Singh

Machine Learning | Data Science | MLOps

---

# License

This project is intended for educational and portfolio purposes.
