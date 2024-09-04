from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import dotenv
from engine.utils import logger

dotenv.load_dotenv()

# Loading all component to create a chain
model = ChatOpenAI(model="gpt-4")
system_template = "You are to act as summarizer. Summarize the following message by the user {message}:"
prompt_template = ChatPromptTemplate.from_template(system_template)
parser = StrOutputParser()


def get_summary(message: str):
    """
    This function helps us generated a summarization from an LLM based in a specific
    text to .txt document provided by the user.
    NB: Only one of messages or file_path should be provided, if both are provided, the file path will be used.
    :param message: The text that will be summarized by the LLM
    :param file_path: The path to the text document to be summarized.
    :return: the summary generated by the model
    """

    try:
        assert len(message) < 10000
    except AssertionError:
        logger.debug("The number of character in text must not exceed 10000.")
        return None

    chain = prompt_template | model | parser
    response = chain.invoke({'message': f"{message}"})
    logger.info("Summary successfully generated.")
    return response