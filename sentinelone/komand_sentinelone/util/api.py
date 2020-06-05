import requests
from json import dumps, loads
from re import match


class SentineloneAPI:
    def __init__(self, url, make_token_header):
        self.url = url
        self.token_header = make_token_header

    def search_agents(self,  agent_details: str, results_length: int = 0) -> list:
        results = []
        for search in self.__get_searches(agent_details):
            endpoint = f"{self.url}web/api/v2.0/agents?{search}={agent_details}"
            output = requests.get(endpoint, headers=self.token_header)

            if output.status_code is 200 and output.json()["pagination"]["totalItems"] >= 1:
                results.append(loads(dumps(output.json()['data'][0]).replace('null', '"None"')))
                if results_length:
                    if len(results) >= results_length:
                        return results

        return results

    @staticmethod
    def __get_searches(agent_details: str) -> list:
        if match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", agent_details):
            return ["networkInterfaceInet__contains", "externalIp__contains"]
        if match(r"((?:(\d{1,2}|[a-fA-F]{1,2}){2})(?::|-*)){6}", agent_details):
            return ["networkInterfacePhysical__contains", "uuid"]
        if len(agent_details) == 18 and agent_details.isdigit():
            return ["ids"]
        else:
            return ["computerName"]
