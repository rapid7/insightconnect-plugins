import aiohttp
import json
from insightconnect_plugin_runtime.exceptions import PluginException

class AsyncRequests:

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_async_session(self):
        """
        Create and return a new aiohttp ClientSession
        :return: aiohttp ClientSession
        """

        headers =  {
            "Authorization": f"Token token={self.api_key}"
        }
        return aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=True), headers=headers)

    async def async_request(self, session, url: str, method: str = "get", params: dict = None, body: dict = None) -> dict:
        """
        Sends an asynchronous request to PagerDuty
        :param session: asynchronous session
        :param url: url endpoint
        :param method: http method for API request
        :param params: URL parameters
        :param body: request body
        :return: JSON response body
        """

        extras = {"json": body, "params": params}
        response = await session.request(url=url, method=method, **extras)
        self.status_code_handling(response.text(), response.status)
        return response.json()

    @ staticmethod
    def status_code_handling(response_text, status_code):
        _ERRORS = {
            400: 'Caller provided invalid arguments. Please review the response for error details. '
                 'Retrying with the same arguments will not work.',
            401: 'Supplied credentials were incorrect. Ensure API key is correct.',
            403: 'You do not have authorization to view the resources.',
            404: 'The requested resource was not found.',
            429: 'Too many requests have been made, the rate limit has been reached.',
            000: 'Unexpected response from PagerDuty. Please contact support for assistance.'
        }
        if status_code != 200:
            assistance = _ERRORS.get(status_code, _ERRORS[000])
            try:
                response_json = json.loads(response_text)
            except (KeyError, json.decoder.JSONDecodeError):
                raise PluginException(cause=f'Malformed JSON received along with a status code of {status_code}',
                                      assistance=f'{assistance}',
                                      data=response_text)
            raise PluginException(cause=f'PagerDuty returned a response code of {status_code}',
                                  assistance=assistance,
                                  data=response_json)