import insightconnect_plugin_runtime
from .schema import SearchInput, SearchOutput, Input, Component, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import requests
import json
import validators


def format_query(query: str, input_type: str) -> str:
    """
    A function to handle properly format the query after
    determining the input type

    :param query: Query to be formatted
    :type query: str
    :param input_type: URL/Domain/Custom
    :type input_type: str

    :return search_query: Formatted query used in URL scanning
    :rtype: str
    """

    # If input_type is Custom
    if input_type == "Custom":
        search_query = query

    # If input_type is URL, determine if the query is a valid URL,
    # then append page.url: to the query
    elif input_type == "URL":
        if not validators.url(query):
            raise PluginException(
                cause="URL entered as input type, but not provided in query.",
                assistance="Please check URL and try again.",
            )
        search_query = f'page.url: "{query}"'

    # If input_type is domain, check if it is a valid domain,
    # then append page.domain: to the query
    else:
        if not validators.domain(query):
            raise PluginException(
                cause="Domain entered as input type, but not provided in query.",
                assistance="Please check domain address and try again.",
            )
        search_query = f'page.domain:"{query}"'

    return search_query


def get_response(url: str, headers: dict) -> requests.models.Response:
    """
    This method runs a GET request and returns a response.
    It also handles all exceptions, and specifically handles 400s
    to prevent the plugin from returning a successful but empty
    response.
    :param url: Input URL for the request
    :param headers:
    :return response: The full HTTP response
    """
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as error:
        status_code = error.response.status_code
        if status_code == 400:
            raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.text)
    except Exception as error:
        raise PluginException(cause="Something went wrong during the request.", assistance=error)

    return response


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

        search_query = format_query(query=query, input_type=input_type)

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
            headers = self.connection.headers
            search_query = format_query(query=query, input_type=input_type)

            response = get_response(url=url, headers=headers)

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
