import json
from werkzeug.exceptions import HTTPException

from server.common.constants import *
from server.controllers.views import (
    handle_error, ping_pong, index
)
# from server.controllers.tests import ()

url_patterns = [
    (f'/', index),
    (f'/ping', ping_pong),


    # Vue routes
    # (f'/{PROJECT_NAME}', vue),

    # API routes
    # (f'/{PROJECT_NAME}/tests', get_tests),
    # (f'/{PROJECT_NAME}/tests/create', create_test, {'methods': ['POST']})
]


def register_urlpatterns(app):
    endpoint = 1
    for pattern in url_patterns:
        assert len(pattern) in (2, 3), f'Invalid pattern: {pattern}'
        options = {}
        if len(pattern) == 3:
            rule, view_func, options = pattern
        else:
            rule, view_func = pattern
        endpoint = endpoint + 1
        app.add_url_rule(rule, endpoint=str(endpoint), view_func=view_func, **options)
        app.errorhandler(HTTPException)(handle_error) 
