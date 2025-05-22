import re

from icon_html.util.constants import HTML_TAG_PARSER
from icon_html.util.strategies import HTMLConverterStrategy
from insightconnect_plugin_runtime.exceptions import PluginException


class HTMLConverter:
    """HTMLConverter context"""

    def __init__(self, strategy: HTMLConverterStrategy) -> None:
        self._strategy = strategy

    def convert(self, input_html_string: str) -> str:
        self._validate_input_html(input_html_string)
        try:
            return self._strategy.convert(input_html_string)
        except Exception as error:
            raise PluginException(
                cause="Error converting doc file. ",
                assistance="Check stack trace log.",
                data=error,
            )

    @staticmethod
    def _validate_input_html(input_html_string: str) -> None:
        if not re.findall(HTML_TAG_PARSER, input_html_string):
            raise PluginException(cause="Invalid input.", assistance="Input must be of type HTML.")
