from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

_ = load_dotenv()

gpt_4o = init_chat_model("gpt-4o-mini", 
                         model_provider="openai", 
                         temperature=0)

claude_opus = init_chat_model("claude-3-opus-20240229", 
                              model_provider="anthropic", 
                              temperature=0)

gemini_15 = init_chat_model("gemini-1.5-pro", 
                            model_provider="google_genai", 
                            temperature=0)

prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")

chain = prompt | claude_opus | StrOutputParser()

response = chain.invoke({"topic": "bears"})

print(response)

