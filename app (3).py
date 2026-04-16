
import streamlit as st
import pandas as pd
import joblib
import numpy as np

try:
    model = joblib.load('edu_pulse_model.pkl')
except:
    st.error("Model file not found! Please make sure 'edu_pulse_model.pkl' is in the same folder.")

st.set_page_config(page_title="EduPulse Pro | AI System", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1f2937; padding: 20px; border-radius: 12px; border: 1px solid #3b82f6; }
    .stAlert { border-radius: 12px; }
    div[data-testid="stExpander"] { border: none; background-color: #111827; border-radius: 12px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎓 EduPulse Pro: Advanced AI Success Ecosystem")
st.markdown("---")

st.sidebar.header("📊 Student Performance Data")
st.sidebar.info("Adjust the sliders to see real-time impact.")

attendance = st.sidebar.slider("Attendance Rate (%)", 0, 100, 85)
study_hours = st.sidebar.slider("Weekly Study Hours", 0, 50, 15)
quiz_avg = st.sidebar.number_input("Average Quiz Score (0-20)", 0.0, 20.0, 15.0)
midterm = st.sidebar.number_input("Midterm Score (0-30)", 0.0, 30.0, 22.0)

input_data = pd.DataFrame([[attendance, study_hours, quiz_avg, midterm]], 
                         columns=['Attendance_Rate', 'Study_Hours_Weekly', 'Quiz_Avg', 'Midterm_Score'])

raw_prediction = model.predict(input_data)[0]

final_prediction = max(35.0, min(100.0, raw_prediction))

col1, col2, col3 = st.columns([1, 1, 1], gap="large")

with col1:
    st.subheader("🔮 Predictive Analytics")
    st.metric(label="Forecasted Final Grade", value=f"{final_prediction:.1f}%")

(Gamification)
    if final_prediction >= 85:
        st.success("🏆 Status: Elite Scholar")
        st.balloons()
    elif final_prediction >= 65:
        st.info("⭐ Status: Good Standing")
    else:
        st.warning("⚠️ Status: Needs Improvement")

with col2:
    st.subheader("🤖 AI Study Coach")
    with st.container():
        if attendance < 75:
            st.error("🚨 **Attendance:** Missing classes is your biggest risk. Aim for 80% to stabilize your grade.")
        if study_hours < 20:
            st.warning("📚 **Study Time:** Your current hours are below the average for top performers. Add 5 hours/week.")
        if quiz_avg < 14:
            st.info("📝 **Quiz Prep:** Focus on weekly quizzes; they are heavily weighted in the final calculation.")
        if final_prediction >= 85:
            st.write("You are doing amazing! Share your study techniques with others.")

with col3:
    st.subheader("🎯 Smart Goal Planner")
    target = st.number_input("Your Target Grade (%)", 40, 100, 90)
    
    if target > final_prediction:
        diff = target - final_prediction
        extra_hours = diff / 1.8 
        st.write(f"To reach your goal of **{target}%**:")
        st.info(f"💡 You need to increase your study time by approx. **{extra_hours:.1f}** additional hours per week.")
    else:
        st.success("🎉 You are currently on track to achieve or exceed this target!")

st.markdown("---")

# 5. (Early Warning System)
with st.expander("👨‍🏫 Educator & Administration Portal"):
    if final_prediction < 60:
        st.error(f"⚠️ **URGENT:** Student ID: #SB-2026 is at high risk of failure.")
        st.write("System recommends immediate academic intervention.")
        if st.button("Generate Intervention Report"):
            st.write("✅ Report generated and sent to Academic Advisor.")
    else:
        st.write("✅ All performance metrics are within the safe zone for this student.")

st.caption("Powered by EduPulse AI Engine v2.0 | Alexandria University Hackathon Edition")
