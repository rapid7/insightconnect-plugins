import insightconnect_plugin_runtime
from typing import List, Dict

from .schema import LookupInput, LookupOutput, Input, Component, Output
from insightconnect_plugin_runtime.exceptions import PluginException

import requests


class Lookup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="lookup",
            description=Component.DESCRIPTION,
            input=LookupInput(),
            output=LookupOutput(),
        )

    def _check_threat_type(self, threat_types: List[str], params: Dict[str, str], threat_type: str, name: str) -> None:
        if params.get(threat_type):
            threat_types.append(name)

    def _build_threat_types(self, params: Dict[str, str]) -> List[str]:
        threat_types = []
        self._check_threat_type(threat_types, params, Input.THREAT_TYPE_MALWARE, "MALWARE")
        self._check_threat_type(threat_types, params, Input.THREAT_TYPE_UNWANTED, "UNWANTED_SOFTWARE")
        self._check_threat_type(threat_types, params, Input.THREAT_TYPE_SOCIAL, "SOCIAL_ENGINEERING")
        return threat_types

    def run(self, params={}) -> Dict[str, str]:
        endpoint = f"{self.connection.base}uris:search"
        parameters = {
            "key": self.connection.key,
            "threatTypes": self._build_threat_types(params),
            "uri": params.get(Input.URL),
        }
        result = requests.get(endpoint, params=parameters)
        if result.status_code != 200:
            raise PluginException(result.json()["error"]["message"])

        obj = result.json().get("threat")
        if obj is not None:  # threat detected
            return {Output.THREATTYPES: obj["threatTypes"], Output.EXPIRETIME: obj["expireTime"]}
        else:  # no threat detected
            return {}
