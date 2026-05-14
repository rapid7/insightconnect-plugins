import re

DEFAULT_ENCODING = "utf-8"
SUBPROCESS_TIMEOUT = 60

ALLOWED_OPTIONS = frozenset({"-n", "-r", "-E", "--regexp-extended"})
SAFE_COMMANDS = "pdq=nNgGhHlx"
SUBSTITUTION_FLAGS_RE = re.compile(r"^[giImMp0-9]*$")
