import re
import insightconnect_plugin_runtime
from komand_dig.util import util


def safe_parse(regex):
    regex = regex.group(1) if re else "NO MATCHES FOUND"
    return regex


def not_empty(regex):
    return False if regex == "NO MATCHES FOUND" else True


def execute_command(logger, cmd, answer_section_regex, flags):
    binary = "/usr/bin/dig"
    cmd = f"{binary} {cmd}"
    logger.info(f"Executing command {cmd}")
    r = insightconnect_plugin_runtime.helper.exec_command(cmd)
    stdout = r['stdout'].decode('utf-8')

    # Grab query status
    status = util.safe_parse(re.search('status: (.+?),', stdout))
    # Grab nameserver
    ns = util.safe_parse(re.search('SERVER: (.+?)#', stdout))
    # Grab number of answers
    answers = util.safe_parse(re.search(r'ANSWER: ([0-9]+)', stdout))
    if util.not_empty(answers):
        answers = int(answers)

    answer_section = None
    # We need answers to continue
    if answers > 0:
        # Grab resolved address section
        if flags is None:
            answer_section = util.safe_parse(re.search(answer_section_regex, stdout))
        else:
            answer_section = util.safe_parse(re.search(answer_section_regex, stdout, flags=flags))

    if status != "NOERROR":
        stdout = f'Resolution failed, nameserver {ns} returned {status} status'

    return {
        'answer_section': answer_section,
        'fulloutput': stdout + r['stderr'].decode('utf-8'),
        'nameserver': ns,
        'status': status
    }
