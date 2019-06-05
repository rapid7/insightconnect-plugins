from requests import request, HTTPError
import komand
from komand.exceptions import ConnectionTestException
import logging

# suppress request logging
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class RedCanary3:
    EMPTY_RESULT = {'relationships': {}, 'links': {}}

    def __init__(self, api_token, customer_id, logger):
        self.base_url = 'https://{}.my.redcanary.co/openapi/v3/'.format(
            customer_id
        )
        self.api_token = api_token
        self.logger = logger

    def test_call(self):
        return request("GET", self.base_url + "endpoints", params={"auth_token": self.api_token})

    def create_activity_monitor(
        self, name, type_, active, file_modification_types_monitored,
        file_paths_monitored, usernames_matched=None, usernames_excluded=None
    ):
        data = {
            'activity_monitor': {
                'name': name,
                'type': type_,
                'active': active,
                'file_modification_types_monitored':
                    file_modification_types_monitored,
                'file_paths_monitored': file_paths_monitored,
                'usernames_matched': usernames_matched,
                'usernames_excluded': usernames_excluded
            }
        }

        return self._call_api('POST', 'activity_monitors', json=data)[0]

    def list_activity_monitors(self, max_results=None):
        return self._call_api(
            'GET', 'activity_monitors', max_results=max_results
        )

    def list_activity_monitor_matches(
        self, activity_monitor_id, max_results=None
    ):
        return self._call_api(
            'GET', 'activity_monitors/{}/matches'.format(activity_monitor_id),
            max_results=max_results
        )

    def deactivate_activity_monitor(self, activity_monitor_id):
        return self._call_api(
            'DELETE', 'activity_monitors/{}'.format(activity_monitor_id)
        )[0]

    def get_activity_monitor(self, activity_monitor_id):
        return self._call_api(
            'GET', 'activity_monitors/{}'.format(activity_monitor_id)
        )[0]

    def list_all_activity_monitor_matches(self, max_results=None):
        return self._call_api(
            'GET', 'activity_monitor_matches', max_results=max_results
        )

    def get_event(self, event_id):
        return self._call_api('GET', 'events/{}'.format(event_id))[0]

    def list_events(self, max_results=None):
        return self._call_api('GET', 'events', max_results=max_results)

    def search_for_endpoint_hostname_usages(
        self, endpoint_hostname, max_results=None
    ):
        return self._call_api(
            'GET', 'search/endpoint_hostnames/{}'.format(endpoint_hostname),
            max_results=max_results, allow_404=True
        )

    def search_for_mac_address_usages(self, mac_address, max_results=None):
        return self._call_api(
            'GET', 'search/mac_addresses/{}'.format(mac_address),
            max_results=max_results, allow_404=True
        )

    def search_for_ip_address_usages(self, ip_address, max_results=None):
        return self._call_api(
            'GET', 'search/ip_addresses/{}'.format(ip_address),
            max_results=max_results, allow_404=True
        )

    def get_detections(self, since, max_results=None):
        return self._call_api(
            'GET', 'detections',
            params={'since': since.isoformat()} if since else None,
            max_results=max_results
        )

    def retrieve_indicators(self, detection_id, max_results):
        indicators = self._call_api(
            'GET', 'detections/{}/marked_indicators_of_compromise'.format(
                detection_id
            ), max_results=max_results
        )

        for indicator in indicators:
            attributes = indicator.get('attributes', {})
            for key in attributes.keys():
                if key.endswith('?'):
                    new_key = key[:-1]
                    attributes[new_key] = attributes.pop(key)
        return indicators

    def update_remediation_state(
        self, detection_id, remediation_state, comment
    ):
        return self._call_api(
            'PATCH',
            'detections/{}/update_remediation_state'.format(detection_id),
            data={'comment': comment, 'remediation_state': remediation_state}
        )[0]

    def acknowledge_detection(self, detection_id):
        return self._call_api(
            'PATCH', 'detections/{}/mark_acknowledged'.format(detection_id)
        )[0]

    def _call_api(
        self, method, endpoint_url, params=None, data=None, json=None,
        max_results=None, allow_404=False
    ):
        url = self.base_url + endpoint_url

        if params is None:
            params = {}
        params['auth_token'] = self.api_token

        results = []

        kwargs = {
            'params': params, 'data': data, 'json': json
        }

        while True:
            response = request(method, url, **kwargs)
            try:
                response.raise_for_status()
            except HTTPError:
                if response.status_code == 404:
                    # API dumps HTML page when customer_id field is invalid - other conditions may cause this too but we don't know
                    if '<!DOCTYPE html' in response.content.decode("utf-8"):
                        raise ConnectionTestException(cause="Verify the customer ID value in the Connection is correct.",
                                                      assistance="Double-check the ID from your Red Canary account URL e.g. https://<customer_id>.my.redcanary.co.")
                if response.status_code == 404 and allow_404:
                    self.logger.info(
                        'API returned 404, meaning no results are available'
                    )
                    break
                if response.status_code == 403:
                    raise ConnectionTestException(cause="Verify your API key configured in your Connection is correct.",
                                                  assistance="Double-check the API authorization key from your Red Canary account at https://<customer_id>.my.redcanary.co/users/edit.")
                raise Exception(
                    'Failed to call Red Canary v3 API: {} {}'.format(
                        response.status_code, response.content
                    )
                )

            json_response = komand.helper.clean(response.json())
            data = json_response['data']

            for item in data:
                if item != self.EMPTY_RESULT:
                    break
            else:
                if len(data) > 0:
                    self.logger.info(
                        'Empty results returned by API. '
                        'Assuming no more results are available.'
                    )
                    self._clean_empty_results(results)
                    break
                else:
                    break

            results.extend(data)

            if max_results is not None and len(results) >= max_results:
                self.logger.info('Maximum number of results reached')
                results = results[:max_results]
                break

            if 'links' in json_response and 'next' in json_response['links']:
                url = json_response['links']['next']
            else:
                break

        return results

    def _clean_empty_results(self, results):
        while results and results[-1] == self.EMPTY_RESULT:
            results.pop()
