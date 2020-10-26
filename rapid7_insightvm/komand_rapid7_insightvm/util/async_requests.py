import aiohttp
from typing import Collection
from komand.exceptions import PluginException
from .shared_resources import *


class AsyncRequests:

    def __init__(self, username: str, password: str):
        self.auth = aiohttp.BasicAuth(login=username, password=password)

    def get_async_session(self) -> aiohttp.ClientSession:
        """
        Create and return a new aiohttp ClientSession
        :return: aiohttp ClientSession
        """
        return aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False), auth=self.auth)

    @staticmethod
    async def async_request(session, endpoint: str, method: str = 'get', params: Collection = None, payload: dict = None,
                            json_response: bool = True):
        """
        Sends an asynchronous request to APIv3 with the provided endpoint and optional method/body
        :param session: The asynchronous session
        :param endpoint: Endpoint for the APIv3 call defined in endpoints.py
        :param method: HTTP method for the API request
        :param params: URL parameters to append to the request
        :param payload: JSON body for the API request if required
        :param json_response: Boolean to return raw response
        :return: Dict containing the JSON response body
        """
        if not params:
            params = {}
        if isinstance(params, list):
            parameters = RequestParams.from_tuples(params)
        else:
            parameters = RequestParams.from_dict(params)

        extras = {"json": payload, "params": parameters.params}
        response = await session.request(url=endpoint, method=method, **extras)

        resource_request_status_code_check(response.text(), response.status)

        if json_response:
            try:
                resp_json = await response.json()
            except aiohttp.ContentTypeError:
                raise PluginException(cause='InsightVM returned malformed JSON.',
                                      assistance='If this issue persists contact support for assistance.\n',
                                      data=response.text())
            return resp_json
        return response.text()
