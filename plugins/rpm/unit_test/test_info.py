import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_rpm.actions.info import Info
from komand_rpm.actions.info.schema import Input
from parameterized import parameterized

from util import STUB_CACHED_RESULT, STUB_INFO2DIC_RESULT, Util


class TestInfo(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(Info())

    @parameterized.expand(
        [
            (
                "basic_package_lookup",
                {
                    Input.NAME: "curl",
                    Input.ARCH: "x86_64",
                    Input.DISTRO: "CentOS 7",
                },
                None,
                STUB_INFO2DIC_RESULT,
            ),
            (
                "with_version_and_release",
                {
                    Input.NAME: "curl",
                    Input.VERSION: "7.29.0",
                    Input.RELEASE: "54.el7_6.3",
                    Input.ARCH: "x86_64",
                    Input.DISTRO: "CentOS 7",
                },
                None,
                STUB_INFO2DIC_RESULT,
            ),
            (
                "with_epoch_zero_stripped",
                {
                    Input.NAME: "curl",
                    Input.EPOCH: "0",
                    Input.ARCH: "x86_64",
                    Input.DISTRO: "CentOS 7",
                },
                None,
                STUB_INFO2DIC_RESULT,
            ),
            (
                "with_custom_repo_and_key",
                {
                    Input.NAME: "curl",
                    Input.ARCH: "x86_64",
                    Input.DISTRO: "CentOS 7",
                    Input.REPO: "https://mirror.centos.org/centos/7/os/x86_64/",
                    Input.KEY: "https://www.redhat.com/security/data/fd431d51.txt",
                },
                None,
                STUB_INFO2DIC_RESULT,
            ),
            (
                "cache_hit",
                {
                    Input.NAME: "cached-pkg",
                    Input.ARCH: "x86_64",
                    Input.DISTRO: "CentOS 7",
                },
                STUB_CACHED_RESULT,
                STUB_CACHED_RESULT,
            ),
        ]
    )
    @patch("komand_rpm.actions.info.action.RPMHelper")
    def test_info(
        self, _name: str, params: dict, cache_return: dict | None, expected: dict, mock_helper_cls: MagicMock
    ) -> None:
        # Setup mock for helper
        helper = Util.mock_helper(mock_helper_cls, package_name=params.get(Input.NAME, ""))
        helper.check_rpm_cache.return_value = cache_return

        # Run the action and check results
        result = self.action.run(params)
        self.assertEqual(result, expected)
        helper.list_package.assert_called_once()

        # Verify cache behavior
        if cache_return:
            helper.download_package.assert_not_called()
        else:
            helper.download_package.assert_called_once()

    @parameterized.expand(
        [
            (
                "invalid_name_shell_metachar",
                {
                    Input.NAME: "curl;rm -rf /",
                    Input.ARCH: "x86_64",
                    Input.DISTRO: "CentOS 7",
                },
            ),
            (
                "invalid_repo_url_scheme",
                {
                    Input.NAME: "curl",
                    Input.ARCH: "x86_64",
                    Input.DISTRO: "CentOS 7",
                    Input.REPO: "ftp://bad.repo/file.repo",
                },
            ),
            (
                "invalid_key_url_scheme",
                {
                    Input.NAME: "curl",
                    Input.ARCH: "x86_64",
                    Input.DISTRO: "CentOS 7",
                    Input.KEY: "ftp://bad.key/key.txt",
                },
            ),
        ]
    )
    @patch("komand_rpm.actions.info.action.RPMHelper")
    def test_info_validation_error(self, _name: str, params: dict, mock_helper_cls: MagicMock) -> None:
        # Setup mock for helper
        helper = mock_helper_cls.return_value
        helper.validate_input.side_effect = Util.mock_validate_input
        helper.validate_url.side_effect = Util.mock_validate_url

        # Run the action and check that a PluginException is raised
        with self.assertRaises(PluginException):
            self.action.run(params)

    @patch("komand_rpm.actions.info.action.RPMHelper")
    def test_info_package_not_found(self, mock_helper_cls: MagicMock) -> None:
        # Setup mock for helper
        helper = Util.mock_helper(mock_helper_cls, package_name="nonexistent")
        helper.list_package.side_effect = PluginException(
            cause="Package not found with label nonexistent",
            assistance="Verify the package name, version, architecture, and distribution are correct.",
        )

        # Run the action and check that a PluginException is raised
        with self.assertRaises(PluginException):
            self.action.run(
                {
                    Input.NAME: "nonexistent",
                    Input.ARCH: "x86_64",
                    Input.DISTRO: "CentOS 7",
                }
            )

    @patch("komand_rpm.actions.info.action.RPMHelper")
    def test_info_download_failure(self, mock_helper_cls: MagicMock) -> None:
        # Setup mock for helper
        helper = Util.mock_helper(mock_helper_cls)
        helper.download_package.side_effect = PluginException(
            cause="Failed to download package curl",
            assistance="Verify the package exists in the configured repositories.",
        )

        # Run the action and check that a PluginException is raised
        with self.assertRaises(PluginException):
            self.action.run(
                {
                    Input.NAME: "curl",
                    Input.ARCH: "x86_64",
                    Input.DISTRO: "CentOS 7",
                }
            )

    @patch("komand_rpm.actions.info.action.os.path.isfile", return_value=False)
    @patch("komand_rpm.actions.info.action.RPMHelper")
    def test_info_checksig_failure_with_key(self, mock_helper_cls: MagicMock, _mock_isfile: MagicMock) -> None:
        # Setup mock for helper
        helper = Util.mock_helper(mock_helper_cls)
        helper.checksig.side_effect = PluginException(
            cause="RPM signature check failed for /tmp/curl.rpm",
            assistance="The package signature could not be verified.",
        )

        # Run the action and check that a PluginException is raised
        with self.assertRaises(PluginException):
            self.action.run(
                {
                    Input.NAME: "curl",
                    Input.ARCH: "x86_64",
                    Input.DISTRO: "CentOS 7",
                    Input.REPO: "https://mirror.centos.org/centos/7/os/x86_64/",
                    Input.KEY: "https://www.redhat.com/security/data/fd431d51.txt",
                }
            )

    @patch("komand_rpm.actions.info.action.RPMHelper")
    def test_info_minimal_inputs(self, mock_helper_cls: MagicMock) -> None:
        # Setup mock for helper
        helper = Util.mock_helper(mock_helper_cls, package_name="wget")
        helper.check_rpm_cache.return_value = None

        # Run the action and check that optional helpers are not called
        result = self.action.run(
            {
                Input.NAME: "wget",
                Input.ARCH: "x86_64",
                Input.DISTRO: "CentOS 7",
            }
        )

        self.assertEqual(result, STUB_INFO2DIC_RESULT)
        helper.add_repo.assert_not_called()
        helper.add_key.assert_not_called()
        helper.checksig.assert_not_called()

    @parameterized.expand(
        [
            (
                "nonzero_epoch",
                {Input.NAME: "curl", Input.EPOCH: "2", Input.ARCH: "x86_64", Input.DISTRO: "CentOS 7"},
                ("curl", "2", "", ""),
            ),
            (
                "version_no_release",
                {Input.NAME: "curl", Input.VERSION: "7.29.0", Input.ARCH: "x86_64", Input.DISTRO: "CentOS 7"},
                ("curl", "", "7.29.0", ""),
            ),
        ]
    )
    @patch("komand_rpm.actions.info.action.RPMHelper")
    def test_info_make_label_args(
        self, _name: str, params: dict, expected_label_args: tuple, mock_helper_cls: MagicMock
    ) -> None:
        # Setup mock for helper
        helper = Util.mock_helper(mock_helper_cls, package_name="curl")
        helper.check_rpm_cache.return_value = None

        # Run the action and check make_label receives correct arguments
        self.action.run(params)

        helper.make_label.assert_called_once_with(*expected_label_args)

    @patch("komand_rpm.actions.info.action.RPMHelper")
    def test_info_repo_only(self, mock_helper_cls: MagicMock) -> None:
        # Setup mock for helper
        helper = Util.mock_helper(mock_helper_cls, package_name="curl")
        helper.check_rpm_cache.return_value = None

        # Run the action and check repo-only flow
        self.action.run(
            {
                Input.NAME: "curl",
                Input.ARCH: "x86_64",
                Input.DISTRO: "CentOS 7",
                Input.REPO: "https://mirror.centos.org/centos/7/os/x86_64/",
            }
        )

        # Verify add_repo called, add_key/checksig not called, repo_ids passed correctly
        helper.add_repo.assert_called_once_with("https://mirror.centos.org/centos/7/os/x86_64/")
        helper.add_key.assert_not_called()
        helper.checksig.assert_not_called()
        helper.list_package.assert_called_once_with("curl", "x86_64", "CentOS 7", ["custom-repo"])
        helper.download_package.assert_called_once_with("curl", "x86_64", "CentOS 7", ["curl.rpm"], ["custom-repo"])

    @patch("komand_rpm.actions.info.action.RPMHelper")
    def test_info_key_only(self, mock_helper_cls: MagicMock) -> None:
        # Setup mock for helper
        helper = Util.mock_helper(mock_helper_cls, package_name="curl")
        helper.check_rpm_cache.return_value = None

        # Run the action and check key-only flow
        self.action.run(
            {
                Input.NAME: "curl",
                Input.ARCH: "x86_64",
                Input.DISTRO: "CentOS 7",
                Input.KEY: "https://www.redhat.com/security/data/fd431d51.txt",
            }
        )

        # Verify add_key/checksig called, add_repo not called, repo_ids=None
        helper.add_key.assert_called_once_with("https://www.redhat.com/security/data/fd431d51.txt")
        helper.checksig.assert_called_once_with("/tmp/curl.rpm")
        helper.add_repo.assert_not_called()
        helper.list_package.assert_called_once_with("curl", "x86_64", "CentOS 7", None)

    @patch("komand_rpm.actions.info.action.RPMHelper")
    def test_info_centos7_non_x86_64(self, mock_helper_cls: MagicMock) -> None:
        # Setup mock for helper
        helper = Util.mock_helper(mock_helper_cls, package_name="curl")
        helper.check_rpm_cache.return_value = None

        # Run the action and check that arch mismatch is logged
        with self.assertLogs("action logger", level="ERROR") as log_ctx:
            result = self.action.run(
                {
                    Input.NAME: "curl",
                    Input.ARCH: "i686",
                    Input.DISTRO: "CentOS 7",
                }
            )

        self.assertEqual(result, STUB_INFO2DIC_RESULT)
        self.assertTrue(any("CentOS 7 only supports x86_64" in msg for msg in log_ctx.output))

    @patch("komand_rpm.actions.info.action.RPMHelper")
    def test_info_cache_hit_skips_download(self, mock_helper_cls: MagicMock) -> None:
        # Setup mock for helper with cache hit
        helper = Util.mock_helper(mock_helper_cls, package_name="cached-pkg")
        helper.check_rpm_cache.return_value = STUB_CACHED_RESULT

        # Run the action and check that download/info/cache update are skipped
        result = self.action.run(
            {
                Input.NAME: "cached-pkg",
                Input.ARCH: "x86_64",
                Input.DISTRO: "CentOS 7",
            }
        )

        self.assertEqual(result, STUB_CACHED_RESULT)
        helper.download_package.assert_not_called()
        helper.package_info.assert_not_called()
        helper.info2dic.assert_not_called()
        helper.update_cache.assert_not_called()

    @parameterized.expand(
        [
            ("metachar_name", {Input.NAME: "curl;rm -rf /", Input.ARCH: "x86_64", Input.DISTRO: "CentOS 7"}),
            (
                "metachar_epoch",
                {Input.NAME: "curl", Input.EPOCH: "1|bad", Input.ARCH: "x86_64", Input.DISTRO: "CentOS 7"},
            ),
            (
                "metachar_version",
                {Input.NAME: "curl", Input.VERSION: "1.0&bad", Input.ARCH: "x86_64", Input.DISTRO: "CentOS 7"},
            ),
            (
                "metachar_release",
                {Input.NAME: "curl", Input.RELEASE: "1<bad", Input.ARCH: "x86_64", Input.DISTRO: "CentOS 7"},
            ),
            (
                "metachar_repo",
                {
                    Input.NAME: "curl",
                    Input.REPO: "https://ok.com/`bad`",
                    Input.ARCH: "x86_64",
                    Input.DISTRO: "CentOS 7",
                },
            ),
            (
                "metachar_key",
                {
                    Input.NAME: "curl",
                    Input.KEY: "https://ok.com/key;bad",
                    Input.ARCH: "x86_64",
                    Input.DISTRO: "CentOS 7",
                },
            ),
        ]
    )
    @patch("komand_rpm.actions.info.action.RPMHelper")
    def test_info_per_field_metachar_validation(self, _name: str, params: dict, mock_helper_cls: MagicMock) -> None:
        # Setup mock for helper
        helper = mock_helper_cls.return_value
        helper.validate_input.side_effect = Util.mock_validate_input
        helper.validate_url.side_effect = Util.mock_validate_url

        # Run the action and check that a PluginException is raised
        with self.assertRaises(PluginException):
            self.action.run(params)

    @patch("komand_rpm.actions.info.action.os.remove")
    @patch("komand_rpm.actions.info.action.os.path.isfile", return_value=True)
    @patch("komand_rpm.actions.info.action.RPMHelper")
    def test_info_cleanup_success_with_repo(
        self, mock_helper_cls: MagicMock, mock_isfile: MagicMock, mock_remove: MagicMock
    ) -> None:
        # Setup mock for helper
        helper = Util.mock_helper(mock_helper_cls, package_name="curl")
        helper.check_rpm_cache.return_value = None

        # Run the action and check cleanup removes both package and repo file
        self.action.run(
            {
                Input.NAME: "curl",
                Input.ARCH: "x86_64",
                Input.DISTRO: "CentOS 7",
                Input.REPO: "https://mirror.centos.org/centos/7/os/x86_64/",
            }
        )

        mock_remove.assert_any_call("/tmp/curl.rpm")
        mock_remove.assert_any_call("/tmp/custom.repo")
        self.assertEqual(mock_remove.call_count, 2)

    @patch("komand_rpm.actions.info.action.os.remove")
    @patch("komand_rpm.actions.info.action.os.path.isfile", return_value=True)
    @patch("komand_rpm.actions.info.action.RPMHelper")
    def test_info_cleanup_success_without_repo(
        self, mock_helper_cls: MagicMock, mock_isfile: MagicMock, mock_remove: MagicMock
    ) -> None:
        # Setup mock for helper
        helper = Util.mock_helper(mock_helper_cls, package_name="curl")
        helper.check_rpm_cache.return_value = None

        # Run the action and check cleanup removes package file only
        self.action.run(
            {
                Input.NAME: "curl",
                Input.ARCH: "x86_64",
                Input.DISTRO: "CentOS 7",
            }
        )

        mock_remove.assert_called_once_with("/tmp/curl.rpm")

    @patch("komand_rpm.actions.info.action.os.remove")
    @patch("komand_rpm.actions.info.action.os.path.isfile", return_value=True)
    @patch("komand_rpm.actions.info.action.RPMHelper")
    def test_info_cleanup_exception_isfile_true(
        self, mock_helper_cls: MagicMock, mock_isfile: MagicMock, mock_remove: MagicMock
    ) -> None:
        # Setup mock for helper with checksig failure
        helper = Util.mock_helper(mock_helper_cls, package_name="curl")
        helper.check_rpm_cache.return_value = None
        helper.checksig.side_effect = PluginException(
            cause="Signature check failed",
            assistance="Verify the package signature.",
        )

        # Run the action and check that cleanup still runs on exception
        with self.assertRaises(PluginException):
            self.action.run(
                {
                    Input.NAME: "curl",
                    Input.ARCH: "x86_64",
                    Input.DISTRO: "CentOS 7",
                    Input.KEY: "https://www.redhat.com/security/data/fd431d51.txt",
                }
            )

        mock_remove.assert_any_call("/tmp/curl.rpm")

    @patch("komand_rpm.actions.info.action.os.remove")
    @patch("komand_rpm.actions.info.action.os.path.isfile", return_value=False)
    @patch("komand_rpm.actions.info.action.RPMHelper")
    def test_info_cleanup_exception_isfile_false(
        self, mock_helper_cls: MagicMock, mock_isfile: MagicMock, mock_remove: MagicMock
    ) -> None:
        # Setup mock for helper with checksig failure
        helper = Util.mock_helper(mock_helper_cls, package_name="curl")
        helper.check_rpm_cache.return_value = None
        helper.checksig.side_effect = PluginException(
            cause="Signature check failed",
            assistance="Verify the package signature.",
        )

        # Run the action and check that os.remove is NOT called when isfile=False
        with self.assertRaises(PluginException):
            self.action.run(
                {
                    Input.NAME: "curl",
                    Input.ARCH: "x86_64",
                    Input.DISTRO: "CentOS 7",
                    Input.KEY: "https://www.redhat.com/security/data/fd431d51.txt",
                }
            )

        mock_remove.assert_not_called()
