import komand
import tempfile
import shutil

# Specify path for unix utils grep and wc:
grep = "egrep"
wc = "wc"

FOUND = "found"
HITS = "hits"
MATCHES = "matches"
TEMP_PATH = tempfile.mkdtemp() + "/"


def cat_lines(log, text, pattern, behavior):
    temp_file_name = "tmp.txt"
    with open(TEMP_PATH + temp_file_name, 'w') as f:
        f.write(text)

    return print_lines(log, 'cat', TEMP_PATH + temp_file_name, pattern, behavior)


def echo_lines(log, text, pattern, behavior):
    return print_lines(log, 'echo', text, pattern, behavior)


# Run grep on text for pattern, return stdout
def print_lines(log, command, text, pattern, behavior):
    if behavior == "Default":
        cmd = "{0} '{1}' | {2} {3} > {4}results.txt".format(command, text, grep, pattern, TEMP_PATH)
        log.info(cmd)
        komand.helper.exec_command(cmd)
    elif behavior == "Only matching":
        cmd = "{0} '{1}' | {2} -o {3} > {4}results.txt".format(command, text, grep, pattern, TEMP_PATH)
        log.info(cmd)
        komand.helper.exec_command(cmd)
    results = ''
    try:
        with open(TEMP_PATH + "results.txt", 'r') as f:
            results = f.read()
    except Exception as ex:
        log.info("No Matches found")
        log.info(ex)
    return results


def process_grep(result_lines):
    matches = str.splitlines(result_lines)
    if matches:
        found = True
        hits = len(matches)
    else:
        found = False
        matches = ""
        hits = 0
    shutil.rmtree(TEMP_PATH)
    matches = matches if hits != 0 else []
    return {FOUND: found, HITS: hits, MATCHES: matches}