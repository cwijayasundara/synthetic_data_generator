from llama_parse import LlamaParse
from typing import List
from llama_index.core.schema import TextNode
import json

parsing_instruction = """
You are given a document with tables, graphs and diagrams. 
For any graphs, try to create a 2D table of relevant values, along with a description of the graph.
For any schematic diagrams, MAKE SURE to describe a list of all components and their connections to each other.
Make sure that you always parse out the text with the correct reading order.
"""

def get_text_nodes(json_list: List[dict]):
    text_nodes = []
    for idx, page in enumerate(json_list):
        text_node = TextNode(text=page["md"], metadata={"page": page["page"]})
        text_nodes.append(text_node)
    return text_nodes

def save_jsonl(data_list, filename):
    """Save a list of dictionaries as JSON Lines."""
    with open(filename, "w") as file:
        for item in data_list:
            json.dump(item, file)
            file.write("\n")


def load_jsonl(filename):
    """Load a list of dictionaries from JSON Lines."""
    data_list = []
    with open(filename, "r") as file:
        for line in file:
            data_list.append(json.loads(line))
    return data_list

def parse_pdf_file(file_path: str) -> str:

    parser = LlamaParse(
        result_type="markdown",
        use_vendor_multimodal_model=True,
        vendor_multimodal_model_name="gemini-2.0-flash-001",
        invalidate_cache=True,
        parsing_instruction=parsing_instruction,
    )

    json_objs = parser.get_json_result(file_path)
    json_list = json_objs[0]["pages"]
    docs = get_text_nodes(json_list)
    return docs



