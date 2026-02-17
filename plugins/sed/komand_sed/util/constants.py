DEFAULT_ENCODING = "utf-8"
SUBPROCESS_TIMEOUT = 60

DANGEROUS_PATTERNS = [
    r"[;&|`$]",
    r"\$\(",
    r"`.*`",
    r"\|\|",
    r"&&",
    r">\s*/",
    r"<\s*/",
    r"\.\.",
    r"/etc/",
    r"/bin/",
    r"/usr/bin/",
    r"rm\s+-",
    r"chmod\s+",
    r"chown\s+",
]
