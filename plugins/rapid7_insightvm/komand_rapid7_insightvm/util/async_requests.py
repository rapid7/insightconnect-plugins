import aiohttp
from typing import Collection
from .shared_resources import RequestParams, resource_request_status_code_check
from insightconnect_plugin_runtime.exceptions import PluginException


class AsyncRequests:
    """
    Class for helper methods for making async requests against the APIv3. A new instance should
    be instantiated within the action/trigger being developed. New methods should be
    created as instance methods to allow reference of the logger and session passed to
    the __init__ function during instantiation.
    """

    def __init__(self, username: str, password: str):
        self.auth = aiohttp.BasicAuth(login=username, password=password)

    def get_async_session(self) -> aiohttp.ClientSession:
        """
        Create and return a new aiohttp ClientSession
        :return: aiohttp ClientSession
        """
        # Per aiohttp verify_ssl is deprecated, and use ssl=False should be used instead
        # However during testing I confirmed that this behaves differently, and some times
        # causes request to fail. For now reverting to verify_ssl
        return aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False), auth=self.auth)

    @staticmethod
    async def async_request(
        session,
        endpoint: str,
        method: str = "get",
        params: Collection = None,
        payload: dict = None,
        json_response: bool = True,
    ):
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
        text = await response.text()
        status = response.status

        resource_request_status_code_check(text, status)

        if json_response:
            try:
                resp_json = await response.json()
            except aiohttp.ContentTypeError:
                raise PluginException(
                    cause="InsightVM returned malformed JSON.",
                    assistance="If this issue persists contact support for assistance.\n",
                    data=response.text(),
                )
            return resp_json
        return text
