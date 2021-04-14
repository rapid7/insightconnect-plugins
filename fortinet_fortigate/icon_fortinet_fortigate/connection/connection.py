import komand
from .schema import ConnectionSchema, Input

# Custom imports below
from requests import Session
from icon_fortinet_fortigate.util.util import Helpers
from komand.exceptions import PluginException
import requests
import json


class Connection(komand.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.api_key = params.get(Input.API_KEY).get("secretKey")
        self.host = params.get(Input.HOSTNAME)

        self.session_params = {"access_token": self.api_key}
        self.ssl_verify = params.get(Input.SSL_VERIFY)

        self.session = Session()
        self.session.params = self.session_params
        # Strip http:// or https://
        if self.host.startswith("http://"):
            self.host = self.host[7:]
        if self.host.startswith("https://"):
            self.host = self.host[8:]
        # Strip out any URL character after /
        self.host = self.host.split("/", 1)[0]

        # This is broken. Leaving this here as its supposed to be fixed in a future version of requests
        # self.session.verify = self.ssl_verify

    def get_address_group(self, address_group_name, is_ipv6):
        endpoint = "firewall/addrgrp"

        if is_ipv6:
            endpoint = "firewall/addrgrp6"

        result = self.call_api(
            path=endpoint,
            params={
                "access_token": self.api_key,
                "filter": f"name=@{address_group_name}",  # I have no idea why they need the @ symbol
            }
        )

        groups = result.json().get("results")
        if not len(groups) > 0:
            raise PluginException(
                cause=f"Could not find address group '{address_group_name}' in results.\n",
                assistance=f"Please make sure the group '{address_group_name}' exists.\n",
                data=result.text,
            )

        return groups[0]

    def get_address_object(self, address_name):
        try:
            response_ipv4_json = self.call_api(
                path=f"firewall/address/{address_name}"
            ).json()

            if response_ipv4_json["http_status"] == 200:
                return response_ipv4_json
        except (PluginException, json.decoder.JSONDecodeError, requests.exceptions.HTTPError):
            pass

        response_ipv6 = self.call_api(
            path=f"firewall/address6/{address_name}"
        )
        response_ipv6_json = response_ipv6.json()

        if response_ipv6_json["http_status"] == 200:
            return response_ipv6_json

        raise PluginException(
            cause=f"Get address object failed. Address object '{address_name}' does not exists.\n",
            assistance="Contact support for assistance.",
            data=response_ipv6.text,
        )

    def test(self):
        helper = Helpers(self.logger)
        response = self.call_api(
            path="firewall.consolidated/policy"
        )

        try:
            json_response = response.json()
        except ValueError:
            raise PluginException(
                cause="Data sent by FortiGate was not in JSON format.\n",
                assistance="Contact support for help.",
                data=response.text,
            )
        helper.http_errors(json_response, response.status_code)

        return response.json()

    def call_api(
            self,
            path: str,
            method: str = "GET",
            params: dict = None,
            json_data: dict = None
    ) -> requests.Response:
        try:
            response = self.session.request(
                method=method.upper(),
                url=f"https://{self.host}/api/v2/cmdb/{path}",
                verify=self.ssl_verify,
                json=json_data,
                params=params
            )

            if response.status_code == 401:
                raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD, data=response.text)
            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
            if response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
            if 400 <= response.status_code < 500:
                raise PluginException(
                    preset=PluginException.Preset.UNKNOWN,
                    data=response.json().get("message", response.text),
                )
            if response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)

            if 200 <= response.status_code < 300:
                return response

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=e)
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
