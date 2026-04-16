
import streamlit as st
import pandas as pd
import joblib

# 1. تحميل الموديل
try:
    model = joblib.load('edu_pulse_model.pkl')
except:
    st.error("Model file not found!")

st.set_page_config(page_title="EduPulse Pro", layout="wide")

# العنوان
st.title("🎓 EduPulse Pro: AI Success Ecosystem")
st.markdown("---")

# 2. القائمة الجانبية
st.sidebar.header("📊 Student Data")
attendance = st.sidebar.slider("Attendance Rate (%)", 0, 100, 85)
study_hours = st.sidebar.slider("Weekly Study Hours", 0, 50, 15)
quiz_avg = st.sidebar.number_input("Quiz Score (0-20)", 0.0, 20.0, 15.0)
midterm = st.sidebar.number_input("Midterm Score (0-30)", 0.0, 30.0, 22.0)

# 3. الحسابات
input_data = pd.DataFrame([[attendance, study_hours, quiz_avg, midterm]], 
                         columns=['Attendance_Rate', 'Study_Hours_Weekly', 'Quiz_Avg', 'Midterm_Score'])
raw_prediction = model.predict(input_data)[0]
final_prediction = max(35.0, min(100.0, raw_prediction))

# 4. العرض في 3 أعمدة
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🔮 Prediction")
    st.metric("Forecasted Grade", f"{final_prediction:.1f}%")
    if final_prediction >= 85:
        st.success("🏆 Status: Elite Scholar")
        st.balloons()
    elif final_prediction >= 65:
        st.info("⭐ Status: Good Standing")
    else:
        st.warning("⚠️ Status: Needs Improvement")

with col2:
    st.subheader("🤖 AI Coach")
    if attendance < 75:
        st.error("🚨 Attendance is low!")
    if study_hours < 20:
        st.warning("📚 Study more hours.")
    if final_prediction >= 85:
        st.write("Keep it up!")

with col3:
    st.subheader("🎯 Goal Planner")
    target = st.number_input("Target Grade %", 40, 100, 90)
    if target > final_prediction:
        extra_hours = (target - final_prediction) / 1.8
        st.info(f"💡 Add {extra_hours:.1f} hrs/week.")
    else:
        st.success("Target reached!")

st.markdown("---")
with st.expander("👨‍🏫 Educator Portal"):
    if final_prediction < 60:
        st.error("⚠️ Student at high risk!")
    else:
        st.write("✅ Performance is stable.")
