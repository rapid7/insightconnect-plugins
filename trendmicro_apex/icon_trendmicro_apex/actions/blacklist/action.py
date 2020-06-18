# Custom imports below
import json

import requests
import validators
from icon_trendmicro_apex.util.util import get_expiration_utc_date_string
from requests.exceptions import RequestException

import komand
from komand.exceptions import PluginException
from .schema import BlacklistInput, BlacklistOutput, Input, Output, Component


class Blacklist(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='blacklist',
            description=Component.DESCRIPTION,
            input=BlacklistInput(),
            output=BlacklistOutput())
        self.api_path = '/WebApp/api/SuspiciousObjects/UserDefinedSO'
        self.MAX_NOTES_LENGTH = 256
        self.MAX_SHA_LENGTH = 40
        self.MAX_URL_LENGTH = 2046

    def run(self, params={}):
        payload = self.generate_payload(params)
        json_payload = json.dumps(payload)
        blacklist_state = params.get(Input.BLACKLIST_STATE, True)
        if blacklist_state is False:
            method = "DELETE"
            payload_type = payload.get("param", {}).get("type")
            content = payload["param"]["content"]
            self.api_path = f"{self.api_path}?type={payload_type}&content={content}"
        else:
            method = "PUT"

        self.connection.create_jwt_token(self.api_path, method, json_payload)
        request_url = self.connection.url + self.api_path

        response = None
        try:
            response = requests.request(
                method.lower(),
                request_url,
                headers=self.connection.header_dict,
                data=json_payload,
                verify=False
            )
            response.raise_for_status()
            return {Output.SUCCESS: response is not None}
        except RequestException as rex:
            if response:
                self.logger.error(f"Received status code: {response.status_code}")
                self.logger.error(f"Response was: {response.text}")
            raise PluginException(
                assistance="Please verify the connection details and input data.",
                cause=f"Error processing the Apex request: {rex}"
            )

    @staticmethod
    def get_data_type(indicator):
        if validators.ipv4(indicator) or validators.ipv6(indicator):
            return "IP"
        elif validators.url(indicator):
            return "URL"
        elif validators.domain(indicator):
            return "DOMAIN"
        elif validators.sha1(indicator):
            return "FILE_SHA1"

        raise PluginException(
            cause="Invalid indicator input provided.",
            assistance="Supported indicators are IP, URL, domain and SHA1 hash."
        )

    def generate_payload(self, params):
        payload_notes = ''
        user_notes = params.get(Input.DESCRIPTION)
        if user_notes:
            if len(user_notes) > self.MAX_NOTES_LENGTH:
                self.logger.warning(f"Note: exceeds maximum length, truncated to {self.MAX_NOTES_LENGTH} characters")
            payload_notes = user_notes[:self.MAX_NOTES_LENGTH]
        indicator = params.get(Input.INDICATOR).lower()
        payload_type = self.get_data_type(indicator)
        payload_scan_action = params.get(Input.SCAN_ACTION, "BLOCK")
        num_days = params.get(Input.EXPIRY_DATE, 30)
        payload_expiry_date = get_expiration_utc_date_string(int(num_days))

        return {
            "param": {
                "content": indicator,
                "expiration_utc_date": payload_expiry_date,
                "notes": payload_notes,
                "scan_action": payload_scan_action.lower(),
                "type": payload_type.lower()
            }
        }
