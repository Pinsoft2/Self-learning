import cv2
#pip install opencv-python
import streamlit as st
from datetime import datetime

st.title("Motion Detector")
cam = st.button("start camera")
streamlit_image = st.image([])

if cam:
    camera = cv2.VideoCapture(1,cv2.CAP_DSHOW)

    while camera.isOpened() is True:
        check, frame = camera.read()
        if check:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            dt = datetime.now()
            weekday = dt.strftime("%A")
            current_time = dt.strftime("%H:%M:%S")
            cv2.putText(img=frame, text=f"{weekday}",org=(50,50),fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(20,100,200),thickness=2,lineType=cv2.LINE_AA)

            cv2.putText(img=frame, text=f"{current_time}",org=(50,80),fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(20,100,200),thickness=2,lineType=cv2.LINE_AA)

            streamlit_image.image(frame)
        else:
            break
            print("Error : Failed to capture frame")
