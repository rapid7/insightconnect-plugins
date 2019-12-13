import komand


# Specify path for unix utils grep and wc:
grep = "egrep"
wc = "wc"


# Run grep on text for pattern, return stdout
def print_lines(log, text, pattern, behavior, tmpdir):

    if behavior == "Default":
        cmd = 'cat %s | %s %s > %sresults.txt' % (text, grep, pattern, tmpdir)
        log.info(cmd)
        komand.helper.exec_command(cmd)
    elif behavior == "Only matching":
        cmd = 'cat %s | %s -o %s  > %sresults.txt' % (text, grep, pattern, tmpdir)
        log.info(cmd)
        komand.helper.exec_command(cmd)
    results = ''
    try:
        with open(tmpdir + "results.txt", 'r') as f:
            results = f.read()
    except Exception as ex:
        log.info(ex)
        log.info("No Matches found")
    return results


# Count all instances of pattern in text
def count_matches(tmpdir):
    cmd = 'wc -l %sresults.txt' % (tmpdir)
    return int(komand.helper.exec_command(cmd)['stdout'])
