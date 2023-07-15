from pptx import Presentation
import json

def pptx_generator():
    json_data=None
    with open('sample.json','r') as f:
        json_data=json.load(f)
    for item in json_data['presentation']:
        print(item)
        
pptx_generator()