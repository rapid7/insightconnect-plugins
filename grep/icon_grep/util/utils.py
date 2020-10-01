from insightconnect_plugin_runtime.exceptions import PluginException
from subprocess import run, CalledProcessError
import tempfile


def run_grep(log: object, text: str, pattern: str, behavior: str) -> str:
    with tempfile.NamedTemporaryFile() as fp:
        fp.write(text.encode())
        fp.seek(0)
        if behavior == 'Default':
            matches = run(['egrep', pattern, fp.name], capture_output=True)
        elif behavior == 'Only matching':
            matches = run(['egrep', '-o', pattern, fp.name], capture_output=True)

    if matches.returncode == 2:
        raise PluginException(cause='The grep process returned an error',
                              assistance=matches.stderr.decode())
    if matches.stderr:
        log.error(matches.stderr.decode())
    return matches.stdout.decode()


def process_grep(result_lines: str) -> dict:
    matches = str.splitlines(result_lines)
    if matches:
        found = True
        hits = len(matches)
    else:
        found = False
        matches = ''
        hits = 0
    matches = matches if hits != 0 else []
    return {'found': found, 'hits': hits, 'matches': matches}
