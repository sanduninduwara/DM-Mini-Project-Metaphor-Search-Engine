import gradio as gr
from elasticsearch import Elasticsearch
from search import *

es = Elasticsearch([{'host': 'localhost', 'port': 9200, "scheme": "http"}])

def clean_text(text):
    cleaned_text = text.replace('\n', '')
    return cleaned_text

def generate_poem_response(poem_data):
    response_string = ""
    for obj in poem_data:
        cleaned_data = {key: clean_text(value) if isinstance(value, str) else value for key, value in obj["_source"].items()}
        response_string += '\n'.join([f'{key}: {value}' for key, value in cleaned_data.items()])
        response_string += "\n______________________________________________________________________________\n"
    return response_string

def random_response(key,fuzzy,data):
    print(key,fuzzy,data)
    res=match_query(es,key,data,fuzzy)
    return generate_poem_response((res["hits"])["hits"])


iface = gr.Interface(
    fn=random_response, 
    inputs=[
        gr.Dropdown(
            ["poem_name", "poet", "line","Metaphor_in_English","Metaphor meaning in English" , "Year" ], label="Keys", 
        ),
        gr.Dropdown(
            [True,False], label="Fuzzy", 
        ),
        gr.inputs.Textbox(lines=2, label="value"),
    ], 
    outputs="text",
    title="Metaphore Search"
)

iface.launch()

