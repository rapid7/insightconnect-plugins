import re
from pathlib import Path

SHELL_METACHAR_PATTERN = re.compile(r"[;|&<>`\n\r]")

CACHE_DIR = Path("/var/cache/rpm_plugin/")
TEMP_DIR = Path("/tmp/")  # noqa: B108
DNF_REPO_DIR = Path("/etc/yum.repos.d/")
REPOS_SOURCE_DIR = Path("/opt/rpm-plugin/repos/")

FIELD_MAP = {
    "Name": "name",
    "Version": "version",
    "Release": "release",
    "Architecture": "architecture",
    "License": "license",
    "Source RPM": "source",
    "Build Date": "build_date",
    "Build Host": "build_host",
    "Relocations": "relocations",
    "Vendor": "vendor",
    "Packager": "packager",
    "Summary": "summary",
    "URL": "url",
}

REPOS = {
    "CentOS 6": ["base6", "epel6", "extras6", "updates6", "centosplus6"],
    "CentOS 7": ["base7", "epel7", "extras7", "updates7", "centosplus7"],
    "Fedora 24": ["fedora24"],
    "Fedora 25": ["fedora25"],
    "Fedora 26": ["fedora26"],
}

# Number of expected fields in an RPM
RPM_DUMP_FIELD_COUNT = 11

# Default subprocess timeout in seconds
SUBPROCESS_TIMEOUT = 120

# Substitution map for _modify_repofile
REPO_SUBSTITUTIONS = {
    r"enabled=1": "0",
    r"\$basearch": "$arch",
    r"gpgcheck=1": "gpgcheck=0",
}
