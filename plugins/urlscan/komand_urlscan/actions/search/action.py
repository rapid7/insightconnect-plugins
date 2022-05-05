import insightconnect_plugin_runtime
from .schema import SearchInput, SearchOutput, Input, Component, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import requests
import json
import validators


class Search(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search",
            description=Component.DESCRIPTION,
            input=SearchInput(),
            output=SearchOutput(),
        )

    def run(self, params={}):
        input_type = params.get(Input.INPUT_TYPE, "Custom")
        query = params.get(Input.Q)
        sort = params.get(Input.SORT, "_score")
        if input_type == "Custom":
            search_query = query
        elif input_type == "URL":
            if not validators.url(query):
                raise PluginException(
                    cause="URL entered as input type, but not provided in query.",
                    assistance="Please check URL and try again.",
                )
            search_query = f'page.url: "{query}"'
        else:
            if not validators.domain(query):
                raise PluginException(
                    cause="Domain entered as input type, but not provided in query.",
                    assistance="Please check domain address and try again.",
                )
            search_query = f'page.domain:"{query}"'

        search_after = None
        results = []
        size = 10000
        has_more = True
        while has_more:
            query_params = [
                f"q={search_query}",
                f"size={size}",
                f"sort={sort}",
            ]
            if search_after:
                query_params.append(f"search_after={search_after}")

            url = f'{self.connection.server}/search/?{"&".join(query_params)}'
            self.logger.info(url)

            try:
                response = requests.get(url, headers=self.connection.headers)
            except Exception as e:
                raise PluginException(cause="Something went wrong during the request.", assistance=e)

            try:
                responses = response.json()
                response_results = responses.get("results", [])
                if not response_results or not isinstance(response_results, list):
                    break

                results.extend(response_results)
                has_more = responses.get("has_more", False)
                if not has_more:
                    break

                if "sort" in response_results[-1] and len(response_results[-1]["sort"]) == 2:
                    returned_sort = response_results[-1]["sort"]
                    search_after = f"{returned_sort[0]},{returned_sort[1]}"
                else:
                    break

            except json.decoder.JSONDecodeError:
                raise PluginException(
                    cause="Received an unexpected response from the Urlscan API. ",
                    assistance=f"(non-JSON or no response was received). Response was: {response.text}",
                )

        return {Output.RESULTS: results, Output.TOTAL: len(results), Output.HAS_MORE: has_more}
