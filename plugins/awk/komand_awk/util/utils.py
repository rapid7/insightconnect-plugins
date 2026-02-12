from insightconnect_plugin_runtime.exceptions import PluginException
import base64
import re
import subprocess  # noqa: B404
from .constants import DEFAULT_ENCODING, DEFAULT_SUBPROCESS_TIMEOUT
from logging import Logger

# Specify path for unix utils grep and wc:
awk = "gawk"

# Safe AWK syntax patterns whitelist
SAFE_AWK_PATTERNS = [
    # Field references: $1, $2, $NF, etc.
    r"\$\d+",
    r"\$NF",
    r"\$NR",
    r"\$0",
    # Built-in variables
    r"\b(NR|NF|FS|RS|OFS|ORS|FILENAME|FNR|ARGC|ARGV|CONVFMT|OFMT|RLENGTH|RSTART|SUBSEP)\b",
    # Common AWK functions - string functions
    r"\b(print|printf|sprintf|gsub|sub|gensub|match|split|patsplit|substr|length|tolower|toupper|index)\b",
    # AWK functions - arithmetic
    r"\b(sin|cos|atan2|exp|log|sqrt|int|rand|srand)\b",
    # AWK functions - type and I/O (safe ones only)
    r"\b(typeof|isarray|close|fflush)\b",
    # AWK aggregate functions
    r"\b(sum|count|avg|min|max)\b",
    # Arithmetic operators
    r"[+\-*/%^]",
    # Increment/decrement operators
    r"(\+\+|--)",
    # Comparison operators (including spaces around them)
    r"(==|!=|<=|>=|<|>|~|!~)",
    # Logical operators
    r"(\|\||&&|!)",
    # Pattern matching
    r"/(\\.|[^/])*/",
    # Braces and parentheses
    r"[{}()\[\]]",
    # Quotes and strings
    r'"(\\.|[^"])*"',
    r"'(\\.|[^'])*'",
    # Whitespace and punctuation
    r"[\s,;:\?]",
    # Assignment operators
    r"(\+=|-=|\*=|/=|%=|\^=|=)",
    # Numbers
    r"\b\d+(\.\d+)?([eE][+-]?\d+)?\b",
    r"\b0[xX][0-9a-fA-F]+\b",
    # Common patterns
    r"\b(BEGIN|END|BEGINFILE|ENDFILE)\b",
    # Control flow statements
    r"\b(if|else|while|for|do|break|continue|next|nextfile|exit|return)\b",
    # Field separators and other common constructs
    r"-F\s*[^\s]+",  # Field separator with argument
    r"-v\s+\w+=",  # Variable assignment
    # Ternary operator
    r"\?.*:",
    # Comments
    r"#.*$",
]

DANGEROUS_PATTERNS = [
    # System and command execution
    r"system\s*\(",  # system() calls
    r"\bexec\b",  # exec command
    r"\bcmd\b",  # cmd reference
    r"\bsh\b",  # shell reference
    r"\bbash\b",  # bash reference
    r"\bzsh\b",  # zsh reference
    r"\bksh\b",  # ksh reference
    r"\bcsh\b",  # csh reference
    r"\bperl\b",  # perl reference
    r"\bpython\b",  # python reference
    r"\bruby\b",  # ruby reference
    r"\bphp\b",  # php reference
    # Command substitution
    r"`[^`]*`",  # Backticks (command substitution)
    r"\$\([^)]*\)",  # Command substitution $()
    r"\$\{[^}]*\}",  # Variable expansion ${}
    # File descriptor manipulation
    r">\s*&",  # Output redirection with file descriptors
    r"<\s*&",  # Input redirection with file descriptors
    r"\|\s*&",  # Pipe with co-process
    r"\d+>\s*&",  # Numbered file descriptor redirection
    r"&>\s*",  # Redirect both stdout and stderr
    # Dangerous shell commands after semicolon or in pipes
    r";\s*(rm|mv|cp|dd|chmod|chown|chgrp|kill|pkill|killall|shutdown|reboot|halt|poweroff)\b",
    r"\|\s*(rm|mv|cp|dd|chmod|chown|chgrp|kill|pkill|killall|shutdown|reboot|halt|poweroff)\b",
    # Network and remote access
    r"\b(curl|wget|nc|netcat|ncat|socat|telnet|ssh|scp|sftp|ftp|rsync)\b",
    r"\b(nmap|ping|traceroute|dig|nslookup|host)\b",
    # File operations via pipes/redirects
    r'\|\s*"',  # Pipe to command
    r'"\s*\|',  # Pipe from command
    r'>\s*"/',  # Output redirection to absolute path
    r'<\s*"/',  # Input redirection from absolute path
    r'>>\s*"',  # Append redirection to file
    r">\s*/[a-zA-Z]",  # Direct redirection to absolute path
    r">>\s*/[a-zA-Z]",  # Direct append to absolute path
    # AWK file/network operations
    r"getline\s*<",  # getline from file
    r"getline\s+\w+\s*<",  # getline into variable from file
    r"\|\s*getline",  # pipe to getline
    r"print.*>\s*\"",  # print to file
    r"print.*>>\s*\"",  # print append to file
    r"print.*\|\s*\"",  # print to pipe
    r"printf.*>\s*\"",  # printf to file
    r"printf.*>>\s*\"",  # printf append to file
    r"printf.*\|\s*\"",  # printf to pipe
    # Environment and system info access
    r"\bENVIRON\s*\[",  # Environment variable access
    r"\bPROCINFO\s*\[",  # Process info access
    # File path access patterns
    r'"/etc/',  # Access to /etc directory
    r'"/proc/',  # Access to /proc filesystem
    r'"/sys/',  # Access to /sys filesystem
    r'"/dev/',  # Access to /dev directory
    r'"/tmp/',  # Access to /tmp directory
    r'"/var/',  # Access to /var directory
    r'"/root/',  # Access to root home
    r'"/home/',  # Access to home directories
    r'"/usr/',  # Access to /usr directory
    r'"/bin/',  # Access to /bin directory
    r'"/sbin/',  # Access to /sbin directory
    r'"/opt/',  # Access to /opt directory
    r'"~/',  # Access via home directory shortcut
    r'"\.\.',  # Path traversal attempt
    # Dangerous file operations
    r"\b(unlink|remove|rename|mkdir|rmdir|link|symlink)\s*\(",
    # Code evaluation
    r"\beval\b",  # eval command
    r"@include\b",  # gawk include directive
    r"@load\b",  # gawk load directive
    r"@namespace\b",  # gawk namespace directive
    # Binary/hex injection attempts
    r"\\x[0-9a-fA-F]{2}",  # Hex escape sequences
    r"\\[0-7]{3}",  # Octal escape sequences
    # Null byte injection
    r"\\0",  # Null byte
    r"\x00",  # Literal null byte
    # Extension loading (gawk)
    r"extension\s*\(",  # Extension loading
    r"-l\s+\w+",  # Load extension via command line
    r"-f\s+/",  # Load script from absolute path
    r"-i\s+\w+",  # Include file
    # Coprocess (gawk)
    r"\|&",  # Two-way pipe
    # Dangerous gawk features
    r"\bBINMODE\b",  # Binary mode
    r"\bFIELDWIDTHS\b",  # Fixed field widths
    r"\bFPAT\b",  # Field pattern
    r"\bTEXTDOMAIN\b",  # Text domain
    # SQL injection style patterns
    r";\s*DROP\s+",
    r";\s*DELETE\s+",
    r";\s*INSERT\s+",
    r";\s*UPDATE\s+",
    r"--\s*$",  # SQL comment at end of line
    # Additional dangerous utilities
    r"\b(awk|gawk|mawk|nawk)\b",  # Nested AWK calls
    r"\b(sed|grep|egrep|fgrep|cut|sort|uniq|head|tail|cat|tee|xargs)\b",  # Shell utilities that could be piped
    r"\b(echo|printf)\s+.*[|>]",  # Echo/printf with redirection
]


def validate_expression(expression: str) -> None:
    """
    Validate the awk expression.

    :param expression: AWK expression to validate
    :type expression: str
    """

    # Check for dangerous patterns
    for pattern in DANGEROUS_PATTERNS:
        if re.search(pattern, expression, re.IGNORECASE):
            raise PluginException(
                cause="The awk expression contains wrong syntax.",
                assistance="Please make sure that the expression is valid and try again.",
            )

    # Build combined safe pattern regex
    combined_pattern = "|".join(f"({pattern})" for pattern in SAFE_AWK_PATTERNS)

    # Remove all safe patterns and check if anything dangerous remains
    cleaned = re.sub(combined_pattern, "", expression)
    cleaned = re.sub(r"\s+", "", cleaned)  # Remove remaining whitespace

    # If there are remaining characters that aren't in our whitelist, it might be suspicious
    if cleaned and re.search(r"[^\s]", cleaned):
        # Allow some additional safe characters that might be valid AWK syntax
        remaining_unsafe = re.sub(r"[_a-zA-Z0-9\s]", "", cleaned)
        if remaining_unsafe:
            raise PluginException(
                cause="The awk expression contains unrecognized syntax.",
                assistance="The expression contains characters or patterns that are not recognized as safe AWK syntax. Please ensure the expression uses only standard AWK patterns and functions.",
            )


def preprocess_expression(expression: str) -> str:
    """
    Preprocess and decode base64 encoded expression if needed.

    :param expression: AWK expression (may be base64 encoded)
    :type expression: str

    :return: Decoded expression string
    :rtype str
    """

    # Skip base64 decoding if expression starts with AWK syntax
    if expression.strip().startswith(("{", "/", "$", "BEGIN", "END", "-")):
        return expression

    try:
        # Verify the decoded string looks like valid AWK
        decoded = base64.b64decode(expression).decode(DEFAULT_ENCODING)
        if any(keyword in decoded for keyword in ["{", "print", "$", "BEGIN", "END", "/"]):
            return decoded
    except Exception:
        return expression


def process_lines(log: Logger, text: str | bytes, expression: str) -> bytes:
    """
    Process text using awk expression.

    :param log: Logger instance
    :type log: Logger

    :param text: Text content to process (string or bytes)
    :type text: str or bytes

    :param expression: awk expression to execute
    :type expression: str

    :return: Processed output as bytes
    :rtype bytes
    """

    # Validate inputs
    validate_expression(expression)

    # Convert text to bytes if it's a string
    if isinstance(text, str):
        text_bytes = text.encode(DEFAULT_ENCODING)
    else:
        text_bytes = text

    log.info(f"ProcessLines: awk {expression}")

    try:
        # Use subprocess with proper stdin handling
        with subprocess.Popen(
            [awk, expression],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False,  # noqa: B603
        ) as process:
            stdout, stderr = process.communicate(input=text_bytes, timeout=DEFAULT_SUBPROCESS_TIMEOUT)
            if process.returncode != 0:
                error_msg = stderr.decode(DEFAULT_ENCODING, errors="ignore") if stderr else "Unknown AWK error"
                raise PluginException(
                    cause="The awk execution failed.",
                    assistance="The awk expression resulted in an error. Please verify the expression syntax is correct and compatible with gawk.",
                    data=error_msg,
                )
            return stdout
    except subprocess.TimeoutExpired:
        if process:
            process.kill()
        raise PluginException(
            cause="The awk execution timeout exceeded.",
            assistance="The awk expression took longer than 30 seconds to execute. Please simplify the expression or reduce the input data size.",
        )
    except FileNotFoundError as error:
        raise PluginException(
            cause="AWK executable not found.",
            assistance=f"The '{awk}' executable is not installed or not in the system PATH. Please install gawk on the system.",
            data=error,
        )
    except Exception as error:
        raise PluginException(
            cause="Unexpected error during AWK execution.",
            assistance="An unexpected error occurred. Please verify your input and expression are correct. If the issue persists, please contact support.",
            data=error,
        )
