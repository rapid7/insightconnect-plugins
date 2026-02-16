import logging
import subprocess

logger = logging.getLogger()


def exec_command(command: list, text: str):
    """Return dict with keys stdout, stderr, and return code of executed subprocess command."""

    try:
        p = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            close_fds=True,
        )

        stdout, stderr = p.communicate(input=text.encode("utf-8"))
        rcode = p.returncode

        return {"stdout": stdout, "stderr": stderr, "rcode": rcode}
    except OSError as e:
        logger.error("SubprocessError: %s %s: %s", str(e.filename), str(e.strerror), str(e.errno))
    raise Exception("ExecCommand")
