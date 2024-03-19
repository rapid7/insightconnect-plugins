STATUS_CODE_FIELD_NAME = "status_code"
RESULTS_FIELD_NAME = "results"

IP_LOOKUP_FLAG_DEFAULT = 1
REPORT_FLAG_DEFAULT = 1
SAMPLES_FLAG_DEFAULT = 1
DOMAIN_LOOKUP_FLAG_DEFAULT = 1
SEARCH_LOOKUP_FLAG_DEFAULT = 1

DOMAIN_LOOKUP_FLAG_MAP = {
    "WHOIS": 1,
    "Passive DNS": 2,
    "Example Query URI": 3,
    "Related Samples": 4,
    "Subdomains": 5,
    "Report tagging": 6,
}
IP_LOOKUP_FLAG_MAP = {
    "WHOIS": 1,
    "PASSIVE DNS": 2,
    "URIs": 3,
    "Related Samples": 4,
    "SSL Certificates": 5,
    "Report Tagging": 6,
}
REPORT_FLAG_MAP = {"Domains": 1, "Hosts": 2, "Emails": 3, "Samples": 4}
SAMPLES_LOOKUP_FLAG_MAP = {
    "Metadata": 1,
    "HTTP Traffic": 2,
    "Hosts": 3,
    "Mutants": 4,
    "Registry keys": 5,
    "AV detections": 6,
    "Report Tagging": 7,
}
SEARCH_LOOKUP_FLAG_MAP = {"Full Text": 1, "By Year": 2}
