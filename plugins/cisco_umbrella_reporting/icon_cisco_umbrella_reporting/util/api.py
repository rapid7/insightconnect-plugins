import json
import requests

from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.clients.oauth import OAuth20ClientCredentialMixin

from logging import Logger
from typing import Optional, Dict, Any, List
from icon_cisco_umbrella_reporting.util.utils import convert_get_domain_output

from icon_cisco_umbrella_reporting.util.endpoints import Endpoints
from icon_cisco_umbrella_reporting.util.constants import (
    LIMIT_DEFAULT_VALUE,
    LIMIT_MAX_API_RETURN_VALUE,
    OFFSET_MAX_API_INPUT_VALUE,
)

DEFAULT_QUERY_PARAMETERS = {"to": "now", "limit": LIMIT_MAX_API_RETURN_VALUE}


class CiscoUmbrellaReportingAPI(OAuth20ClientCredentialMixin):
    def __init__(self, api_key: str, api_secret: str, logger: Logger):
        super().__init__(api_key, api_secret, Endpoints.OAUTH20_TOKEN_URL)
        self.base_url = "https://api.umbrella.com/reports/v2"
        self.logger = logger

    def destinations_most_recent_request(
        self, query_parameters: Optional[Dict[str, Any]] = None, limit: Optional[int] = LIMIT_DEFAULT_VALUE
    ) -> List[Dict[str, Any]]:
        """
        destinations_most_recent_request. Performs the action main data retriever method. Selects the necessary method according to the limit value.

        :param query_parameters:
        :type: Optional[Dict[str, Any]]

        :param limit:
        :type: Optional[int]

        :return: List of obtained records.
        :rtype: List[Dict[str, Any]]
        """

        parameters = {} if query_parameters is None else query_parameters
        if limit:
            return self.get_activity_dns({**parameters, "limit": limit})
        return self.get_all_activity_records(query_parameters)

    def get_all_activity_records(self, query_parameters: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """
        get_all_activity_records. Retrieves all the records with a pagination offset query parameter. Reaches to the maximum offset value.

        :param query_parameters: Query parameters passed to the requests.
        :type: Dict[str, Any]

        :return: List of records retrieved.
        :rtype: List[Dict[str, Any]]
        """

        output_records = []
        for offset in range(0, OFFSET_MAX_API_INPUT_VALUE + LIMIT_MAX_API_RETURN_VALUE, LIMIT_MAX_API_RETURN_VALUE):
            output_records += self.get_activity_dns({**query_parameters, "offset": offset})
        return output_records

    def get_activity_dns(self, query_parameters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        get_activity_dns. Retrieves records activity/dns with query parameters specified or defaults.

        :param query_parameters: Optional query parametrs to be added to the request. If None default parameters will be passed.
        :type:  Optional[Dict[str, Any]]

        :return:
        :rtype: List[Dict[str, Any]]
        """

        response = self._call_api(
            "GET",
            "/activity/dns",
            params={**DEFAULT_QUERY_PARAMETERS, **query_parameters},
        ).get("data", [])
        return convert_get_domain_output(response)

    def _call_api(
        self,
        method: str,
        path: str,
        json_data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        try:
            response = self.oauth.request(
                method,
                self.base_url + path,
                json=json_data,
                params=params,
            )
            if response.status_code == 401:
                raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD)
            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
            if response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND)
            if response.status_code in (201, 204):
                return {}
            if 200 <= response.status_code < 300:
                return response.json()
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as error:
            self.logger.info(f"Invalid JSON: {error}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)
        except requests.exceptions.HTTPError as error:
            self.logger.info(f"Call to Cisco Umbrella Reporting API failed: {error}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
