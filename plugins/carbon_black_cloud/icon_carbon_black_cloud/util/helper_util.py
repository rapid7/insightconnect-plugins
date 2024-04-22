from hashlib import sha1


def hash_sha1(log: dict) -> str:
    hash_ = sha1()  # nosec B303
    for key, value in log.items():
        hash_.update(f"{key}{value}".encode("utf-8"))
    return hash_.hexdigest()