import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.title("Employee Salary Prediction")

st.divider()

st.write("This is a simple linear regression model to predict employee salaries based on their years of experience and job rate. The model is trained on a dataset containing employee information such as years of experience, job rate, and annual salary. The user can input the years of experience and job rate, and the model will predict the annual salary based on these inputs.")

years = st.number_input("Enter the years at company", value=1, step=1, min_value=0)
jobrate = st.number_input("Enter the job rate", value=3.5, step=0.5, min_value=0.0)

x = [years, jobrate]

model = joblib.load("linearmodel.pkl")

st.divider()

predict = st.button("Press the button for salary prediction")

st.divider()

if predict:
    st.balloons()
    x1 = pd.DataFrame([x], columns=["Years", "Job Rate"])  # Use DataFrame with feature names
    prediction = model.predict(x1)
    st.write(f"Salary prediction is ₹{prediction[0]:,.2f}")
else:
   st.warning("Please press the button to predict salary.")