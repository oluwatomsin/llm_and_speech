from dotenv import load_dotenv
from engine.audio_synthesis import get_audio
from engine.chat_utils import get_response
import os


load_dotenv()
# Using OpenAI GPT4o


text = get_response(message="")
get_audio(text=text)
