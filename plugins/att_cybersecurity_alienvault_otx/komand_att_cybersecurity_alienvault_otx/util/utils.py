import IndicatorTypes
from insightconnect_plugin_runtime.exceptions import PluginException

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
