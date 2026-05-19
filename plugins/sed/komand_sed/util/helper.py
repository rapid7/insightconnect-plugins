import re
import shlex
import subprocess  # noqa: B404

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_sed.util.constants import (
    ALLOWED_OPTIONS,
    DEFAULT_ENCODING,
    SAFE_COMMANDS,
    SUBPROCESS_TIMEOUT,
    SUBSTITUTION_FLAGS_RE,
)

# Matches optional address (number, $, /regex/, or range) followed by s or y + delimiter
SUBSTITUTION_RE = re.compile(
    r"^(?:\d+|\$|/(?:[^/\\]|\\.)*/)?"  # optional single address
    r"(?:,(?:\d+|\$|/(?:[^/\\]|\\.)*/))?!?s"  # optional range end + optional '!' + 's'
    r"([^\w\\])"  # delimiter
)
TRANSLITERATION_RE = re.compile(
    r"^(?:\d+|\$|/(?:[^/\\]|\\.)*/)?"
    r"(?:,(?:\d+|\$|/(?:[^/\\]|\\.)*/))?!?y"
    r"([^\w\\])"  # pylint: disable=implicit-str-concat
)

# Matches optional address followed by optional '!' and exactly one safe command character
ADDRESS_COMMAND_RE = re.compile(
    r"^(?:\d+|\$|/(?:[^/\\]|\\.)*/)?" r"(?:,(?:\d+|\$|/(?:[^/\\]|\\.)*/))?!?[" + re.escape(SAFE_COMMANDS) + r"]$"
)


class Helper:
    def process(self, input_string: bytes, expressions: list[str], options: str = "") -> bytes:
        try:
            with subprocess.Popen(  # nosec B603
                self._build_sed_command(expressions, options),
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=False,
            ) as process:  # noqa: B603
                try:
                    # Execute the command with a timeout to prevent hanging
                    stdout, stderr = process.communicate(input=input_string, timeout=SUBPROCESS_TIMEOUT)
                except subprocess.TimeoutExpired:
                    # Kill the process if it exceeds the timeout
                    process.kill()
                    raise PluginException(
                        cause="Command timeout. ",
                        assistance=f"Sed command exceeded default {SUBPROCESS_TIMEOUT} seconds timeout",
                    )

                # Check for non-zero return code and stderr details if it fails
                if process.returncode != 0:
                    error_message = stderr.decode(DEFAULT_ENCODING, errors="ignore").strip()
                    raise PluginException(
                        cause="Sed command execution failed. ",
                        assistance=f"Sed returned error code ({process.returncode}): {error_message}",
                    )
                return stdout
        except subprocess.SubprocessError as error:
            raise PluginException(cause="Subprocess error. ", assistance=f"Failed to execute sed command: {error}")
        except PluginException:
            raise
        except Exception as error:
            raise PluginException(
                cause="Unexpected error during sed execution", assistance=f"An unexpected error occurred: {error}"
            )

    @staticmethod
    def shell_quote(string: str) -> str:
        return shlex.quote(string)

    def _build_sed_command(self, expressions: list[str], options: str) -> list[str]:
        # Start with the base command
        sed_args = ["sed", "--sandbox"]

        # Validate and add options if provided
        if options:
            self._validate_options(options)
            try:
                sed_args.extend(shlex.split(options))
            except ValueError as error:
                raise PluginException(cause="Invalid options format. ", assistance=f"Unable to parse options: {error}")

        # Validate and add expressions to the command if provided
        for expression in expressions:
            self._validate_expression(expression)
            sed_args.extend(["-e", expression])

        return sed_args

    @staticmethod
    def _validate_expression(expression: str) -> None:
        """
        Reject expressions that don't match a allowed expression pattern.

        :param expression: A sed expression to validate.
        :type expression: str
        """

        # Strip the expression string
        expression = expression.strip()

        # Reject empty expressions
        if not expression:
            raise PluginException(
                cause="Invalid expression detected. ",
                assistance="Empty expressions are not permitted.",
            )

        # Address single safe command (regex anchors ensure no trailing content like ';')
        if ADDRESS_COMMAND_RE.match(expression):
            return

        # Extract flags after the last delimiter and validate them
        if sub_match := SUBSTITUTION_RE.match(expression):
            delimiter = sub_match.group(1)
            flags = _extract_flags_after_last_delimiter(expression, sub_match.end() - 1, delimiter)
            if flags is not None and SUBSTITUTION_FLAGS_RE.match(flags) and "e" not in flags:
                return

        # No flags allowed
        if trans_match := TRANSLITERATION_RE.match(expression):
            delimiter = trans_match.group(1)
            flags = _extract_flags_after_last_delimiter(expression, trans_match.end() - 1, delimiter)
            if flags is not None and flags == "":
                return

        # Otherwise, the expression is not allowed
        raise PluginException(
            cause="Invalid expression detected. ",
            assistance=f"The expression '{expression}' is not permitted. "
            "Only substitution (s/…/…/flags), transliteration (y/…/…/), "
            "and address+safe command forms are allowed.",
        )

    @staticmethod
    def _validate_options(options: str) -> None:
        """
        Validate sed options against the list of allowed options.

        :param options: A string of sed options.
        :type options: str
        """

        # Handle empty or whitespace-only options
        if not options or not options.strip():
            return

        # Split the options string into tokens
        try:
            tokens = shlex.split(options)
        except ValueError as error:
            raise PluginException(
                cause="Invalid options detected. ",
                assistance=f"Unable to parse options: {error}",
            )

        # Validate each token
        for token in tokens:
            if token not in ALLOWED_OPTIONS:
                raise PluginException(
                    cause="Invalid options detected. ",
                    assistance=f"The option '{token}' is not permitted. "
                    f"Allowed options are: {', '.join(ALLOWED_OPTIONS)}",
                )


def _extract_flags_after_last_delimiter(expression: str, start: int, delimiter: str) -> str | None:
    """
    Walk through two delimiter-separated sections and return trailing flags.

    :param expression: Full expression string (starting from the delimiter after s/y).
    :type expression: str

    :param start: Index of the first delimiter character.
    :type start: int

    :param delimiter: The delimiter character.
    :type delimiter: str

    :return: The flags string after the closing delimiter, or None if structure is invalid.
    :rtype: str | None
    """

    # Find the end of the second section
    position = start + 1

    # Walk through first section
    for _ in range(2):
        while position < len(expression):
            char = expression[position]
            if char == "\\":
                position += 2  # skip escaped character
            elif char == delimiter:
                position += 1
                break
            else:
                position += 1
        else:
            return None

    return expression[position:]
