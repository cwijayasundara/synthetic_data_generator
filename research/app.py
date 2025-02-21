from openai import OpenAI
import json
from IPython.display import display, HTML
from sklearn.metrics import precision_score, recall_score, f1_score
from concurrent.futures import ThreadPoolExecutor, as_completed
import csv
import pandas as pd
from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI
from llama_index.core import ChatPromptTemplate
from llama_index.core.llms import ChatMessage, MessageRole
from prompt_txt import data_gen_prompt, data_examples
import time
from tenacity import retry, stop_after_attempt, wait_exponential

_ = load_dotenv()

# Configure LLM with longer timeout and retry settings
llm = OpenAI(
    model="gpt-4o-mini",
    temperature=1.0,
    timeout=60,  # Increase timeout to 60 seconds
    max_retries=3,  # Add retry attempts
)

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10)
)
def generate_response(template, prompt):
    try:
        return llm.complete(prompt)
    except Exception as e:
        print(f"Error generating response: {str(e)}")
        raise

message_templates = [
    ChatMessage(
        content="You are an expert system.",
        role=MessageRole.SYSTEM
    ),
    ChatMessage(
        content=data_gen_prompt,
        role=MessageRole.USER,
    ),
]

chat_template = ChatPromptTemplate(message_templates=message_templates)
prompt = chat_template.format(examples=data_examples)

try:
    response = generate_response(chat_template, prompt)
    print(response)
except Exception as e:
    print(f"Failed to generate response after retries: {str(e)}")