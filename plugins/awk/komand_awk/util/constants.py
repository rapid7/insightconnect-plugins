DEFAULT_ENCODING = "utf-8"
DEFAULT_SUBPROCESS_TIMEOUT = 60

# Specify path for unix utils grep and wc:
AWK = "gawk"

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
