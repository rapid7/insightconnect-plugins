from typing import Optional
from logging import Logger

from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from komand_elasticsearch.util.api import RequestAPI
from komand_elasticsearch.util.api import ElasticSearchAPI
from komand_elasticsearch.util.api6 import ElasticSearchAPI6
from requests.exceptions import HTTPError, SSLError


class APIFactory:
    def __init__(self, url: str, logger: Logger, ssl_verify: bool, username: str = None, password: str = None):
        self.url: str = url.rstrip("/")
        self.username: str = username
        self.password: str = password
        self.ssl_verify: bool = ssl_verify
        self.logger: Logger = logger

    def get_api(self) -> RequestAPI:
        url: str = self.url
        urls: [] = [self.url]
        if "://" not in self.url:
            urls = [f"https://{self.url}", f"http://{self.url}"]

        error: Optional[Exception] = None
        number: Optional[str] = "7"
        for url in urls:
            try:
                api = RequestAPI(url, self.logger, self.ssl_verify, self.username, self.password)
                number = api.get_main_version()
                break
            except (SSLError, HTTPError, PluginException) as e:
                number = None
                error = e
                continue

        if isinstance(error, PluginException):
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)

        if not number:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNKNOWN)

        if number == "7":
            return ElasticSearchAPI(url, self.logger, self.ssl_verify, self.username, self.password)
        else:
            return ElasticSearchAPI6(url, self.logger, self.ssl_verify, self.username, self.password)
