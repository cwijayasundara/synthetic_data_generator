from dotenv import load_dotenv
import os
from llama_index.llms.gemini import Gemini
from llama_index.core import PromptTemplate
from data_gen_prompts import customer_data_gen_prompts

_ = load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

llm = Gemini(model="models/gemini-2.0-flash")

prompt_template = """\
Context information is below.
---------------------
{context_str}
---------------------
Test Data:
"""

prompt = PromptTemplate(prompt_template)

final_prompt = prompt.format(context_str=customer_data_gen_prompts)

response = llm.complete(final_prompt)

response_text = response.text if hasattr(response, 'text') else str(response)

with open("synthetic_customer_data.csv", "w") as f:
    f.write(response_text)

print(response_text)



