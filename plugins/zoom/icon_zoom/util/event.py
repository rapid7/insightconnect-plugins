from hashlib import sha1


class Event(object):
    # pylint: disable=redefined-builtin
    def __init__(self, client_type: str, email: str, ip_address: str, time: str, type: str, version: str):
        self.client_type = client_type
        self.email = email
        self.ip_address = ip_address
        self.time = time
        self.type = type
        self.version = version

    def __eq__(self, other):
        return (
            self.client_type == other.client_type
            and self.email == other.email
            and self.ip_address == other.ip_address
            and self.time == other.time
            and self.type == other.type
            and self.version == other.version
        )

    def __gt__(self, other):
        return self.time > other.time

    def __lt__(self, other):
        return self.time < other.time

    def __repr__(self):
        return self.time

    def sha1(self):
        hash_ = sha1()  # nosec B303
        for key, value in self.__dict__.items():
            hash_.update(f"{key}{value}".encode("utf-8"))
        return hash_.hexdigest()
