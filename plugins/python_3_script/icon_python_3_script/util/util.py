import hashlib
import re
from pathlib import Path
from typing import Any, Union

import yaml

from icon_python_3_script.util.constants import DEFAULT_ENCODING, ENVIRONMENT_BASE_DIRECTORY

# Package name: letters, digits, and the separators -_. (PEP 508 name grammar)
_NAME_SPEC_RE = re.compile(r"^([A-Za-z0-9][A-Za-z0-9._-]*)(.*)$", re.DOTALL)
# PEP 503: runs of -, _ or . in a name normalise to a single -
_NAME_SEP_RE = re.compile(r"[-_.]+")
_WHITESPACE_RE = re.compile(r"\s+")


def _canonical_spec(spec: str) -> str:
    """
    Return a stable canonical representation of a pip requirement specifier.

    Version operators are preserved verbatim so genuinely different constraints
    (``numpy`` vs ``numpy>1``) never collapse together. Specs containing an
    environment marker (``;``) or a direct URL (``@``) are normalised only for
    whitespace/case and otherwise left intact, since reordering or rewriting
    those risks changing their meaning.

    :param spec: A pip requirement specifier string.
    :type spec: str

    :return: Canonical string used for identity/hashing purposes.
    :rtype: str
    """
    spec = spec.strip()

    # Don't risk rewriting markers/URLs; normalise whitespace + case only.
    if ";" in spec or "@" in spec:
        return _WHITESPACE_RE.sub(" ", spec).lower()

    spec_match = _NAME_SPEC_RE.match(spec)
    if not spec_match:
        return spec.lower()

    package_name, version_specifier = spec_match.group(1), spec_match.group(2)
    package_name = _NAME_SEP_RE.sub("-", package_name).lower()
    # Strip all whitespace from the version/extras portion and lower-case it
    # (PEP 440 versions and extras names are case-insensitive).
    version_specifier = _WHITESPACE_RE.sub("", version_specifier).lower()
    return f"{package_name}{version_specifier}"


def environment_key(modules: list[str]) -> str:
    """
    Return a stable SHA-256 key for a given set of modules.

    :param modules: List of pip package specifiers.
    :type modules: list[str]

    :return: Hex-encoded SHA-256 digest identifying this module set.
    :rtype: str
    """

    normalised_specs = sorted({_canonical_spec(module) for module in modules if module.strip()})
    hash_payload = ",".join(normalised_specs).encode(DEFAULT_ENCODING)
    return hashlib.sha256(hash_payload).hexdigest()


def environment_dir(key: str) -> Path:
    """
    Return the absolute path to the virtual environment directory for a given key.

    :param key: The key returned by :func:`environment_key`.
    :type key: str

    :return: Path to ``<ENVS_BASE_DIR>/<key>``.
    :rtype: Path
    """

    return Path(ENVIRONMENT_BASE_DIRECTORY) / key


def environment_interpreter_path(key: str) -> Path:
    """
    Return the absolute path to the Python interpreter inside a keyed environment.

    :param key: The key returned by :func:`environment_key`.
    :type key: str

    :return: Path to ``<ENVS_BASE_DIR>/<key>/bin/python``.
    :rtype: Path
    """

    return environment_dir(key) / "bin" / "python"


def environment_ready(key: str) -> bool:
    """
    Return True when the virtual environment for *key* is fully built and usable.

    Readiness is determined solely by the presence of the final interpreter
    binary, which is written atomically via ``Path.rename`` at the end of a
    successful build.

    :param key: The key returned by :func:`environment_key`.
    :type key: str

    :return: True if the interpreter exists, False otherwise.
    :rtype: bool
    """

    return environment_interpreter_path(key).is_file()


def extract_output_from_stdout(input_stdout: str, output_prefix: str) -> Union[dict[str, Any], None]:
    """
    Extract output from a string representing standard output.

    This function parses the provided `input_stdout` string and extracts any output data
    that start with the specified `output_prefix`. The extracted output is returned as a
    dictionary where the keys are the extracted output lines without the prefix.

    :param input_stdout: The string representing the standard output to extract from.
    :type: str

    :param output_prefix: The prefix indicating the lines to extract from `input_stdout`.
    :type: str

    :return: A dictionary containing the extracted output.
    :rtype: Union[dict[str, Any], None]
    """

    if output_prefix in input_stdout:
        function_output = yaml.safe_load(input_stdout[input_stdout.index(output_prefix) + len(output_prefix) :])
        if isinstance(function_output, str) and function_output.lower().strip() == "none":
            return None
        return function_output
    return None
