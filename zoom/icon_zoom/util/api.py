import requests
from insightconnect_plugin_runtime.exceptions import PluginException
import json
from icon_zoom.util.util import generate_jwt_token


class ZoomAPI:
    def __init__(self, api_key, secret, logger):
        self.url = "https://api.zoom.us/v2"
        self.api_key = api_key
        self.secret = secret
        self.logger = logger

    def get_user(self, user_id):
        return self._call_api("GET", f"{self.url}/users/{user_id}")

    def create_user(self, payload):
        return self._call_api("POST", f"{self.url}/users", json_data=payload)

    def delete_user(self, user_id, params):
        return self._call_api("DELETE", f"{self.url}/users/{user_id}", params=params)

    def get_user_activity_events(self, start_date=None, end_date=None, page_size=None, next_page_token=None):
        activities_url = f"{self.url}/report/activities"

        events = []
        params = {
            "from": start_date,
            "to": end_date,
            "page_size": page_size,
            "next_page_token": next_page_token
        }

        while True:
            response = self._call_api("GET", activities_url, params=params)

            events = events + response.get('activity_logs', [])

            if "next_page_token" in response and response.get("next_page_token") != "":
                params["next_page_token"] = response.get("next_page_token")
            else:
                return events

    def _call_api(self, method, url, params=None, json_data=None, allow_404=False):
        token = generate_jwt_token(self.api_key, self.secret)
        headers = {
            "authorization": f"Bearer {token}",
            "content-type": "application/json"
        }

        try:
            response = requests.request(method, url,
                                        json=json_data,
                                        params=params,
                                        headers=headers)

            if response.status_code == 401:
                resp = json.loads(response.text)
                raise PluginException(cause=resp.get("message"),
                                      assistance="Verify your JWT App API key and Secret configured in your "
                                                 "connection is correct.")
            if response.status_code == 404:
                resp = json.loads(response.text)
                if allow_404:
                    return None
                else:
                    raise PluginException(cause=resp.get("message"),
                                          assistance=f"The object at {url} does not exist. Verify the ID and fields "
                                                     f"used are valid.")
            # Success; no content
            if response.status_code == 204:
                return None
            if 200 <= response.status_code < 300:
                return response.json()

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            self.logger.info(f"Invalid json: {e}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)
        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Request to f{url} failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN)
