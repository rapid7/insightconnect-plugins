from typing import Any, Dict, List

from insightconnect_plugin_runtime.exceptions import PluginException

MIN_NAME_FILTER_LENGTH = 3  # the GravityZone details.name filter needs at least 3 characters
ENDPOINT_SUMMARY_FIELDS = ("id", "name", "fqdn", "ip", "macs", "is_managed", "is_isolated")


def normalize_hostname(value: Any) -> str:
    """Prepare a hostname or FQDN for comparison: no surrounding whitespace, no trailing dot, case folded."""
    return str(value or "").strip().rstrip(".").casefold()


def get_short_label(hostname: str) -> str:
    """Return the part of a normalized hostname before the first dot."""
    return hostname.split(".", 1)[0]


def find_exact_matches(endpoints: List[Dict[str, Any]], hostname: str) -> List[Dict[str, Any]]:
    """
    Return the endpoints that match the hostname exactly, ignoring case.
    A short name is compared with the endpoint name. An FQDN is compared with the endpoint FQDN first. If no FQDN
    matches, its short label is compared with the endpoint name: several such endpoints are ambiguous, and a single
    one counts only when GravityZone has no FQDN for it, so an endpoint in another domain is never returned.
    """
    target = normalize_hostname(hostname)
    unique_endpoints = _deduplicate(endpoints)
    short_label = get_short_label(target)
    name_matches = [
        endpoint for endpoint in unique_endpoints if normalize_hostname(endpoint.get("name")) == short_label
    ]
    if "." not in target:
        return name_matches

    fqdn_matches = [endpoint for endpoint in unique_endpoints if normalize_hostname(endpoint.get("fqdn")) == target]
    if fqdn_matches:
        return fqdn_matches
    if len(name_matches) == 1:
        candidate_fqdn = normalize_hostname(name_matches[0].get("fqdn"))
        if candidate_fqdn and candidate_fqdn != target:
            return []
    return name_matches


def clean_endpoint_id(endpoint_id: Any) -> str:
    cleaned_endpoint_id = str(endpoint_id or "").strip()
    if not cleaned_endpoint_id:
        raise PluginException(
            cause="The endpoint ID is empty.",
            assistance="Provide the ID of a managed endpoint, for example the ID returned by Find Endpoint.",
        )
    return cleaned_endpoint_id


def to_endpoint_item(endpoint: Dict[str, Any]) -> Dict[str, Any]:
    """Map a getEndpointsList item to the endpoint_item type."""
    return {
        "id": endpoint.get("id") or "",
        "name": endpoint.get("name") or "",
        "label": endpoint.get("label") or "",
        "fqdn": endpoint.get("fqdn") or "",
        "group_id": endpoint.get("groupId") or "",
        "is_managed": bool(endpoint.get("isManaged")),
        "machine_type": endpoint.get("machineType") or 0,
        "operating_system_version": endpoint.get("operatingSystemVersion") or "",
        "ip": endpoint.get("ip") or "",
        "macs": endpoint.get("macs") or [],
        "managed_with_best": bool(endpoint.get("managedWithBest")),
        "is_isolated": bool(endpoint.get("isIsolated")),
    }


def to_endpoint_summary(endpoint: Dict[str, Any]) -> Dict[str, Any]:
    """Map a getEndpointsList item to the endpoint_summary type."""
    endpoint_item = to_endpoint_item(endpoint)
    return {field: endpoint_item[field] for field in ENDPOINT_SUMMARY_FIELDS}


def _deduplicate(endpoints: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Drop repeated endpoint IDs, which can appear when the inventory changes while pages are read."""
    seen_ids = set()
    unique_endpoints = []
    for endpoint in endpoints:
        endpoint_id = endpoint.get("id")
        if endpoint_id and endpoint_id in seen_ids:
            continue
        seen_ids.add(endpoint_id)
        unique_endpoints.append(endpoint)
    return unique_endpoints
