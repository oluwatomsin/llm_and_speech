import streamlit as st

st.markdown('# Vocal Summarization')

st.write("""
Welcome to the Vocal Summarization project! This tool is designed to help you quickly digest large amounts of information by summarizing text and converting it into audio.

### What This Project Does:
- **Input Options**: You can either type in text directly or upload a .txt file containing the information you want summarized.
- **Summary Generation**: Using advanced AI (GPT-4.0), the application generates a concise summary of the provided content.
- **Audio Conversion**: The summary is then converted into clear, natural-sounding speech using the ElevenLabs API.
- **Listen to Your Summary**: Finally, you can listen to the audio summary right within the application.

### Benefits of This Application:
1. **Time-Saving**: Quickly understand large documents without having to read through all the text.
2. **Accessibility**: Provides an audio format, making it accessible to those who prefer listening over reading or have visual impairments.
3. **Convenience**: Easily listen to summaries while multitasking, whether you're commuting, exercising, or relaxing.
4. **Improved Retention**: Listening to summaries can help reinforce the information and improve retention.
""")
