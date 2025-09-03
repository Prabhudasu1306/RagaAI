import streamlit as st
import pandas as pd
from src.agent import SchedulingAgent

st.set_page_config(page_title="AI Scheduling Agent", layout="centered")

st.title("🩺 AI Medical Appointment Scheduler")

if "agent" not in st.session_state:
    st.session_state.agent = SchedulingAgent()

if "greeted" not in st.session_state:
    st.chat_message("assistant").write(
        "👋 Hello! I’m your AI Medical Assistant.\n\n"
        "I can help you schedule a doctor’s appointment.\n"
        "Please start by telling me your **full name** and **date of birth (YYYY-MM-DD)**."
    )
    st.session_state.greeted = True

user_input = st.chat_input("Enter your response...")

if user_input:
    response = st.session_state.agent.chat(user_input)
    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(response)
