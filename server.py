from dotenv import load_dotenv
import streamlit as st

load_dotenv()


pg = st. navigation([
    st.Page('tabs/about.py', title='About Project', icon=":material/favorite:"),
    st.Page('tabs/text_summary.py', title='Text Summarization', icon=":material/summarize:"),
    st.Page('tabs/author.py', title='About Author', icon=":material/person:")

])
pg.run()
