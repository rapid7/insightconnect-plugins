import insightconnect_plugin_runtime
from .schema import UrlExtractorInput, UrlExtractorOutput, Input, Output, Component

# Custom imports below
import base64
import html
import urllib.parse
from icon_extractit.util.util import Regex
from icon_extractit.util.extractor import (
    extract,
    clear_urls,
    remove_extracted_urls_from_links,
    extract_content_from_file,
)

DEFAULT_ENCODING = "utf-8"


class UrlExtractor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="url_extractor",
            description=Component.DESCRIPTION,
            input=UrlExtractorInput(),
            output=UrlExtractorOutput(),
        )

    def run(self, params={}):
        keep_original_urls = params.get(Input.KEEP_ORIGINAL_URLS)
        urls = clear_urls(
            remove_extracted_urls_from_links(
                extract(Regex.URL, params.get(Input.STR), params.get(Input.FILE), keep_original_urls)
            ),
            keep_original_urls,
        )

        input_str = self.get_input_string(params.get(Input.STR), params.get(Input.FILE), keep_original_urls)

        for i, url in enumerate(urls):
            if url[len(url) - 1] == ")":
                # URLs are unescaped unless kept original, so search the input in the same form
                searched_input = input_str if keep_original_urls else html.unescape(input_str)
                if searched_input[(searched_input.find(url) - 1)] == "(":
                    urls[i] = url[: len(url) - 1]

        return {Output.URLS: urls}

    def get_input_string(self, provided_string: str, provided_file: str, keep_original_url: bool = False):
        if provided_string:
            if keep_original_url:
                return provided_string
            else:
                provided_string = urllib.parse.unquote(provided_string)
                return provided_string
        elif provided_file:
            try:
                if keep_original_url:
                    provided_file = base64.b64decode(provided_file.encode(DEFAULT_ENCODING)).decode(DEFAULT_ENCODING)
                else:
                    provided_file = urllib.parse.unquote(
                        base64.b64decode(provided_file.encode(DEFAULT_ENCODING)).decode(DEFAULT_ENCODING)
                    )
                return provided_file
            except UnicodeDecodeError:
                file_content = extract_content_from_file(base64.b64decode(provided_file))
                return file_content
