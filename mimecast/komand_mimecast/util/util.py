from komand_mimecast.util.log_helper import LogHelper
from komand.exceptions import PluginException
import json
import base64
import hashlib
import hmac
import uuid
import datetime
import requests


# For mapping params{} to the values needed for request payloads
def normalize(key: str, value: str) -> dict:
    if '_' not in key:
        if value != '' and value != 'none':
            return {key: value}
        return {}

    chunks = list(filter(lambda c: len(c), key.split("_")))

    for i in range(1, len(chunks)):
        chunks[i] = chunks[i].capitalize()
    if value != '' and value != 'none':
        return {''.join(chunks): value}
    return {}


class MimecastRequests:

    def __init__(self, logger=None):
        if logger:
            self.logger = logger
        else:
            self.logger = LogHelper().logger

    def mimecast_post(self, url: str, uri: str, access_key: str,
                      secret_key: str, app_id: str, app_key: str, data: dict, meta: dict = None) -> dict:
        """
        This method will send a properly formatted post request to the Mimecast server
        :param url: The server URL
        :param uri: The URI for the api call
        :param access_key: The access key for the session
        :param secret_key: The secret key for the session
        :param app_id: The application ID for the app that will be logging in
        :param app_key: The key associated with the app_id
        :param data: The payload for the api call
        :param meta: The meta information for request
        :return:
        """
        # Set full URL
        url = url + uri

        # Generate request header values
        request_id = str(uuid.uuid4())
        hdr_date = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S") + " UTC"

        # Decode secret key
        encoded_secret_key = secret_key.encode()
        bytes_secret_key = base64.b64decode(encoded_secret_key)

        # Create hmac message
        msg = ':'.join([hdr_date, request_id, uri, app_key])

        # Create the HMAC SHA1 of the Base64 decoded secret key for the Authorization header
        hmac_sha1 = hmac.new(bytes_secret_key, msg.encode(), digestmod=hashlib.sha1).digest()

        # Use the HMAC SHA1 value to sign the hdrDate + ":" requestId + ":" + URI + ":" + appkey
        sig = base64.encodebytes(hmac_sha1).rstrip()
        sig = sig.decode('UTF-8')

        # Create request headers
        headers = {
            'Authorization': 'MC ' + access_key + ':' + sig,
            'x-mc-app-id': app_id,
            'x-mc-date': hdr_date,
            'x-mc-req-id': request_id,
            'Content-Type': 'application/json'
        }

        # build payload data
        if data is not None:
            payload = {
                'data': [
                    data
                ]
            }
        else:
            payload = {
                'data': [
                ]
            }

        if meta is not None:
            payload['meta'] = meta

        try:
            request = requests.post(url=url, headers=headers, data=str(payload))
        except requests.exceptions.RequestException as e:
            raise PluginException(data=e)

        try:
            response = request.json()
        except json.decoder.JSONDecodeError:
            self.logger.error(request.text)
            raise PluginException(cause='Unknown error.',
                                  assistance='The Mimecast server did not respond correctly. Response not in JSON format. Response in logs.')

        try:
            # Check for expired key
            if response['fail']:
                for errors in response['fail']:
                    for codes in errors['errors']:
                        if codes['code'] == 'err_xdk_binding_expired':
                            raise PluginException(cause='AccessKey has expired.',
                                                  assistance='Please provide a valid AccessKey.')
        except KeyError:
            self.logger.error(response)
            raise PluginException(cause='Unknown error.',
                                  assistance='The Mimecast server did not respond correctly. Response in logs.')

        try:
            if response['meta']['status'] != 200:
                self.logger.error(response['fail'])
                raise PluginException(cause='Server request failed.',
                                      assistance='Status code is {}, see log for details.'.format(
                                          response['meta']['status']))
        except KeyError:
            self.logger.error(response)
            raise PluginException(cause='Unknown error.',
                                  assistance='The Mimecast server did not respond correctly. Response in logs.')

        return response
