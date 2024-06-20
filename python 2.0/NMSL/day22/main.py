import streamlit as st
import pandas
from PIL import Image


st.set_page_config(layout="wide")

st.title("The best company")
content = """
Hi, I am Ardit! I am a Python programmer, teacher, and founder of PythonHow. I graduated in 2013 with a Master of Science in Geospatial Technologies from the University of Muenster in Germany with a focus on using Python for remote sensing.
I have worked with companies from various countries, such as the Center for Conservation Geography, to map and understand Australian ecosystems, image processing with the Swiss in-Terra, and performing data mining to gain business insights with the Australian Rapid Intelligence.
"""
st.info(content)

body = "Below you can find blablabla"
st.text(body)

col1, col2, col3= st.columns(3)

data = pandas.read_csv("data.csv")

number_per_col = round((len(data)-1)/3)

with col1:
    for index,row in data[:number_per_col].iterrows():
        st.header(row["first name"]+row["last name"])
        st.write(row["role"])
        st.image(Image.open("images/"+row["image"]))


with col2:
    for index,row in data[number_per_col:number_per_col*2].iterrows():
        st.header(row["first name"]+row["last name"])
        st.write(row["role"])
        st.image(Image.open("images/"+row["image"]))


with col3:
    for index,row in data[number_per_col*2:].iterrows():
        st.header(row["first name"]+row["last name"])
        st.write(row["role"])
        st.image(Image.open("images/"+row["image"]))


