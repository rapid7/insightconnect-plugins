import komand
from .schema import LookupInput, LookupOutput, Input, Component, Output
from komand.exceptions import PluginException

import requests


class Lookup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='lookup',
                description=Component.DESCRIPTION,
                input=LookupInput(),
                output=LookupOutput())

    @staticmethod
    def _check_threat_type(threat_types: [str], params: dict, threat_type: str, name: str) -> None:
        if params.get(threat_type):
            threat_types.append(name)

    @staticmethod
    def _build_threat_types(params: dict) -> [str]:
        threat_types = []
        Lookup._check_threat_type(threat_types, params, Input.THREAT_TYPE_MALWARE, "MALWARE")
        Lookup._check_threat_type(threat_types, params, Input.THREAT_TYPE_UNWANTED, "UNWANTED_SOFTWARE")
        Lookup._check_threat_type(threat_types, params, Input.THREAT_TYPE_SOCIAL, "SOCIAL_ENGINEERING")
        return threat_types

    def run(self, params={}):
        endpoint = f"{self.connection.base}uris:search"
        parameters = {
            "key": self.connection.key,
            "threatTypes": Lookup.build_threat_types(params),
            "uri": params.get(Input.URL)
        }
        result = requests.get(endpoint, params=parameters)
        if result.status_code != 200:
            raise PluginException(result.json()["error"]["message"])

        obj = result.json().get("threat")
        if obj is not None:  # threat detected
            return {Output.THREATTYPES: obj["threatTypes"], Output.EXPIRETIME: obj["expireTime"]}
        else:  # no threat detected
            return {}
