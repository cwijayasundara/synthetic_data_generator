from dotenv import load_dotenv
import os
from llama_index.readers.web import SimpleWebPageReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.core import VectorStoreIndex
from llama_index.embeddings.openai import OpenAIEmbedding
import chromadb

_ = load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

embed_model = OpenAIEmbedding(model_name="text-embedding-3-large")

vector_db_loc = "./account_data"
vector_db_name = "accounts"

page_urls = [
    "https://www.lloydsbank.com/savings.html",
    "https://www.lloydsbank.com/isas.html#instant",
    "https://www.lloydsbank.com/isas.html#investments",
    "https://www.gov.uk/individual-savings-accounts/how-isas-work"
]

documents = SimpleWebPageReader(html_to_text=True).load_data(page_urls)

db = chromadb.PersistentClient(path=vector_db_loc)

chroma_collection = db.get_or_create_collection(vector_db_name)

vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

storage_context = StorageContext.from_defaults(vector_store=vector_store)

index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, embed_model=embed_model
)

# test
# query = "whats the intrest rate for club Lloyds advantage ISA saver?"
# query_engine = index.as_query_engine()
# response_1 = query_engine.query(query) 
# print(response_1)

