import json
import os
import re
import secrets
import shutil
import subprocess  # noqa: B404
import tempfile
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
        for package in package_list:
            package_path = TEMP_DIR / package
            if package_path.is_file():
                return str(package_path)

        self.logger.info(f"DownloadPackage: Downloading package with label {label}")

        parameters = self._build_params(arch, distro, repo_ids)
        command = ["dnf", "download", "--destdir", str(TEMP_DIR)] + parameters + [label]
        self._run_subprocess(
            command,
            error_context=f"Failed to download package {label}",
        )

        # Check destdir for the downloaded RPM rather than parsing dnf output
        for package in package_list:
            package_path = TEMP_DIR / package
            if package_path.is_file():
                self.logger.info(f"DownloadPackage: Found {package_path}")
                return str(package_path)

        raise PluginException(
            cause=f"Failed to download package {label}",
            assistance="Verify the package exists in the configured repositories.",
        )

    def info2dic(self, info: Dict[str, str]) -> Dict:  # noqa: MC0001
        # Parse rpm query output into structured package dict
        package_info_dict: dict = {"found": True}
        package_lines = info.get("package", "").splitlines()[:17]
        package_description = (
            info.get("package", "").splitlines()[18] if len(info.get("package", "").splitlines()) > 18 else ""
        )
        file_lines = info.get("files", "").splitlines()

        files = []
        for file_line in file_lines:
            fields = file_line.split()
            if len(fields) < RPM_DUMP_FIELD_COUNT:
                self.logger.warning(f"Info2Dic: Skipping malformed file-dump line: {file_line}")
                continue
            files.append(
                {
                    "path": fields[0],
                    "size": int(fields[1]),
                    "mtime": fields[2],
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

        for line in package_lines:
            title, _, content = line.partition(":")
            title, content = title.strip(), content.strip()
            if title == "Size":
                package_info_dict["size"] = int(content)
            elif title == "Signature":
                signature_parts = content.split(",")
                package_info_dict["signature"] = {
                    "scheme": signature_parts[0].strip(),
                    "time": signature_parts[1].strip(),
                    "key": signature_parts[2].strip(),
                }
            elif title in FIELD_MAP:
                package_info_dict[FIELD_MAP[title]] = content

        package_info_dict["description"] = "".join(package_description)
        package_info_dict["files"] = files
        return package_info_dict

    def list_package(self, label: str, arch: str, distro: str, repo_ids: Optional[List[str]] = None) -> List[str]:
        # Query repo for packages matching label
        parameters = self._build_params(arch, distro, repo_ids)
        command = ["dnf", "repoquery", "-q"] + parameters + [label]
        result = self._run_subprocess(
            command,
            error_context=f"Package not found with label {label}",
        )
        if not result.stdout.strip():
            self.logger.error(f"ListPackage: {result.stdout}{result.stderr}")
            raise PluginException(
                cause=f"Package not found with label {label}",
                assistance="Verify the package name, version, architecture, and distribution are correct.",
            )
        return self._add_rpm_exts(self._trim_epochs(result.stdout.splitlines()))

    def make_label(self, name: str, epoch: str, version: str, release: str) -> str:
        # Build package label from name, epoch, version, release
        label = name
        if epoch and epoch != "0":
            label += f"-{epoch}:"
        else:
            label += "-"

        if version and release:
            return f"{label}{version}-{release}"
        elif version:
            return f"{label}{version}"
        else:
            return name

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
        return {
            "package": info_result.stdout,
            "files": dump_result.stdout,
        }

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

    def _add_rpm_ext(self, package: str) -> str:
        # Add .rpm extension if not present
        return package if package.endswith(".rpm") else f"{package}.rpm"

    def _add_rpm_exts(self, packages: List[str]) -> List[str]:
        # Add .rpm extension to packages if not present
        return [package if package.endswith(".rpm") else f"{package}.rpm" for package in packages]

    def _build_params(self, arch: str, distro: str, repo_ids: Optional[List[str]] = None) -> List[str]:
        # Build dnf command parameters for architecture, distro, and repos
        parameters: List[str] = ["--disableplugin=system_upgrade"]
        if arch and arch != "noarch":
            if arch == "i686":
                parameters.append("--archlist=i386,i686,noarch")
            else:
                parameters.append(f"--archlist={arch},noarch")
        else:
            parameters.append("--archlist=noarch")

        parameters.append(f"--releasever={distro.split()[1]}")
        parameters.append("--disablerepo=*")
        repos_to_enable = repo_ids if repo_ids else REPOS.get(distro, [])
        for repo in repos_to_enable:
            parameters.append(f"--enablerepo={repo}")
        return parameters

    def _format_repofile(self, repo_name: str) -> str:
        # Add .repo extension if not present
        return repo_name if repo_name.endswith(".repo") else f"{repo_name}.repo"

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

    def _run_subprocess(
        self,
        command: Union[List[str], str],
        *,
        error_context: str,
        shell: bool = False,
        text: bool = True,
        timeout: int = SUBPROCESS_TIMEOUT,
    ) -> subprocess.CompletedProcess:
        # Execute subprocess and raise PluginException on non-zero exit
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

    def _trim_epoch(self, package_label: str) -> str:
        # Remove epoch prefix (0:) from package label
        return re.sub(r"(-)(0:)", r"\1", package_label)

    def _trim_epochs(self, packages: List[str]) -> List[str]:
        # Remove epoch prefixes from a list of packages
        return [self._trim_epoch(package) for package in packages]
