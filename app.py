from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from file_parser import parse_pdf_file, save_jsonl

_ = load_dotenv()

file_path = "./data/sample_invoice_1.pdf"

gemini_2_flash_thinking = init_chat_model("gemini-2.0-flash-thinking-exp-01-21", 
                                          model_provider="google_genai",  
                                          temperature=1.0)

docs = parse_pdf_file(file_path)

save_jsonl([d.dict() for d in docs], "./parsed_data/dental.jsonl")                            
                           

