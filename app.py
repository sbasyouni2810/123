import streamlit as st
import pandas as pd
import joblib
import numpy as np

# تحميل الموديل
model = joblib.load('edu_pulse_model.pkl')

# إعدادات الصفحة
st.set_page_config(page_title="EduPulse AI", layout="centered")

st.title("🎓 EduPulse: Student Success Predictor")
st.markdown("---")

st.sidebar.header("Student Input Metrics")
attendance = st.sidebar.slider("Attendance Rate (%)", 0, 100, 85)
study_hours = st.sidebar.slider("Weekly Study Hours", 0, 50, 15)
quiz_avg = st.sidebar.number_input("Average Quiz Score (out of 20)", 0.0, 20.0, 15.0)
midterm = st.sidebar.number_input("Midterm Score (out of 30)", 0.0, 30.0, 22.0)

# تجهيز البيانات للتوقع
input_data = pd.DataFrame({
    'Attendance_Rate': [attendance],
    'Study_Hours_Weekly': [study_hours],
    'Quiz_Avg': [quiz_avg],
    'Midterm_Score': [midterm]
})

# التوقع
prediction = model.predict(input_data)[0]
prediction = max(0, min(100, prediction))

st.subheader("Your Predicted Performance")
col1, col2 = st.columns(2)

with col1:
    st.metric(label="Predicted Final Grade", value=f"{prediction:.1f} / 100")

with col2:
    if prediction >= 85:
        status = "Excellent! 🌟"
        color = "green"
    elif prediction >= 65:
        status = "Good Standing 👍"
        color = "blue"
    else:
        status = "At Risk! ⚠️"
        color = "red"
    st.markdown(f"Status: <span style='color:{color}; font-weight:bold;'>{status}</span>", unsafe_allow_html=True)

st.markdown("---")
st.info("💡 Tip: Increasing your study hours by 5 hours could improve your score significantly!")
