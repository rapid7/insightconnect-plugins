
from komand.exceptions import PluginException
from requests.models import Response


def tryJSON(response: Response) -> dict:
    """
    Try to convert response data to JSON
    """

    try:
        response_data = response.json()
    except json.decoder.JSONDecodeError:
        raise PluginException(cause="Received an unexpected response from Deep Security",
                              assistance="(non-JSON or no response was received).",
                              data=response.text)
    return response_data


def checkResponse(response: Response) -> None:
    """
    Check the response code and extract the error message
    """
    if response.status_code not in range(200, 299):
        response_data = tryJSON(response)
        if "message" in response_data:
            message = f"{response.status_code}, {response_data['message']}"
        else:
            message = f"{response.status_code}, {response.text}"

        raise PluginException(cause="Received HTTP %d status code. The request was not successful." % response.status_code,
                              assistance="Please check the server address and the rules to be assigned.",
                              data=message)
