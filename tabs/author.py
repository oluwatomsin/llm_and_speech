import streamlit as st

st.markdown('# About the Author')

st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f5;
    }
    .main-content {
        background-color: white;
        padding: 30px;
        border-radius: 10px;
        border: 1px solid #dcdcdc; /* Tiny border */
        box-shadow: 4px 0px 6px rgba(0, 0, 0, 0.1); /* Right shadow */
    }
    h1 {
        color: #2c3e50;
    }
    h3 {
        color: #3498db;
        font-size: 24px;
    }
    p {
        color: #34495e;
        line-height: 1.6;
        font-size: 16px;
    }
    a {
        color: #e74c3c;
        text-decoration: none;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write("""
<div class="main-content">
Hi there! I'm Amusa Abdulahi Tomisin, a passionate Data Scientist with over 4 years of experience specializing in Natural Language Processing (NLP).

### A Little About Me:
- **AI Expertise**: I've had the opportunity to work on diverse projects, including developing AI assistants for MTN at SuperBo and designing data pipelines and training models at Uniccon Group of Companies.
- **Open Source & Volunteering**: I actively contribute to open-source initiatives and have volunteered with organizations like Omdena, where I’ve focused on using AI to address global challenges, particularly in healthcare.
- **Thought Leadership**: Beyond my technical work, I enjoy sharing insights on AI and NLP through writing. My articles on Medium delve into the latest trends, challenges, and innovations in the field.
- **Continuous Learning**: I’m committed to staying at the forefront of technology, continuously learning, and pushing the boundaries of what AI can achieve.

### Let's Connect:
- [Subscribe to my Medium](https://amusatomisin65.medium.com/subscribe) for insights and articles on AI and NLP.
- [Connect with me on LinkedIn](https://www.linkedin.com/in/amusaoluwatomisin/) to explore potential collaborations and stay in touch.
</div>
""", unsafe_allow_html=True)
