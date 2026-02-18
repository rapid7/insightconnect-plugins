from logging import Logger
import subprocess  # nosec B404

from typing import List, Dict, Any

from komand_tr.util.exceptions import ExecCommandError

DEFAULT_ENCODING = "utf-8"


def exec_command(command: List[str], text: str, logger: Logger) -> Dict[str, Any]:
    """Return dict with keys stdout, stderr, and return code of executed subprocess command."""

    try:
        with subprocess.Popen(  # nosec B603
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            close_fds=True,
            shell=False,
        ) as process:
            stdout, stderr = process.communicate(input=text.encode(DEFAULT_ENCODING))
            rcode = process.returncode

            return {"stdout": stdout, "stderr": stderr, "rcode": rcode}
    except OSError as error:
        logger.error("SubprocessError: %s %s: %s", str(error.filename), str(error.strerror), str(error.errno))
        raise ExecCommandError("Failed to execute subprocess")
