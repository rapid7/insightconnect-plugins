import json
import logging
import os
import sys
from typing import Any, Dict, List

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.action import Action
from komand_dig.connection.connection import Connection
from komand_dig.util.constants import DEFAULT_ENCODING

KEYS_TO_REMOVE = ["fulloutput", "nameserver"]


class Util:
    @staticmethod
    def default_connector(action: Action, params: Dict[str, Any] = None) -> Action:
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_dict(filename: str, encoding_enabled: bool = False) -> Dict[str, Any]:
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), filename), "r", encoding=DEFAULT_ENCODING
        ) as file_reader:
            data = json.load(file_reader)
            if encoding_enabled:
                encoded_data = {}
                for key, value in data.items():
                    encoded_data[key] = value.encode("utf-8")
                return encoded_data
            else:
                return data

    @staticmethod
    def remove_unnecessary_keys(
        input_dict: Dict[str, Any], remove_answers: bool = False, key_names: List[str] = KEYS_TO_REMOVE
    ) -> None:
        keys_to_remove = key_names.copy()
        if remove_answers:
            keys_to_remove += ["all_answers", "last_answer"]
        for key in keys_to_remove:
            input_dict.pop(key, None)

    @staticmethod
    def mock_dig(*args, **kwargs) -> Dict[str, Any]:
        command = args[0]
        if command == "/usr/bin/dig @8.8.8.8 rapid7.com MX":
            filename = "forward.json.resp"
            return Util.read_file_to_dict(f"responses/{filename}", encoding_enabled=True)
        elif command == "/usr/bin/dig rapid7.com MX":
            filename = "forward_no_resolver.json.resp"
            return Util.read_file_to_dict(f"responses/{filename}", encoding_enabled=True)
        elif command == "/usr/bin/dig @8 rapid7.com MX":
            filename = "forward_raise_error.json.resp"
            return Util.read_file_to_dict(f"responses/{filename}", encoding_enabled=True)
        elif command == "/usr/bin/dig @8.8.8.8 -x 13.33.252.129":
            filename = "reverse.json.resp"
            return Util.read_file_to_dict(f"responses/{filename}", encoding_enabled=True)
        elif command == "/usr/bin/dig -x 13.33.252.129":
            filename = "reverse_no_resolver.json.resp"
            return Util.read_file_to_dict(f"responses/{filename}", encoding_enabled=True)
        elif command == "/usr/bin/dig @8 -x 13.33.252.129":
            filename = "reverse_raise_error.json.resp"
            return Util.read_file_to_dict(f"responses/{filename}", encoding_enabled=True)
        raise Exception("Response Not Implemented!")
