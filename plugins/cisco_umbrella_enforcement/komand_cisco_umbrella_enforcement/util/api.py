import json
import requests
from typing import Optional
from insightconnect_plugin_runtime.exceptions import PluginException


class CiscoUmbrellaEnforcementAPI:
    VERSION = "1.0"

    EVENT_ERR = ValueError("Event must be list")
    REQUIRED_ERR = ValueError("Some required values are missing")

    def __init__(self, customer_key, verify):
        self._uris = {"events": "events", "domains": "domains"}
        self.verify = verify
        self.url = f"https://s-platform.api.opendns.com/{CiscoUmbrellaEnforcementAPI.VERSION}"
        self.params = {"customerKey": customer_key}

    def get_domains(self):
        """
        Method to make a GET request for list domains action.
        :return: Response containing list of domains
        """
        return self._call_api("GET", "/domains")

    def add_event(self, data):
        """
        Method to make a POST request to register a domain.
        :param data: List of domain information
        :return:
        """
        return self._call_api("POST", "/events", data=data)

    def delete_event(self, name: Optional[str] = None, domain_id: Optional[int] = None):
        """
        Method to make a DELETE request to delete a domain either by name or ID.
        :param name: Name of the domain
        :param domain_id: ID for the domain
        :return:
        """
        if name and domain_id:
            raise PluginException(
                cause="Only one input for delete can be provided.",
                assistance="Either choose name or domain_id, but not both.",
            )

        if name:
            return self._call_api("DELETE", f"/domains/{name}")

        if domain_id:
            return self._call_api("DELETE", f"/domains/{domain_id}")

    def _call_api(
        self,
        # method -> GET/POST/DELETE
        method: str,
        # path -> url
        path: str,
        # data -> payload
        data: Optional = None,
    ):

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        response = requests.request(
            method, self.url + path, params=self.params, data=json.dumps(data), headers=headers, verify=self.verify
        )

        # Error handling
        if response.status_code == 400:
            raise PluginException(cause="Invalid request.")
        if 401 <= response.status_code <= 403:
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
        if response.status_code == 404:
            raise PluginException(preset=PluginException.Preset.NOT_FOUND)
        if response.status_code >= 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR)
        if 200 <= response.status_code < 300:
            return response.json()

    # def post(self, uri, params={}, data={}):
    #     """A generic method to make POST requests to the OpenDNS Enforcement API on the given URI."""
    #     params["customerKey"] = self.customer_key
    #     return requests.post(
    #         urljoin(self.url, uri),
    #         params=params,
    #         data=data,
    #         headers={"Content-Type": "application/json"},
    #         verify=self.verify,
    #     )

    # def _request_parse(self, method, *args):
    #     r = method(*args)
    #     try:
    #         r.raise_for_status()
    #     except Exception as err:
    #         err.args = (
    #             re.sub(
    #                 r"customerKey=[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}",
    #                 "customerKey=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    #                 err.args[0],
    #             ),
    #         )
    #         raise
    #     return r.json()

    # def post_parse(self, uri, params={}, data={}):
    #     """Convenience method to call post() on an arbitrary URI and parse the response
    #     into a JSON object. Raises an error on non-200 response status.
    #     """
    #     return self._request_parse(self.post, uri, params, data)
    #
    # def delete_parse(self, uri, params={}):
    #     """Convenience method to call post() on an arbitrary URI and parse the response
    #     into a JSON object. Raises an error on non-200 response status.
    #     """
    #     r = self.delete(uri, params)
    #     return r.status_code

    # def add_event(self, event):
    #     if type(event) is list:
    #         return self.post_parse(self._uris["events"], {}, json.dumps(event))
    #     else:
    #         raise CiscoUmbrellaEnforcementAPI.EVENT_ERR
