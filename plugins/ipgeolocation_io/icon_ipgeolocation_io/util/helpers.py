import ipaddress
from typing import Any, List, Optional, Sequence

from insightconnect_plugin_runtime.exceptions import PluginException

from .constants import MAX_BULK_ENTRIES, SUPPORTED_LANGUAGES


def to_csv(values: Optional[List[str]]) -> Optional[str]:
    """
    Convert a list input into the comma separated string the API expects.

    Blank entries are dropped and duplicates are removed while preserving the
    order the user supplied. Returns None when nothing is left, so the caller
    can omit the query parameter entirely rather than sending an empty value.
    """

    if not values:
        return None

    seen, ordered = set(), []
    for value in values:
        item = str(value).strip()
        if item and item not in seen:
            seen.add(item)
            ordered.append(item)

    return ",".join(ordered) if ordered else None


def normalize_choices(values: Optional[List[str]], allowed: Sequence[str], field_title: str) -> Optional[str]:
    """
    Validate list values against a fixed vocabulary and return them as CSV.

    Matching is case insensitive and the canonical spelling is returned, so
    'livehostname' still reaches the API as 'liveHostname'. Unknown values raise
    rather than being forwarded, because the API ignores anything it does not
    recognise and a typo would otherwise look like missing data.
    """

    if not values:
        return None

    lookup = {choice.lower(): choice for choice in allowed}
    seen, ordered, invalid = set(), [], []

    for value in values:
        item = str(value).strip()
        if not item:
            continue

        canonical = lookup.get(item.lower())
        if canonical is None:
            invalid.append(item)
        elif canonical not in seen:
            seen.add(canonical)
            ordered.append(canonical)

    if invalid:
        raise PluginException(
            cause=f"The {field_title} input contained unsupported value(s): {', '.join(repr(i) for i in invalid)}.",
            assistance=f"Choose from: {', '.join(allowed)}.",
        )

    return ",".join(ordered) if ordered else None


def clean_string(value: Any) -> Optional[str]:
    """Return a stripped string, or None when the input is blank or missing."""

    if value is None:
        return None

    text = str(value).strip()
    return text or None


def normalize_asn(value: Any) -> Optional[str]:
    """
    Accept an ASN with or without the AS prefix and return the bare number.

    The /v3/asn endpoint expects a plain number, so 'AS24940', 'as24940', and
    '24940' all have to arrive as '24940'.
    """

    text = clean_string(value)
    if text is None:
        return None

    if text[:2].upper() == "AS":
        text = text[2:].strip()

    if not text.isdigit():
        raise PluginException(
            cause=f"'{value}' is not a valid Autonomous System Number.",
            assistance="Provide an ASN as a number, with or without the AS prefix, such as 24940 or AS24940.",
        )

    return text


def validate_ip(value: Any, field_title: str, require_routable: bool = True) -> Optional[str]:
    """
    Validate that a value is an IPv4 or IPv6 address and return it stripped.

    Domains are rejected here because the security, abuse, and ASN endpoints
    only accept addresses, and the API answers a domain with an opaque 401.
    When require_routable is set, bogon and private addresses are rejected
    before the request is sent, since the API answers those with a 423.
    """

    text = clean_string(value)
    if text is None:
        return None

    try:
        address = ipaddress.ip_address(text)
    except ValueError:
        raise PluginException(
            cause=f"The {field_title} input '{text}' is not a valid IPv4 or IPv6 address.",
            assistance=(
                "Provide a single IPv4 or IPv6 address. This action does not accept domain names, "
                "CIDR ranges, or URLs."
            ),
        )

    if require_routable and not address.is_global:
        raise PluginException(
            cause=f"The {field_title} input '{text}' is a private or bogon address.",
            assistance=(
                "Provide a public, routable address. IPGeolocation.io cannot look up private, "
                "loopback, link-local, multicast, or otherwise reserved addresses."
            ),
        )

    return text


def validate_bulk_entries(values: Optional[List[str]], field_title: str) -> List[str]:
    """
    Normalize a bulk input list and enforce the API's size limits.

    Entries are neither deduplicated nor reordered, because the API returns one
    result per submitted entry in the order it was sent and callers rely on
    that alignment.
    """

    entries = [str(value).strip() for value in (values or []) if str(value).strip()]

    if not entries:
        raise PluginException(
            cause=f"The {field_title} input did not contain any entries.",
            assistance=f"Provide between 1 and {MAX_BULK_ENTRIES:,} entries.",
        )

    if len(entries) > MAX_BULK_ENTRIES:
        raise PluginException(
            cause=f"The {field_title} input contained {len(entries):,} entries.",
            assistance=(
                f"IPGeolocation.io accepts at most {MAX_BULK_ENTRIES:,} entries per bulk request. "
                "Split the input across multiple runs of this action."
            ),
        )

    return entries


def validate_bulk_ips(values: Optional[List[str]], field_title: str) -> List[str]:
    """
    Validate a bulk list that must contain addresses rather than domains.

    Bogon and private entries are left in place. The API reports those per
    entry with a message field instead of failing the whole request, and
    dropping them here would break the alignment between input and output.
    """

    entries = validate_bulk_entries(values, field_title)

    invalid = []
    for entry in entries:
        try:
            ipaddress.ip_address(entry)
        except ValueError:
            invalid.append(entry)

    if invalid:
        preview = ", ".join(f"'{entry}'" for entry in invalid[:5])
        if len(invalid) > 5:
            preview = f"{preview}, and {len(invalid) - 5:,} more"
        raise PluginException(
            cause=f"The {field_title} input contained {len(invalid):,} value(s) that are not IP addresses: {preview}.",
            assistance="This action accepts IPv4 and IPv6 addresses only. Domain names are not supported.",
        )

    return entries


def normalize_language(value: Any) -> Optional[str]:
    """Validate the language code and drop the default so it is not sent needlessly."""

    text = clean_string(value)
    if text is None:
        return None

    language = text.lower()
    if language not in SUPPORTED_LANGUAGES:
        raise PluginException(
            cause=f"'{text}' is not a language supported by IPGeolocation.io.",
            assistance=f"Choose one of the supported language codes: {', '.join(SUPPORTED_LANGUAGES)}.",
        )

    return None if language == "en" else language
