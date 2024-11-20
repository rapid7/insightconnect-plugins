import json
import logging
import os.path
import sys

sys.path.append(os.path.abspath("../"))
from komand_redis.connection import Connection

class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {"host": "127.0.0.1", "port": 8080, "db": 0}
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def load_json(filename):
        with open((os.path.join(os.path.dirname(os.path.realpath(__file__)), filename))) as file:
            return json.loads(file.read())

    @staticmethod
    def mock_redis():
        class MockResponse:
            def __init__(self):
                pass

            @staticmethod
            def delete(key_name: str):
                return 10

            @staticmethod
            def hmget(key_name: str, fields: list):
                return [b'20', b'Test User']

            @staticmethod
            def hgetall(key_name: str):
                return {b"age": b"20", b"email": b"Test@example.com", b"name": b"Test User"}

            @staticmethod
            def hmset(key_name: str, key_name2: dict):
                # Differentiate between hmset and hash_set action
                if key_name == "user:4567":
                    return True
                elif key_name == "user:1234":
                    return "OK"

            @staticmethod
            def hincrby(key_name: str, key_name2: str, key_name3: str):
                return 0

            @staticmethod
            def keys(key_name: str):
                return {b"count": 2, b"keys": [b"count", b"keys"]}

            @staticmethod
            def lrange(key_name: str, key_name2: int, key_name3: int):
                return []

            @staticmethod
            def setex(key_name: str, key_name2: str, key_name3: str):
                return "OK"

            @staticmethod
            def rpush(key_name: str, *values: any):
                return "OK"

            @staticmethod
            def get(params: str):
                if params == "test":
                    return True
                if params == "key":
                    return ""

        return MockResponse()
