from insightconnect_plugin_runtime.exceptions import PluginException
import requests


class ResourceHelper(object):
    """
    Class for helper methods for making requests against the InsightAppSec API. A new instance should
    be instantiated within the action/trigger being developed. New methods should be
    created as instance methods to allow reference of the logger and session passed to
    the __init__ function during instantiation.
    """

    _ERRORS = {
        400: "Bad Request",
        401: "Unauthorized",
        404: "Not Found",
        500: "Internal Server Error",
        503: "Service Unavailable",
        000: "Unknown Status Code",
    }

    def __init__(self, session, logger):
        """
        Creates a new instance of ResourceHelper
        :param session: Session object available to Komand actions/triggers, usually self.connection.session
        :param logger: Logger object available to Komand actions/triggers, usually self.logger
        :return: ResourceHelper object
        """
        self.logger = logger
        self.session = session

    def resource_request(self, endpoint: str, method: str = "get", params: dict = None, payload: dict = None) -> dict:
        """
        Sends a request to API with the provided endpoint and optional method/payload
        :param endpoint: Endpoint for the API call defined in endpoints.py
        :param method: HTTP method for the API request
        :param params: URL parameters to append to the request
        :param payload: JSON body for the API request if required
        :return: Dict containing the JSON response body
        """
        try:
            request_method = getattr(self.session, method.lower())

            if not params:
                params = {}
            if not payload:
                response = request_method(url=endpoint, params=params, verify=False)
            else:
                response = request_method(url=endpoint, params=params, json=payload, verify=False)
        except requests.RequestException as e:
            self.logger.error(e)
            raise

        if response.status_code in range(200, 299):
            resource = response.text
            return {"resource": resource, "status": response.status_code}
        else:
            try:
                error = response.json()["message"]
            except KeyError:
                self.logger.error(f"Code: {response.status_code}, message: {error}")
                error = "Unknown error occurred. Please contact support or try again later."

            status_code_message = self._ERRORS.get(response.status_code, self._ERRORS[000])
            self.logger.error(f"{status_code_message} ({response.status_code}): {error}")
            raise PluginException(f"InsightIDR returned a status code of {response.status_code}: {status_code_message}")
