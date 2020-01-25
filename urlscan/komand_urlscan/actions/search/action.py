import komand
from .schema import SearchInput, SearchOutput, Input, Component
# Custom imports below
from komand.exceptions import PluginException
import requests
import json


class Search(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='search',
                description=Component.DESCRIPTION,
                input=SearchInput(),
                output=SearchOutput())

    def run(self, params={}):
        url = f'{self.connection.server}/search/?q={params.get(Input.Q)}&size={str(params.get(Input.SIZE, 100))}&offset={str(params.get(Input.OFFSET, 0))}&sort={params.get(Input.SORT, "_score")}'
        self.logger.info(url)

        try:
            response = requests.get(url, headers=self.connection.headers)
        except Exception as e:
            raise PluginException(cause="Something went wrong during the request. ",
                                  assistance=e)

        try:
            out = response.json()
        except json.decoder.JSONDecodeError:
            raise PluginException(cause="Received an unexpected response from the Urlscan API. ",
                                  assistance=f"(non-JSON or no response was received). Response was: {response.text}")

        return out

    def test(self):
        # TODO: Implement test function
        return {}
