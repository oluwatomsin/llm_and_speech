from dotenv import load_dotenv
from engine.audio_synthesis import get_audio
from engine.chat_utils import get_summary
from engine.utils import logger
import streamlit as st

load_dotenv()


pg = st. navigation([
    st.Page('tabs/about.py', title='About Project', icon=":material/favorite:"),
    st.Page('tabs/text_summary.py', title='Text Summarization', icon=":material/summarize:")
])
pg.run()
