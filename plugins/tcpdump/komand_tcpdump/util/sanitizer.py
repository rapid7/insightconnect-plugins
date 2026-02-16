import re
import shlex
from insightconnect_plugin_runtime.exceptions import PluginException
from .constants import (
    DANGEROUS_CHARS_PATTERN,
    DANGEROUS_SEQUENCES,
    ALLOWED_TCPDUMP_OPTIONS,
    MAX_FILTER_LENGTH,
    MAX_OPTIONS_LENGTH,
)


def validate_options(options: str) -> list:  # noqa: MC0001
    # If options is empty or only whitespace, return an empty list
    if not options or not options.strip():
        return []

    # Check length
    if len(options) > MAX_OPTIONS_LENGTH:
        raise PluginException(
            cause="Options string too long. ", assistance=f"Options must be less than {MAX_OPTIONS_LENGTH} characters"
        )

    # Check for dangerous sequences
    for sequence in DANGEROUS_SEQUENCES:
        if sequence in options:
            raise PluginException(
                cause="Invalid options provided. ", assistance=f"Options contain dangerous sequence: {sequence}"
            )

    # Parse options safely using shlex
    try:
        parsed_options = shlex.split(options)
    except ValueError as error:
        raise PluginException(cause="Invalid options format. ", assistance=f"Failed to parse options: {str(error)}")

    # Validate each option against whitelist
    validated_options = []
    for option in parsed_options:
        if option.startswith("-"):
            # Extract the option flag (e.g., '-v' from '-v' or '-c' from '-c=value')
            option_flag = option.split("=")[0]

            # Check if it's a valid option
            if option_flag not in ALLOWED_TCPDUMP_OPTIONS:
                raise PluginException(
                    cause="Invalid tcpdump option. ", assistance=f"Option '{option_flag}' is not in the allowed list"
                )

            # Additional validation for options with = separator
            if "=" in option:
                if re.search(DANGEROUS_CHARS_PATTERN, option.split("=", 1)[1]):
                    raise PluginException(
                        cause="Invalid option value. ",
                        assistance=f"Option value contains dangerous characters: {option}",
                    )
        else:
            # This is an argument to the previous option (e.g., '10' in '-c 10')
            # Validate it doesn't contain dangerous characters
            if re.search(DANGEROUS_CHARS_PATTERN, option):
                raise PluginException(
                    cause="Invalid option argument. ",
                    assistance=f"Option argument contains dangerous characters: {option}",
                )

        validated_options.append(option)
    return validated_options


def validate_filter(filter_: str) -> str:
    # If filter is empty or only whitespace, return an empty string
    if not filter_ or not filter_.strip():
        return ""

    # Check length
    if len(filter_) > MAX_FILTER_LENGTH:
        raise PluginException(
            cause="Filter expression too long. ", assistance=f"Filter must be less than {MAX_FILTER_LENGTH} characters"
        )

    # Check for dangerous sequences
    for sequence in DANGEROUS_SEQUENCES:
        if sequence in filter_:
            raise PluginException(
                cause="Invalid filter expression. ", assistance=f"Filter contains dangerous sequence: {sequence}"
            )

    # Check for shell metacharacters that shouldn't be in BPF
    dangerous_chars = ["|", "&", ";", "`", "$", "<", ">"]
    for character in dangerous_chars:
        if character in filter_:
            raise PluginException(
                cause="Invalid filter expression. ", assistance=f"Filter contains dangerous character: {character}"
            )

    # Basic regex to allow only characters typically used in syntax
    allowed_pattern = r"^[a-zA-Z0-9\s\.\:\[\]\(\)\/\-\=\!\<\>]+$"
    if not re.match(allowed_pattern, filter_):
        raise PluginException(
            cause="Invalid filter expression. ", assistance="Filter contains invalid characters for BPF syntax"
        )
    return filter_.strip()
