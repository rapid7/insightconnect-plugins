import base64
import pypandoc
from tempfile import NamedTemporaryFile


def from_bytes(_bytes):
    return base64.b64decode(bytes(_bytes, 'UTF-8')).decode('UTF-8')


def to_bytes(_string):
    return base64.b64encode(bytes(_string, 'UTF-8')).decode('UTF-8')


def make_file(filetype):
    with NamedTemporaryFile('w', suffix='.'+filetype, delete=False) as f:
        return f.name


def read_file(filename):
    with open(filename, 'rb') as f:
        return f.read()


def write_file(filename, content):
    with open(filename, 'wb') as f:
        f.write(content)


def convert(content, from_format, to_format, use_file=False):
    if use_file:
        filename = make_file(to_format)
    else:
        filename = None
    output = pypandoc.convert_text(
        content, to_format, format=from_format, outputfile=filename)
    if use_file:
        content = read_file(filename)
        try:
            return content.decode('UTF-8')
        except UnicodeDecodeError:
            return content.decode('latin-1')
    else:
        return output
