import json
import logging
from pathlib import Path
from typing import Any, Callable, Dict, Union

from insightconnect_plugin_runtime.trigger import Trigger
from komand_rss.connection.connection import Connection, Input
from timeout_decorator import timeout_decorator

STUB_CONNECTION = {
    Input.URL: "https://example.com",
}


class Util:
    @staticmethod
    def default_connector(trigger: Trigger) -> Trigger:
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect(STUB_CONNECTION)
        trigger.connection = default_connection
        trigger.logger = logging.getLogger("trigger logger")
        trigger.run = Util.timeout_pass(trigger.run)
        return trigger

    @staticmethod
    def timeout_pass(function_: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            try:
                return function_(*args, **kwargs)
            except timeout_decorator.TimeoutError:
                return None

        return wrapper

    @staticmethod
    def load_file(filename: str, is_feed: bool = True) -> Union[bytes, Dict[str, Any]]:
        filename_ = f"responses/{filename}.xml.resp"
        if not is_feed:
            filename_ = f"expected/{filename}.json.resp"
        with open(Path(__file__).resolve().parent / filename_, f"r{'b' if is_feed else ''}") as file_:
            content = file_.read()
        return content if is_feed else json.loads(content)
