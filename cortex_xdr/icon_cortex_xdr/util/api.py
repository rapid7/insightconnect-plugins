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

        batch_size = 100
        search_from = 0
        search_to = search_from + batch_size

        # Request incidents in ascending order so that we get the oldest events first.
        post_body = {
            "request_data": {
                "search_from": search_from,
                "search_to": search_to,
                "sort": {
                    "field": time_field,
                    "keyword": "asc"
                }
            }
        }

        # If time constraints have been provided for the request, add them to the post body
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

        done = False
        all_incidents = []

        # Keep paging through and requesting incidents until we have requested all incidents which match our query
        while not done:
            resp_json = self._post_to_api(api_url, post_body)
            if resp_json is not None:
                total_count = resp_json.get('reply', {}).get("total_count", -1)
                all_incidents.extend(resp_json.get("reply", {}).get("incidents", []))
                # If the number of incidents we have received so far is greater than or equal to the total number of
                # incidents which match the query, then we can stop paging.
                if len(all_incidents) >= total_count or total_count < 0:
                    done = True

                # Update the indices of search_from and search_to to we can request the next page
                search_from = search_from + batch_size
                search_to = search_to + batch_size if search_to + batch_size < total_count else total_count

                # Add the updated page indices to the request body for when we request the next page
                post_body['request_data']['search_from'] = search_from
                post_body['request_data']['search_to'] = search_to
            else:
                done = True

            # Back-off between making requests to the API.
            time.sleep(1)

        return all_incidents

    def _post_to_api(self, url, post_body):
        # Add auth details from connection to the request headers
        headers = {
            "x-xdr-auth-id": self.api_key_id,
            "Authorization": self.api_key,
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url=url, data=json.dumps(post_body), headers=headers)

            if response.status_code == 400:
                resp = json.loads(response.text)
                raise PluginException(
                    cause=resp.get("message"),
                    assistance="Bad request, invalid JSON.",
                )
            if response.status_code == 401:
                resp = json.loads(response.text)
                raise PluginException(
                    cause=resp.get("message"),
                    assistance="Authorization failed. Check your API_KEY_ID & API_KEY.",
                )
            if response.status_code == 402:
                resp = json.loads(response.text)
                raise PluginException(
                    cause=resp.get("message"),
                    assistance="Unauthorized access. User does not have the required license type to run this API.",
                )
            if response.status_code == 403:
                resp = json.loads(response.text)
                raise PluginException(
                    cause=resp.get("message"),
                    assistance=
                    "Forbidden. The provided API Key does not have the required RBAC permissions to run this API.",
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
