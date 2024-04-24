import re
from insightconnect_plugin_runtime.helper import exec_command
from komand_dig.util.constants import DEFAULT_ENCODING
from logging import Logger
from typing import Dict, Any


def safe_parse(regex) -> str:
    # pylint: disable=using-constant-test
    if not regex:
        return "NO MATCHES FOUND"
    return regex.group(1) if re else "NO MATCHES FOUND"


def not_empty(regex: str) -> bool:
    return not regex == "NO MATCHES FOUND"


def execute_command(
    logger: Logger, cmd: str, answer_section_regex: str, regex_flags: re.RegexFlag = 0
) -> Dict[str, Any]:
    # Execute the command
    logger.info(f"Executing command: {cmd}")
    response = exec_command(f"/usr/bin/dig {cmd}")

    # Grab stdout and stderr
    stdout = response.get("stdout", "").decode(DEFAULT_ENCODING)
    stderr = response.get("stderr", "").decode(DEFAULT_ENCODING)

    # Grab query status
    status = safe_parse(re.search("status: (.+?),", stdout))

    # Grab nameserver
    nameserver = safe_parse(re.search("SERVER: (.+?)#", stdout))

    # Grab number of answers
    answers = safe_parse(re.search(r"ANSWER: ([0-9]+)", stdout))

    answer_section = None
    if not_empty(answers):
        answers = int(answers)
        # We need answers to continue
        if answers > 0:
            # Grab resolved address section
            answer_section = safe_parse(re.search(answer_section_regex, stdout, flags=regex_flags))

    if status != "NOERROR":
        stdout = f"Resolution failed, nameserver {nameserver} returned {status} status"

    return {
        "answer_section": answer_section,
        "full_output": stdout + stderr,
        "nameserver": nameserver,
        "status": status,
    }
