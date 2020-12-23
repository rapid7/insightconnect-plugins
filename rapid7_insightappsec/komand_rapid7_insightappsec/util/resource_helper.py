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
        401: "Unauthenticated",
        403: "Unauthorized",
        404: "Not Found",
        409: "Action Conflict",
        415: "Unsupported Media Type",
        500: "Internal Server Error",
        503: "Service Unavailable",
        000: "Unknown Status Code"
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

    def resource_request(self, endpoint: str, method: str = 'get', params: dict = None,
                         payload: dict = None) -> dict:
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
                response = request_method(url=endpoint, params=params,
                                          verify=True)
            else:
                response = request_method(url=endpoint, params=params,
                                          json=payload, verify=True)
        except requests.RequestException as e:
            self.logger.error(e)
            raise

        if response.status_code in range(200, 204, 299):
            resource = response.text
            return {'resource': resource, 'status': response.status_code, 'headers': response.headers}
        else:
            try:
                error = response.json()["message"]
            except KeyError:
                self.logger.error(f'Code: {response.status_code}, message: {response.text}')
                error = 'Unknown error occurred. Please contact support or try again later.'

            status_code_message = self._ERRORS.get(response.status_code, self._ERRORS[000])
            self.logger.error(f'{status_code_message} ({response.status_code}): {error}')
            raise Exception(f'Insight AppSec returned a status code of {response.status_code}: {status_code_message}')

    def paged_resource_request(self, endpoint: str, method: str = 'get', params: dict = None,
                               payload: dict = None, number_of_results: int = 0) -> dict:
        """
        Sends a paged request to API with the provided endpoint and optional method/payload
        :param endpoint: Endpoint for the API call defined in endpoints.py
        :param method: HTTP method for the API request
        :param params: URL parameters to append to the request
        :param payload: JSON body for the API request if required
        :param number_of_results: The total number of results to retrieve. 0 is unlimited
        :return: Dict containing the JSON response body
        """

        resources = []
        current_page = 0
        results_retrieved = 0
        last_page = False

        if not params.get('size'):
            params['size'] = 50

        if not params.get('index'):
            params['index'] = 50
