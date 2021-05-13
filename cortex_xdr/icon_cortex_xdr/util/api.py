import requests
import json
import time

from insightconnect_plugin_runtime.exceptions import PluginException


class CortexXdrAPI:
    def __init__(self, api_key_id, api_key, fully_qualified_domain_name, logger):
        self.api_key_id = api_key_id
        self.api_key = api_key
        self.fully_qualified_domain_name = fully_qualified_domain_name
        self.logger = logger

    def get_incidents(self, from_time, to_time, time_field):
        api_url = "https://api-{fqdn}/public_api/v1/incidents/get_incidents/"\
            .format(fqdn=self.fully_qualified_domain_name)

        post_body = {
            "request_data": {
                "search_from": 0,
                "search_to": 100,
                "sort": {
                    "field": time_field,
                    "keyword": "asc"
                }
            }
        }

        if from_time is not None and to_time is not None:
            post_body['request_data']['filters'] = [
                {
                    "field": time_field,
                    "operator": "gte",
                    "value": from_time
                },
                {
                    "field": time_field,
                    "operator": "lte",
                    "value": to_time
                }
            ]

        resp_json = self._post_to_api(api_url, post_body)

        if resp_json is not None:
            return resp_json.get("reply", {}).get("incidents", [])

        return []

    def _post_to_api(self, url, post_body):
        headers = {
            "x-xdr-auth-id": self.api_key_id,
            "Authorization": self.api_key,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url=url, data=json.dumps(post_body), headers=headers)

            if response.status_code == 401:
                resp = json.loads(response.text)
                raise PluginException(
                    cause=resp.get("message"),
                    assistance="Authorization failed. Check your API_KEY_ID & API_KEY.",
                )
            if response.status_code == 404:
                resp = json.loads(response.text)
                raise PluginException(
                    cause=resp.get("message"),
                    assistance=f"The object at {url} does not exist.",
                )
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


# TODO: remove main method, solely for testing during development
if __name__ == "__main__":
    api = CortexXdrAPI("api_key_id", "api_key", "rapid7.fqdn.com", None)
    now_ms = int(time.time() * 1000)
    incidents = api.get_incidents((now_ms - 24*60*60*1000), now_ms, "creation_time")
    print(json.dumps(incidents))




