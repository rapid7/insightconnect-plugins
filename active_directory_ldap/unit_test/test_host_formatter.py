from unittest import TestCase
from komand_active_directory_ldap.connection import Connection
import logging


class TestHostFormatter(TestCase):

    def test_host_formatter(self):
        host_types = ['10.10.10.10', '11.11.11.11:345', 'ldaps://12.12.12.12', 'ldaps://14.14.14.14:345',
                      'mydomain.com', 'mydomain.com:345', 'ldaps://mydomain.com', 'ldaps://mydomain.com:345',
                      'mydomain.com/stuff', 'mydomain.com/stuff:345', 'ldaps://mydomain.com/stuff', 'ldaps://mydomain.com/stuff:345']
        output = list()
        connection = Connection()
        for item in host_types:
            output.append(connection.host_formatter(item))
        self.assertEqual(output, ['10.10.10.10', '11.11.11.11', '12.12.12.12', '14.14.14.14',
                                  'mydomain.com', 'mydomain.com', 'mydomain.com', 'mydomain.com',
                                  'mydomain.com', 'mydomain.com', 'mydomain.com', 'mydomain.com'])
