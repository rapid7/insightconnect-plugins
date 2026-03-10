import base64
import pypandoc
from tempfile import NamedTemporaryFile
from icon_markdown.util.constants import UTF_ENCODING, LATIN_ENCODING


def from_bytes(_bytes):
    return base64.b64decode(bytes(_bytes, UTF_ENCODING)).decode(UTF_ENCODING)


def to_bytes(_string):
    return base64.b64encode(bytes(_string, UTF_ENCODING)).decode(UTF_ENCODING)


def to_bytes_pdf(_bytes):
    return base64.b64encode(_bytes).decode(UTF_ENCODING)


def make_file(filetype):
    with NamedTemporaryFile("w", suffix="." + filetype, delete=False) as f:
        return f.name


def read_file(filename):
    with open(filename, "rb") as f:
        return f.read()


def write_file(filename, content):
    with open(filename, "wb") as f:
        f.write(content)


def convert(content, from_format, to_format, use_file=False):
    if use_file:
        filename = make_file(to_format)
    else:
        filename = None
    # Use --markdown-headings=atx for pandoc >= 2.11.2
    output = pypandoc.convert_text(
        content,
        to_format,
        format=from_format,
        outputfile=filename,
        extra_args=["--markdown-headings=atx"],
    )
    if use_file:
        content = read_file(filename)
        try:
            return content.decode(UTF_ENCODING)
        except UnicodeDecodeError:
            return content.decode(LATIN_ENCODING)
    else:
        return output
