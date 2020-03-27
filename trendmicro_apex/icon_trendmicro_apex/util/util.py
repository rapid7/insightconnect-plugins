import base64
import jwt
import hashlib
import time

from datetime import timedelta
from datetime import datetime


def create_base64_checksum(http_method: str, raw_url: str, raw_header: str, request_body: str) -> str:
    """Create a base64 encoded hash string for an Apex JWT token"""
    string_to_hash = http_method.upper() + '|' + raw_url.lower() + '|' + raw_header + '|' + request_body
    base64_hash_string = base64.b64encode(hashlib.sha256(str.encode(string_to_hash)).digest()).decode('utf-8')
    return base64_hash_string


def create_jwt_token(application_id: str, api_key: str, http_method: str, raw_url: str, header: str,
                     request_body: str, algorithm='HS256') -> str:
    """Generate a JWT token for an Apex HTTP request. Specific to a url destination and payload"""
    issue_time = time.time()
    payload = {'appid': application_id,
               'iat': issue_time,
               'version': 'V1',
               'checksum': create_base64_checksum(http_method, raw_url, header, request_body)}
    token = jwt.encode(payload, api_key, algorithm).decode('utf-8')
    return token


def get_expiration_utc_date_string(num_days=30):
    if not isinstance(num_days, int) or num_days < 1:
        num_days = 1
    today = datetime.now()
    # +5 hours for timezones, just a buffer
    timedelta_days = timedelta(days=num_days, hours=5)
    future = today + timedelta_days
    return future.strftime("%Y-%m-%dT%H:%MU")
