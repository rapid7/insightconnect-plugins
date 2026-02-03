import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from komand_rapid7_insightvm.actions import UpdateSharedCredential
from komand_rapid7_insightvm.actions.update_shared_credential.schema import Input

from util import Util


@patch("requests.sessions.Session.put", side_effect=Util.mocked_requests)
class TestUpdateSharedCredential(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UpdateSharedCredential())

    @parameterized.expand(
        [
            [
                "as400 service test",
                {"service": "as400", "domain": "rapid7.com", "username": "username", "password": "password"},
                "test for as400 service",
                "",
                1,
                "as400_test_valid",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
            [
                "cifs service test",
                {"service": "cifs", "domain": "rapid7.com", "username": "username", "password": "password"},
                "test for cifs service",
                "",
                1,
                "cifs_test_valid",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
            [
                "cifshash service test",
                {"service": "cifshash", "domain": "rapid7.com", "username": "username", "ntlm_hash": "ntlm_hash"},
                "test for cifshash service",
                "",
                1,
                "cifshash_test_valid",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
            [
                "cvs service test",
                {"service": "cvs", "domain": "rapid7.com", "username": "username", "password": "password"},
                "test for cvs service",
                "",
                1,
                "cvs_test_valid",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
            [
                "db2 service test",
                {"service": "db2", "database": "rapid7_database", "username": "username", "password": "password"},
                "test for db2 service",
                "",
                1,
                "db2_test_valid",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
            [
                "ftp service test",
                {"service": "ftp", "username": "username", "password": "password"},
                "test for ftp service",
                "",
                1,
                "ftp_test_valid",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
            [
                "http service test",
                {"service": "http", "realm": "realm", "username": "username", "password": "password"},
                "test for http service",
                "",
                1,
                "http_test_valid",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
            [
                "ms-sql service test - Windows Auth true",
                {
                    "service": "ms-sql",
                    "database": "rapid7_database",
                    "use_windows_authentication": True,
                    "domain": "rapid7.com",
                    "username": "username",
                    "password": "password",
                },
                "test for ms-sql service, windows auth true",
                "",
                1,
                "db2_test_valid",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
            [
                "ms-sql service test - Windows Auth false",
                {
                    "service": "ms-sql",
                    "database": "rapid7_database",
                    "use_windows_authentication": False,
                    "username": "username",
                    "password": "password",
                },
                "test for ms-sql service, windows auth false",
                "",
                1,
                "db2_test_valid",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
            [
                "mysql service test",
                {"service": "mysql", "database": "rapid7_database", "username": "username", "password": "password"},
                "test for mysql service",
                "",
                1,
                "mysql_test_valid",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
            [
                "notes service test",
                {"service": "notes", "notes_id_password": "password"},
                "test for mysql service",
                "",
                1,
                "mysql_test_valid",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
            [
                "oracle service test sids false",
                {"service": "oracle", "username": "username", "password": "password", "enumerate_sids": False},
                "test for oracle service without using oracle listener password",
                "",
                1,
                "oracle_test_valid",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
            [
                "oracle service test sids true",
                {
                    "service": "oracle",
                    "username": "username",
                    "password": "password",
                    "enumerate_sids": True,
                    "oracle_listener_password": "password",
                },
                "test for oracle service using oracle listener password",
                "",
                1,
                "oracle_test_valid",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
            [
                "pop service test",
                {
                    "service": "pop",
                    "username": "username",
                    "password": "password",
                },
                "test for pop service",
                "",
                1,
                "pop_test_valid",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
            [
                "postgresql service test",
                {
                    "service": "postgresql",
                    "database": "rapid7_database",
                    "username": "username",
                    "password": "password",
                },
                "test for postgresql service",
                "",
                1,
                "postgresql_test_valid",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
            [
                "remote-exec service test",
                {"service": "remote-exec", "username": "username", "password": "password"},
                "test for remote-exec service",
                "",
                1,
                "remote_exec_test_valid",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
            [
                "snmp service test",
                {"service": "snmp", "community_name": "community_name"},
                "test for snmp service",
                "",
                1,
                "snmp_test_valid",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
            [
                "snmpv3 service private password test",
                {
                    "service": "snmpv3",
                    "authentication_type": "no-authentication",
                    "username": "username",
                    "password": "password",
                    "privacy_type": "no-privacy",
                    "privacy_password": "private-password",
                },
                "test for snmp service with private password",
                "",
                1,
                "snmp_test_valid",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
            [
                "snmpv3 service sha test",
                {
                    "service": "snmpv3",
                    "authentication_type": "sha",
                    "username": "username",
                    "password": "password",
                    "privacy_type": "no-privacy",
                },
                "test for snmp service with authentication type set to sha",
                "",
                1,
                "snmp_test_valid sha",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
            [
                "ssh service no elevation test",
                {
                    "service": "ssh",
                    "username": "username",
                    "password": "password",
                    "permission_elevation": "none",
                },
                "test for the ssh service when permission elevation is set to none",
                "",
                1,
                "ssh_test_valid none",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
            [
                "ssh service sudo elevation test",
                {
                    "service": "ssh",
                    "username": "username",
                    "password": "password",
                    "permission_elevation": "sudo",
                    "permission_elevation_username": "username",
                    "permission_elevation_password": "password",
                },
                "test for the ssh service when permission elevation is set to sudo",
                "",
                1,
                "ssh_test_valid sudo",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
            [
                "ssh-key service test",
                {
                    "service": "ssh-key",
                    "username": "username",
                    "private_key_password": "private_key_password",
                    "pem_key": "pem_key",
                    "permission_elevation": "sudo",
                    "permission_elevation_username": "username",
                    "permission_elevation_password": "password",
                },
                "test for ssh-key service",
                "",
                1,
                "ssh_key_test_valid sudo",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
            [
                "sybase service windows auth true test",
                {
                    "service": "sybase",
                    "database": "rapid7_database",
                    "use_windows_authentication": True,
                    "domain": "rapid7.com",
                    "username": "username",
                    "password": "password",
                },
                "test for sybase service windows auth true",
                "",
                1,
                "sybase_test_valid windows true",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
            [
                "sybase service windows auth false test",
                {
                    "service": "sybase",
                    "database": "rapid7_database",
                    "use_windows_authentication": False,
                    "username": "username",
                    "password": "password",
                },
                "test for sybase service windows auth false",
                "",
                1,
                "sybase_test_valid windows false",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
            [
                "telnet service windows auth false test",
                {"service": "telnet", "username": "username", "password": "password"},
                "test for telnet service",
                "",
                1,
                "telnet_test_valid",
                "",
                "all-sites",
                [],
                {
                    "links": [
                        {
                            "href": "https://ivm-console-test.vuln.lax.rapid7.com:3780/api/3/shared_credentials/1",
                            "rel": "self",
                        }
                    ]
                },
            ],
        ]
    )
    def test_update_shared_credentials_valid(
        self,
        mock_put,
        test_name,
        account,
        description,
        host_restrictions,
        id_,
        name,
        port_restrictions,
        site_assignment,
        sites,
        expected,
    ) -> None:
        actual = self.action.run(
            {
                Input.ACCOUNT: account,
                Input.DESCRIPTION: description,
                Input.HOST_RESTRICTION: host_restrictions,
                Input.ID: id_,
                Input.NAME: name,
                Input.PORT_RESTRICTION: port_restrictions,
                Input.SITE_ASSIGNMENT: site_assignment,
                Input.SITES: sites,
            }
        )
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "snmpv3 service no private password test",
                {
                    "service": "snmpv3",
                    "authentication_type": "no-authentication",
                    "username": "username",
                    "password": "password",
                    "privacy_type": "no-privacy",
                    "privacy_password": "",
                },
                "test for snmp service without private password",
                "",
                2,
                "snmp_test_invalid",
                "",
                "all-sites",
                [],
                "Privacy_password is required when authentication_type is no-authentication and privacy_type is no-privacy.",
            ],
            [
                "check_not_null test",
                {
                    "service": "",
                    "authentication_type": "sha",
                    "username": "username",
                    "password": "password",
                    "privacy_type": "no-privacy",
                    "privacy_password": "",
                },
                "test for check_not_null",
                "",
                2,
                "snmp_test_invalid",
                "",
                "all-sites",
                [],
                "service has not been entered.",
            ],
        ]
    )
    def test_update_shared_credentials_error(
        self,
        mock_put,
        test_name,
        account,
        description,
        host_restrictions,
        id_,
        name,
        port_restrictions,
        site_assignment,
        sites,
        expected,
    ) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(
                {
                    Input.ACCOUNT: account,
                    Input.DESCRIPTION: description,
                    Input.HOST_RESTRICTION: host_restrictions,
                    Input.ID: id_,
                    Input.NAME: name,
                    Input.PORT_RESTRICTION: port_restrictions,
                    Input.SITE_ASSIGNMENT: site_assignment,
                    Input.SITES: sites,
                }
            )
        self.assertEqual(context.exception.cause, expected)
