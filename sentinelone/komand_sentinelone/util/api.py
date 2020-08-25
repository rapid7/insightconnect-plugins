from json import dumps, loads
from re import match

import requests


class SentineloneAPI:
    def __init__(self, url, make_token_header):
        self.url = url
        self.token_header = make_token_header

    def search_agents(self, agent_details: str, agent_active, results_length: int = 0) -> list:
        results = []
        if agent_details:
            for search in self.__get_searches(agent_details):
                endpoint = f"{self.url}web/api/v2.0/agents?{search}={agent_details}"
                output = requests.get(endpoint, headers=self.token_header)

                if output.status_code is 200 and output.json()["pagination"]["totalItems"] >= 1:
                    results.append(output.json()['data'][0])
                    if results_length:
                        if len(results) >= results_length:
                            break

        else:
            output = requests.get(f"{self.url}web/api/v2.0/agents?isActive={agent_active}", headers=self.token_header)
            results.extend(output.json()['data'])
        return loads(dumps(results).replace('null', '"None"'))

    @staticmethod
    def __get_searches(agent_details: str) -> list:
        if len(agent_details) == 18 and agent_details.isdigit():
            return ["ids"]
        if match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", agent_details):
            return ["networkInterfaceInet__contains", "externalIp__contains"]
        if match(r"((?:(\d{1,2}|[a-fA-F]{1,2}){2})(?::|-*)){6}", agent_details):
            return ["networkInterfacePhysical__contains", "uuid"]
        else:
            return ["computerName"]
