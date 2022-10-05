import json
import logging
import os
import sys

sys.path.append(os.path.abspath("../"))
from insightconnect_plugin_runtime import Action
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_dynamodb.connection import Connection
from komand_dynamodb.util.api import AWSCommunicationAPI
from unittest.mock import create_autospec


class Util:
    @staticmethod
    def load_json(filename):
        with open((os.path.join(os.path.dirname(os.path.realpath(__file__)), filename))) as file:
            return json.loads(file.read())

    @staticmethod
    def _scan_side_effect(*args, **kwargs):
        return Util.load_json("payloads/action_scan.json.exp")

    @staticmethod
    def _get_item_side_effect(*args, **kwargs):
        return Util.load_json("payloads/action_get_item.json.exp")

    @staticmethod
    def _insert_side_effect(*args, **kwargs):
        if kwargs["params"]["item"].get("wrong_key", ""):
            raise PluginException(
                cause="Error occurred when invoking the aws-cli.",
                assistance="Check client connection keys and input arguments and try again.",
                data=Util.load_json("payloads/action_bad_insert_resource_not_found.resp"),
            )

    @staticmethod
    def _update_side_effect(*args, **kwargs):
        if kwargs["params"]["key"].get("wrong_key", ""):
            raise PluginException(
                cause="Error occurred when invoking the aws-cli.",
                assistance="Check client connection keys and input arguments and try again.",
                data=Util.load_json("payloads/action_bad_update_validation_exception.exp"),
            )

    @staticmethod
    def _prepare_client():
        client = create_autospec(AWSCommunicationAPI)
        client.configure_mock(**{"insert_data.side_effect": Util._insert_side_effect})
        client.configure_mock(**{"scan_table.side_effect": Util._scan_side_effect})
        client.configure_mock(**{"update_data.side_effect": Util._update_side_effect})
        client.configure_mock(**{"get_item.side_effect": Util._get_item_side_effect})
        return client

    @staticmethod
    def default_connection(action: Action) -> Action:
        default_connection = Connection()
        default_connection.client = Util._prepare_client()
        default_connection.logger = logging.getLogger("connection logger")
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action
