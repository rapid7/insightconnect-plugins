from komand.exceptions import PluginException
import tempfile
import subprocess


def run_grep(text: str, pattern: str, behavior: str) -> str:
    with tempfile.NamedTemporaryFile() as fp:
        fp.write(text.encode())
        fp.seek(0)
        if behavior == 'Default':
            matches = subprocess.run(['egrep', pattern, fp.name], capture_output=True)
        elif behavior == 'Only matching':
            matches = subprocess.run(['egrep', '-o', pattern, fp.name], capture_output=True)
    if matches.stderr:
        raise from PluginException(cause='Grep returned an error.',
                                   assistance='Ensure that you pattern and data are correct',
                                   data=f'Error: {matches.stderr}, Pattern {pattern}')
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
