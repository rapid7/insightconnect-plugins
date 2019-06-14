import komand
from .schema import SearchInput, SearchOutput
# Custom imports below
from komand.exceptions import PluginException
import requests


class Search(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='search',
                description='Search urlscan.io',
                input=SearchInput(),
                output=SearchOutput())

    def run(self, params={}):
        """TODO: Run action"""
        server = self.connection.server
        url = server + '/search/?q={query}&size={size}&offset={offset}&sort={sort}'.format(
            query=params.get('q'),
            size=str(params.get('size', 100)),
            offset=str(params.get('offset', 0)),
            sort=params.get('sort', '_score')
        )
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
                                  assistance="(non-JSON or no response was received). Response was: %s" % response.text)

        return out
