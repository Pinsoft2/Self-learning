import requests
import selectorlib
import pandas as pd
import streamlit as st
import plotly.express as px
import sqlite3
from datetime import datetime
import time

URL = "https://programmer100.pythonanywhere.com/"

def scrape(URL):
    response = requests.get(URL)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["home"]
    # print(f"Data scrapped! {value}")
    return value

def store(extracted):
    with open("data.txt","a") as file:
        file.write("date,temp\n")
    with open("data.txt","a") as file:
        file.write(current_time + "," + extracted + "\n")


#initiate SQL"""
def SQL_initiate(db):
    cursor = connection.cursor()
#     cursor.execute("""SELECT tableName FROM sqlite_master WHERE type='table'
#   AND tableName='events'; """)
    if cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='events'""").fetchone() ==None:
        table = """ CREATE TABLE events (
                Date text NOT NULL,
                Temp integer NOT NULL
            ) """
        cursor.execute(table)
        connection.commit()
        print("Table is Ready")

#store data into SQL"""
def SQL_store(current_time, extracted):
    # row = extracted.split(",")
    # row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?)", (current_time, extracted))
    connection.commit()

#read data from SQL"""
def SQL_read():
    # row = extracted.split(",")
    # row = [item.strip() for item in row]
    # print(row)
    # date, temp = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events")
    # cursor.execute("SELECT * FROM events WHERE Date=? AND Temp=?", (current_time, extracted))
    rows = cursor.fetchall()
    cursor = connection.cursor()
    row = cursor.execute("""SELECT * FROM events ORDER BY Date""").fetchall()
    for i in row:
        dates_array.append(i[0])
        temps_array.append(i[1])
    return dates_array, temps_array

#read from SQL and then pull plot """
def plot(dates_array, temps_array):
#     SQLSource = "data.txt"
#     df = pd.read_csv(SQLSource)
#     dates = df["date"]
#     temps = df["temp"]
    figure = px.line(x = dates_array, y = temps_array, labels={"x": "date", "y": "Temperature"})
    st.plotly_chart(figure)

if __name__ == "__main__":
    connection = sqlite3.connect("data.db")
    while True:
        SQL_initiate("data.db")
        dates_array = []
        temps_array = []
        pl = st.empty()
        scraped = scrape(URL)
        extracted = extract(scraped)
        dt = datetime.now()
        current_time = dt.strftime("%y-%m-%d-%H-%M-%S")
        SQL_store(current_time, extracted)
        SQL_read()
        pl = plot(dates_array, temps_array)
        time.sleep(1)
        # Close the connection
        #connection_obj.close()



