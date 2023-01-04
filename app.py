from streamlit_webrtc import webrtc_streamer, RTCConfiguration
import av
import cv2


from io import StringIO
from pathlib import Path
import streamlit as st
import time
import os
import sys
import argparse
from PIL import Image


from io import BytesIO
import base64
from rembg import remove


#################################### GUI Code ##################################################

st.title('Computer Vision')
st.sidebar.write("## Upload and download :gear:")
col1, col2 = st.columns(2)
source = ("Face Recognization in Image", "Face detection in MP4 Video", "Face detection in Webcam", "Remove background")
source_index = st.sidebar.selectbox("Select", range(
        len(source)), format_func=lambda x: source[x])


############################### Download Fuction ################################################
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


################################## Code for Face recognization ###################################

cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

class VideoProcessor:
	def recv(self, frame):
		frm = frame.to_ndarray(format="bgr24")

		faces = cascade.detectMultiScale(cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY), 1.1, 3)

		for x,y,w,h in faces:
			cv2.rectangle(frm, (x,y), (x+w, y+h), (0,255,0), 3)

		return av.VideoFrame.from_ndarray(frm, format='bgr24')



################################# Uploading image ##################################################

if source_index == 0:
        uploaded_file1 = st.sidebar.file_uploader("Upload Picture", type=['png', 'jpeg', 'jpg'])
        if uploaded_file1 is not None:
            with st.spinner(text='Loading...'):
                 st.sidebar.image(uploaded_file1)
                 picture = Image.open(uploaded_file1)
                 st.caption("**:red[This is original uploaded image.]** :pencil:")
                 st.image(uploaded_file1)
                 
       
################################# Uploading Video ##################################################

if source_index == 1:
        uploaded_file2 = st.sidebar.file_uploader("Upload Video", type=['mp4'])
        if uploaded_file2 is not None:
            with st.spinner(text='Loading...'):
                 st.sidebar.video(uploaded_file2)
                 st.caption("**:red[This is original uploaded video.]** :pencil:")
                 st.video(uploaded_file2)
                 col1.video(uploaded_file2)
                 
               

################################# Connecting Webcam ##################################################

if source_index == 2:
    st.caption("**:green[Face Detection Fuction.]** :pencil:")
    webrtc_streamer(key="key", video_processor_factory=VideoProcessor,
				rtc_configuration=RTCConfiguration(
					{"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
					)
	)
	
################################# Background Remove ##################################################

if source_index == 3: 
    st.write("**:blue[This is Background Remove Fuction.]** :pencil:")
    uploaded_file3 = st.sidebar.file_uploader("Upload Picture", type=['png', 'jpeg', 'jpg'])
    #st.markdown("**:green[Let's Start the program.]** :pencil:")
    if uploaded_file3 is not None:
                with st.spinner(text='Loading...'):
                 st.sidebar.image(uploaded_file3)
                 picture = Image.open(uploaded_file3)
                 fixed = remove(picture)
                 col1.write("Original Image :wrench:")
                 col1.image(picture)
                 col2.write("Result Image :wrench:")
                 col2.image(fixed)
                 st.sidebar.markdown("\n")
                 st.sidebar.download_button("Download Result Image", convert_image(fixed), "Result.png", "image/png")
   





