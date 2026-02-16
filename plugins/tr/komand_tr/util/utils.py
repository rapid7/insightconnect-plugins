import logging
import subprocess  # nosec B404

from typing import List, Dict

logger = logging.getLogger()


class ExecCommandError(RuntimeError):
    """Raised when subprocess execution fails."""


def exec_command(command: List[str], text: str) -> Dict[str, bytes | int]:
    """Return dict with keys stdout, stderr, and return code of executed subprocess command."""

    try:
        # nosec B603 - We are not using shell=True, so this is not vulnerable to command injection.
        with subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            close_fds=True,
            shell=False,
        ) as p:
            stdout, stderr = p.communicate(input=text.encode("utf-8"))
            rcode = p.returncode

            return {"stdout": stdout, "stderr": stderr, "rcode": rcode}
    except OSError as e:
        logger.error("SubprocessError: %s %s: %s", str(e.filename), str(e.strerror), str(e.errno))
        raise ExecCommandError("Failed to execute subprocess")
