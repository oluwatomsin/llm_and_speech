import requests as r
from envyaml import EnvYAML
from engine.utils import retry_on_failure, save_to_memory
import dotenv
from engine.utils import logger


dotenv.load_dotenv()

# loading configurations and environment variables for the audio service
eleven_labs_config = EnvYAML('config/config.yaml').get('audio_services.eleven_labs')


@save_to_memory(audio_name="audios/final_audio.mp3", chunk_size=eleven_labs_config.get('CHUNK_SIZE'))
@retry_on_failure(max_retries=3, delay=2)
def get_audio(text: str):
    """
    This function is responsible for speech synthesis using the elevenlabs API.
    :param text: The input text by the user.
    :return: the response object from the API.
    """
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": f"{eleven_labs_config.get('xi-api-key')}"
    }

    data = {
        "text": f"{text}",
        "model_id": f"{eleven_labs_config.get('model_id')}",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }
    response = r.post(url=eleven_labs_config.get('url'), json=data, headers=headers)
    if response.status_code != 200:
        logger.error("Error occurred while attempting to generate audio")
        raise Exception(f"Connection was established, but error occurred in communication with API:\n Connection "
                        f"Status code: {response.status_code}\n"
                        f"Content: {response.content}")
    logger.info("Audio Generation Successful")
    return response
