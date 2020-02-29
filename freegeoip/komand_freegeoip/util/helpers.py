import requests


class Ipstack:
    def __init__(self, access_token):
        self.access_token = access_token

    def get_hosts_information(self, hosts, language, should_return_hostname, should_use_security):
        query_parameters = '&'.join(self._get_query_parameters(language, should_return_hostname, should_use_security))
        r = requests.get(f"http://api.ipstack.com/{','.join(hosts)}?{query_parameters}")
        return r.json()

    def lookup(self, language, should_return_hostname, should_use_security):
        query_parameters = '&'.join(self._get_query_parameters(language, should_return_hostname, should_use_security))
        r = requests.get(f"http://api.ipstack.com/check?{query_parameters}")
        return r.json()

    def _get_query_parameters(self, language, should_return_hostname, should_use_security):
        return (
            f"language={language}",
            f"hostname={1 if should_return_hostname else 0}",
            f"security={1 if should_use_security else 0}",
            f"access_key={self.access_token}",
            f"format=1"
        )
