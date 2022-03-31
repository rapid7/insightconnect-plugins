import insightconnect_plugin_runtime
from .schema import SearchInput, SearchOutput

# Custom imports below
import googlesearch


class Search(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search",
            description="Return URLs from a Google search",
            input=SearchInput(),
            output=SearchOutput(),
        )

    def run(self, params={}):
        urls = []

        self.logger.info("Parameters: %s", params)
        count = 0
        stop = params.get("stop", 10)
        for url in googlesearch.search(
            query=params.get("query"),
            lang=params.get("lang", "en"),
            stop=stop,
            num=params.get("num", 10),
            pause=params.get("pause", 1.0),
        ):

            urls.append(url)
            count += 1
            self.logger.info("Iteration: %s (%s)", count, url)

            if count == stop:
                break

        return {"urls": urls}

    def test(self):
        return {"urls": ["https://google.com", "https://www.google.com"]}
