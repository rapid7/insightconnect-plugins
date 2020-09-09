import hmac
import hashlib
from datetime import datetime
import json
import requests
from urllib import parse
from insightconnect_plugin_runtime.exceptions import PluginException


class DarkTraceAPI:
    def __init__(self, url: str, public_token: str, private_token: str, logger: object):
        self.url = url.rstrip("/")
        self.public_token = public_token
        self.private_token = private_token
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.logger = logger

    def get_status(self):
        return self._call_api("GET", "status")

    def update_intelfeed(self, status: bool, entry: str, description: str, source: str, expiration: str, hostname: bool):
        return self._call_api("POST", "intelfeed", data={
            ("addentry" if status else "removeentry"): entry,
            "description": description,
            "expiry": expiration,
            "hostname": hostname,
            "source": source,
            "fulldetails": True
        })

    def _get_signature(self, request: str) -> str:
        return hmac.new(
            self.private_token.encode('ASCII'),
            f"{request}\n{self.public_token}\n{self.date}".encode('ASCII'),
            hashlib.sha1
        ).hexdigest()

    def _call_api(
            self,
            method: str,
            path: str,
            data: dict = None
    ) -> dict:
        response = {"text": ""}
        query = None
        if data:
            query = parse.urlencode(data)

        endpoint = f"/{path}"
        if query:
            endpoint = f"{endpoint}?{query}"

        headers = {
            "DTAPI-Token": self.public_token,
            "DTAPI-Date": self.date,
            "DTAPI-Signature": self._get_signature(endpoint)
        }

        try:
            response = requests.request(
                method,
                f"{self.url}/{path}",
                data=data,
                headers=headers
            )

            if response.status_code == 401:
                raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD, data=response.text)
            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
            if response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
            if response.status_code >= 400:
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)

            if 200 <= response.status_code < 300:
                if response.text:
                    return response.json()
                return {}

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
