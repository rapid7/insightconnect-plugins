import logging
from typing import Any, Dict, Optional

from icon_ipgeolocation_io.connection.connection import Connection

STUB_API_KEY = "0123456789abcdef0123456789abcdef"
UNAUTHORIZED_API_KEY = "unauthorized-key"

# Addresses used to steer the mock transport toward specific responses.
IP_SWEDEN = "91.128.103.196"
IP_MALICIOUS = "2.56.188.34"
IP_CLEAN = "2.56.188.35"
IP_ABUSE = "1.0.0.0"
IP_HETZNER = "49.12.0.0"
IP_UNKNOWN = "5.5.5.5"
IP_BOGON = "10.0.0.0"
IP_SERVER_ERROR = "9.9.9.9"
IP_RATE_LIMITED = "9.9.9.10"
IP_MALFORMED_BODY = "9.9.9.11"
DOMAIN = "ipgeolocation.io"

LOCATION_SWEDEN = {
    "continent_code": "EU",
    "continent_name": "Europe",
    "country_code2": "SE",
    "country_code3": "SWE",
    "country_name": "Sweden",
    "country_name_official": "Kingdom of Sweden",
    "country_capital": "Stockholm",
    "state_prov": "Stockholms län",
    "state_code": "SE-AB",
    "district": "Stockholm",
    "city": "Stockholm",
    "locality": "Stockholm",
    "accuracy_radius": "9.148",
    "confidence": "high",
    "dma_code": "",
    "zipcode": "164 40",
    "latitude": "59.40510",
    "longitude": "17.95510",
    "is_eu": True,
    "country_flag": "https://ipgeolocation.io/static/flags/se_64.png",
    "geoname_id": "9972319",
    "country_emoji": "\U0001f1f8\U0001f1ea",
}

TIME_ZONE_STOCKHOLM = {
    "name": "Europe/Stockholm",
    "offset": 1,
    "offset_with_dst": 1,
    "current_time": "2026-03-07 10:37:38.987+0100",
    "current_time_unix": 1772876258.987,
    "current_tz_abbreviation": "CET",
    "current_tz_full_name": "Central European Standard Time",
    "standard_tz_abbreviation": "CET",
    "standard_tz_full_name": "Central European Standard Time",
    "is_dst": False,
    "dst_savings": 0,
    "dst_exists": True,
    "dst_tz_abbreviation": "CEST",
    "dst_tz_full_name": "Central European Summer Time",
    "dst_start": {
        "utc_time": "2026-03-29 TIME 01:00",
        "duration": "+1.00H",
        "gap": True,
        "date_time_after": "2026-03-29 TIME 03:00",
        "date_time_before": "2026-03-29 TIME 02:00",
        "overlap": False,
    },
    "dst_end": {
        "utc_time": "2026-10-25 TIME 01:00",
        "duration": "-1.00H",
        "gap": False,
        "date_time_after": "2026-10-25 TIME 02:00",
        "date_time_before": "2026-10-25 TIME 03:00",
        "overlap": True,
    },
}

SECURITY_CLEAN = {
    "threat_score": 0,
    "is_tor": False,
    "is_proxy": False,
    "proxy_provider_names": [],
    "proxy_confidence_score": 0,
    "proxy_last_seen": "",
    "is_residential_proxy": False,
    "is_vpn": False,
    "vpn_provider_names": [],
    "vpn_confidence_score": 0,
    "vpn_last_seen": "",
    "is_relay": False,
    "relay_provider_name": "",
    "is_anonymous": False,
    "is_known_attacker": False,
    "is_bot": False,
    "is_spam": False,
    "is_cloud_provider": False,
    "cloud_provider_name": "",
}

SECURITY_MALICIOUS = {
    "threat_score": 80,
    "is_tor": False,
    "is_proxy": True,
    "proxy_provider_names": ["Zyte Proxy"],
    "proxy_confidence_score": 80,
    "proxy_last_seen": "2025-12-12",
    "is_residential_proxy": True,
    "is_vpn": True,
    "vpn_provider_names": ["Nord VPN"],
    "vpn_confidence_score": 80,
    "vpn_last_seen": "2026-01-19",
    "is_relay": False,
    "relay_provider_name": "",
    "is_anonymous": True,
    "is_known_attacker": True,
    "is_bot": False,
    "is_spam": False,
    "is_cloud_provider": True,
    "cloud_provider_name": "Packethub S.A.",
}

ABUSE_APNIC = {
    "route": "1.0.0.0/24",
    "country": "AU",
    "name": "IRT-APNICRANDNET-AU",
    "organization": "",
    "kind": "group",
    "address": "PO Box 3646\nSouth Brisbane, QLD 4101\nAustralia",
    "emails": ["helpdesk@apnic.net"],
    "phone_numbers": ["+61 7 3858 3100"],
}

IPGEO_SWEDEN = {
    "ip": IP_SWEDEN,
    "hostname": IP_SWEDEN,
    "location": LOCATION_SWEDEN,
    "country_metadata": {"calling_code": "+46", "tld": ".se", "languages": ["sv-SE", "se", "sma", "fi-SE"]},
    "network": {"connection_type": "", "route": "91.128.0.0/14", "is_anycast": False},
    "currency": {"code": "SEK", "name": "Swedish Krona", "symbol": "kr"},
    "asn": {
        "as_number": "AS1257",
        "organization": "Tele2 Sverige AB",
        "country": "SE",
        "type": "ISP",
        "domain": "tele2.com",
        "date_allocated": "2002-09-19",
        "rir": "RIPE",
    },
    "company": {"name": "Tele2 Sverige AB", "type": "ISP", "domain": "tele2.com"},
    "security": SECURITY_CLEAN,
    "abuse": {
        "route": "91.128.0.0/14",
        "country": "SE",
        "name": "Swipnet Staff",
        "organization": "",
        "kind": "group",
        "address": "Tele2 AB/Swedish IP Network\nIP Registry\nTorshamnsgatan 17 164 40 Kista SWEDEN",
        "emails": ["abuse@tele2.com"],
        "phone_numbers": ["+46 8 5626 42 10"],
    },
    "time_zone": TIME_ZONE_STOCKHOLM,
    "user_agent": {
        "user_agent_string": "python-requests/2.32.4",
        "name": "Python-Requests",
        "type": "Robot",
        "version": "2.32.4",
        "version_major": "2",
        "device": {"name": "Python Requests", "type": "Robot", "brand": "Python", "cpu": "Unknown"},
        "engine": {"name": "python-requests", "type": "Robot", "version": "2.32.4", "version_major": "2"},
        "operating_system": {"name": "Cloud", "type": "Cloud", "version": "??", "version_major": "??", "build": "??"},
    },
}

IPGEO_DOMAIN = {
    "ip": "104.26.5.14",
    "domain": DOMAIN,
    "location": LOCATION_SWEDEN,
    "time_zone": TIME_ZONE_STOCKHOLM,
}

ASN_HETZNER = {
    "as_number": "AS24940",
    "organization": "Hetzner Online GmbH",
    "country": "DE",
    "type": "HOSTING",
    "domain": "hetzner.com",
    "date_allocated": "2002-06-03",
    "asn_name": "HETZNER-AS",
    "allocation_status": "ASSIGNED",
    "num_of_ipv4_routes": "84",
    "num_of_ipv6_routes": "6",
    "rir": "RIPE",
}

ASN_WITH_RELATIONS = dict(
    ASN_HETZNER,
    peers=[{"as_number": "AS3356", "description": "Level 3 Parent, LLC", "country": "US"}],
    upstreams=[{"as_number": "AS286", "description": "GTT Communications Inc.", "country": "US"}],
    downstreams=[{"as_number": "AS54965", "description": "Polytechnic Institute of NYU", "country": "US"}],
    routes=["49.12.0.0/16", "2a01:4f8::/29"],
    whois_response="ASNumber:       24940\nASName:         HETZNER-AS\n",
)


class MockResponse:
    """Minimal stand-in for requests.Response."""

    def __init__(
        self,
        status_code: int = 200,
        payload: Any = None,
        text: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
    ):
        self.status_code = status_code
        self._payload = payload
        self.text = text if text is not None else str(payload)
        self.headers = headers or {}

    def json(self) -> Any:
        if self._payload is None:
            raise ValueError("No JSON object could be decoded")
        return self._payload


def _error(status: int, message: str) -> MockResponse:
    return MockResponse(status_code=status, payload={"message": message})


def mock_request(method: str, url: str, **kwargs) -> MockResponse:
    """
    Route a mocked HTTP call to a canned response.

    Patched onto requests.Session.request, so it receives the method, the URL,
    and the keyword arguments the client built.
    """

    params = kwargs.get("params") or {}
    body = kwargs.get("json") or {}
    ip = params.get("ip")

    if params.get("apiKey") == UNAUTHORIZED_API_KEY:
        return _error(401, "Provided API key is not valid.")

    if ip == IP_UNKNOWN:
        return _error(404, "IP address not found in our database.")
    if ip == IP_BOGON:
        return _error(423, f"'{IP_BOGON}' is a bogon IP address.")
    if ip == IP_SERVER_ERROR:
        return MockResponse(status_code=500, payload={"message": "Internal Server Error"})
    if ip == IP_RATE_LIMITED:
        return _error(429, "API usage limit reached.")
    if ip == IP_MALFORMED_BODY:
        return MockResponse(status_code=200, payload=None, text="<html>gateway</html>")

    headers = {"X-Credits-Charged": "1"}

    if url.endswith("/ipgeo"):
        if ip == DOMAIN:
            return MockResponse(payload=IPGEO_DOMAIN, headers=headers)
        return MockResponse(payload=IPGEO_SWEDEN, headers=headers)

    if url.endswith("/ipgeo-bulk"):
        results = []
        for entry in body.get("ips", []):
            if entry == IP_BOGON:
                results.append({"message": f"'{IP_BOGON}' is a bogon IP address."})
            elif entry == DOMAIN:
                results.append(IPGEO_DOMAIN)
            else:
                results.append(dict(IPGEO_SWEDEN, ip=entry))
        return MockResponse(
            payload=results,
            headers={"X-Credits-Charged": str(len(results)), "X-Successful-Record": str(len(results))},
        )

    if url.endswith("/security-bulk"):
        results = []
        for entry in body.get("ips", []):
            if entry == IP_BOGON:
                results.append({"message": f"'{IP_BOGON}' is a bogon IP address."})
            elif entry == IP_MALICIOUS:
                results.append({"ip": entry, "security": SECURITY_MALICIOUS})
            else:
                results.append({"ip": entry, "security": SECURITY_CLEAN})
        return MockResponse(payload=results, headers={"X-Credits-Charged": str(2 * len(results))})

    if url.endswith("/security"):
        security = SECURITY_MALICIOUS if ip == IP_MALICIOUS else SECURITY_CLEAN
        return MockResponse(
            payload={"ip": ip or IP_CLEAN, "security": security},
            headers={"X-Credits-Charged": "2"},
        )

    if url.endswith("/asn"):
        asn = ASN_WITH_RELATIONS if params.get("include") else ASN_HETZNER
        payload = {"asn": asn}
        if params.get("ip"):
            payload = {"ip": params["ip"], "asn": asn}
        return MockResponse(payload=payload, headers=headers)

    if url.endswith("/abuse"):
        return MockResponse(payload={"ip": ip, "abuse": ABUSE_APNIC}, headers=headers)

    return _error(404, f"Unmapped endpoint in test: {url}")


def make_connection(api_key: str = STUB_API_KEY) -> Connection:
    """Build a connected Connection wired to a quiet logger."""

    connection = Connection()
    connection.logger = logging.getLogger("test-connection")
    connection.connect({"api_key": {"secretKey": api_key}})
    return connection


def make_action(action_class, api_key: str = STUB_API_KEY):
    """Build an action instance with a live connection object attached."""

    action = action_class()
    action.connection = make_connection(api_key)
    action.logger = logging.getLogger("test-action")
    return action


def sent_params(mocked) -> Dict[str, Any]:
    """Return the query parameters from the most recent mocked request."""

    return mocked.call_args.kwargs.get("params") or {}


def sent_body(mocked) -> Dict[str, Any]:
    """Return the JSON body from the most recent mocked request."""

    return mocked.call_args.kwargs.get("json") or {}
