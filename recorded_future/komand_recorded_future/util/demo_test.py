import requests
from komand.exceptions import ConnectionTestException


def demo_test(token):
    demo_url = "https://api.recordedfuture.com/v2/hash/demoevents?limit=1"
    if not token:
        raise ConnectionTestException(
            cause="Missing API Key.",
            assistance="Please provide API key."
        )
    try:
        test_headers = {"X-RFToken": token}
        response = requests.get(demo_url, headers=test_headers)
        if 200 <= response.status_code < 300:
            return {"status": "Success"}
        elif response.status_code == 401:
            raise ConnectionTestException(
                preset=ConnectionTestException.Preset.API_KEY
            )
        elif response.status_code == 403:
            raise ConnectionTestException(
                preset=ConnectionTestException.Preset.UNAUTHORIZED
            )
        elif response.status_code == 404:
            raise ConnectionTestException(
                preset=ConnectionTestException.Preset.NOT_FOUND
            )
        elif response.status_code >= 400:
            raise ConnectionTestException(
                preset=ConnectionTestException.Preset.UNKNOWN,
                data=response.text
            )
    except requests.exceptions.ConnectionError as e:
        raise ConnectionTestException(
            cause="A network problem occurred.",
            assistance="Please try again and if the issue persists please contact support.",
            data=e
        )
    except requests.exceptions.Timeout as e:
        raise ConnectionTestException(
            cause="Timeout occurred.",
            assistance="Please try again and if the issue persists please contact support.",
            data=e
        )
    except requests.exceptions.TooManyRedirects as e:
        raise ConnectionTestException(
            cause="Too many redirects.",
            assistance="Please try again and if the issue persists please contact support.",
            data=e
        )
