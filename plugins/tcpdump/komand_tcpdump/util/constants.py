DEFAULT_TIMEOUT = 300
MAX_FILTER_LENGTH = 1000
MAX_OPTIONS_LENGTH = 500

# Security patterns for input validation
DANGEROUS_CHARS_PATTERN = r"[;&|`$<>]"
DANGEROUS_SEQUENCES = ["&&", "||", "|", ";", "\n", "\r", "`", "$", "$(", "${"]

# Allowed tcpdump options (whitelist approach)
# NOTE: Only read-only options are allowed. Write operations (-w, -C, -G, -W, -z, -Z)
# are explicitly excluded as this plugin is read-only for .pcap files.
ALLOWED_TCPDUMP_OPTIONS = [
    "-A",
    "-c",
    "-d",
    "-dd",
    "-ddd",
    "-e",
    "-E",
    "-f",
    "-F",
    "-h",
    "-H",
    "-j",
    "-J",
    "--time-stamp-precision",
    "-l",
    "-L",
    "-m",
    "-M",
    "-n",
    "-nn",
    "-N",
    "-#",
    "--number",
    "-O",
    "--no-optimize",
    "-q",
    "-Q",
    "-r",
    "-s",
    "-S",
    "-t",
    "-tt",
    "-ttt",
    "-tttt",
    "-ttttt",
    "-u",
    "-v",
    "-vv",
    "-vvv",
    "-V",
    "-x",
    "-xx",
    "-X",
    "-XX",
    "-y",
]
