import streamlit as st
import plotly.express as px
import pandas as pd


st.title("In Search for Happiness")
x = st.selectbox("Select the data for the X-axis",("GDP","happiness","generosity"))
x = x.lower()
y = st.selectbox("Select the data for the Y-axis",("GDP","happiness","generosity"))
y = y.lower()

st.subheader(f"{x} and {y}")

df = pd.read_csv("happy.csv",index_col=False)

X = df[x]
Y = df[y]

figure = px.line(X,Y,labels={"x":f"{x}","y":f"{y}"})
st.plotly_chart(figure)
