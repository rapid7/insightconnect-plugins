import re


class Input:
    # shared input attributes across all actions
    ASCII = "ascii"
    DOTALL = "dotall"
    IGNORECASE = "ignorecase"
    MULTILINE = "multiline"


def constructFlags(input):
    combined_flags = 0

    if input.get(Input.IGNORECASE, False):
        combined_flags = combined_flags | re.IGNORECASE
    if input.get(Input.MULTILINE, False):
        combined_flags = combined_flags | re.MULTILINE
    if input.get(Input.DOTALL, False):
        combined_flags = combined_flags | re.DOTALL
    if input.get(Input.ASCII, False):
        combined_flags = combined_flags | re.ASCII

    return combined_flags
