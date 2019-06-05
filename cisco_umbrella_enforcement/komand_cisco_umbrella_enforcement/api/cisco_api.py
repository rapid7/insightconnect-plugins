import json
import re
import requests
from urllib.parse import urljoin
import urllib
import datetime, time


class Cisco_Api(object):
    VERSION = '1.0'
    BASE_URL = 'https://s-platform.api.opendns.com/' + VERSION + '/'
    
    EVENT_ERR = ValueError("Event must be list")
    REQUIRED_ERR = ValueError("Some required values are missing")

    def __init__(self, customer_key):
        self.customer_key = customer_key
        self._uris = {
            "events":       "events",
            "domains":        "domains"
        }

    def get(self, uri, params={}):
        '''A generic method to make GET requests to the OpenDNS Enforcement API on the given URI.'''
        params["customerKey"] = self.customer_key;
        return requests.get(urljoin(Cisco_Api.BASE_URL, uri),
            params=params, headers={}, proxies={}
        )

    def post(self, uri, params={}, data={}):
        '''A generic method to make POST requests to the OpenDNS Enforcement API on the given URI.'''
        params["customerKey"] = self.customer_key;
        return requests.post(
            urljoin(Cisco_Api.BASE_URL, uri),
            params=params, data=data, headers={"Content-Type": "application/json"}
        )

    def delete(self, uri, params={}):
        '''A generic method to make DELETE requests to the OpenDNS Enforcement API on the given URI.'''
        params["customerKey"] = self.customer_key;
        return requests.delete(
            urljoin(Cisco_Api.BASE_URL, uri),
            params=params, headers={}, proxies={}
        )

    def _request_parse(self, method, *args):
        r = method(*args)
        try:
            r.raise_for_status()
        except Exception as err:
            err.args = (re.sub(r'customerKey=[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}', 'customerKey=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', err.args[0]),)
            raise
        return r.json()

    def get_parse(self, uri, params={}):
        '''Convenience method to call get() on an arbitrary URI and parse the response
        into a JSON object. Raises an error on non-200 response status.
        '''
        return self._request_parse(self.get, uri, params)

    def post_parse(self, uri, params={}, data={}):
        '''Convenience method to call post() on an arbitrary URI and parse the response
        into a JSON object. Raises an error on non-200 response status.
        '''
        return self._request_parse(self.post, uri, params, data)

    def delete_parse(self, uri, params={}):
        '''Convenience method to call post() on an arbitrary URI and parse the response
        into a JSON object. Raises an error on non-200 response status.
        '''
        r = self.delete(uri, params)
        return r.status_code

    def add_event(self, event):
        if type(event) is list:
            return self.post_parse(self._uris['events'], {}, json.dumps(event))
        else:
            raise Cisco_Api.EVENT_ERR

    def get_domains(self):
        return self.get_parse(self._uris['domains'], {})

    def delete_domains_by_name(self, name):
        return self.delete_parse(self._uris['domains'], {"where[name]": name})

    def delete_domains_by_id(self, id):
        return self.delete_parse(self._uris['domains'] + "/" + str(id), {})
