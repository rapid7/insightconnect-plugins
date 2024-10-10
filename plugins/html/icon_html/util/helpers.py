import base64
from typing import Union

import pypandoc

from icon_html.util.constants import DEFAULT_ENCODING


def encode_to_base64(content: Union[str, bytes]) -> str:
    if isinstance(content, str):
        content = content.encode(DEFAULT_ENCODING)
    return base64.b64encode(content).decode(DEFAULT_ENCODING)


def read_file_content(filename: str) -> str:
    with open(filename, "rb") as file_:
        return encode_to_base64(file_.read())


def convert_with_temporary_file(
    input_html_string: str, to_format: str, from_format: str, temporary_filename: str, *args, **kwargs
) -> str:
    pypandoc.convert_text(input_html_string, to_format, from_format, outputfile=temporary_filename, *args, **kwargs)
    return read_file_content(temporary_filename)
