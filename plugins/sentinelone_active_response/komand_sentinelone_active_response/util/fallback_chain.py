from typing import Dict, List

FALLBACK_CHAINS: Dict[str, List[str]] = {
    "uuid": ["computerName", "networkInterfaceInet__contains"],
    "hostname": ["uuid", "networkInterfaceInet__contains"],
    "ip": ["computerName", "uuid"],
    "mac": ["computerName", "uuid"],
    "agent_id": [],  # No fallback — error immediately
}


def get_fallback_chain(classification: str) -> List[str]:
    """Return the fallback chain for the given classification type."""
    return FALLBACK_CHAINS.get(classification, [])
