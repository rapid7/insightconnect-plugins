import ipaddress

import requests
from insightconnect_plugin_runtime.exceptions import PluginException

API_URL = "https://api.vpndetection.io/"
TIMEOUT = 10
USER_AGENT = "rapid7-insightconnect-vpndetection/1.0.0"

DETECTIONS = ("vpn", "relay", "tor", "hosting", "cdn", "resproxy", "dcproxy", "mobproxy", "pubproxy")
# Without a key, once a free key's trial is spent, or past the organization's overage cap, the API leaves
# these flags out or null: that must not read as a clean address.
KEYED_FLAGS = (
    "is_hosting",
    "is_cdn",
    "is_resproxy",
    "is_dcproxy",
    "is_mobproxy",
    "is_pubproxy",
    "is_carrier",
    "is_satellite",
    "is_ssh",
    "is_smtp",
    "is_web",
    "is_dns_resolver",
    "is_bittorrent",
)
KEYLESS_FLAGS = ("is_bogon", "is_vpn", "is_relay", "is_tor", "is_anycast")
DETECTION_FIELDS = ("provider", "provider_name", "confidence", "last_seen")
LOCATION_FIELDS = (
    "continent",
    "continent_name",
    "country",
    "country_name",
    "region",
    "region_code",
    "city",
    "postal_code",
    "latitude",
    "longitude",
    "accuracy_radius",
    "timezone",
)
ASN_FIELDS = ("asn", "name", "domain", "type", "prefix", "country", "rpki_status")
COMPANY_FIELDS = ("name", "domain", "type", "country")
ABUSE_FIELDS = ("email", "name", "phone", "address", "country", "network")


class VPNDetectionAPI:
    def __init__(self, api_key: str, logger):
        self.api_key = (api_key or "").strip()
        self.logger = logger

    def lookup(self, address: str) -> dict:
        try:
            address = str(ipaddress.ip_address(str(address).strip()))
        except ValueError:
            raise PluginException(
                cause=f"'{address}' is not a valid IP address.",
                assistance="Provide an IPv4 or IPv6 address, such as 185.220.101.1.",
            )
        headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
        if self.api_key:
            # The key goes in a header, never in the URL, where it would end up in logs.
            headers["Authorization"] = f"Bearer {self.api_key}"
        try:
            response = requests.request("GET", API_URL + address, headers=headers, timeout=TIMEOUT)
        except requests.exceptions.Timeout as error:
            raise PluginException(preset=PluginException.Preset.TIMEOUT, data=error)
        except requests.exceptions.RequestException as error:
            raise PluginException(preset=PluginException.Preset.CONNECTION_ERROR, data=error)

        if response.status_code == 401:
            raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
        if response.status_code == 403:
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED, data=response.text)
        if response.status_code == 429:
            raise PluginException(preset=PluginException.Preset.RATE_LIMIT, data=response.text)
        if response.status_code == 400:
            raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.text)
        if response.status_code >= 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)
        if response.status_code != 200:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        try:
            data = response.json()
        except ValueError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)
        if not isinstance(data, dict):
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        return to_output(data)


def _value(value):
    """A field's value, or None when the API left it empty."""
    if value is None or value == "" or (isinstance(value, (dict, list)) and not value):
        return None
    return value


def _object(data: dict, key: str, fields: tuple) -> dict:
    source = data.get(key) if isinstance(data.get(key), dict) else {}
    return {field: source[field] for field in fields if _value(source.get(field)) is not None}


def to_output(data: dict) -> dict:
    """The action's output from an API answer: the flags it holds, and each object without its empty fields."""
    output = {"ip": data.get("ip", "")}
    for flag in KEYLESS_FLAGS:
        output[flag] = data.get(flag) is True
    for flag in KEYED_FLAGS:
        if isinstance(data.get(flag), bool):
            output[flag] = data[flag]
    output["partial"] = not output["is_bogon"] and any(not isinstance(data.get(flag), bool) for flag in KEYED_FLAGS)
    for detection in DETECTIONS:
        if data.get(f"is_{detection}") is True and (details := _object(data, detection, DETECTION_FIELDS)):
            output[detection] = details
    for key, fields in (
        ("location", LOCATION_FIELDS),
        ("company", COMPANY_FIELDS),
        ("abuse", ABUSE_FIELDS),
    ):
        if details := _object(data, key, fields):
            output[key] = details
    asn = _object(data, "asn", ASN_FIELDS)
    if asn.get("asn"):
        output["asn"] = asn
    if _value(data.get("hostname")) is not None:
        output["hostname"] = data["hostname"]
    return output
