import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_cylance_protect.connection.connection import Connection
from icon_cylance_protect.actions.delete_asset import DeleteAsset
import json
import logging
from icon_cylance_protect.util.find_helpers import find_in_whitelist, find_agent_by_ip


class TestDeleteAsset(TestCase):
    def test_integration_delete_asset(self):
        """
        TODO: Implement assertions at the end of this test case

        This is an integration test that will connect to the services your plugin uses. It should be used
        as the basis for tests below that can run independent of a "live" connection.

        This test assumes a normal plugin structure with a /tests directory. In that /tests directory should
        be json samples that contain all the data needed to run this test. To generate samples run:

        icon-plugin generate samples

        """

        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = DeleteAsset()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("../tests/delete_asset.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except Exception as e:
            message = """
            Could not find or read sample tests from /tests directory
            
            An exception here likely means you didn't fill out your samples correctly in the /tests directory 
            Please use 'icon-plugin generate samples', and fill out the resulting test files in the /tests directory
            """
            self.fail(message)


        test_conn.connect(connection_params)
        test_action.connection = test_conn

        # results = test_action.run(action_params)
        # self.assertEquals({"deleted": ["10.0.2.15"], "not_deleted": [], "success": true}, results)

    def test_find_in_whitelist(self):
        dic = {'id': 'cf9c26cc-6d3d-454a-b242-7e9f565c6cf7', 'name': 'VAGRANT-PC', 'host_name': 'vagrant-pc',
               'os_version': 'Microsoft Windows 7 Professional, Service Pack 1', 'state': 'Online',
               'agent_version': '2.0.1540', 'products': [{'name': 'protect', 'version': '2.0.1540'}],
               'policy': {'id': 'c6f694e8-5ddd-4988-8a6b-3a1d3d2da631', 'name': 'Default'},
               'last_logged_in_user': 'vagrant-pc\\vagrant', 'update_available': False,
               'background_detection': False, 'is_safe': True, 'date_first_registered': '2020-09-14T15:39:14',
               'date_last_modified': '2020-09-14T15:45:53', 'ip_addresses': ['10.0.2.15'],
               'mac_addresses': ['08-00-27-33-9F-CE']}

        self.assertEqual(find_in_whitelist(dic, ["1.1.1.1", "2.2.2.2"]), [])
        self.assertEqual(find_in_whitelist(dic, []), [])
        self.assertNotEqual(find_in_whitelist(dic, ["1.1.1.1", "2.2.2.2"]), ["1.1.1.1"])
        self.assertEqual(find_in_whitelist(dic, ['10.0.2.15']), ['10.0.2.15'])
        self.assertEqual(find_in_whitelist(dic, ['08-00-27-33-9F-CE']), ['08-00-27-33-9F-CE'])
        self.assertEqual(find_in_whitelist(dic, ['vagrant-pc']), ['vagrant-pc'])

    def test_find_agent_by_ip(self):
        ip = "10.0.2.15"
        ip_device_id = "07538729-cb7a-482b-9c91-4623123afb2a"
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = DeleteAsset()
        test_conn.logger = log
        test_action.logger = log

        try:
            with open("../tests/delete_asset.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
        except Exception as e:
            message = "Could not connection from /tests directory"
            self.fail(message)

        test_conn.connect(connection_params)
        test_action.connection = test_conn

        self.assertEqual(find_agent_by_ip(test_action.connection, "1.1.1.1"), [])
        # self.assertEqual(find_in_whitelist(dic, []), [])
        # self.assertNotEqual(find_in_whitelist(dic, ["1.1.1.1", "2.2.2.2"]), ["1.1.1.1"])
        # self.assertEqual(find_in_whitelist(dic, ['10.0.2.15']), ['10.0.2.15'])
        # self.assertEqual(find_in_whitelist(dic, ['08-00-27-33-9F-CE']), ['08-00-27-33-9F-CE'])
        # self.assertEqual(find_in_whitelist(dic, ['vagrant-pc']), ['vagrant-pc'])


