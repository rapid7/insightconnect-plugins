import komand
from .schema import SearchInput, SearchOutput, Input, Component

# Custom imports below
from komand.exceptions import PluginException
import requests
import json
import validators


class Search(komand.Action):
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

        query_params = [
            f"q={search_query}",
            f"size={str(params.get(Input.SIZE, 100))}",
            f"offset={str(params.get(Input.OFFSET, 0))}",
            f'sort={params.get(Input.SORT, "_score")}',
        ]

        url = f'{self.connection.server}/search/?{"&".join(query_params)}'
        self.logger.info(url)

        try:
            response = requests.get(url, headers=self.connection.headers)
        except Exception as e:
            raise PluginException(cause="Something went wrong during the request. ", assistance=e)

        try:
            output = response.json()
        except json.decoder.JSONDecodeError:
            raise PluginException(
                cause="Received an unexpected response from the Urlscan API. ",
                assistance=f"(non-JSON or no response was received). Response was: {response.text}",
            )

        return output
