import base64
import magic
from .algorithm import Algorithm

def base64_encode(string):
    return base64.b64encode(string)


def base64_decode(string):
    return base64.b64decode(string)


def determine_compression_type(file_bytes):

    type_description = magic.from_buffer(file_bytes).lower()

    if Algorithm.GZIP in type_description:
        return Algorithm.GZIP
    elif Algorithm.BZIP in type_description:
        return Algorithm.BZIP
    elif Algorithm.LZ in type_description:
        return Algorithm.LZ
    elif Algorithm.XZ in type_description:
        return Algorithm.XZ
    elif Algorithm.ZIP in type_description:
        return Algorithm.ZIP
    else:
        raise Exception("No compression type could be discerned from magic type description.")
