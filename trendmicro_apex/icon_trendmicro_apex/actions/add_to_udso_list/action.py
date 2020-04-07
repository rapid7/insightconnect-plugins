import komand
from .schema import AddToUdsoListInput, AddToUdsoListOutput, Input, Output, Component
# Custom imports below
import ipaddress
import json
import requests
import re
from icon_trendmicro_apex.util.util import get_expiration_utc_date_string
from komand.exceptions import PluginException
from requests.exceptions import RequestException

class AddToUdsoList(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_to_udso_list',
                description=Component.DESCRIPTION,
                input=AddToUdsoListInput(),
                output=AddToUdsoListOutput())
        self.api_path = '/WebApp/api/SuspiciousObjects/UserDefinedSO'
        self.api_http_method = 'PUT'
        self.MAX_NOTES_LENGTH = 256
        self.MAX_SHA_LENGTH = 40
        self.MAX_URL_LENGTH = 2046

    def validate_domain(self, domain):
        # HTTP or HTTPS is not allowed, otherwise I would have validated like a URL
        if not re.search('^(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+$', domain):
            raise PluginException(cause='Improperly formatted DOMAIN provided when sending data type DOMAIN',
                                  assistance='Please verify the fields DATA_TYPE and CONTENT')
        if len(domain) > self.MAX_URL_LENGTH:
            self.logger.warning(f"DOMAIN exceeds the maximum length, truncated to {self.MAX_URL_LENGTH} characters")
        return domain[:self.MAX_URL_LENGTH]

    def validate_ip(self, ip_address):
        try:
            ipaddress.ip_address(ip_address)
        except ValueError:
            raise PluginException(cause='Invalid IP provided when sending data type IP',
                                  assistance='Please verify the fields DATA_TYPE and CONTENT')
        return ip_address

    def validate_sha(self, sha):
        if len(sha) > self.MAX_SHA_LENGTH:
            self.logger.warning(f"SHA exceeds the maximum length, truncated to {self.MAX_SHA_LENGTH} characters")
        return sha[:self.MAX_SHA_LENGTH]

    def validate_url(self, url):
        # url regex's provided by urlregex.com
        start_of_content = url[:6].lower()
        if not start_of_content == "https:" and not start_of_content[:5] == "http:":
            raise PluginException(cause='HTTP or HTTPS needed when submitting data type URL',
                                  assistance='Please start the URL with http or https')
        elif not re.search('^http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+$', url):
            raise PluginException(cause='Improperly formatted URL provided when sending data type URL',
                                  assistance='Please verify the fields DATA_TYPE and CONTENT')
        if len(url) > self.MAX_URL_LENGTH:
            self.logger.warning(f"URL exceeds the maximum length, truncated to {self.MAX_URL_LENGTH} characters")
        return url[:self.MAX_URL_LENGTH]

    def validate_content_to_type(self, payload_content, payload_type):
        if payload_type == 'FILE_SHA1':
            payload_content = self.validate_sha(payload_content)
        elif payload_type == 'IP':
            payload_content = self.validate_ip(payload_content)
        elif payload_type == 'URL':
            payload_content = self.validate_url(payload_content)
        elif payload_type == 'DOMAIN':
            payload_content = self.validate_domain(payload_content)
        return payload_content

    def generate_payload(self, params={}):
        payload_notes = ''
        user_notes = params.get(Input.NOTES)
        if user_notes:
            if len(user_notes) > self.MAX_NOTES_LENGTH:
                self.logger.warning(f"Notes exceeds maximum length, truncated to {self.MAX_NOTES_LENGTH} characters")
            payload_notes = user_notes[:self.MAX_NOTES_LENGTH]
        payload_scan_action = params.get(Input.SCAN_ACTION)
        payload_content = params.get(Input.CONTENT).lower()
        payload_type = params.get(Input.DATA_TYPE)
        num_days = params.get(Input.EXPIRY_DATE, 30)
        payload_expiry_date = get_expiration_utc_date_string(int(num_days))

        payload = {
            "param": {
                "content": payload_content,
                "expiration_utc_date": payload_expiry_date,
                "notes": payload_notes,
                "scan_action": payload_scan_action.lower(),
                "type": payload_type.lower()
            }
        }
        return json.dumps(payload)

    def run(self, params={}):
        json_payload = self.generate_payload(params)
        self.connection.create_jwt_token(self.api_path, self.api_http_method, json_payload)
        request_url = self.connection.url + self.api_path

        response = None
        try:
            response = requests.put(request_url, headers=self.connection.header_dict, data=json_payload, verify=False)
            response.raise_for_status()
            return {Output.SUCCESS : response is not None}
        except RequestException as rex:
            if response:
                self.logger.error(f"Received status code: {response.status_code}")
                self.logger.error(f"Response was: {response.text}")
            raise PluginException(assistance="Please verify the connection details and input data.",
                                  cause=f"Error processing the Apex request: {rex}")

        return {Output.SUCCESS : False}

