# Electric Vehicle Adoption Forecasting Using Deep Learning-Based Artificial Neural Network (ANN)

## 1. Project Overview

This project presents a predictive system designed to forecast future Electric Vehicle (EV) adoption using a Deep Learning-based Artificial Neural Network (ANN). The model analyzes historical transportation, economic, and environmental indicators to estimate future EV registrations.

The system is implemented as an end-to-end machine learning pipeline including data preprocessing, feature scaling, model training, evaluation, and deployment through a Streamlit-based web application.

---

## 2. Problem Statement

Accurate forecasting of EV adoption is essential for:

- Government policy planning  
- Charging infrastructure expansion  
- Energy demand forecasting  
- Automotive industry strategy development  

This project develops a regression-based ANN model to estimate EV adoption using structured numerical inputs.

---

## 3. Model Architecture

- Algorithm: Artificial Neural Network (ANN)  
- Implementation Library: Scikit-learn (MLPRegressor)  
- Learning Type: Supervised Learning (Regression)  
- Feature Scaling: StandardScaler  
- Model Serialization: Joblib (.pkl files)  

The ANN model learns nonlinear relationships between socio-economic variables and EV adoption trends.

---

## 4. Input Features

The model uses the following input variables:

- Year  
- Total Vehicles Registered  
- Charging Stations Count  
- Average EV Cost  
- Average Gasoline Vehicle Cost  
- Government Incentive Amount  
- CO2 Emissions per Vehicle  
- Fuel Price per Liter  
- Electricity Price per kWh  

---

## 5. Target Variable

- Predicted EV Adoption (Total EV Registrations)

---

## 6. Model Evaluation Metrics

Model performance is evaluated using:

- R² Score  
- Mean Absolute Error (MAE)  
- Mean Squared Error (MSE)  

These metrics assess predictive accuracy and regression reliability.

---

## 7. Web Application

An interactive web interface is developed using Streamlit. The application allows users to:

- Enter future economic and transportation parameters  
- Generate real-time EV adoption forecasts  
- Instantly view prediction results  

---

## 8. How to Run the Project Locally

Step 1: Install required dependencies

pip install -r requirements.txt

Step 2: Launch the Streamlit application

streamlit run app.py

The application will open in a local browser window.

---

## 9. Project Structure

EV-Adoption-Forecasting-Using-Deep-Learning-ANN/
│
├── EV_Adoption_ANN_Training.ipynb
├── app.py
├── ann_model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md

---

## 10. Key Contributions

- Developed a regression-based ANN model for EV forecasting  
- Implemented feature scaling and preprocessing pipeline  
- Built a deployable Streamlit interface  
- Structured the project for reproducibility and clarity  

---

## 11. Future Enhancements

- Integration with real-world public datasets  
- Hyperparameter tuning for improved performance  
- Model comparison with advanced deep learning architectures  
- Cloud deployment for global accessibility  
