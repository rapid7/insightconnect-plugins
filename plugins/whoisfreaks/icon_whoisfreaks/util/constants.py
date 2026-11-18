API_BASE_URL = "https://api.whoisfreaks.com"
FILES_BASE_URL = "https://files.whoisfreaks.com"
USER_AGENT = "rapid7-insightconnect-plugin-whoisfreaks/1.0.0"

# (connect, read) timeouts in seconds
LOOKUP_TIMEOUT = (10, 90)
FEED_TIMEOUT = (10, 180)

# Upper bounds on response bodies, so a misbehaving upstream cannot exhaust plugin memory
MAX_LOOKUP_BODY_BYTES = 50 * 1024 * 1024
MAX_FEED_BODY_BYTES = 200 * 1024 * 1024

MAX_BULK_ITEMS = 100
MAX_FEED_PAGE_SIZE = 1000
MIN_POLL_INTERVAL_MINUTES = 60
MAX_POLL_INTERVAL_MINUTES = 7 * 24 * 60

NOT_AVAILABLE = "Not Available"
DATE_FORMAT = "%Y-%m-%d"

# Lookup endpoints (api.whoisfreaks.com)
PATH_LIVE_WHOIS = "/v2.0/whois/live"
PATH_HISTORICAL_WHOIS = "/v2.0/whois/history"
PATH_REVERSE_WHOIS = "/v2.0/whois/reverse"
PATH_BULK_WHOIS = "/v2.0/bulkwhois/live"
PATH_LIVE_DNS = "/v2.0/dns/live"
PATH_HISTORICAL_DNS = "/v2.0/dns/historical"
PATH_REVERSE_DNS = "/v2.1/dns/reverse"
PATH_BULK_DNS = "/v2.0/dns/bulk/live"
PATH_DOMAIN_AVAILABILITY = "/v2.0/domain/availability"
PATH_TYPOSQUATTING = "/v3.0/domain/typos"
PATH_DOMAIN_REPUTATION = "/v1/domain/security"
PATH_SSL = "/v1.0/ssl/live"
PATH_SUBDOMAINS = "/v1.0/subdomains"
PATH_IP_GEOLOCATION = "/v1.0/geolocation"
PATH_IP_SECURITY = "/v2.0/security"
PATH_BULK_IP_SECURITY = "/v1.0/security"
PATH_IP_WHOIS = "/v1.0/ip-whois"
PATH_ASN_WHOIS = "/v2.0/asn-whois"
PATH_ACCOUNT_USAGE = "/v1.0/whoisapi/usage"

# Feed endpoints (files.whoisfreaks.com)
PATH_FEED_STATUS = "/v3.4/status"
PATH_NRD_STREAM = "/v3.3/stream/domainer/{family}"
PATH_THREAT_STREAM = "/v3.4/stream/threat-feed/{threat_type}"

DNS_RECORD_TYPES = {"A", "AAAA", "MX", "NS", "TXT", "SOA", "SPF", "CNAME", "PTR"}

THREAT_FEED_COLUMNS = [
    "domain",
    "threat_type",
    "confidence",
    "first_seen",
    "last_seen",
    "is_seed",
    "is_extrapolated",
    "is_dropped",
    "is_parked",
    "parked_reason",
    "matched_pivots",
]

_CONTACT_FIELDS = [
    "id",
    "id_type",
    "handle",
    "name",
    "company",
    "address",
    "city",
    "state",
    "zip",
    "country_code",
    "country",
    "email",
    "phone",
    "fax",
]

NRD_WHOIS_COLUMNS = (
    [
        "num",
        "domain_name",
        "query_time",
        "create_date",
        "update_date",
        "expiry_date",
        "domain_registrar_id",
        "domain_registrar_name",
        "domain_registrar_whois",
        "domain_registrar_url",
        "domain_registrar_email_address",
        "domain_registrar_phone",
        "domain_registrar_authoritative_registry_name",
    ]
    + [
        f"{role}_{field}"
        for role in ("registrant", "administrative", "technical", "billing")
        for field in _CONTACT_FIELDS
    ]
    + ["eligibility_id", "eligibility_name", "eligibility_type"]
    + [f"name_server_{index}" for index in range(1, 5)]
    + [f"domain_status_{index}" for index in range(1, 5)]
    + ["reseller_name", "reseller_email", "reseller_phone"]
)
