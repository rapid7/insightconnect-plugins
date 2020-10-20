import json
from komand.exceptions import PluginException


class RequestParams(object):
    """
    This class transforms a dictionary of parameters into a list of tuples,
    and allows for their easy manipulation. Accommodates multiple query parameters needed for sorting/filtering requests.
    """

    def __init__(self, params: [tuple]):
        self.params = params

    @classmethod
    def from_dict(cls, params: dict):
        params_list = list()
        for key, item in params.items():
            params_list.append((key, item))
        return cls(params=params_list)

    @classmethod
    def from_tuples(cls, params: [tuple]):
        return cls(params=params)

    # Allows users to get values from this object in the same way you would get values from a dictionary
    def __getitem__(self, item):
        for a in self.params:
            if item in a[0]:
                return a[1]

    # Allows users to set values from this object in the same way you would set values from a dictionary
    def __setitem__(self, key, value):
        for idx, item in enumerate(self.params):
            if key in item:
                self.params[idx] = (key, value)
            else:
                self.params.append((key, value))


@staticmethod
def resource_request_status_code_check(response):
    """
    Checks for non 2xx status codes and if json_response is true converts response to JSON
    :param response: A requests response
    """
    _ERRORS = {
        400: "Bad Request",
        401: "Unauthorized",
        404: "Not Found",
        500: "Internal Server Error",
        503: "Service Unavailable",
        000: "Unknown Status Code"
    }

    _ASSISTANCE = {
        400: "Bad Request",
        401: "Ensure that the user name and password are correct.",
        404: "Ensure that the requested resource exists.",
        500: "If this issue persists contact support for assistance.",
        503: "If this issue persists contact support for assistance.",
        000: "If this issue persists contact support for assistance."
    }
    _CHECK_CONSOLE = 'Verify your connection is pointing to your local console and not `exposure-analytics.insight.rapid7.com`'
    if response.status_code not in [200, 201]:  # 200 is documented, 201 is undocumented
        status_code_message = _ERRORS.get(response.status_code, _ERRORS[000])
        assistance = _ASSISTANCE.get(response.status_code, _ASSISTANCE[000])
        try:
            response_json = response.json()
            error = response_json.get('message', {})
        except (KeyError, json.decoder.JSONDecodeError):
            raise PluginException(cause=f'Malformed JSON received along with a status code of {status_code_message}',
                                  assistance=f'{_CHECK_CONSOLE} {assistance}',
                                  data=response.text)
        raise PluginException(cause=f'InsightVM returned an error message. {status_code_message}',
                              assistance=assistance,
                              data=error)