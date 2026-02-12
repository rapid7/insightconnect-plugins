import base64
import re
import subprocess  # noqa: B404
from logging import Logger

from insightconnect_plugin_runtime.exceptions import PluginException

from .constants import AWK, DANGEROUS_PATTERNS, DEFAULT_ENCODING, DEFAULT_SUBPROCESS_TIMEOUT, SAFE_AWK_PATTERNS


def validate_expression(expression: str) -> None:
    """
    Validate the awk expression.

    :param expression: AWK expression to validate
    :type expression: str
    """

    # Check for dangerous patterns
    for pattern in DANGEROUS_PATTERNS:
        if re.search(pattern, expression, re.IGNORECASE):
            raise PluginException(
                cause="The awk expression contains wrong syntax.",
                assistance="Please make sure that the expression is valid and try again.",
            )

    # Build combined safe pattern regex
    combined_pattern = "|".join(f"({pattern})" for pattern in SAFE_AWK_PATTERNS)

    # Remove all safe patterns and check if anything dangerous remains
    cleaned = re.sub(combined_pattern, "", expression)
    cleaned = re.sub(r"\s+", "", cleaned)  # Remove remaining whitespace

    # If there are remaining characters that aren't in our whitelist, it might be suspicious
    if cleaned and re.search(r"[^\s]", cleaned):
        # Allow some additional safe characters that might be valid AWK syntax
        remaining_unsafe = re.sub(r"[_a-zA-Z0-9\s]", "", cleaned)
        if remaining_unsafe:
            raise PluginException(
                cause="The awk expression contains unrecognized syntax.",
                assistance="The expression contains characters or patterns that are not recognized as safe AWK syntax. Please ensure the expression uses only standard AWK patterns and functions.",
            )


def preprocess_expression(expression: str) -> str:
    """
    Preprocess and decode base64 encoded expression if needed.

    :param expression: AWK expression (may be base64 encoded)
    :type expression: str

    :return: Decoded expression string
    :rtype str
    """

    # Skip base64 decoding if expression starts with AWK syntax
    if expression.strip().startswith(("{", "/", "$", "BEGIN", "END", "-")):
        return expression

    try:
        # Verify the decoded string looks like valid AWK
        decoded = base64.b64decode(expression).decode(DEFAULT_ENCODING)
        if any(keyword in decoded for keyword in ["{", "print", "$", "BEGIN", "END", "/"]):
            return decoded
    except Exception:  # noqa: B110
        # If decoding fails or doesn't look like valid AWK
        # Return original expression for further validation
        pass
    return expression


def process_lines(log: Logger, text: str | bytes, expression: str) -> bytes:
    """
    Process text using awk expression.

    :param log: Logger instance
    :type log: Logger

    :param text: Text content to process (string or bytes)
    :type text: str or bytes

    :param expression: awk expression to execute
    :type expression: str

    :return: Processed output as bytes
    :rtype bytes
    """

    # Validate inputs
    validate_expression(expression)

    # Convert text to bytes if it's a string
    if isinstance(text, str):
        text_bytes = text.encode(DEFAULT_ENCODING)
    else:
        text_bytes = text

    log.info(f"ProcessLines: awk {expression}")

    try:
        # Use subprocess with proper stdin handling
        with subprocess.Popen(
            [AWK, expression],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False,  # noqa: B603
        ) as process:
            stdout, stderr = process.communicate(input=text_bytes, timeout=DEFAULT_SUBPROCESS_TIMEOUT)
            if process.returncode != 0:
                error_msg = stderr.decode(DEFAULT_ENCODING, errors="ignore") if stderr else "Unknown AWK error"
                raise PluginException(
                    cause="The awk execution failed.",
                    assistance="The awk expression resulted in an error. Please verify the expression syntax is correct and compatible with gawk.",
                    data=error_msg,
                )
            return stdout
    except subprocess.TimeoutExpired:
        if process:
            process.kill()
        raise PluginException(
            cause="The awk execution timeout exceeded.",
            assistance="The awk expression took longer than 30 seconds to execute. Please simplify the expression or reduce the input data size.",
        )
    except FileNotFoundError as error:
        raise PluginException(
            cause="AWK executable not found.",
            assistance=f"The '{AWK}' executable is not installed or not in the system PATH. Please install gawk on the system.",
            data=error,
        )
    except Exception as error:
        raise PluginException(
            cause="Unexpected error during AWK execution.",
            assistance="An unexpected error occurred. Please verify your input and expression are correct. If the issue persists, please contact support.",
            data=error,
        )
