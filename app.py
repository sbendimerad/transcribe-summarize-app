import streamlit as st
from audio_utils import convert_to_mp3, transcribe_audio
from summarization_utils import summarize_text_with_chatgpt


def main():
    st.title("Audio Transcription and Summarization App")

    # File upload
    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

    # Initialize variables
    transcribed_text = ""
    summarized_text = ""

    if uploaded_file is not None:
        st.audio(uploaded_file, format="audio/mp3")

        # Convert uploaded audio to MP3 format
        mp3_file_path = convert_to_mp3(uploaded_file)

        # Transcribe the MP3 audio
        transcribed_text = transcribe_audio(mp3_file_path)
        summarized_text = summarize_text_with_chatgpt(transcribed_text)

    # Display results
    st.write("Summarized Text:")
    st.write(summarized_text)

if __name__ == "__main__":
    main()
