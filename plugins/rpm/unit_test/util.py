import logging
from unittest.mock import MagicMock

from insightconnect_plugin_runtime.action import Action
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_rpm.connection.connection import Connection

STUB_PACKAGE_INFO_OUTPUT = (
    "Name        : curl\n"
    "Version     : 7.29.0\n"
    "Release     : 54.el7_6.3\n"
    "Architecture: x86_64\n"
    "License     : MIT\n"
    "Signature   : RSA/SHA256, Mon 01 Apr 2019 12:00:00 PM UTC, Key ID 24c6a8a7f4a80eb5\n"
    "Source RPM  : curl-7.29.0-54.el7_6.3.src.rpm\n"
    "Build Date  : Mon 01 Apr 2019 12:00:00 PM UTC\n"
    "Build Host  : x86-01.bsys.centos.org\n"
    "Relocations : (not relocatable)\n"
    "Packager    : CentOS BuildSystem <http://bugs.centos.org>\n"
    "Vendor      : CentOS\n"
    "URL         : https://curl.haxx.se/\n"
    "Summary     : A utility for getting files from remote servers\n"
    "Size        : 533840\n"
    "             \n"
    "             \n"
    "             \n"
    "curl is a command line tool for transferring data with URL syntax"
)

STUB_DUMP_OUTPUT = "/usr/bin/curl 156000 1554120000 d41d8cd98f00b204e9800998ecf8427e" " 0100755 root root 0 0 0 (none)"

STUB_INFO2DIC_RESULT = {
    "found": True,
    "name": "curl",
    "version": "7.29.0",
    "release": "54.el7_6.3",
    "architecture": "x86_64",
    "license": "MIT",
    "signature": {
        "scheme": "RSA/SHA256",
        "time": "Mon 01 Apr 2019 12:00:00 PM UTC",
        "key": "Key ID 24c6a8a7f4a80eb5",
    },
    "source": "curl-7.29.0-54.el7_6.3.src.rpm",
    "build_date": "Mon 01 Apr 2019 12:00:00 PM UTC",
    "build_host": "x86-01.bsys.centos.org",
    "relocations": "(not relocatable)",
    "vendor": "CentOS",
    "packager": "CentOS BuildSystem <http://bugs.centos.org>",
    "summary": "A utility for getting files from remote servers",
    "url": "https://curl.haxx.se/",
    "size": 533840,
    "description": "curl is a command line tool for transferring data with URL syntax",
    "files": [
        {
            "path": "/usr/bin/curl",
            "size": 156000,
            "mtime": "1554120000",
            "hash": "d41d8cd98f00b204e9800998ecf8427e",
            "mode": "0100755",
            "owner": "root",
            "group": "root",
            "isconfig": 0,
            "isdoc": 0,
            "rdev": 0,
            "symlink": "(none)",
        }
    ],
}

STUB_CACHED_RESULT = {
    "found": True,
    "name": "cached-pkg",
    "version": "1.0.0",
}

SHELL_METACHARACTERS = ";|&<>`\n\r"


class Util:
    @staticmethod
    def default_connector(action: Action) -> Action:
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def mock_helper(mock_helper_cls: MagicMock, *, package_name: str = "curl") -> MagicMock:
        helper = mock_helper_cls.return_value
        helper.check_rpm_cache.return_value = None
        helper.make_label.return_value = package_name
        helper.list_package.return_value = [f"{package_name}.rpm"]
        helper.add_repo.return_value = {"path": "/tmp/custom.repo", "ids": ["custom-repo"]}
        helper.download_package.return_value = f"/tmp/{package_name}.rpm"
        helper.package_info.return_value = {"package": STUB_PACKAGE_INFO_OUTPUT, "files": STUB_DUMP_OUTPUT}
        helper.info2dic.return_value = STUB_INFO2DIC_RESULT
        return helper

    @staticmethod
    def mock_validate_input(value: str, field: str) -> None:
        if any(char in value for char in SHELL_METACHARACTERS):
            raise PluginException(
                cause=f"Invalid characters in {field}",
                assistance=f"The {field} field contains shell metacharacters which are not allowed.",
            )

    @staticmethod
    def mock_validate_url(url: str) -> None:
        if not url.startswith(("http://", "https://")):
            raise PluginException(
                cause=f"Invalid URL scheme: {url}",
                assistance="Only http:// and https:// URLs are supported.",
            )
