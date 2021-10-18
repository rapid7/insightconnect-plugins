# import sys
# import os
#
# sys.path.append(os.path.abspath("../"))
#
# from unittest import TestCase
# from icon_palo_alto_cortex_xdr.connection.connection import Connection
# from icon_palo_alto_cortex_xdr.actions.block_file import BlockFile
# import json
# import logging
#
#
# class TestBlockFile(TestCase):
#     def test_integration_block_file(self):
#         log = logging.getLogger("Test")
#         test_conn = Connection()
#         test_action = BlockFile()
#
#         test_conn.logger = log
#         test_action.logger = log
#
#         try:
#             with open("../tests/block_file.json") as file:
#                 test_json = json.loads(file.read()).get("body")
#                 connection_params = test_json.get("connection")
#                 action_params = test_json.get("input")
#         except Exception as e:
#             message = """
#             Could not find or read sample tests from /tests directory
#
#             An exception here likely means you didn't fill out your samples correctly in the /tests directory
#             Please use 'icon-plugin generate samples', and fill out the resulting test files in the /tests directory
#             """
#             self.fail(message)
#
#         test_conn.connect(connection_params)
#         test_action.connection = test_conn
#         results = test_action.run(action_params)
#
#         self.assertTrue(results.get("success"))
