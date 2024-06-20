import streamlit as st
import smtplib, ssl
import pandas
import sys
sys.path.append("/workspaces/43708898/python 2.0/NMSL/day22")
from sendemail import email

st.header("contact us")

with st.form(key = "contact_form",clear_on_submit = True):
    user_email = st.text_input("Your email address")
    topics = pandas.read_csv("/workspaces/43708898/python 2.0/NMSL/day22/pages/topics.csv")
    option = st.selectbox("What topic do you want to discuss?", options = topics,key="topic")

    raw_msg = st.text_area("Your message")

    message = f"""\
Subject: Email alert from {user_email}
From: {user_email}
{raw_msg}
"""

    button = st.form_submit_button()

    if button:
        email(message)
        st.info("Email sent!")