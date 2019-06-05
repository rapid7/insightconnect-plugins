from komand_mimecast.util.log_helper import LogHelper
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


class Authentication:
    # URI's for login and logout
    _URI_LOGIN = '/api/login/login'
    _URI_LOGOUT = '/api/login/logout'

    def __init__(self, logger=None):
        if logger:
            self.logger = logger
        else:
            self.logger = LogHelper().logger

    def login(self, url: str, username: str, password: str, auth_type: str, app_id: str) -> dict:
        """
        This method is used to create the initial connection and return an access and secret key
        for further api calls
        :param url: The server URL
        :param username: Username to login with
        :param password: Users password
        :param auth_type: The type of authentication: cloud or domain
        :param app_id: The application ID for the app that will be logging in
        :return: an access_key and a secret_key
        """
        # Set full URL
        url = url + self._URI_LOGIN

        # Base64 encode credentials
        credentials = username + ':' + password
        credentials = base64.b64encode(credentials.encode())
        credentials = credentials.decode("UTF-8")

        # Generate request header values
        request_id = str(uuid.uuid4())
        hdr_date = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S") + " UTC"

        # Create request headers
        headers = {
            'Authorization': auth_type + ' ' + credentials,
            'x-mc-app-id': app_id,
            'x-mc-date': hdr_date,
            'x-mc-req-id': request_id,
            'Content-Type': 'application/json'
        }

        payload = {
            "data": [
                {
                    "userName": username
                }
            ]
        }

        try:
            request = requests.post(url=url, headers=headers, data=str(payload))
        except requests.exceptions.RequestException as e:
            raise Exception(e)

        if request.status_code in range(300, 399):
            raise Exception(f'Redirect error. The Mimecast server responded with a {request.status_code} code.'
                            f' Check the Mimecast URL and contact support if this issue persists')
        if request.status_code in range(400, 499):
            self.logger.error(request.text)
            raise Exception(f'Bad request error. The Mimecast server responded with a {request.status_code} code.'
                            f' Check the username and password, as well as the Mimecast app ID and key.')

        try:
            response = request.json()
        except json.decoder.JSONDecodeError:
            self.logger.error(request.text)
            raise Exception(
                'Unknown error. The Mimecast server did not respond correctly. Response not in JSON format. Response in logs')

        try:
            # Catch errors returned by Mimecast api
            if response['fail']:
                self.logger.error(response['fail'])
                raise Exception(
                    'Failed to authenticate. Please double-check the credentials in the Connection.'
                    ' If the issue persists, please contact support.'
                    ' Status code is {code},'
                    ' Mimecast error message: {message}. See log for more details'.format(code=response['meta']['status'],
                                                                                          message=response['fail'][0]['message']))

        except KeyError:
            self.logger.error(response)
            raise Exception(
                'Unknown error. The Mimecast server did not respond correctly. See the response in logs')

        try:
            access_key = response['data'][0]['accessKey']
        except KeyError:
            self.logger.error(response)
            raise Exception('Error: Unable to authenticate to the Mimecast API.'
                            ' Please double-check the credentials in the Connection.'
                            ' If the issue persists, please contact support. See log for more details')

        try:
            secret_key = response['data'][0]['secretKey']
            self.logger.error(response)
        except KeyError:
            raise Exception('Error: Unable to authenticate to the Mimecast API.'
                            ' Please double-check the credentials in the Connection.'
                            ' If the issue persists, please contact support. See log for more details')

        return {'access_key': access_key, 'secret_key': secret_key}

    def refresh_key(self, url: str, username: str, password: str,
                    access_key: str, app_id: str, auth_type: str)-> dict:
        """
        This method is used to refresh a connection if the connection has timed out.
        :param url: The server URL
        :param username: Username to login with
        :param password: Users password
        :param access_key: The access_key for the connection that needs to be refreshed
        :param auth_type: The type of authentication: cloud or domain
        :param app_id: The application ID for the app that will be logging in
        :param auth_type: The auth type used
        :return: A dictionary that contains information about the connection refresh
        """
        # Set full URL
        url = url + self._URI_LOGIN

        # Generate request header values
        request_id = str(uuid.uuid4())
        hdr_date = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S") + " UTC"

        # Base64 encode credentials
        credentials = username + ':' + password
        credentials = base64.b64encode(credentials.encode())
        credentials = credentials.decode("UTF-8")

        # Create request headers
        headers = {
            'Authorization': auth_type + ' ' + credentials,
            'x-mc-app-id': app_id,
            'x-mc-date': hdr_date,
            'x-mc-req-id': request_id,
            'Content-Type': 'application/json'
        }

        payload = {
            "data": [
                {
                    "userName": username,
                    "accessKey": access_key
                }
            ]
        }

        try:
            request = requests.post(url=url, headers=headers, data=str(payload))
        except requests.exceptions.RequestException as e:
            raise Exception(e)

        try:
            response = request.json()
        except json.decoder.JSONDecodeError:
            self.logger.error(request.text)
            raise Exception(
                'Unknown error. The Mimecast server did not respond correctly. Response not in JSON format. Response in logs')

        try:
            # Catch errors returned by Mimecast api
            if response['fail']:
                self.logger.error(response['fail'])
                raise Exception(
                    'Failed to refresh key. Status code is {}, see log for details'.format(
                        response['meta']['status']))

        except KeyError:
            self.logger.error(response)
            raise Exception(
                'Unknown error. Mimecast server did not respond correctly. Response in logs')

        return response

    def logout(self, url: str, username: str, password: str, auth_type: str,
               access_key: str, secret_key: str, app_id: str, app_key: str, refresh=False)-> dict:
        """
        This method removes the binding of an access and secret key to a username.
        This method should always be called when an action is finished, as too many keys bound to
        a user will lockout the user
        :param url: The server URL
        :param username: Username to login with
        :param password: Users password
        :param auth_type: The type of authentication: cloud or domain
        :param access_key: The access key to unbind
        :param secret_key: The secret key to unbind
        :param app_id: The application ID for the app that will be logging in
        :param app_key: The key associated with the app_id
        :param refresh: Used to stop possible infinite loop with key refresh recursive function
        :return: Dictionary with information about logout
        """
        # Set full URL
        url = url + self._URI_LOGOUT

        # Generate request header values
        request_id = str(uuid.uuid4())
        hdr_date = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S") + " UTC"

        # Decode secret key
        encoded_secret_key = secret_key.encode()
        bytes_secret_key = base64.b64decode(encoded_secret_key)

        # Create hmac message
        msg = ':'.join([hdr_date, request_id, self._URI_LOGOUT, app_key])

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

        payload = {
            "data": [
                {
                    "accessKey": access_key
                }
            ]
        }

        # Logout
        try:
            request = requests.post(url=url, headers=headers, data=str(payload))
        except requests.exceptions.RequestException as e:
            raise Exception(e)

        try:
            response = request.json()
        except json.decoder.JSONDecodeError:
            self.logger.error(request.text)
            raise Exception(
                'Unknown error. The Mimecast server did not respond correctly. Response not in JSON format. Response in logs')

        # Check for expired key
        try:
            if response['fail']:
                for errors in response['fail']:
                    for codes in errors['errors']:
                        if codes['code'] == 'err_xdk_binding_expired':
                            self.logger.info('Key expired. Refreshing')
                            # Try to refresh key
                            self.refresh_key(url, username,
                                             password, access_key,
                                             app_id, auth_type)

                            # Rerun logout with refreshed key
                            if not refresh:
                                self.logout(url, username, password,
                                            auth_type, access_key,
                                            secret_key, app_id, access_key, True)
                        else:
                            self.logger.error(response)
                            raise Exception('Something went wrong. Contact support')
        except KeyError:
            self.logger.error(response)
            raise Exception(
                'Unknown error. The Mimecast server did not respond correctly. Response in logs')

        return response


class MimecastRequests:

    def __init__(self, logger=None):
        if logger:
            self.logger = logger
        else:
            self.logger = LogHelper().logger

    def mimecast_post(self, url: str, uri: str, username: str, password: str, auth_type: str,
                      access_key: str, secret_key: str, app_id: str, app_key: str, data: dict, refresh=False)-> dict:
        """
        This method will send a properly formatted post request to the Mimecast server
        :param url: The server URL
        :param uri: The URI for the api call
        :param username: Username to login with
        :param password: Users password
        :param auth_type: The type of authentication: cloud or domain
        :param access_key: The access key for the session
        :param secret_key: The secret key for the session
        :param app_id: The application ID for the app that will be logging in
        :param app_key: The key associated with the app_id
        :param data: The payload for the api call
        :param refresh: Used to stop possible infinite loop with key refresh recursive function
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

        try:
            request = requests.post(url=url, headers=headers, data=str(payload))
        except requests.exceptions.RequestException as e:
            logout = Authentication()
            logout.logout(url, username, password,
                          auth_type, access_key,
                          secret_key, app_id, access_key)
            raise Exception(e)
        try:
            response = request.json()
        except json.decoder.JSONDecodeError:
            self.logger.error(request.text)
            logout = Authentication()
            logout.logout(url, username, password,
                          auth_type, access_key,
                          secret_key, app_id, access_key)
            raise Exception(
                'Unknown error. The Mimecast server did not respond correctly. Response not in JSON format. Response in logs')

        try:
            # Check for expired key
            if response['fail']:
                for errors in response['fail']:
                    for codes in errors['errors']:
                        if codes['code'] == 'err_xdk_binding_expired':
                            self.logger.info('Key expired. Refreshing')
                            # Try to refresh key
                            refresh_key = Authentication()
                            refresh_key.refresh_key(url, username,
                                                    password, access_key,
                                                    app_id, auth_type)

                            # Resend request after key refresh
                            if not refresh:
                                response = self.mimecast_post(url, uri,
                                                              access_key, secret_key,
                                                              app_id, app_key, data, True)

        except KeyError:
            self.logger.error(response)
            logout = Authentication()
            logout.logout(url, username, password,
                          auth_type, access_key,
                          secret_key, app_id, access_key)
            raise Exception(
                    'Unknown error. The Mimecast server did not respond correctly. Response in logs')

        try:
            if response['fail']:
                self.logger.error(response['fail'])
                logout = Authentication()
                logout.logout(url, username, password,
                              auth_type, access_key,
                              secret_key, app_id, access_key)
                raise Exception(
                    'Server request failed. Status code is {}, see log for details'.format(
                        response['meta']['status']))

        except KeyError:
            self.logger.error(response)
            logout = Authentication()
            logout.logout(url, username, password,
                          auth_type, access_key,
                          secret_key, app_id, access_key)
            raise Exception(
                'Unknown error. The Mimecast server did not respond correctly. Response in logs')

        return response
