import re
import shlex
import subprocess  # noqa: B404
from typing import List
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_sed.util.constants import DANGEROUS_PATTERNS, SUBPROCESS_TIMEOUT, DEFAULT_ENCODING

COMPILED_PATTERNS = [re.compile(pattern) for pattern in DANGEROUS_PATTERNS]


class Helper:
    def process(self, input_string: bytes, expressions: List[str], options: str = "") -> bytes:
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
        except PluginException as error:
            raise error
        except Exception as error:
            raise PluginException(
                cause="Unexpected error during sed execution", assistance=f"An unexpected error occurred: {error}"
            )

    @staticmethod
    def shell_quote(string: str) -> str:
        return shlex.quote(string)

    def _build_sed_command(self, expressions: List[str], options: str) -> List[str]:
        # Start with the base command
        sed_args = ["sed"]

        # Validate and add options if provided
        if options:
            self._validate_input(options, "options")
            try:
                sed_args.extend(shlex.split(options))
            except ValueError as error:
                raise PluginException(cause="Invalid options format. ", assistance=f"Unable to parse options: {error}")

        # Validate and add expressions to the command if provided
        for expression in expressions:
            self._validate_input(expression, "expression")
            sed_args.extend(["-e", expression])

        return sed_args

    @staticmethod
    def _validate_input(value: str, input_type: str) -> None:
        for pattern in COMPILED_PATTERNS:
            if pattern.search(value):
                raise PluginException(
                    cause="Invalid input detected. ",
                    assistance=(
                        f"The `{input_type}` contains forbidden characters or patterns. "
                        "Please review your input and try again."
                    ),
                )
