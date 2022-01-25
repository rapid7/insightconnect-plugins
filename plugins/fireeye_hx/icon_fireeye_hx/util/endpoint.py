def hosts() -> str:
    return "hosts"


def version() -> str:
    return "version"


def host_containment(agent_id: str) -> str:
    return f"hosts/{agent_id}/containment"
