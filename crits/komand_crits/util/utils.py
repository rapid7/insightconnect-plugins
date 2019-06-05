import re
from io import StringIO

def file_from_params(filename, content):
    return filename, StringIO(content)


def slugify(name):
    return re.sub(r"([\s:,\-]+)", r"_", name.lower())


def make_response(response):
    message = response.get('message')
    if message and type(message) == list:
        message = ", ".join(message)
        response['message'] = message

    return response
