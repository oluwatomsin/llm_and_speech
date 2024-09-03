from dotenv import load_dotenv
from engine.audio_synthesis import get_audio
from engine.chat_utils import get_summary
from engine.utils import logger

load_dotenv()


def main(path='doc.txt'):
        logger.info("Starting the Vocal Summarization Process...")
        logger.info("Step 1. Attempting to get summarization")
        text = get_summary(file_path=path)
        logger.info("Step 2. Attempting to generate audio")
        get_audio(text=text)
        logger.info('Process Completed Successfully.')


if __name__ == '__main__':
        main()
