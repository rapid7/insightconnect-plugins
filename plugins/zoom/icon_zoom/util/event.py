from hashlib import sha1


class Event(object):

    def __init__(self, client_type: str, email: str, ip_address: str, time: str, type_: str, version: str):
        self.client_type = client_type
        self.email = email
        self.ip_address = ip_address
        self.time = time
        self.type_ = type_
        self.version = version

    def __eq__(self, other):
        return self.client_type == other.client_type \
               and self.email == other.email \
               and self.ip_address == other.ip_address \
               and self.time == other.time \
               and self.type_ == other.type_ \
               and self.version == other.version

    def __hash__(self):
        m = sha1()
        for k, v in self.__dict__.items():
            m.update(f"{k}{v}".encode("utf-8"))

        return m.hexdigest()
