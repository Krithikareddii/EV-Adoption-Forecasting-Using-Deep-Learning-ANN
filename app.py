import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load("ann_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Electric Vehicle Adoption Forecasting")
st.write("Deep Learning-Based Artificial Neural Network (ANN)")

st.subheader("Enter Future Year Details")

year = st.number_input("Year", min_value=2024, max_value=2050, value=2025)
total_vehicles = st.number_input("Total Vehicles Registered", value=25000000)
charging = st.number_input("Charging Stations Count", value=20000)
avg_cost_ev = st.number_input("Average Cost of EV", value=35000)
avg_cost_gas = st.number_input("Average Cost of Gasoline Vehicle", value=30000)
gov_incentive = st.number_input("Government Incentive Amount", value=5000)
co2 = st.number_input("CO2 Emissions per Vehicle", value=120.0)
fuel_price = st.number_input("Fuel Price per Liter", value=1.5)
electricity_price = st.number_input("Electricity Price per kWh", value=0.2)

if st.button("Predict EV Adoption"):
    input_data = [[year, total_vehicles, charging, avg_cost_ev,
                   avg_cost_gas, gov_incentive,
                   co2, fuel_price, electricity_price]]

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    st.success(f"Predicted EV Adoption: {int(prediction[0])}")
