import logging
import os
import json

from komand_google_search.connection.connection import Connection
from komand_google_search.connection.schema import Input


class Util:
    @staticmethod
    def read_file_to_dict(filename):
        with open(filename, "rt", encoding="utf8"):
            return json.loads(
                Util.read_file_to_string(os.path.join(os.path.dirname(os.path.realpath(__file__)), filename))
            )

    @staticmethod
    def read_file_to_string(filename):
        with open(filename, "rt", encoding="utf8") as my_file:
            return my_file.read()
