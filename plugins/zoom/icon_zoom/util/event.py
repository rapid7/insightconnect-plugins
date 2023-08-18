class Event:
    # pylint: disable=redefined-builtin
    def __init__(self, client_type: str, email: str, ip_address: str, time: str, type: str, version: str) -> None:
        self.client_type = client_type
        self.email = email
        self.ip_address = ip_address
        self.time = time
        self.type = type
        self.version = version

    def __eq__(self, other) -> bool:
        return (
            self.client_type == other.client_type
            and self.email == other.email
            and self.ip_address == other.ip_address
            and self.time == other.time
            and self.type == other.type
            and self.version == other.version
        )

    def __gt__(self, other) -> bool:
        return self.time > other.time

    def __lt__(self, other) -> bool:
        return self.time < other.time

    def __repr__(self) -> str:
        return self.time
