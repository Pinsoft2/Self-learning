import streamlit as st
from PIL import Image
import requests
import urllib.request

NASA_Apikey = "CxLrteSIWNibhb08R0E8T4eqSLEhMZfbnvNLSvl8"

url = "https://api.nasa.gov/planetary/apod?" \
    "api_key=f'{NASA_Apikey}'"

url2 = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# Make request
response = requests.get(url2)
apod = response.json()
print(apod)
st.set_page_config(layout="wide")

APOD_title = apod["title"]
st.title(APOD_title)

APOD_image = apod["hdurl"]
APOD_image2 = urllib.request.urlretrieve(APOD_image, "APOD.jpg")
st.image(APOD_image)

APOD_content = APOD_image = apod["explanation"]
st.info(APOD_content)

# # body = "Below you can find blablabla"
# # st.text(body)
