import insightconnect_plugin_runtime
from .schema import UrlExtractorInput, UrlExtractorOutput, Input, Output, Component

# Custom imports below
from icon_extractit.util.util import Regex
from icon_extractit.util.extractor import extract, clear_urls


class UrlExtractor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="url_extractor",
            description=Component.DESCRIPTION,
            input=UrlExtractorInput(),
            output=UrlExtractorOutput(),
        )

    def run(self, params={}):
        clear_urls = extract(Regex.URL, params.get(Input.STR), params.get(Input.FILE), params.get(Input.KEEP_ORIGINAL_URLS))
        clear_urls = self.balance_parentheses(clear_urls)

        return {
            Output.URLS: clear_urls
        }

    def balance_parentheses(self, clear_urls):
        check = []
        for url in clear_urls:
            for i in range(len(url)):
                if url[i] in ('(', '[', '{'):
                    check.append(i)
                elif url[i] in (')', ']', '{'):
                    if len(check) != 0:
                        check.pop()
                    else:
                        new_url = url[:i] + url[i+1:]
                        clear_urls = list(map(lambda x: x.replace(url, new_url), clear_urls))
            if len(check) != 0:
                for i in check:
                    new_url = url[:i] + url[i+1:]
                    clear_urls = list(map(lambda x: x.replace(url, new_url), clear_urls))
            check.clear()
        return clear_urls
