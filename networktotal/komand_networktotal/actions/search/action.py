import komand
from .schema import SearchInput, SearchOutput
# Custom imports below
import requests


class Search(komand.Action):

    __PRELIMINARY_SEARCH_URL = "https://networktotal.com/search.php?q={md5}&json=1"

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search',
                description='Search based on MD5 hash',
                input=SearchInput(),
                output=SearchOutput())

    def run(self, params={}):
        md5 = params.get("md5")

        search_url = self.create_search_url(md5=md5)
        results = self.search(url=search_url)
        signatures = results["events"]

        return {"signatures": signatures}

    def create_search_url(self, md5):
        """Uses regex to capture components from response text to create appropriate search URL."""
        search_url = self.__PRELIMINARY_SEARCH_URL.format(md5=md5)
        return search_url

    def search(self, url):
        """Performs a search against NetworkTotal and returns the JSON response."""
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(self.__REQ_FAIL_TEXT)


def test(self):
    """TODO: Test action"""
    return {}
