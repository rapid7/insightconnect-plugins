import requests
import json
import logging

from insightconnect_plugin_runtime.exceptions import PluginException
from .endpoints import Endpoint
from typing import Dict, Any, List
from icon_azure_sentinel.util.tools import return_non_empty

logger = logging.getLogger(__name__)


class AzureSentinelClient:
    def __init__(self, auth_token: str, api_version: str, subscription_id: str):
        self.auth_token = auth_token
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer %s" % auth_token,
        }
        self.api_version = api_version
        self.subscription_id = subscription_id

    def _call_api(self, method: str, url: str, headers: dict, payload: dict = None):
        try:
            data = json.dumps(payload) if payload else None
            response = requests.request(
                method,
                url,
                headers=headers,
                data=data,
            )
            response.raise_for_status()
            if method.upper() != "DELETE":
                return response.json()
            else:
                return response.status_code
        except json.decoder.JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.raw())
        except requests.exceptions.HTTPError as error:
            if error.response.status_code == 400:
                raise PluginException(cause="Bad Request", assistance=error.response.json())
            raise PluginException(cause="HTTP Error", assistance=str(error))
        except requests.exceptions.Timeout as timeout:
            raise PluginException(cause="Timeout error", assistance=str(timeout))
        except Exception as exception:
            raise PluginException(cause="URL Request Failed", assistance=str(exception))

    def _list_all(self, method: str, uri: str, filters: Dict={}) -> List[Any]:
        final_uri = uri
        for key in filters: 
            final_uri += "&$" + key + "=" + str(filters[key])
        objects = self._call_api(method, final_uri, self.headers)
        results = objects.get("value", [])
        nextLink = objects.get("nextLink", None)
        while nextLink:
            return_object = self._call_api(method, nextLink, self.headers)
            results += return_object.get("value", [])
            nextLink = return_object.get("nextLink", None)
            logger.info("nextLink: %s", nextLink)
        return results

    def get_incident(self, incident_id: str, resource_group_name: str, workspace_name: str) -> Dict[str, Any]:
        uri = Endpoint.GETINCIDENT
        final_uri = uri.format(
            self.subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            self.api_version,
        )
        return self._call_api("GET", final_uri, self.headers)

    def create_incident(self, incident_id: str, resource_group_name: str, workspace_name: str, **kwargs):
        uri = Endpoint.CREATEINCIDENT
        final_uri = uri.format(
            self.subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            self.api_version,
        )
        kwargs = return_non_empty(kwargs)
        return self._call_api("PUT", final_uri, self.headers, payload=kwargs)

    def list_incident(self, resource_group_name: str, workspace_name: str, filters: Dict):
        uri = Endpoint.LISTINCIDENTS
        final_uri = uri.format(self.subscription_id, resource_group_name, workspace_name, self.api_version)
        logger.info(filters)
        filters = return_non_empty(filters)

        results = self._list_all("GET", final_uri, filters)
        return [return_non_empty(incident) for incident in results]

    def delete_incident(self, incident_id: str, resource_group_name: str, workspace_name: str):
        uri = Endpoint.DELETEINCIDENT
        final_uri = uri.format(
            self.subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            self.api_version,
        )
        return self._call_api("DELETE", final_uri, self.headers)

    def list_bookmarks(self, incident_id: str, resource_group_name: str, workspace_name: str):
        uri = Endpoint.LISTBOOKMARKS
        final_uri = uri.format(
            self.subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            self.api_version,
        )
        results = self._list_all("POST", final_uri)
        return [return_non_empty(bookmark) for bookmark in results]

    def list_alerts(self, incident_id: str, resource_group_name: str, workspace_name: str):
        uri = Endpoint.LISTALERTS
        final_uri = uri.format(
            self.subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            self.api_version,
        )
        results = self._list_all("POST", final_uri)
        return [return_non_empty(alert) for alert in results]

    def list_entities(self, incident_id: str, resource_group_name: str, workspace_name: str):
        uri = Endpoint.LISTENTITIES
        final_uri = uri.format(
            self.subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            self.api_version,
        )
        results = self._list_all("POST", final_uri)
        return [return_non_empty(entity) for entity in results]
