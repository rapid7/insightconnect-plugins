import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import SearchInput, SearchOutput, Input

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
        if params.get(Input.STOP) <= 0 or params.get(Input.NUM) <= 0 or params.get(Input.PAUSE) <= 0:
            raise PluginException(
                cause="One or more inputs were of an invalid value",
                assistance="Please check that 'Num', 'Pause', and 'Stop' are values greater than 0",
                data=f"Num: {params.get(Input.NUM)}, Pause: {params.get(Input.PAUSE)}, Stop: {params.get(Input.STOP)}"
            )
        count = 0
        stop = params.get(Input.STOP, 10)
        for url in googlesearch.search(
            query=params.get(Input.QUERY),
            lang=params.get(Input.LANG, "en"),
            stop=stop,
            num=params.get(Input.NUM, 10),
            pause=params.get(Input.PAUSE, 1.0),
        ):

            urls.append(url)
            count += 1
            self.logger.info("Iteration: %s (%s)", count, url)

            if count == stop:
                break

        return {"urls": urls}

    def test(self):
        return {"urls": ["https://google.com", "https://www.google.com"]}
