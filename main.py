import streamlit as st
import os
from utils import transcribe

# Streamlit app title and description
st.title("Audio Transcription")


# File upload widget
uploaded_file = st.file_uploader("Upload an audio file (max 10MB)", type=["mp3", "wav"])


if uploaded_file:
    # Display the uploaded audio file
    st.audio(uploaded_file, format="audio/mp3")

    # Save the uploaded audio file
    with open("uploaded_audio.mp3", "wb") as f:
        f.write(uploaded_file.read())

    if st.button("Transcribe"):
        # Call the transcribe_audio function to get the transcription
        with st.spinner("Transcribing..."):
            transcription = transcribe(os.path.abspath("uploaded_audio.mp3"))

        if transcription:
            st.success("Transcription complete!")
            st.text_area("Transcription", transcription, disabled=True)

        # Provide a link to download the PDF
        st.download_button(
            label="Download",
            data=transcription,
            file_name="transcription.txt"
        )

        # Clean up the temporary file
        if os.path.exists("uploaded_audio.mp3"):
            os.remove("uploaded_audio.mp3")
