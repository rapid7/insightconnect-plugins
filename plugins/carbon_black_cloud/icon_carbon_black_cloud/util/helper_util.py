from hashlib import sha1
from icon_carbon_black_cloud.util.constants import ENCODE_TYPE


def hash_sha1(log: dict) -> str:
    hash_ = sha1()  # nosec B303
    for key, value in log.items():
        # CB does can return list values which can change order between API calls - to avoid further
        # manipulating the data in this method, hash the values as they are returned, although it may mean
        # returning duplicate data from the task.
        hash_.update(f"{key}{value}".encode(ENCODE_TYPE))
    return hash_.hexdigest()
