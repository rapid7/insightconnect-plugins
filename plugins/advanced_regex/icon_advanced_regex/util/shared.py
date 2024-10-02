import re
from typing import Dict, Any


class Input:
    # shared input attributes across all actions
    ASCII = "ascii"
    DOTALL = "dotall"
    IGNORECASE = "ignorecase"
    MULTILINE = "multiline"


def construct_flags(parameters: Dict[str, Any]) -> int:
    combined_flags = 0
    if parameters.get(Input.IGNORECASE, False):
        combined_flags = combined_flags | re.IGNORECASE
    if parameters.get(Input.MULTILINE, False):
        combined_flags = combined_flags | re.MULTILINE
    if parameters.get(Input.DOTALL, False):
        combined_flags = combined_flags | re.DOTALL
    if parameters.get(Input.ASCII, False):
        combined_flags = combined_flags | re.ASCII
    return combined_flags
