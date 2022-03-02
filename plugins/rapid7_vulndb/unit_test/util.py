import os
import json


class Util:
    @staticmethod
    def read_file_to_dict(filename):
        with open(filename, "rt") as my_file:
            return json.loads(
                Util.read_file_to_string(os.path.join(os.path.dirname(os.path.realpath(__file__)), filename))
            )

    @staticmethod
    def read_file_to_string(filename):
        with open(filename, "rt") as my_file:
            return my_file.read()
