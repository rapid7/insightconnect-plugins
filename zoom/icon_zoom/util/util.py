import jwt
import datetime

DEFAULT_TASK_TYPE = "CMEF"


class UserType:
    @staticmethod
    def value_of(user_type: str) -> int:
        return {
            "Basic": 1,
            "Licensed": 2,
            "On-Prem": 3
        }.get(user_type)


def generate_jwt_token(api_key: str, secret: str) -> str:
    """Generate a JWT token for a Zoom API Auth; short lived"""
    payload = {
        "iss": api_key,
        "exp": datetime.datetime.now() + datetime.timedelta(seconds=60)
    }
    jwt_encoded = str(jwt.encode(payload, secret), "utf-8")
    return jwt_encoded
