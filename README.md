Vocal Summarizer
================

Project Overview
----------------

Vocal Summarizer is a versatile tool designed to transform articles, small books, and other textual content into concise, easy-to-digest summaries. These summaries are then converted into high-quality audio, providing users with an accessible and convenient way to consume content on the go. This project harnesses the power of OpenAI's advanced language models for text summarization and ElevenLabs' cutting-edge technology for generating human-like speech.

Features
--------

*   **Text Summarization:** Automatically distills lengthy texts into concise, meaningful summaries using advanced natural language processing (NLP) techniques.
    
*   **Audio Generation:** Converts text summaries into clear, realistic audio, allowing users to listen to summaries anytime, anywhere.
    
*   **Customizable Output:** Users can adjust the length and level of detail in the summaries to suit their preferences.
    
*   **File Upload Support:** Accepts text input directly or through uploaded .txt files, providing flexibility in how content is processed.
    

Technology Stack
----------------

*   **OpenAI:** Utilized for generating accurate and contextually relevant summaries through GPT-4 models.
    
*   **ElevenLabs:** Employed to convert text summaries into high-quality, human-like speech audio.
    

Getting Started
---------------

1.  `` git clone https://github.com/oluwatomsin/llm_and_speech.git
    ``
2.  **Create a .env File:**
    
    *   Create a .env file in the project root by copying the provided .env\_example file.
    
    *   `` cp .env\_example .env
        ``
    *   Open the .env file and replace the placeholder values with your actual API keys and configuration details.
        
3.  `` pip install -r requirements.txt
    ``
    
4.  `` streamlit run app.py
    ``
    

Usage
-----

1.  **Input:** Enter text directly into the input field or upload a .txt file.
    
2.  **Summarization:** Click "Summarize" to generate a concise summary.
    
3.  **Audio Generation:** Convert the summary to audio with a single click.
    

Future Enhancements
-------------------

*   **Multi-language Support:** Expand capabilities to support multiple languages for both text and audio.
    
*   **API Integration:** Provide an API for external applications to use the summarization and audio features.
    
*   **Advanced Customization:** Offer more granular control over the summarization process, including tone and style options.
    

Contributing
------------

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss potential improvements or features.

License
-------

This project is licensed under the MIT License