from json import dumps, loads
from re import match

import requests


class SentineloneAPI:
    def __init__(self, url, make_token_header):
        self.url = url
        self.token_header = make_token_header

    def search_agents(self, agent_details: str, agent_active: bool = True, case_sensitive: bool = True, results_length: int = 0) -> list:
        results = []
        if agent_details:
            for search in self.__get_searches(agent_details):
                agents = [agent_details]

                # Normalize casing if specified
                if not case_sensitive:
                    if search == "computerName":
                        agents = [agent_details.lower(), agent_details.upper()]
                    if search == "uuid":
                        agents = [agent_details.lower()]

                for agent in agents:
                    endpoint = f"{self.url}web/api/v2.0/agents?{search}={agent}"
                    output = requests.get(endpoint, headers=self.token_header)

                    if output.status_code is 200 and output.json()["pagination"]["totalItems"] >= 1:
                        results.append(output.json()['data'][0])

                if results_length:
                    if len(results) >= results_length:
                        return self.clean_results(results)

        else:
            output = requests.get(f"{self.url}web/api/v2.0/agents?isActive={agent_active}", headers=self.token_header)
            results.extend(output.json()['data'])
        return self.clean_results(results)

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

    @staticmethod
    def clean_results(results):
        return loads(dumps(results).replace('null', '"None"'))
