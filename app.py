import streamlit as st
import pandas as pd
from utils import analyze_student
from ai_helper import get_feedback

st.set_page_config(page_title="Student AI Analyzer")

st.title("📊 Student Performance Assistant")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader("Select Student")
    student_name = st.selectbox("Choose", df["Name"])

    student_row = df[df["Name"] == student_name].iloc[0]

    analysis = analyze_student(student_row)

    st.subheader("📌 Performance Summary")
    st.write(f"Average Score: {analysis['Average']}")
    st.write(f"Strong Subject: {analysis['Strong']}")
    st.write(f"Weak Subject: {analysis['Weak']}")

    st.subheader("📉 Subject Gaps (vs your average)")
    st.write(analysis["Gaps"])

    if st.button("Get AI Advice"):
        feedback = get_feedback(student_name, analysis)
        st.subheader("🤖 AI Feedback")
        st.write(feedback)
