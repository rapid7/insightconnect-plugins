from pyldfire import WildFire

UNKNOWN_VERDICT_CODE = -102
# pylint: disable=protected-access
UNKNOWN_VERDICT = WildFire._verdicts.get(UNKNOWN_VERDICT_CODE)
SUPPORTED_FILES = (
    ".apk",
    ".flash",
    ".jar",
    ".msi",
    ".dmg",
    ".pkg",
    ".doc",
    ".iqy",
    ".7z",
    ".slk",
    ".dll",
    ".dng",
    ".fon",
    ".lnk",
    ".ooxml",
    ".pkg",
    ".ps1",
    ".vbs",
    ".bat",
    ".docx",
    ".elf",
    ".hta",
    ".js",
    ".mach-o",
    ".pdf",
    ".pe",
    ".ppt",
    ".pptx",
    ".rar",
    ".rtf",
    ".xls",
    ".xlsx",
)
