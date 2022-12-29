import json
import sys
from typing import Any, Dict, List, Tuple, Optional, Union
import urllib.parse
from oauthlib.oauth2.rfc6749.endpoints import resource

import requests
from icon_azure_sentinel.util.tools import return_non_empty
from insightconnect_plugin_runtime.exceptions import PluginException

from .endpoints import Endpoint
from .tools import request_execution_time

from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient


class OAuth20ClientCredentialMixin():
    def __init__(self, client_id, client_secret, token_url, **kwargs):
        client = BackendApplicationClient(client_id=client_id)
        self.oauth = OAuth2Session(client=client)
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = token_url
        self.kwargs = kwargs
        self.token = self.oauth.fetch_token(token_url=token_url, client_id=client_id, client_secret=client_secret, **kwargs)

    @property
    def auth_token(self):
        self.token = self.oauth.fetch_token(token_url=self.token_url, client_id=self.client_id, client_secret=self.client_secret, **self.kwargs)
        return self.token

class AzureClient(OAuth20ClientCredentialMixin):
    def __init__(self, logger: Any, tenant_id: str, client_id: str, client_secret: str):
        self.O365_AUTH_ENDPOINT = "https://login.microsoftonline.com/{}/oauth2/token"
        self.SCOPE = "https://management.azure.com"
        self._auth_token = ""  # nosec
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.logger = logger
        super().__init__(client_id, client_secret, self.O365_AUTH_ENDPOINT.format(tenant_id), resource=self.SCOPE) 

#    @property
#    def auth_token(self):
#        tenant_id = self.tenant_id
#        client_id = self.client_id
#        client_secret = self.client_secret
#
#        self.logger.info("Updating auth token...")
#
#        data = {
#            "grant_type": "client_credentials",
#            "client_id": client_id,
#            "resource": self.SCOPE,
#            "client_secret": client_secret,
#        }
#
#        formatted_endpoint = self.O365_AUTH_ENDPOINT.format(tenant_id)
#        self.logger.info("Getting token from: " + formatted_endpoint)
#
#        request = requests.request("POST", formatted_endpoint, data=data)
#        self.logger.info("Authentication request status: " + str(request.status_code))
#
#        if request.status_code != 200:
#            self.logger.error(request.text)
#            raise PluginException(
#                cause="Unable to authorize against Microsoft graph API.",
#                assistance="The application may not be authorized to connect "
#                "to the Microsoft Graph API. Please verify your connection information is correct and contact your "
#                "Azure administrator.",
#                data=request.text,
#            )
#        token = request.json().get("access_token")
#        self._auth_token = token
#        self.logger.info(f"Authentication Token: ****************{self._auth_token[-5:]}")
#        return token


class AzureSentinelClient(AzureClient):
    def __init__(self, logger: Any, tenant_id: str, client_id: str, client_secret: str):
        super(AzureSentinelClient, self).__init__(logger, tenant_id, client_id, client_secret)  # noqa
        self.headers = {"Content-Type": "application/json" }

    def _call_api(
        self, method: str, url: str, headers: dict, payload: Optional[dict] = None, params: Optional[dict] = None
    ) -> Tuple[int, Dict]:
        """_call_api. Send a http call to a given endpoint.

        :param method: Http method to be called.
        :type method: str
        :param url: Url to be called.
        :type url: str
        :param headers: Headers to be sent in the http call.
        :type headers: dict
        :param payload: Payload to be sent in the http call.
        :type payload: Optional[dict]
        :rtype: Union[Dict, int]
        """

        try:
            data = json.dumps(payload) if payload else None
            kwargs = {"headers": headers, "data": data}
            if params:
                payload_str = urllib.parse.urlencode(params, safe="$")
                kwargs["params"] = payload_str

            response = self.oauth.request(method, url, **kwargs)
            response.raise_for_status()
            if response.headers.get("content-type") == "application/json; charset=utf-8":
                return response.status_code, response.json()
            return response.status_code, {}

        except json.decoder.JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)
        except requests.exceptions.HTTPError as error:
            if error.response.status_code == 400:
                raise PluginException(
                    cause="Combination of input arguments is incorrect", assistance=error.response.json().get("error")
                )
            if error.response.status_code == 401:
                raise PluginException(cause=error.response.json().get("error"))
            if error.response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
            if error.response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND)
            if error.response.status_code == 409:
                raise PluginException(
                    cause="Conflicted state of the target resource",
                    assistance=error.response.json().get("error", {}).get("message"),
                )
            if error.response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR)
            raise PluginException(cause=error.response.json().get("error"))
        except requests.exceptions.Timeout:
            raise PluginException(preset=PluginException.Preset.TIMEOUT)

    def _list_all(self, method: str, uri: str, filters: Dict = {}, type_: str = "value") -> List[Any]:
        """_list_all. Get all the objects of a given type. It sends multiple requests
            in order to get everything.

        :param method: HTTP method used to call the api.
        :type method: str
        :param uri: URL to be called.
        :type uri: str
        :param filters: Filters to be used to fetch the data. Order, amount etc.
        :type filters: Dict
        :rtype: List[Any]
        """
        final_uri = uri
        filters = {f"${key}": filters[key] for key in filters}
        N = filters.pop("$top", sys.maxsize)
        _, objects = self._call_api(method, final_uri, self.headers, params=filters)
        results = objects.get(type_, [])
        nextLink = objects.get("nextLink", None)
        while nextLink and len(results) < N:
            _, return_object = self._call_api(method, nextLink, self.headers)
            results += return_object.get(type_, [])
            nextLink = return_object.get("nextLink", None)
            if len(results) > N:
                return results[:N]
        return results[:N]

    def get_incident(
        self,
        incident_id: str,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        api_version: str = "2021-04-01",
    ) -> Union[Dict, int]:
        uri = Endpoint.GETINCIDENT
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            api_version,
        )
        _, results = self._call_api("GET", final_uri, self.headers)
        return return_non_empty(results)

    def create_incident(
        self,
        incident_id: str,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        api_version: str = "2021-04-01",
        **kwargs,
    ) -> Union[Dict, int]:
        uri = Endpoint.CREATEINCIDENT
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            api_version,
        )
        kwargs = return_non_empty(kwargs)
        _, results = self._call_api("PUT", final_uri, self.headers, payload=kwargs)
        return results

    @request_execution_time
    def list_incident(
        self,
        resource_group_name: str,
        workspace_name: str,
        filters: Dict,
        subscription_id: str,
        api_version: str = "2021-04-01",
    ) -> List:
        uri = Endpoint.LISTINCIDENTS
        final_uri = uri.format(subscription_id, resource_group_name, workspace_name, api_version)
        filters = return_non_empty(filters)
        results = self._list_all("GET", final_uri, filters)
        return [return_non_empty(incident) for incident in results]

    def delete_incident(
        self,
        incident_id: str,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        api_version: str = "2021-04-01",
    ) -> Union[Dict, int]:
        uri = Endpoint.DELETEINCIDENT
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            api_version,
        )
        status, _ = self._call_api("DELETE", final_uri, self.headers)
        return status

    def list_bookmarks(
        self,
        incident_id: str,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        api_version: str = "2021-04-01",
    ) -> List:
        uri = Endpoint.LISTBOOKMARKS
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            api_version,
        )
        results = self._list_all("POST", final_uri)
        return [return_non_empty(bookmark) for bookmark in results]

    def list_alerts(
        self,
        incident_id: str,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        api_version: str = "2021-04-01",
    ) -> List:
        uri = Endpoint.LISTALERTS
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            api_version,
        )
        results = self._list_all("POST", final_uri)
        return [return_non_empty(alert) for alert in results]

    def list_entities(
        self,
        incident_id: str,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        api_version: str = "2021-04-01",
    ) -> List:
        uri = Endpoint.LISTENTITIES
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            api_version,
        )
        results = self._list_all("POST", final_uri, type_="entities")
        return [return_non_empty(entity) for entity in results]

    def get_comment(
        self,
        incident_id: str,
        incident_comment_id: str,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        api_version: str = "2021-04-01",
    ):
        uri = Endpoint.GETCOMMENT
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            incident_comment_id,
            api_version,
        )
        _, result = self._call_api("GET", final_uri, self.headers)
        return return_non_empty(result)

    def list_comments(
        self,
        incident_id: str,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        api_version: str = "2021-04-01",
    ) -> List:
        uri = Endpoint.LISTCOMMENTS
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            api_version,
        )
        results = self._list_all("GET", final_uri)
        return [return_non_empty(result) for result in results]

    def create_update_comment(
        self,
        incident_id: str,
        incident_comment_id: str,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        api_version: str = "2021-04-01",
        **kwargs,
    ):
        uri = Endpoint.CREATEUPDATECOMMENT
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            incident_comment_id,
            api_version,
        )
        kwargs = return_non_empty(kwargs)
        data = kwargs
        _, result = self._call_api("PUT", final_uri, headers=self.headers, payload=data)
        return return_non_empty(result)

    def delete_comment(
        self,
        incident_id: str,
        incident_comment_id: str,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        api_version: str = "2021-04-01",
    ):
        uri = Endpoint.DELETECOMMENT
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            incident_comment_id,
            api_version,
        )
        status_code, _ = self._call_api("DELETE", final_uri, self.headers)
        return status_code

    def create_indicator(
        self,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        api_version: str = "2021-10-01",
        **kwargs,
    ):
        uri = Endpoint.CREATEINDICATOR
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            api_version,
        )
        data = kwargs
        _, result = self._call_api("POST", final_uri, headers=self.headers, payload=data)
        return result

    def update_indicator(
        self,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        indicator_name: str,
        api_version: str = "2021-10-01",
        **kwargs,
    ):
        uri = Endpoint.UPDATEINDICATOR
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            indicator_name,
            api_version,
        )
        indicator = self.get_indicator(resource_group_name, workspace_name, subscription_id, indicator_name)
        data = return_non_empty(kwargs)
        data = self._prepared_necessary_data(indicator, data)

        _, result = self._call_api("PUT", final_uri, headers=self.headers, payload=data)
        return result

    def get_indicator(
        self,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        indicator_name: str,
        api_version: str = "2021-10-01",
    ):
        uri = Endpoint.GETINDICATOR
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            indicator_name,
            api_version,
        )
        _, result = self._call_api("GET", final_uri, headers=self.headers)
        return result

    def delete_indicator(
        self,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        indicator_name: str,
        api_version: str = "2021-10-01",
    ):
        uri = Endpoint.DELETEINDICATOR
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            indicator_name,
            api_version,
        )
        _, result = self._call_api("DELETE", final_uri, headers=self.headers)
        return result

    def query_indicator(
        self,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        api_version: str = "2021-10-01",
        **kwargs,
    ):
        uri = Endpoint.QUERYINDICATORS
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            api_version,
        )
        data = kwargs
        data = return_non_empty(data)
        _, result = self._call_api("POST", final_uri, headers=self.headers, payload=data)
        return result

    def append_tags(
        self,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        indicator_name: str,
        api_version: str = "2021-10-01",
        **kwargs,
    ):
        uri = Endpoint.APPENDTAGS
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            indicator_name,
            api_version,
        )
        data = kwargs
        _, result = self._call_api("POST", final_uri, headers=self.headers, payload=data)
        return result

    def replace_tags(
        self,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        indicator_name: str,
        api_version: str = "2021-10-01",
        **kwargs,
    ):
        uri = Endpoint.REPLACETAGS
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            indicator_name,
            api_version,
        )
        data = kwargs
        _, result = self._call_api("POST", final_uri, headers=self.headers, payload=data)
        return result

    def create_update_watchlist(
        self,
        resource_group_name: str,
        workspace_name: str,
        watchlist_alias: str,
        subscription_id: str,
        api_version: str = "2021-04-01",
        **kwargs,
    ):
        kwargs = return_non_empty(kwargs)
        uri = Endpoint.CREATEUPDATEWATCHLIST
        final_uri = uri.format(subscription_id, resource_group_name, workspace_name, watchlist_alias, api_version)
        _, result = self._call_api("PUT", final_uri, self.headers, payload=kwargs)
        return return_non_empty(result)

    def get_watchlist(
        self,
        resource_group_name: str,
        workspace_name: str,
        watchlist_alias: str,
        subscription_id: str,
        api_version: str = "2021-04-01",
    ):
        uri = Endpoint.GETWATCHLIST
        final_uri = uri.format(subscription_id, resource_group_name, workspace_name, watchlist_alias, api_version)
        _, result = self._call_api("GET", final_uri, self.headers)
        return return_non_empty(result)

    def delete_watchlist(
        self,
        resource_group_name: str,
        workspace_name: str,
        watchlist_alias: str,
        subscription_id: str,
        api_version: str = "2021-04-01",
    ):
        uri = Endpoint.DELETEWATCHLIST
        final_uri = uri.format(subscription_id, resource_group_name, workspace_name, watchlist_alias, api_version)
        status_code, _ = self._call_api("DELETE", final_uri, self.headers)
        return status_code

    def list_watchlists(
        self, resource_group_name: str, workspace_name: str, subscription_id: str, api_version: str = "2021-04-01"
    ):
        uri = Endpoint.LISTWATCHLISTS
        final_uri = uri.format(subscription_id, resource_group_name, workspace_name, api_version)
        results = self._list_all("GET", final_uri)
        return [return_non_empty(result) for result in results]

    def create_update_watchlist_items(
        self,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        watchlist_alias: str,
        watchlist_item_id: str,
        api_version: str = "2021-10-01",
        **kwargs,
    ):
        uri = Endpoint.CREATE_UPDATE_WATCHLIST_ITEMS
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            watchlist_alias,
            watchlist_item_id,
            api_version,
        )
        data = kwargs
        data = return_non_empty(data)
        _, result = self._call_api("PUT", final_uri, headers=self.headers, payload=data)
        return result

    def get_watchlist_items(
        self,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        watchlist_alias: str,
        watchlist_item_id: str,
        api_version: str = "2021-10-01",
    ):
        uri = Endpoint.GET_WATCHLIST_ITEMS
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            watchlist_alias,
            watchlist_item_id,
            api_version,
        )
        _, result = self._call_api("GET", final_uri, headers=self.headers)
        return result

    def delete_watchlist_items(
        self,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        watchlist_alias: str,
        watchlist_item_id: str,
        api_version: str = "2021-10-01",
    ):
        uri = Endpoint.DELETE_WATCHLIST_ITEMS
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            watchlist_alias,
            watchlist_item_id,
            api_version,
        )
        _, result = self._call_api("DELETE", final_uri, headers=self.headers)
        return result

    def list_watchlist_items(
        self,
        resource_group_name: str,
        workspace_name: str,
        subscription_id: str,
        watchlist_alias: str,
        api_version: str = "2021-10-01",
    ):
        uri = Endpoint.LIST_WATCHLIST_ITEMS
        final_uri = uri.format(
            subscription_id,
            resource_group_name,
            workspace_name,
            watchlist_alias,
            api_version,
        )
        _, result = self._call_api("GET", final_uri, headers=self.headers)
        return result

    def _prepared_necessary_data(self, indicator, data):
        """
        fields blocked to change for update indicator
        """

        blocked_keys = [
            "description",
            "killChainPhases",
            "validFrom",
            "created",
            "createdByRef",
            "externalId",
            "source",
        ]
        # optional data
        fields_to_update = ["displayName", "pattern", "patternType", "threatTypes"]
        for field in fields_to_update:
            if not data["properties"].get(field):
                blocked_keys.append(field)

        blocked_fields = {"properties": {}}
        for key in blocked_keys:
            if indicator["properties"].get(key) is not None:
                blocked_fields["properties"][key] = indicator["properties"].get(key)

        data["etag"] = indicator.get("etag")
        data["kind"] = indicator.get("kind")
        data["properties"].update(blocked_fields["properties"])

        return data
