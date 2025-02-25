from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.callbacks import StreamingStdOutCallbackHandler
import os

_ = load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

claude_3_7_sonnet = init_chat_model('claude-3-7-sonnet-latest',
                              model_provider='anthropic',
                              temperature=0.5,
                              streaming=True,
                              callbacks=[StreamingStdOutCallbackHandler()])


response = claude_3_7_sonnet.invoke("Generate a sonnet about the ocean.")
print(response.content)