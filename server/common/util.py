import json
import requests
from flask import request
from sqlalchemy.inspection import inspect

def get_all_req_params():
    params = request.args or {}
    post_params = request.get_data(as_text=True)
    try:
        json_params = json.loads(post_params)
        params.update(json_params)
    except Exception:
        pass
    return params

def json_builder(class_name, item):
    output = {}
    columns = [column.name for column in inspect(class_name).c]
    for c in columns:
        output[c] = getattr(item, c)
    return output

def flatten_and_int(t):
    return [int(item) for sublist in t for item in sublist]
