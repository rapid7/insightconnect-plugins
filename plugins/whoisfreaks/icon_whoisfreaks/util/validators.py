import datetime
import ipaddress
import re
from typing import Callable, Iterable, Optional
from urllib.parse import urlsplit

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.util import constants

_LABEL = re.compile(r"^[a-z0-9_]([a-z0-9_-]{0,61}[a-z0-9_])?$")
_ASN = re.compile(r"^(?:AS)?(\d{1,10})$", re.IGNORECASE)

REASON_INVALID_DOMAIN = "Not a valid domain name"
REASON_INVALID_IP = "Not a valid IP address"
REASON_SPECIAL_IP = "Private, reserved or special-use IP address"
REASON_DUPLICATE = "Duplicate value"


def input_error(cause: str, assistance: str) -> PluginException:
    return PluginException(cause=cause, assistance=assistance)


def optional_text(value) -> Optional[str]:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def try_domain(value) -> tuple:
    """Return (normalized_domain, None) or (None, reason). URLs are reduced to their host name."""
    text = optional_text(value) or ""
    if "://" in text:
        text = urlsplit(text).hostname or ""
    text = text.strip().rstrip(".").lower()
    if not text:
        return None, REASON_INVALID_DOMAIN
    try:
        text = text.encode("idna").decode("ascii")
    except UnicodeError:
        return None, REASON_INVALID_DOMAIN
    labels = text.split(".")
    if len(text) > 253 or len(labels) < 2 or not all(_LABEL.match(label) for label in labels):
        return None, REASON_INVALID_DOMAIN
    if labels[-1].isdigit():
        return None, REASON_INVALID_DOMAIN
    return text, None


def domain(value, field: str = "Domain") -> str:
    normalized, reason = try_domain(value)
    if normalized is None:
        raise input_error(
            f"{field} '{optional_text(value) or ''}' is not valid: {reason}",
            "Provide a domain name such as example.com",
        )
    return normalized


def try_ip(value) -> tuple:
    """Return (normalized_ip, None) for public addresses, or (None, reason)."""
    text = optional_text(value)
    try:
        address = ipaddress.ip_address(text or "")
    except ValueError:
        return None, REASON_INVALID_IP
    if is_special_use(address):
        return None, REASON_SPECIAL_IP
    return str(address), None


def is_special_use(address) -> bool:
    mapped = getattr(address, "ipv4_mapped", None)
    if mapped is not None:
        address = mapped
    return (
        not address.is_global
        or address.is_multicast
        or address.is_reserved
        or address.is_loopback
        or address.is_link_local
        or address.is_unspecified
    )


def ip(value, field: str = "IP Address") -> tuple:
    """Return (normalized_ip, None) for a public address, (None, reason) for a special-use address.

    Raises a PluginException for a value that is not an IP address at all.
    """
    normalized, reason = try_ip(value)
    if reason == REASON_INVALID_IP:
        raise input_error(
            f"{field} '{optional_text(value) or ''}' is not a valid IPv4 or IPv6 address",
            "Provide an IP address such as 8.8.8.8 or 2001:4860:4860::8888",
        )
    return normalized, reason


def asn(value) -> str:
    match = _ASN.match(optional_text(value) or "")
    if not match:
        raise input_error(
            f"ASN '{optional_text(value) or ''}' is not valid",
            "Provide an autonomous system number such as AS15169 or 15169",
        )
    return match.group(1)


def date(value, field: str) -> Optional[str]:
    text = optional_text(value)
    if text is None:
        return None
    try:
        return datetime.datetime.strptime(text, constants.DATE_FORMAT).date().isoformat()
    except ValueError:
        raise input_error(
            f"{field} '{text}' is not a valid date", "Use the YYYY-MM-DD format, for example 2026-01-31"
        ) from None


def integer(value, field: str, minimum: int, maximum: Optional[int] = None, default: Optional[int] = None):
    if value is None:
        return default
    if isinstance(value, bool) or not isinstance(value, int):
        raise input_error(f"{field} must be a whole number", f"Provide a whole number of at least {minimum}")
    if value < minimum or (maximum is not None and value > maximum):
        limits = f"between {minimum} and {maximum}" if maximum is not None else f"at least {minimum}"
        raise input_error(f"{field} is {value}, which is out of range", f"{field} must be {limits}")
    return value


def record_types(value, allow_ptr: bool = True) -> str:
    text = (optional_text(value) or "all").replace(" ", "")
    if text.lower() == "all":
        return "all"
    allowed = constants.DNS_RECORD_TYPES if allow_ptr else constants.DNS_RECORD_TYPES - {"PTR"}
    types = [item.upper() for item in text.split(",") if item]
    invalid = [item for item in types if item not in allowed]
    if not types or invalid:
        raise input_error(
            f"Record Types '{text}' contains unsupported values: {', '.join(invalid) or 'none given'}",
            f"Use all, or a comma-separated list of {', '.join(sorted(allowed))}",
        )
    return ",".join(dict.fromkeys(types))


def bulk(values: Optional[Iterable], normalizer: Callable, field: str, required: bool = True) -> tuple:
    """Validate a list input. Returns (valid_values, skipped) where skipped holds {value, reason} objects.

    Raises when a required list is empty or when more than the WhoisFreaks bulk limit of values is valid.
    A list whose values were all skipped is not an error, so workflows can continue with the skipped reasons.
    """
    values = list(values or [])
    if required and not values:
        raise input_error(f"{field} is empty", f"Provide between 1 and {constants.MAX_BULK_ITEMS} values")
    valid, skipped, seen = [], [], set()
    for value in values:
        normalized, reason = normalizer(value)
        if normalized is not None and normalized in seen:
            reason = REASON_DUPLICATE
        if reason:
            skipped.append({"value": str(value), "reason": reason})
            continue
        seen.add(normalized)
        valid.append(normalized)
    if len(valid) > constants.MAX_BULK_ITEMS:
        raise input_error(
            f"{field} contains {len(valid)} valid values, more than the WhoisFreaks limit of {constants.MAX_BULK_ITEMS}",
            f"Split {field} into lists of at most {constants.MAX_BULK_ITEMS} values",
        )
    return valid, skipped


def try_tld(value) -> tuple:
    text = (optional_text(value) or "").lower().strip(".")
    try:
        text = text.encode("idna").decode("ascii")
    except UnicodeError:
        return None, "Not a valid TLD"
    labels = text.split(".")
    if not text or not all(_LABEL.match(label) for label in labels):
        return None, "Not a valid TLD"
    return text, None


def keywords(values: Optional[Iterable]) -> list:
    return list(dict.fromkeys(text.lower() for text in (optional_text(value) for value in values or []) if text))


def tlds(values: Optional[Iterable]) -> list:
    return list(dict.fromkeys(text.lower().strip(".") for text in keywords(values) if text.strip(".")))
