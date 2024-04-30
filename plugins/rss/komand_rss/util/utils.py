from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from requests import Response
from requests.exceptions import HTTPError


def handle_response_exception(response: Response) -> None:
    try:
        response.raise_for_status()
    except HTTPError as error:
        preset = ConnectionTestException.Preset.UNKNOWN
        if error.response.status_code == 400:
            preset = ConnectionTestException.Preset.BAD_REQUEST
        elif error.response.status_code == 404:
            preset = ConnectionTestException.Preset.NOT_FOUND
        elif error.response.status_code == 500:
            preset = ConnectionTestException.Preset.SERVER_ERROR
        elif error.response.status_code == 503:
            preset = ConnectionTestException.Preset.SERVICE_UNAVAILABLE
        raise ConnectionTestException(preset=preset, data=error)
