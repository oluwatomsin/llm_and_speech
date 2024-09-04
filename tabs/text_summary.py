import streamlit as st
import time
from engine.chat_utils import get_summary
from engine.audio_synthesis import get_audio


@st.cache_resource
def stream_data(data: str):
    """
    This function was created to simulate streaming text data.
    :param data: The data
    :return: None
    """
    for word in data.split(" "):
        yield word + " "
        time.sleep(0.02)


def summary(input_text: str):
    summary_data = get_summary(message=input_text)
    ai_summary = st.write_stream(stream_data(data=summary_data))

    get_audio(text=ai_summary)
    st.audio(data='audios/final_audio.mp3', format='audio/mp3')


st.markdown('# Summarization Tabs')
tab1, tab2 = st.tabs(["text_summary", "file_summary"])

with tab1:
    input_text = st.text_area('Kindly paste the text you want to summarize here.')

    if st.button('Generate Summary', key='001'):
        if len(input_text) < 100 or len(input_text) > 10000 or input_text is None:
            st.warning('The provided text must be between 100 and 10000 characters', icon="⚠️")
        else:
            with st.status('Running'):
                summary(input_text)

with tab2:
    file_upload = st.file_uploader('Upload a .txt file', type=['txt'])

    if st.button('Generate Summary', key='002'):
        input_text = file_upload.read().decode('utf-8')
        if len(input_text) < 100 | len(input_text) > 10000 | input_text is None:
            st.warning('The provided text must be between 100 and 10000 characters', icon="⚠️")
        else:
            with st.status('Running'):
                summary(input_text)






