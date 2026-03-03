from .shared_resources import RequestParams
from .shared_resources import resource_request_status_code_check
import json
import requests
import urllib3
from insightconnect_plugin_runtime.exceptions import PluginException
from typing import NamedTuple, Collection
from requests import Session
from logging import Logger

# Suppress insecure request messages
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class RequestResult(NamedTuple):
    """
    Class for data returned in paged InsightVM API requests
    This is the Python 3.6 style for using named tuples with typing
    """

    page_num: int
    total_pages: int
    resources: dict


class TestResult(NamedTuple):
    """
    Class for data returned in test method
    This is the Python 3.6 style for using named tuples with typing
    """

    status: int
    message: str


class ResourceRequests(object):
    """
    Class for helper methods for making requests against the APIv3. A new instance should
    be instantiated within the action/trigger being developed. New methods should be
    created as instance methods to allow reference of the logger and session passed to
    the __init__ function during instantiation.
    """

    # Static headers for all requests
    _HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}
    _ENSURE_CONNECTIVITY = (
        "Ensure proper network connectivity between the InsightConnect orchestrator and the InsightVM console"
    )

    # Currently only handling the most common requests exceptions more can be added as needed
    _REQUEST_EXCEPTIONS = {
        requests.HTTPError: "If this issue persists contact support for assistance.",
        requests.ConnectionError: "Unable to connect to IVM console."
        "If this issue persists contact support for assistance.",
        requests.Timeout: _ENSURE_CONNECTIVITY,
        requests.ConnectTimeout: _ENSURE_CONNECTIVITY,
        requests.ReadTimeout: _ENSURE_CONNECTIVITY,
        requests.TooManyRedirects: _ENSURE_CONNECTIVITY,
    }

    # For request exceptions not in REQUEST_EXCEPTIONS
    _UNHANDLED_EXCEPTION = "Contact support for assistance"

    def __init__(self, session: Session, logger: Logger, ssl_verify: bool) -> None:
        """
        Creates a new instance of ResourceHelper
        :param session: Session object available to Komand actions/triggers, usually self.connection.session
        :param logger: Logger object available to Komand actions/triggers, usually self.logger
        :return: ResourceHelper object
        """
        self.logger = logger
        self.session = session
        self.session.headers.update(self._HEADERS)
        self.ssl_verify = ssl_verify

    def resource_request(
        self,
        endpoint: str,
        method: str = "get",
        params: Collection = None,
        payload: dict = None,
        json_response: bool = True,
    ) -> dict:
        """
        Sends a request to APIv3 with the provided endpoint and optional method/payload
        :param endpoint: Endpoint for the APIv3 call defined in endpoints.py
        :param method: HTTP method for the API request
        :param params: URL parameters to append to the request
        :param payload: JSON body for the API request if required
        :param json_response: Boolean to return raw response
        :return: Dict containing the JSON response body
        """

        request_method = getattr(self.session, method.lower())
        if not payload:
            payload = {}
        if not params:
            params = {}
        if isinstance(params, list):
            parameters = RequestParams.from_tuples(params)
        else:
            parameters = RequestParams.from_dict(params)
        if "rawbody" in payload.keys():
            payload = payload["rawbody"]

        extras = {"json": payload, "params": parameters.params}
        try:
            response = request_method(url=endpoint, verify=self.ssl_verify, **extras)
        except requests.RequestException as error:
            assistance = self._REQUEST_EXCEPTIONS.get(type(error), self._UNHANDLED_EXCEPTION)
            raise PluginException(cause=error, assistance=assistance)

        resource_request_status_code_check(response.text, response.status_code)

        if json_response:
            try:
                resource = response.json()
            except json.decoder.JSONDecodeError as error:
                raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=f"Error returned: {error}")
        else:
            resource = {"raw": response.text}

        # Close session
        self.session.close()
        return resource

    def paged_resource_request(
        self,
        endpoint: str,
        method: str = "get",
        params: Collection = None,
        payload: dict = None,
        number_of_results: int = 0,
    ) -> list:
        """
        Fetches all resources from a paged APIv3 endpoint
        :param endpoint: Endpoint for the APIv3 call defined in endpoints.py
        :param method: HTTP method for the API request
        :param params: URL parameters to append to the request
        :param payload: JSON body for the API request if required
        :param number_of_results: The total number of results to retrieve. 0 is unlimited
        :return: List object of API resources
        """
        resources = []
        current_page = 0
        results_retrieved = 0
        last_page = False

        # Handle various scenarios where params may be passed
        if not payload:
            payload = {}
        if not params:
            params = {"size": 500, "page": current_page}
        if isinstance(params, list):
            parameters = RequestParams.from_tuples(params)
        else:
            parameters = RequestParams.from_dict(params)

        while True:
            self.logger.info(f"Fetching results from page {current_page}")
            parameters["page"] = current_page
            if number_of_results != 0:
                if results_retrieved + parameters["size"] > number_of_results:
                    parameters["size"] = number_of_results - results_retrieved
                    last_page = True
            response = self.get_resource_page(endpoint=endpoint, method=method, params=parameters, payload=payload)
            resources += response.resources  # Grab resources and append to total
            self.logger.info(
                f"Got {len(response.resources)} resources "
                f"from page {(response.page_num+1)} / {response.total_pages}"
            )

            if (response.total_pages == 0) or ((response.total_pages - 1) == response.page_num):
                self.logger.info("All pages consumed, returning results...")
                break  # exit the loop
            if last_page:
                self.logger.info(f"{number_of_results} results consumed, returning results")
                break
            self.logger.info("More pages exist, fetching...")
            current_page += 1

        return resources

    def get_resource_page(self, endpoint: str, method: str, params: RequestParams, payload: dict) -> RequestResult:
        """
        Retrieves resources from a security console
        :param endpoint: Endpoint to reach
        :param method: HTTP method for the API request
        :param params: URL parameters to append to the request
        :param payload: JSON body for the API request if required
        :return: Namedtuple object containing current page number, total pages, and results
        """
        # Get size and page from list of dict param type

        self.logger.info(f'Fetching up to {params["size"]} resources from endpoint page {params["page"]} ...')
        request_method = getattr(self.session, method.lower())

        extras = {"json": payload, "params": params.params}
        try:
            response = request_method(url=endpoint, verify=self.ssl_verify, **extras)
        except requests.RequestException as error:
            assistance = self._REQUEST_EXCEPTIONS.get(type(error), self._UNHANDLED_EXCEPTION)
            raise PluginException(cause=error, assistance=assistance)

        resource_request_status_code_check(response.text, response.status_code)
        try:
            response_json = response.json()
        except json.decoder.JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=f"Error returned: {error}")

        result = RequestResult(
            page_num=response_json["page"]["number"],
            total_pages=response_json["page"]["totalPages"],
            resources=response_json["resources"],
        )

        # Close session
        self.session.close()
        return result
