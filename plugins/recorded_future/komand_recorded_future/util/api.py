from io import BytesIO

from insightconnect_plugin_runtime.exceptions import PluginException
from json import JSONDecodeError
import requests
import xmltodict
import xml.etree.ElementTree as ET

class RecordedFutureApi:
    def __init__(self, logger, meta, token: str):
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

    # Convert XML to dictionary
    def elem_to_dict(self, elem):
        if elem.tag.startswith("{"):
            ns, tag = elem.tag[1:].split("}")
            full_tag = f"{ns}:{tag}"
        else:
            full_tag = elem.tag

        d = {}
        for k, v in elem.attrib.items():
            d[f"@{k}"] = v
        if elem.text and elem.text.strip():
            d["$"] = elem.text.strip()
        for child in elem:
            tag_dict = self.elem_to_dict(child)
            tag_key = tag_dict.pop("$tag")
            if tag_key in d:
                if not isinstance(d[tag_key], list):
                    d[tag_key] = [d[tag_key]]
                d[tag_key].append(tag_dict)
            else:
                d[tag_key] = tag_dict
        d["$tag"] = full_tag
        return d

    def _call_api(self, method: str, endpoint: str, params: dict = None, data: dict = None, json: dict = None):
        _url = self.base_url + endpoint

        response = requests.request(url=_url, method=method, params=params, data=data, json=json, headers=self.headers)
        if response.status_code == 401:
            raise PluginException(preset=PluginException.Preset.API_KEY)
        if response.status_code == 403:
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
        if response.status_code == 404:
            raise PluginException(
                cause="No results found.\n",
                assistance="Please provide valid inputs or verify the endpoint/URL/hostname configured in your plugin.\n",
                data=f"{response.text}\nurl: {_url}",
            )
        if 400 <= response.status_code < 500:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        if response.status_code >= 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)
        if endpoint.endswith("risklist"):
            root = ET.fromstring(response.text)
            dict = self.elem_to_dict(root)
            return dict
        try:
            return response.json()
        except JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)

    def make_request(self, endpoint: str, params: dict = None) -> dict:
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
