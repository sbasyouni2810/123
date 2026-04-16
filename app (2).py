
import streamlit as st
import pandas as pd
import joblib

# 1. التحميل
model = joblib.load('edu_pulse_model.pkl')

st.set_page_config(page_title="EduPulse Pro", layout="wide")

st.title("🎓 EduPulse Pro: AI Success Ecosystem")

# 2. المدخلات في الجنب
st.sidebar.header("📊 Student Data")
attendance = st.sidebar.slider("Attendance %", 0, 100, 85)
study_hours = st.sidebar.slider("Weekly Study Hours", 0, 50, 15)
quiz_avg = st.sidebar.number_input("Quiz Score (0-20)", 0.0, 20.0, 15.0)
midterm = st.sidebar.number_input("Midterm (0-30)", 0.0, 30.0, 22.0)

# 3. الحسابات
input_data = pd.DataFrame([[attendance, study_hours, quiz_avg, midterm]], 
                         columns=['Attendance_Rate', 'Study_Hours_Weekly', 'Quiz_Avg', 'Midterm_Score'])
prediction = model.predict(input_data)[0]
prediction = max(0, min(100, prediction))

# 4. العرض (التقسيم لـ 3 أعمدة)
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🔮 Prediction")
    st.metric("Grade Forecast", f"{prediction:.1f}%")
    if prediction >= 85: st.balloons()

with col2:
    st.subheader("🤖 AI Coach")
    if attendance < 75: st.warning("Increase attendance!")
    if study_hours < 20: st.info("Study more to hit 90%!")

with col3:
    st.subheader("🎯 Goal Planner")
    target = st.number_input("Target Grade %", 0, 100, 90)
    if target > prediction:
        st.write(f"You need approx. {((target-prediction)/0.5):.1f} more hours.")

st.markdown("---")
st.subheader("👨‍🏫 Educator Early Warning")
if prediction < 60:
    st.error("⚠️ ALERT: Student is at risk!")
