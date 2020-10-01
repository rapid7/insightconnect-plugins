import tempfile
import subprocess


def run_grep(text: str, pattern: str, behavior: str) -> str:
    with tempfile.NamedTemporaryFile() as fp:
        fp.write(text.encode())
        fp.seek(0)
        if behavior == 'Default':
            matches = subprocess.check_output(['egrep', pattern, fp.name])
        elif behavior == 'Only matching':
            matches = subprocess.check_output(['egrep', '-o', pattern, fp.name])
    return matches.decode()


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
