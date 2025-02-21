from dotenv import load_dotenv
from langchain_community.document_loaders import RecursiveUrlLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from langchain_chroma import Chroma
from langchain_community.vectorstores.utils import filter_complex_metadata
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

_ = load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

page_urls = [
    "https://www.lloydsbank.com/savings.html",
    "https://www.lloydsbank.com/isas.html#instant",
    "https://www.lloydsbank.com/isas.html#investments",
    "https://www.gov.uk/individual-savings-accounts/how-isas-work"
]

embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004", api_key=api_key)

docs = []

vector_store = Chroma(
    collection_name="account_data",
    embedding_function=embeddings,
    persist_directory="./account_data_kb",
)

docs = []
for url in page_urls:
    loader_multiple_pages = RecursiveUrlLoader(url)
    doc = loader_multiple_pages.load()
    print(doc)
    docs.append(doc)
