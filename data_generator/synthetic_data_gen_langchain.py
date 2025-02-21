from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate
from data_gen_prompts import customer_data_gen_prompts

_ = load_dotenv()

gemini_2_0_flash_thinking = init_chat_model('gemini-2.0-flash-thinking-exp-01-21',
                              model_provider='google_genai',
                              temperature=0.5,
                              streaming=True,
                              callbacks=[StreamingStdOutCallbackHandler()])

prompt_str = """\
Context information is below.
---------------------
{context_str}
---------------------
Test Data:
"""
prompt_template = PromptTemplate.from_template(prompt_str)

prompt = prompt_template.invoke({"context_str": customer_data_gen_prompts})

response = gemini_2_0_flash_thinking.invoke(prompt)

with open('customer_data_output.csv', 'w') as f:
    f.write(response.content)  # changed from response to response.content to write string
    f.close()