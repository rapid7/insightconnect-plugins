import base64
from pathlib import Path
from typing import Optional

import magic
from insightconnect_plugin_runtime.exceptions import PluginException

from .algorithm import Algorithm
from .constants import INVALID_FILENAME_ERROR, UNKNOWN_COMPRESSION_TYPE_ERROR

# Ordered signatures that can be additionaly checked after libmagic
MAGIC_BYTE_SIGNATURES: list = [
    (b"\xfd\x37\x7a\x58\x5a\x00", Algorithm.XZ),
    (b"\x50\x4b\x03\x04", Algorithm.ZIP),
    (b"\x50\x4b\x05\x06", Algorithm.ZIP),
    (b"\x5d\x00\x00", Algorithm.LZ),
    (b"\x1f\x8b", Algorithm.GZIP),
    (b"\x42\x5a", Algorithm.BZIP),
]


def _detect_by_magic_bytes(file_bytes: bytes) -> Optional[str]:
    for signature, algorithm in MAGIC_BYTE_SIGNATURES:
        if file_bytes.startswith(signature):
            return algorithm


def determine_compression_type(file_bytes: bytes) -> str:
    # Get file type description
    type_description = magic.from_buffer(file_bytes).lower()

    # Determine algorithm
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

    # Check magic byte signatures when libmagic returns no results
    if fallback_result := _detect_by_magic_bytes(file_bytes):
        return fallback_result

    # In case no compresion type was found, raise PluginException
    raise PluginException(
        cause="Unknown compression type.",
        assistance=UNKNOWN_COMPRESSION_TYPE_ERROR,
    )


def sanitize_filename(filename: str) -> str:
    sanitized = Path(filename).name
    if not sanitized or sanitized in (".", ".."):
        raise PluginException(
            cause="Invalid filename provided.",
            assistance=INVALID_FILENAME_ERROR,
        )
    return sanitized
