import streamlit as st
import os
from utils import transcribe

# Streamlit app title and description
st.title("Audio Transcription App with Whisper")
st.write("Upload an audio file and get a transcription in PDF format.")

# File upload widget
uploaded_file = st.file_uploader("Upload an audio file (max 10MB)", type=["mp3", "wav"])


if uploaded_file:
    # Display the uploaded audio file
    st.audio(uploaded_file, format="audio/mp3")

    if st.button("Transcribe"):
        # Call the transcribe_audio function to get the transcription
        transcription = transcribe(uploaded_file)

        # Display the transcription
        st.write("Transcription:")
        st.write(transcription)

        # Offer a download link for the transcription in PDF format
        st.write("Download Transcription:")
        # Save transcription to a temporary file
        tmp_file_path = "temp_transcription.txt"
        with open(tmp_file_path, "w") as tmp_file:
            tmp_file.write(transcription)

        # Provide a link to download the PDF
        st.download_button(
            label="Download",
            data=tmp_file_path,
            file_name="transcription.pdf",
            mime="application/pdf"
        )

        # Clean up the temporary file
        os.remove(tmp_file_path)
