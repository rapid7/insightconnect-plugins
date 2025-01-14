from typing import Any, Dict

from insightconnect_plugin_runtime.exceptions import PluginException

from twilio.base.exceptions import TwilioRestException

EXCEPTION_STATUS_CODE_MAP = {
    400: PluginException.Preset.BAD_REQUEST,
    401: PluginException.Preset.API_KEY,
    403: PluginException.Preset.UNAUTHORIZED,
    404: PluginException.Preset.NOT_FOUND,
    429: PluginException.Preset.RATE_LIMIT,
}


def handle_exception_status_code(exception: TwilioRestException, status_code_map: Dict[int, Any] = None) -> None:
    # As dict is mutable default needs to be set this way
    if status_code_map is None:
        status_code_map = EXCEPTION_STATUS_CODE_MAP

    # Match received status code with a preset. If status code doesn't exist in map, set UNKNOWN preset as default.
    preset_to_use = status_code_map.get(exception.status, PluginException.Preset.UNKNOWN)

    # If status code is higher than 500, replace preset with SERVER_ERROR
    if exception.status >= 500:
        preset_to_use = PluginException.Preset.SERVER_ERROR
    raise PluginException(preset=preset_to_use, data=exception)
