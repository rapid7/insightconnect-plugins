import base64
import os
import uuid

import pypandoc
import structlog
from insightconnect_plugin_runtime.exceptions import PluginException
from typing import Union

from icon_html.util.constants import DEFAULT_ENCODING


def encode_to_base64(content: Union[str, bytes]) -> str:
    if isinstance(content, str):
        content = content.encode(DEFAULT_ENCODING)
    return base64.b64encode(content).decode(DEFAULT_ENCODING)


def read_file_content(filename: str) -> str:
    with open(filename, "rb") as file_:
        return encode_to_base64(file_.read())


def delete_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        pass
    except Exception as e:
        log = structlog.getLogger("action logger")
        log.error("failed to delete file", file_name=file_name, exception=e)


def convert_with_temporary_file(
    input_html_string: str,
    to_format: str,
    from_format: str,
    file_type: str,
    *args,
    **kwargs,
) -> str:
    file_name = f"{uuid.uuid4()}_{file_type}"

    try:
        pypandoc.convert_text(
            input_html_string,
            to_format,
            from_format,
            outputfile=file_name,
            *args,
            **kwargs,
        )
        file = read_file_content(file_name)
    except Exception as e:
        log = structlog.getLogger("action logger")
        log.error("failed to execute action step", file_name=file_name, exception=e)
        raise PluginException(
            cause="failed to execute step",
            assistance="Check the plugin logs. If executing in the cloud, ensure html tags are not linking to resources on the internet.",
            data=e,
        )
    finally:
        delete_file(file_name)

    return file
