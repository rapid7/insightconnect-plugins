import re

TIMEOUT = 60.0
HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "accept": "application/json",
}
RETRY_STATUS_CODES = {408, 429, 500, 502, 503, 504}
LUMINAR_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
STIX_PARSER = re.compile(
    r"([\w-]+?):(\w.+?) (?:[!><]?=|IN|MATCHES|LIKE) '([^']+)' *["
    + r"OR|AND|FOLLOWEDBY]?"
)
