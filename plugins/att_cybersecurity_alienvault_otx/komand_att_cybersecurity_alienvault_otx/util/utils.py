import IndicatorTypes
from insightconnect_plugin_runtime.exceptions import PluginException
from OTXv2 import InvalidAPIKey, NotFound, BadRequest

indicator_types = {
    "IPv4": IndicatorTypes.IPv4,
    "IPv6": IndicatorTypes.IPv6,
    "URL": IndicatorTypes.URL,
    "HOSTNAME": IndicatorTypes.HOSTNAME,
}


def get_indicator_type(indicator_type):
    if indicator_type in indicator_types:
        return indicator_types.get(indicator_type)
    raise PluginException(
        cause=f"Indicator type {indicator_type} is not a supported indicator type.",
        assistance="Please provide a valid indicator type.",
    )


def raise_exception(error):
    error_type = type(error)
    if error_type == InvalidAPIKey:
        raise PluginException(preset=PluginException.Preset.API_KEY)
    if error_type == NotFound:
        raise PluginException(preset=PluginException.Preset.NOT_FOUND)
    if error_type == BadRequest:
        raise PluginException(
            cause="The server is unable to process the request.",
            assistance="Verify that your input is correct and try again. If the issue persists, please contact "
            "support.",
            data=error,
        )
    raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
