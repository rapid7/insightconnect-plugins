from insightconnect_plugin_runtime.exceptions import PluginException

from .constants import INTENT_CONTAIN, INTENT_INFO, INTENT_STATUS, INTENT_UNCONTAIN

VALID_INTENTS = {INTENT_CONTAIN, INTENT_UNCONTAIN, INTENT_STATUS, INTENT_INFO}


class InputValidator:
    """
    Validates inputs before any API call. Raises PluginException on failure.
    """

    @staticmethod
    def validate_execute_response_inputs(identifier: str, intent: str, timeout: int, interval: int) -> None:
        """
        Validate all inputs for the execute_response action.

        :param identifier: Endpoint identifier (hostname, IP, MAC, or agent ID)
        :param intent: Desired operation (contain, uncontain, status, info)
        :param timeout: Maximum seconds for monitoring phase
        :param interval: Seconds between polling checks
        :raises PluginException: If any input is invalid
        """
        if not identifier or not identifier.strip():
            raise PluginException(
                cause="Endpoint identifier is empty or whitespace-only.",
                assistance="Please provide a valid endpoint identifier such as a hostname, IP address, MAC address, or SentinelOne agent ID.",
            )

        if intent not in VALID_INTENTS:
            raise PluginException(
                cause=f"Invalid intent '{intent}'.",
                assistance=f"Intent must be one of: {', '.join(sorted(VALID_INTENTS))}.",
            )

        if not isinstance(timeout, int) or timeout <= 0:
            raise PluginException(
                cause=f"Invalid timeout value '{timeout}'.",
                assistance="Timeout must be a positive integer greater than zero.",
            )

        if not isinstance(interval, int) or interval <= 0:
            raise PluginException(
                cause=f"Invalid polling interval value '{interval}'.",
                assistance="Polling interval must be a positive integer greater than zero.",
            )
