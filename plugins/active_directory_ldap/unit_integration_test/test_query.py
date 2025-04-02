from unittest import TestCase
from komand_active_directory_ldap.actions import Query
from komand_active_directory_ldap.connection import Connection
import logging
import json


class TestQuery(TestCase):
    def test_query(self):
        # This is a live test. Run icon-lab set and uncomment to run

        log = logging.getLogger("Test")

        test_connection = Connection()
        test_query = Query()

        test_connection.logger = log
        test_query.logger = log

        with open("../tests/query.json", encoding="utf-8") as file:
            data = json.load(file)
            connection_params = data.get("body").get("connection")

        print(connection_params)

        test_connection.connect(connection_params)
        test_query.connection = test_connection

        # CN=Bob \"SpongePants\" (somestuff),OU=Test Users,OU=User,DC=intad,DC=dslab,DC=internal

        query_params = {
            "search_base": "DC=intad,DC=dslab,DC=internal",
            "search_filter": '(distinguishedName=CN=Bob "Sponge,Pants" (somestuff),OU=Test Users,OU=User,DC=intad,DC=dslab,DC=internal)',
        }

        result = test_query.run(query_params)
        print(result)
        actual = result.get("results")[0].get("attributes")
        dn = result.get("results")[0].get("dn")
        print(actual.get("cn"))
        print(actual.get("dn"))

        self.assertEqual(actual.get("cn"), 'Bob "Sponge,Pants" (somestuff)')
        self.assertEqual(
            dn,
            'CN=Bob "Sponge,Pants" (somestuff),OU=Test Users,OU=User,DC=intad,DC=dslab,DC=internal',
        )
        self.assertEqual(
            actual.get("distinguishedName"),
            'CN=Bob "Sponge,Pants" (somestuff),OU=Test Users,OU=User,DC=intad,DC=dslab,DC=internal',
        )
