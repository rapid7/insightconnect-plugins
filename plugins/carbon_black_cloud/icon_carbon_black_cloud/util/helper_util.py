from hashlib import sha1


def hash_sha1(log: dict) -> str:
    hash_ = sha1()  # nosec B303
    for key, value in log.items():
        # CB does can return list values which can change order between API calls - to avoid further
        # manipulating the data in this method, hash the values as they are returned, although it may mean
        # returning duplicate data from the task.
        hash_.update(f"{key}{value}".encode("utf-8"))
    return hash_.hexdigest()
