import json
import os
from typing import Any, Dict


class Util:
    @staticmethod
    def read_file_to_dict(filename: str) -> Dict[str, Any]:
        return json.loads(Util.read_file_to_string(os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)))

    @staticmethod
    def read_file_to_string(filename: str) -> str:
        with open(filename, "rt") as my_file:
            return my_file.read()
