import json
import os
import re
import secrets
import shutil
import subprocess  # noqa: B404
import tempfile
from datetime import datetime, timezone
from logging import Logger
from pathlib import Path
from typing import Dict, List, Optional, Union

from insightconnect_plugin_runtime.exceptions import PluginException

from komand_rpm.util.constants import (
    CACHE_DIR,
    DNF_REPO_DIR,
    FIELD_MAP,
    REPO_SUBSTITUTIONS,
    REPOS,
    REPOS_SOURCE_DIR,
    RPM_DUMP_FIELD_COUNT,
    SHELL_METACHAR_PATTERN,
    SUBPROCESS_TIMEOUT,
    TEMP_DIR,
)


class RPMHelper:
    def __init__(self, logger: Logger) -> None:
        self.logger = logger
        self._install_builtin_repos()

    def add_key(self, url: str) -> None:
        # Download GPG key from URL and import it
        key_file_descriptor, key_file_path = tempfile.mkstemp(prefix="temp-gpg-key-")
        os.close(key_file_descriptor)
        try:
            self._run_subprocess(
                ["wget", "-O", key_file_path, url],
                error_context=f"Failed to download GPG key from {url}",
            )
            self._run_subprocess(
                ["rpm", "--import", key_file_path],
                error_context=f"Failed to import GPG key from {url}",
            )
            self.logger.info(f"AddKey: Key successfully added from {url}")
        finally:
            if os.path.exists(key_file_path):
                os.remove(key_file_path)

    def add_repo(self, url: str) -> Dict[str, Union[str, List[str]]]:
        # Download repo file from URL and modify it with unique IDs
        self.logger.info(f"AddRepo: Adding new repo at url {url}")
        DNF_REPO_DIR.mkdir(parents=True, exist_ok=True)
        repo_path = str(DNF_REPO_DIR / f"custom-{secrets.token_hex(8)}.repo")
        self._run_subprocess(
            ["wget", "-O", repo_path, url],
            error_context=f"Failed to download repo file from {url}",
        )
        repo_ids = self._modify_repofile(repo_path)
        return {"path": repo_path, "ids": repo_ids}

    def check_rpm_cache(self, package_list: List[str]) -> Optional[Dict]:
        # Return cached package info if any package in list exists in cache
        for package in package_list:
            cachefile_path = CACHE_DIR / package
            if cachefile_path.is_file():
                self.logger.info(f"CheckRpmCache: Cachefile match for {cachefile_path}")
                return json.loads(cachefile_path.read_text(encoding="utf-8"))
        return None

    def checksig(self, path: str) -> None:
        # Verify RPM package signature
        self._run_subprocess(
            ["rpm", "--checksig", path],
            error_context=f"RPM signature check failed for {path}",
        )
        self.logger.info(f"CheckSig: RPM package verified at {path}")

    def download_package(
        self,
        label: str,
        arch: str,
        distro: str,
        package_list: Optional[List[str]] = None,
        repo_ids: Optional[List[str]] = None,
    ) -> str:
        # Download RPM package to temp directory, return path
        if not package_list:
            package_list = self.list_package(label, arch, distro, repo_ids)

        existing = self._find_package_in_temp(package_list)
        if existing:
            return existing

        self.logger.info(f"DownloadPackage: Downloading package with label {label}")
        parameters = self._build_parameters(arch, distro, repo_ids)
        self._run_subprocess(
            ["dnf", "download", "--destdir", str(TEMP_DIR)] + parameters + [label],
            error_context=f"Failed to download package {label}",
        )

        downloaded = self._find_package_in_temp(package_list)
        if downloaded:
            self.logger.info(f"DownloadPackage: Found {downloaded}")
            return downloaded

        raise PluginException(
            cause=f"Failed to download package {label}",
            assistance="Verify the package exists in the configured repositories.",
        )

    def info2dic(self, info: Dict[str, str]) -> Dict:
        # Parse rpm query output into structured package dict
        raw_package = info.get("package", "")
        all_lines = raw_package.splitlines()
        package_lines = all_lines[:17]
        description = all_lines[18] if len(all_lines) > 18 else ""

        result: dict = {"found": True}
        result["files"] = self._parse_file_dump(info.get("files", ""))
        self._parse_package_fields(package_lines, result)
        result["description"] = description
        return result

    def list_package(self, label: str, arch: str, distro: str, repo_ids: Optional[List[str]] = None) -> List[str]:
        # Query repo for packages matching label
        parameters = self._build_parameters(arch, distro, repo_ids)
        command = ["dnf", "repoquery", "-q"] + parameters + [label]
        output = self._run_subprocess(
            command,
            error_context=f"Package not found with label {label}",
        )
        if not output.stdout.strip():
            self.logger.error(f"ListPackage: {output.stdout}{output.stderr}")
            raise PluginException(
                cause=f"Package not found with label {label}",
                assistance="Verify the package name, version, architecture, and distribution are correct.",
            )
        return self._add_rpm_extensions(self._trim_epochs(output.stdout.splitlines()))

    def make_label(self, name: str, epoch: str, version: str, release: str) -> str:
        # Build package label: name-[epoch:]version[-release]
        if not version:
            return name

        # Create label with epoch, version, and release components
        epoch_prefix = f"{epoch}:" if epoch else ""
        release_suffix = f"-{release}" if release else ""
        return f"{name}-{epoch_prefix}{version}{release_suffix}"

    def package_info(self, path: str) -> Dict[str, str]:
        # Query RPM package info and file dump
        self.logger.info(f"PackageInfo: Querying package info at {path}")
        info_result = self._run_subprocess(
            ["rpm", "-qip", path],
            error_context=f"Failed to query package info at {path}",
        )
        dump_result = self._run_subprocess(
            ["rpm", "-qp", "--dump", path],
            error_context=f"Failed to query package file dump at {path}",
        )
        return {"package": info_result.stdout, "files": dump_result.stdout}

    def sanitize_cache_label(self, label: str) -> str:
        # Remove unsafe characters from cache label
        return label.replace("..", "").replace("/", "").replace("\x00", "")

    def update_cache(self, data: dict, label: str) -> None:
        # Write package info dict to cache file
        self.logger.info(f"UpdateCache: Updating cache for {label}")
        cachefile_path = CACHE_DIR / self._trim_epoch(label)
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        cachefile_path.write_text(json.dumps(data), encoding="utf-8")
        self.logger.info(f"UpdateCache: Done updating cache for {label}")

    def validate_input(self, value: str, field_name: str) -> None:
        # Check for shell metacharacters in input
        if SHELL_METACHAR_PATTERN.search(value):
            raise PluginException(
                cause=f"Invalid characters in {field_name}",
                assistance=f"The {field_name} field contains shell metacharacters which are not allowed.",
            )

    def validate_url(self, url: str) -> None:
        # Validate URL uses http:// or https:// scheme
        if not url.startswith(("http://", "https://")):
            raise PluginException(
                cause=f"Invalid URL scheme: {url}",
                assistance="Only http:// and https:// URLs are supported.",
            )

    def _add_rpm_extensions(self, packages: List[str]) -> List[str]:
        # Add .rpm extension to packages if not present
        return [pkg if pkg.endswith(".rpm") else f"{pkg}.rpm" for pkg in packages]

    def _build_parameters(self, arch: str, distro: str, repo_ids: Optional[List[str]] = None) -> List[str]:
        # Build dnf command parameters for architecture, distro, and repos
        if arch == "i686":
            archlist = "i386,i686,noarch"
        elif arch and arch != "noarch":
            archlist = f"{arch},noarch"
        else:
            archlist = "noarch"

        repos_to_enable = repo_ids or REPOS.get(distro, [])
        return [
            "--disableplugin=system_upgrade",
            f"--archlist={archlist}",
            f"--releasever={distro.split()[1]}",
            "--disablerepo=*",
            *[f"--enablerepo={repo}" for repo in repos_to_enable],
        ]

    def _find_package_in_temp(self, package_list: List[str]) -> Optional[str]:
        # Return path of first package found in TEMP_DIR, or None
        for package in package_list:
            package_path = TEMP_DIR / package
            if package_path.is_file():
                return str(package_path)
        return None

    def _install_builtin_repos(self) -> None:
        # Copy bundled .repo files into dnf repo directory
        if not REPOS_SOURCE_DIR.is_dir():
            self.logger.info("InstallRepos: No bundled repos directory found, skipping")
            return
        DNF_REPO_DIR.mkdir(parents=True, exist_ok=True)
        for repo_file in REPOS_SOURCE_DIR.glob("*.repo"):
            destination = DNF_REPO_DIR / repo_file.name
            if not destination.exists():
                shutil.copy2(repo_file, destination)
                self.logger.info(f"InstallRepos: Installed {repo_file.name}")

    def _modify_repofile(self, path: str) -> List[str]:
        # Modify repo file with unique IDs and substitutions, return repo IDs
        repo_path = Path(path)
        lines = []
        repo_ids = []
        for line in repo_path.read_text(encoding="utf-8").splitlines(keepends=True):
            match = re.match(r"\[(.*?)\]", line)
            if match:
                custom_repo = f"{match.group(1)}-{secrets.token_hex(8)}"
                line = re.sub(re.escape(match.group(1)), custom_repo, line)
                repo_ids.append(custom_repo)
            for pattern, replacement in REPO_SUBSTITUTIONS.items():
                line = re.sub(pattern, replacement, line)
            lines.append(line)

        if not repo_ids:
            raise PluginException(
                cause=f"No repository IDs found in repo file at {path}",
                assistance="Verify the repo file contains valid [repo-id] sections.",
            )
        if not lines:
            raise PluginException(
                cause=f"Repo file at {path} is empty after modification",
                assistance="Verify the repo file has valid content.",
            )
        repo_path.write_text("".join(lines), encoding="utf-8")
        self.logger.info(f"ModifyRepofile: Repofile modified at {path}")
        return repo_ids

    def _parse_file_dump(self, raw_files: str) -> List[Dict]:
        # Parse rpm --dump output into list of file info dicts
        files = []
        for line in raw_files.splitlines():
            fields = line.split()
            if len(fields) < RPM_DUMP_FIELD_COUNT:
                self.logger.warning(f"Info2Dic: Skipping malformed file-dump line: {line}")
                continue
            try:
                mtime = datetime.fromtimestamp(int(fields[2]), tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            except (ValueError, OSError):
                mtime = fields[2]
            files.append(
                {
                    "path": fields[0],
                    "size": int(fields[1]),
                    "mtime": mtime,
                    "hash": fields[3],
                    "mode": fields[4],
                    "owner": fields[5],
                    "group": fields[6],
                    "isconfig": int(fields[7]),
                    "isdoc": int(fields[8]),
                    "rdev": int(fields[9]),
                    "symlink": fields[10],
                }
            )
        return files

    def _parse_package_fields(self, package_lines: List[str], result: dict) -> None:
        # Extract structured fields from rpm -qi header lines into result dict
        for line in package_lines:
            title, _, content = line.partition(":")
            title, content = title.strip(), content.strip()
            if title == "Size":
                result["size"] = int(content)
            elif title == "Signature":
                result["signature"] = self._parse_signature(content)
            elif title in FIELD_MAP:
                result[FIELD_MAP[title]] = content

    def _parse_signature(self, content: str) -> Dict[str, str]:
        # Parse RPM signature line into structured dict
        parts = content.split(",")
        if len(parts) >= 3:
            raw_time = parts[1].strip()
            try:
                parsed = datetime.strptime(raw_time, "%a %d %b %Y %I:%M:%S %p %Z")
                normalized_time = parsed.strftime("%Y-%m-%dT%H:%M:%SZ")
            except ValueError:
                normalized_time = raw_time
            return {"scheme": parts[0].strip(), "time": normalized_time, "key": parts[2].strip()}
        self.logger.warning(f"Info2Dic: Unexpected Signature format: {content}")
        return {"scheme": content.strip(), "time": "", "key": ""}

    def _run_subprocess(
        self,
        command: Union[List[str], str],
        *,
        error_context: str,
        shell: bool = False,
        text: bool = True,
        timeout: int = SUBPROCESS_TIMEOUT,
    ) -> subprocess.CompletedProcess:
        # Execute subprocess and raise PluginException on non-zero exit or timeout
        try:
            result = subprocess.run(
                command, shell=shell, capture_output=True, text=text, timeout=timeout, check=False  # noqa: B602
            )
            if result.returncode != 0:
                stderr_output = result.stderr if isinstance(result.stderr, str) else result.stderr.decode("utf-8")
                raise PluginException(
                    cause=error_context,
                    assistance=f"stderr: {stderr_output}",
                )
            return result
        except subprocess.TimeoutExpired:
            raise PluginException(
                cause=f"{error_context}: command timed out after {timeout} seconds",
                assistance="Consider increasing the timeout or verifying network/repository availability.",
            )
        except OSError as error:
            raise PluginException(
                cause=f"{error_context}: OS error executing command",
                assistance=str(error),
            )

    def _trim_epoch(self, package_label: str) -> str:
        # Remove epoch prefix from package label for cache filename
        return re.sub(r"(-)(0:)", r"\1", package_label)

    def _trim_epochs(self, packages: List[str]) -> List[str]:
        # Remove epoch prefixes from a list of packages
        return [self._trim_epoch(package) for package in packages]
