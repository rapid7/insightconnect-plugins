import gzip
import os
from typing import Dict, Tuple, Any
from insightconnect_plugin_runtime.exceptions import PluginException
from json import JSONDecodeError
import requests
from requests import Response
import xmltodict
from binascii import Error as B64EncodingError
import base64
from tempfile import NamedTemporaryFile
from timeout_decorator import timeout, TimeoutError as DecoratorTimeoutError

TIMEOUT_SECONDS = 60 * 5


class RecordedFutureApi:
    def __init__(self, logger, meta, token: str) -> None:
        self.base_url = "https://api.recordedfuture.com/v2/"
        self.token = token
        self.logger = logger
        self.meta = meta
        self.app_version = self.setup_custom_header()
        self.app_name = "rapid7_insightconnect"
        self.headers = {
            "User-Agent": f"{self.app_name}/{self.app_version}",
            "X-RFToken": self.token,
        }

    def setup_custom_header(self):
        try:  # This may not be defined in local komand instances.
            version = self.meta.version
        except AttributeError:
            version = "test-version"
        self.logger.info(f"Plugin Version: {version}")
        return version

    @staticmethod
    def response_handler(response: Response, url: str) -> None:
        """
        Raise the correct PluginException based upon the response status code
        :param response: The response object to be reviewed
        :param url: The endpoint URL to be logged out in result of an error
        :return: None
        """
        if response.status_code == 401:
            raise PluginException(preset=PluginException.Preset.API_KEY)
        if response.status_code == 403:
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
        if response.status_code == 404:
            raise PluginException(
                cause="No results found.\n",
                assistance="Please provide valid inputs or verify the endpoint/URL/hostname configured in your plugin.\n",
                data=f"{response.text}\nurl: {url}",
            )
        if 400 <= response.status_code < 500:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        if response.status_code >= 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)

    @staticmethod
    def decompress_gzip_to_dict(compressed_data: bytes) -> Dict:
        """
        Decompresses and parses a Gzip file in bytes containing XML, returning a JSON representation
        :param compressed_data: The compressed data bytestring
        :return: A JSON representation of the XML file
        """
        decompressed_data = gzip.decompress(compressed_data)
        return dict(xmltodict.parse(decompressed_data))

    def decompress_and_process_gzip(self, filename: str) -> Tuple[Any, Any]:
        """
        Retrieves, decompresses and parses a Gzip file containing XML, returning the compressed file and a JSON
        representation of its contents
        :param filename: filename of the compressed gzip
        :return: The decoded gzip contents in Base64 and the decompressed JSON representation of the XML file
        """
        try:
            with gzip.open(filename, "rb") as file:
                compressed_data = file.read()
                try:
                    # Apply timeout decorator at call time to avoid pickle issues in unittests
                    timed_decompress = timeout(seconds=TIMEOUT_SECONDS, use_signals=False)(
                        RecordedFutureApi.decompress_gzip_to_dict
                    )
                    parsed_data = timed_decompress(compressed_data)
                except (MemoryError, DecoratorTimeoutError):
                    file_size_bytes = os.path.getsize(filename)
                    file_size_mb = file_size_bytes / (1024 * 1024)
                    self.logger.info(f"File size: {round(file_size_mb, 2)}mb is too large to parse.")
                    self.logger.info("Please see troubleshooting for more information. Returning gzip only...")
                    parsed_data = None
                decoded_data = base64.b64encode(compressed_data).decode("utf-8")
                return decoded_data, parsed_data
        except (gzip.BadGzipFile, IOError) as exception:
            raise PluginException(
                cause="Error reading saved gzip response file",
                assistance="File may contain errors or be in an unexpected format",
                data=exception,
            )
        except (B64EncodingError, UnicodeDecodeError):
            raise PluginException(preset=PluginException.Preset.BASE64_DECODE)

    def _call_api_stream_to_file(
        self, method: str, endpoint: str, params: dict = None, data: dict = None, json: dict = None
    ) -> Tuple[Any, Any]:
        _url = self.base_url + endpoint
        response = requests.request(
            url=_url, method=method, params=params, data=data, json=json, headers=self.headers, stream=True
        )
        RecordedFutureApi.response_handler(response, _url)
        try:
            with NamedTemporaryFile(delete=False) as file:
                temp_filename = file.name
                for chunk in response.iter_content(chunk_size=8192):
                    compressed_chunk = gzip.compress(chunk)
                    file.write(compressed_chunk)
                    # flush increases performance overhead but reduces risk of memory error
                    file.flush()
            return self.decompress_and_process_gzip(temp_filename)
        except IOError as exception:
            raise PluginException(
                cause="Error writing response content to file",
                assistance="File may contain errors or the disk may be full",
                data=exception,
            )
        except MemoryError as exception:
            raise PluginException(
                cause="Memory Error writing response content to file",
                assistance="Insufficient memory to process response content",
                data=exception,
            )
        except ValueError as exception:
            raise PluginException(
                cause="Error processing response content when writing to file",
                assistance="Response content may contain invalid data",
                data=exception,
            )
        finally:
            # Finally block removes any temporary files
            if os.path.exists(temp_filename):
                os.remove(temp_filename)

    def _call_api(self, method: str, endpoint: str, params: dict = None, data: dict = None, json: dict = None):
        _url = self.base_url + endpoint
        response = requests.request(url=_url, method=method, params=params, data=data, json=json, headers=self.headers)
        RecordedFutureApi.response_handler(response, _url)
        try:
            return response.json()
        except JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)

    def make_request(self, endpoint: str, params: dict = None) -> dict:
        # risklist endpoints may return large GZIP files as content, to reduce the risk of Memory Errors
        # this content should be streamed directly to file
        if endpoint.endswith("risklist"):
            return self._call_api_stream_to_file("GET", endpoint, params)
        else:
            return self._call_api("GET", endpoint, params)


class Endpoint:
    @staticmethod
    def download_domain_risk_list() -> str:
        return "domain/risklist"

    @staticmethod
    def download_hash_risk_list() -> str:
        return "hash/risklist"

    @staticmethod
    def download_ip_risk_list() -> str:
        return "ip/risklist"

    @staticmethod
    def download_url_risk_list() -> str:
        return "url/risklist"

    @staticmethod
    def download_vulnerability_risk_list() -> str:
        return "vulnerability/risklist"

    @staticmethod
    def list_domain_risk_rules() -> str:
        return "domain/riskrules"

    @staticmethod
    def list_hash_risk_rules() -> str:
        return "hash/riskrules"

    @staticmethod
    def list_ip_risk_rules() -> str:
        return "ip/riskrules"

    @staticmethod
    def list_url_risk_rules() -> str:
        return "url/riskrules"

    @staticmethod
    def list_vulnerability_risk_rules() -> str:
        return "vulnerability/riskrules"

    @staticmethod
    def lookup_alert(alert_id: str) -> str:
        return f"alert/{alert_id}"

    @staticmethod
    def lookup_domain(domain: str) -> str:
        return f"domain/{domain}"

    @staticmethod
    def lookup_entity_list(entity_list_id: str) -> str:
        return f"entitylist/{entity_list_id}"

    @staticmethod
    def lookup_hash(hash_id: str) -> str:
        return f"hash/{hash_id}"

    @staticmethod
    def lookup_ip_address(ip_address: str) -> str:
        return f"ip/{ip_address}"

    @staticmethod
    def lookup_malware(malware_id: str) -> str:
        return f"malware/{malware_id}"

    @staticmethod
    def lookup_url(url: str) -> str:
        return f"url/{url}"

    @staticmethod
    def lookup_vulnerability(vulnerability_id: str) -> str:
        return f"vulnerability/{vulnerability_id}"

    @staticmethod
    def search_alerts() -> str:
        return "alert/search"

    @staticmethod
    def search_domains() -> str:
        return "domain/search"

    @staticmethod
    def search_entity_lists() -> str:
        return "entitylist/search"

    @staticmethod
    def search_hashes() -> str:
        return "hash/search"

    @staticmethod
    def search_ip_addresses() -> str:
        return "ip/search"

    @staticmethod
    def search_malware() -> str:
        return "malware/search"

    @staticmethod
    def search_urls() -> str:
        return "url/search"

    @staticmethod
    def search_vulnerabilities() -> str:
        return "vulnerability/search"
