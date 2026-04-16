import streamlit as st
import pandas as pd
import joblib

model = joblib.load('edu_pulse_model.pkl')

st.title("🎓 EduPulse: Student Success Predictor")
attendance = st.sidebar.slider("Attendance Rate (%)", 0, 100, 85)
study_hours = st.sidebar.slider("Weekly Study Hours", 0, 50, 15)
quiz_avg = st.sidebar.number_input("Average Quiz Score (out of 20)", 0.0, 20.0, 15.0)
midterm = st.sidebar.number_input("Midterm Score (out of 30)", 0.0, 30.0, 22.0)

input_data = pd.DataFrame({
    'Attendance_Rate': [attendance],
    'Study_Hours_Weekly': [study_hours],
    'Quiz_Avg': [quiz_avg],
    'Midterm_Score': [midterm]
})

prediction = model.predict(input_data)[0]
st.subheader(f"Predicted Final Grade: {prediction:.1f} / 100")
