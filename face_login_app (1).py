import streamlit as st
import face_recognition
import cv2
import numpy as np

st.title("🔐 Face Login AI")

# Load the known face image
try:
    known_image = face_recognition.load_image_file("my_face.jpg")
    known_encoding = face_recognition.face_encodings(known_image)[0]
except:
    st.error("❌ Could not load your face image (my_face.jpg). Make sure it's in the same folder.")
    st.stop()

# Start webcam
run = st.button("Start Face Login")

if run:
    st.info("📸 Scanning your face... Please allow camera access.")

    video_capture = cv2.VideoCapture(0)

    result = st.empty()
    match_found = False

    while True:
        ret, frame = video_capture.read()
        rgb_frame = frame[:, :, ::-1]

        faces = face_recognition.face_locations(rgb_frame)
        encodings = face_recognition.face_encodings(rgb_frame, faces)

        for encoding in encodings:
            matches = face_recognition.compare_faces([known_encoding], encoding)
            if True in matches:
                result.success("✅ Access Granted. Welcome!")
                match_found = True
                break

        if match_found:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()