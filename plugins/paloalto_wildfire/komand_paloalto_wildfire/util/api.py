import pyldfire
import requests
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from insightconnect_plugin_runtime.exceptions import PluginException


class PaloAltoWildfireAPI:
    def __init__(self, host: str, api_key: str, proxy: str, verify: bool) -> None:
        self.host = host
        self.api_key = api_key
        self.verify = verify
        if proxy:
            self.proxy = proxy
        else:
            self.proxy = {}
        self.pyldfireClient = pyldfire.WildFire(self.api_key, host=self.host, verify=verify, proxies=self.proxy)

    def test_connection(self):
        try:
            self.pyldfireClient.submit_urls("insight.rapid7.com")
        except pyldfire.WildFireException as e:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY, data=e)

    def get_malware_test_file(self) -> bytes:
        return self.pyldfireClient.get_malware_test_file()

    def get_pcap(self, analysed_hash: str, platform: int) -> bytes:
        return self.pyldfireClient.get_pcap(analysed_hash, platform)

    def get_report(self, analysed_hash: str, report_format: str):
        data = {
            "apikey": (None, self.api_key),
            "hash": (None, analysed_hash),
            "format": (None, report_format),
        }
        return self.__send_request("POST", f"https://{self.host}/publicapi/get/report", data)

    def get_sample(self, analysed_hash: str) -> bytes:
        return self.pyldfireClient.get_sample(analysed_hash)

    def get_verdicts(self, analysed_hash):
        return self.pyldfireClient.get_verdicts(analysed_hash)

    def submit_file(self, _file: bytes, filename: str) -> dict:
        out = {}
        try:
            if filename:
                out = self.pyldfireClient.submit_file(_file, filename)
            else:
                out = self.pyldfireClient.submit_file(_file)
            out["supported_file_type"] = True
        except pyldfire.WildFireException as e:
            if e.args and "Unsupport File type" in e.args[0]:  # Yes, that's the error, not a typo
                out["supported_file_type"] = False
            else:
                raise PluginException(PluginException.Preset.UNKNOWN) from e
        return out

    def submit_file_from_url(self, url: str) -> bytes:
        data = {
            "apikey": (None, self.api_key),
            "url": (None, url),
        }
        return self.__send_request("POST", f"https://{self.host}/publicapi/submit/url", data)

    def submit_url(self, url: str) -> bytes:
        data = {
            "apikey": (None, self.api_key),
            "link": (None, url),
        }
        return self.__send_request("POST", f"https://{self.host}/publicapi/submit/link", data)

    def get_file_from_url(self, url: str) -> bytes:
        return self.__send_request(method="GET", url=url)

    def __send_request(self, method: str, url: str, files: dict = None) -> bytes:
        try:
            response = requests.request(method=method.upper(), url=url, files=files)

            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
            elif response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
            elif 400 <= response.status_code < 500:
                raise PluginException(
                    preset=PluginException.Preset.UNKNOWN,
                    data=response.text,
                )
            elif response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)

            elif 200 <= response.status_code < 300:
                return response.content

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
