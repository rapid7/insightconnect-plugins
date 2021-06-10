import logging
import re


class Formatter(logging.Formatter):
    """This Formatter removes sensitive info, such as API keys, from URLs in logs."""

    @staticmethod
    def _filter(string):
        """
        Substitute with the replacement the first instance in string of a substring that matches pattern.
        The pattern regex matches the api_key URL query parameter. It captures whether or not another parameter
        follows the api_key value in the group named end with an &. The replacement regex retains the end group.
        """
        pattern = r'api_key=([a-zA-Z0-9]+)(?P<end>\&|$)'
        replacement = r'api_key=********\g<end>'
        return re.sub(pattern, replacement, string)

    def format(self, record):
        original = logging.Formatter.format(self, record)
        return self._filter(original)
