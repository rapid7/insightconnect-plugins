
from urllib.parse import unquote


def decode_url(url: str) -> str:
    url_split = url.split("?")
    split_url_params = url_split[1].split("&")
    for param in split_url_params:
        if param.split("=")[0] == "url":
            return unquote(param.split("=")[1])
    return url
