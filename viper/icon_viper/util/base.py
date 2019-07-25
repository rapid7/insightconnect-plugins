import json
import requests
from komand.exceptions import PluginException


class ViperBase:

    def __init__(self, config):
        self.config = config

    @classmethod
    def is_active(cls, config):
        return cls._get(config, "", False)

    @classmethod
    def _get(cls, config, url, binary=False):
        headers = {'Authorization': f'Token {config.token}'}
        response = requests.get(config.api_url + url, headers=headers)
        return ViperBase.__handle_response(response, binary)

    @classmethod
    def _post(cls, config, url, data, files=None, binary=False):
        headers = {'Authorization': f'Token {config.token}'}
        response = requests.post(
            config.api_url + url, headers=headers, data=data, files=files)
        return ViperBase.__handle_response(response, binary)

    @classmethod
    def _put(cls, config, url, data):
        headers = {'Authorization': f'Token {config.token}'}
        response = requests.put(config.api_url + url, headers=headers, data=data)
        return ViperBase.__handle_response(response)

    @classmethod
    def _delete(cls, config, url):
        headers = {'Authorization': f'Token {config.token}'}
        response = requests.delete(config.api_url + url, headers=headers)
        return ViperBase.__handle_response(response)

    @classmethod
    def __handle_response(cls, response, binary=False):
        if response.status_code not in range(200, 299):
            raise PluginException(
                cause='Error: Received HTTP %d status code from Viper. Please verify your Viper server '
                'status and try again. ', assistance='If the issue persists please contact support. '
                'Server response was: %s' % (response.status_code, response.text))
        if response.status_code is not 204:
            try:
                return response.json() if not binary else response
            except json.decoder.JSONDecodeError:
                raise PluginException(cause='Error: Received an unexpected response. Please verify your Viper server '
                                'status and try again. ', assistance='If the issue persists please contact support. '
                                'Server response was: %s' % response.text)

    @classmethod
    def _get_results(cls, config, url):
        response = cls._get(config, url)
        results = []
        while True:
            if 'results' not in response:
                break

            results += response['results']
            if 'next' in response and response['next']:
                next_url = str(response['next'])
                index = next_url.index('?')
                query = next_url[index:]
                response = cls._get(config, url + query)
            else:
                break
        return results
