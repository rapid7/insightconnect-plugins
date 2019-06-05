from requests import request, HTTPError
from komand.helper import clean
from komand.exceptions import ConnectionTestException


def find_value(key, dictionary):
    if key in dictionary:
        return dictionary[key]
    for k, v in dictionary.items():
        if isinstance(v, dict):
            value = find_value(key, v)
            if value is not None:
                return value


class TCell:
    def __init__(self, api_key, logger):
        self.api_key = api_key
        self.logger = logger
        self.base_url = 'https://api.tcell.io/customer/api/v1/'

        # Test API key
        self.list_apps()

    def list_apps(self):
        return self.call_api('GET', 'apps')

    def get_app(self, app_id):
        return self.call_api('GET', 'apps/' + app_id)

    def get_app_tags(self, app_id):
        return self.call_api('GET', 'apps/' + app_id + '/tags')

    def create_app(self, app_display_name):
        return self.call_api(
            'POST', 'apps', json={'app_display_name': app_display_name}
        )

    def change_tags(self, app_id, tags):
        try:
            response = self.call_api(
                'POST', 'apps/' + app_id + '/tags', json={'tags': tags}
            )
        except Exception as e:
            self.logger.error(
                'Failed to change tags to {} for app {}: {}'.format(
                    tags, app_id, str(e)
                )
            )
            return False
        return response.get('message') == 'Request successful'

    def add_tags(self, app_id, tags):
        try:
            response = self.call_api(
                'PUT', 'apps/' + app_id + '/tags', json={'tags': tags}
            )
        except Exception as e:
            self.logger.error(
                'Failed to add tags {} to app {}: {}'.format(
                    tags, app_id, str(e)
                )
            )
            return False
        return response.get('message') == 'Request successful'

    def remove_tags(self, app_id, tags):
        try:
            response = self.call_api(
                'DELETE', 'apps/' + app_id + '/tags', json={'tags': tags}
            )
        except Exception as e:
            self.logger.error(
                'Failed to remove tags from app {}: {}'.format(
                    app_id, str(e)
                )
            )
            return False
        return response.get('message') == 'Request successful'

    def get_agent_details(self, app_id, agent_id):
        return self.call_api('GET', 'apps/' + app_id + '/agents/' + agent_id)

    def list_agents(self, app_id, from_=None, to=None, per_page=10, page=1):
        params = {
            'from': from_,
            'to': to,
            'per_page': per_page,
            'page': page
        }
        params = clean(params)
        return self.call_api(
            'GET', 'apps/' + app_id + '/agents', params=params, allow_404=True
        )

    def get_route_details(self, app_id, route_id):
        return self.call_api('GET', 'apps/' + app_id + '/routes/' + route_id)

    def list_routes(self, app_id, from_=None, to=None, per_page=10, page=1):
        params = {
            'from': from_,
            'to': to,
            'per_page': per_page,
            'page': page
        }
        params = clean(params)
        return self.call_api(
            'GET', 'apps/' + app_id + '/routes', params=params, allow_404=True
        )

    def get_inline_script_details(self, app_id, inline_script_id):
        return self.call_api(
            'GET', 'apps/' + app_id + '/inline_scripts/' + inline_script_id
        )

    def list_inline_scripts(
        self, app_id, from_=None, to=None, per_page=10, page=1
    ):
        params = {
            'from': from_,
            'to': to,
            'per_page': per_page,
            'page': page
        }
        params = clean(params)
        return self.call_api(
            'GET', 'apps/' + app_id + '/inline_scripts', params=params,
            allow_404=True
        )

    def get_package_details(self, app_id, package_id):
        return self.call_api(
            'GET', 'apps/' + app_id + '/packages/' + str(package_id)
        )

    def list_packages(self, app_id, from_=None, to=None, per_page=10, page=1):
        params = {
            'from': from_,
            'to': to,
            'per_page': per_page,
            'page': page
        }
        params = clean(params)
        return self.call_api(
            'GET', 'apps/' + app_id + '/packages', params=params,
            allow_404=True
        )

    def get_active_config(self, app_id):
        return self.call_api('GET', 'apps/' + app_id + '/configs/latest')

    def get_config(self, app_id, config_id):
        return self.call_api(
            'GET', 'apps/' + app_id + '/configs/' + str(config_id)
        )

    def list_configs(self, app_id, from_=None, to=None, per_page=10, page=1):
        params = {
            'from': from_,
            'to': to,
            'per_page': per_page,
            'page': page
        }
        params = clean(params)
        return self.call_api(
            'GET', 'apps/' + app_id + '/configs', params=params,
            allow_404=True
        )

    def revert_config_changes(self, app_id, id_):
        try:
            response = self.call_api(
                'POST', 'apps/' + app_id + '/configs/revert/' + str(id_)
            )
        except Exception as e:
            self.logger.error(
                'Failed to revert config to {} for app {}: {}'.format(
                    id_, app_id, str(e)
                )
            )
            return False
        return response.get('result').get('message') == 'Successfully reverted'

    def post_config_changes(self, app_id, config):
        return self.call_api(
            'POST', 'apps/' + app_id + '/configs', json=config
        )

    def add_ips_to_blacklist(self, app_id, ips):
        return self.call_api(
            'POST', 'apps/' + app_id + '/configs/blockedips/blacklistedips',
            json={'ips': ips}
        )

    def remove_ips_from_blacklist(self, app_id, ips):
        return self.call_api(
            'DELETE', 'apps/' + app_id + '/configs/blockedips/blacklistedips',
            json={'ips': ips}
        )

    def get_events(self, app_id, source, filter_=None, from_=None):
        params = {
            'filter': filter_,
            'from': from_
        }
        params = clean(params)

        return self.call_api(
            'GET', 'apps/' + app_id + '/sources/' + source + '/table',
            params=params, allow_404=True
        )

    def create_ip_group(self, group):
        return self.call_api('POST', 'ipgroups', json=group)

    def update_ip_group(self, group_name, items):
        return self.call_api(
            'POST', 'ipgroups/' + group_name + '/items', json={'items': items}
        )

    def call_api(
        self, method, url, params=None, json=None, data=None, allow_404=False
    ):
        api_url = self.base_url + url

        self.logger.info('Call API: Trying to reach endpoint: ' + api_url)

        kwargs = {'params': params, 'json': json, 'data': data}
        kwargs = clean(kwargs)

        resp = request(method, api_url, headers={
            'Authorization': 'Bearer ' + self.api_key,
        }, **kwargs)

        try:
            resp.raise_for_status()
        except HTTPError:
            if resp.status_code == 401:
                raise ConnectionTestException(
                    preset=ConnectionTestException.Preset.API_KEY
                )
            elif resp.status_code == 404:
                if allow_404:
                    return None
                else:
                    raise ConnectionTestException(
                        preset=ConnectionTestException.Preset.NOT_FOUND
                    )
            else:
                try:
                    content = resp.json()
                    cause = find_value('message', content) or \
                        find_value('error_message', content)
                    cause = cause.capitalize()
                    if not cause.endswith('.'):
                        cause = cause + '.'
                except ValueError:
                    cause = resp.content.decode()
                raise ConnectionTestException(
                    cause=cause,
                    assistance='Please make sure that your API key is valid ' +
                    'and that you did not attempt to create entities that ' +
                    'already exist.'
                )

        try:
            json = resp.json()
        except ValueError as e:
            raise ConnectionTestException(
                cause='Incorrect data format received from API: ' + str(e),
                assistance='Please make sure that your API key ' +
                'has the correct scope and the correct inputs were used.'
            )

        self.logger.info('Call API: Successfully obtained data from the API')

        return json
