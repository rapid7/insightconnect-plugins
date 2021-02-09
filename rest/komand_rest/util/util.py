import requests
from komand.exceptions import ConnectionTestException


class Common:
    '''Merge 2 dictionaries'''

    @staticmethod
    def merge_dicts(x, y):
        """Given two dicts, merge them into a new dict as a shallow copy."""
        z = x.copy()
        z.update(y)
        return z

    '''Copy the case insensitive headers dict to a normal one'''

    @staticmethod
    def copy_dict(x):
        d = {}
        for key in x:
            d[key] = x[key]
        return d

    @staticmethod
    def call_api(url, path, headers, ssl_verify, auth=None):
        try:
            response = requests.request(
                "GET",
                f"{url}{path}",
                headers=headers,
                verify=ssl_verify,
                auth=auth
            )

            if response.status_code == 401:
                raise ConnectionTestException(
                    preset=ConnectionTestException.Preset.USERNAME_PASSWORD,
                    data=response.text
                )
            if response.status_code == 403:
                raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY, data=response.text)
            if response.status_code == 404:
                raise ConnectionTestException(preset=ConnectionTestException.Preset.NOT_FOUND, data=response.text)
            if 400 <= response.status_code < 500:
                raise ConnectionTestException(
                    preset=ConnectionTestException.Preset.UNKNOWN,
                    data=response.json().get("message", response.text)
                )
            if response.status_code >= 500:
                raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVER_ERROR, data=response.text)

            if 200 <= response.status_code < 300:
                return response

            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNKNOWN, data=response.text)
        except requests.exceptions.HTTPError as e:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNKNOWN, data=e)
