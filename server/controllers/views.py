import json
from flask import jsonify, request, send_from_directory


# sanity check routes
def _cleanup_attributes(attributes):
    result = {}
    for key in attributes:
        new_key = key[4:len(key)]
        result[new_key] = attributes[key]
    return result

def handle_error(error):
    """ Return JSON instead of HTML for HTTP errors."""
    response = error.get_response()
    accept = request.headers.get('accept')
    if accept and accept.split(',')[0].lower == 'application/json':
        response.data = json.dumps({
            "code": error.code,
            "name": error.name,
            "description": error.description,
        })
        response.content_type = "application/json"
    else:
        response.data = f'HTTP {error.code}: {error.name}. {error.description}'
    return response

def ping_pong():
    return jsonify('pong!')

def index():
    return send_from_directory("static", "index.html")

