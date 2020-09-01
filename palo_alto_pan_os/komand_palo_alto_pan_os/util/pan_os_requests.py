from komand.exceptions import ConnectionTestException, PluginException
import xmltodict
import requests
import json
from komand.connection import Connection
from xmltodict import ParsingInterrupted


class Request(object):
    def __init__(self, logger, url, session, key, verify_cert):
        self.logger = logger
        self.url = url
        self.session = session
        self.key = key
        self.verify_cert = verify_cert

    @classmethod
    def new_session(cls, connection: Connection, username: str, password: str, hostname: str, verify_cert: bool):
        url = hostname + "/api/"
        querystring = {"type": "keygen", "user": username, "password": password}

        try:
            session = requests.session()
            token_response = session.get(url, params=querystring, verify=verify_cert)
            token_dict = cls.get_output_with_exceptions(token_response)
            pan_os_key = token_dict["response"]["result"]["key"]
            connection.logger.info("Key obtained")
        except KeyError:
            raise ConnectionTestException(
                preset=ConnectionTestException.Preset.USERNAME_PASSWORD
            )
        except PluginException as e:
            raise ConnectionTestException(cause=e.cause, assistance=e.assistance, data=e.data)

        return cls(logger=connection.logger, url=url, session=session, key=pan_os_key,
                   verify_cert=verify_cert)

    def edit_(self, xpath: str, element: str) -> dict:
        """
        Overwrites The current element found at the xpath with the new element
        :param xpath: a syntax for selecting nodes from within an XML document
        :param element: information on a object in XML format
        :return Response from PAN-OS
        """

        querystring = {"type": "config", "action": "edit", "key": self.key, "xpath": xpath,
                       "element": element}

        response = self.make_request("SESSION.POST", querystring)
        output = self.get_output_with_exceptions(response)
        return {"response": output}

    def delete_(self, xpath: str) -> dict:
        """
        Deletes the element at the xpath
        :param xpath: a syntax for selecting nodes from within an XML document
        :return Response from PAN-OS
        """

        querystring = {"type": "config", "action": "delete", "key": self.key, "xpath": xpath}

        response = self.make_request("SESSION.GET", querystring)
        output = self.get_output_with_exceptions(response)
        return output

    def get_(self, xpath: str) -> dict:
        """
        Returns the element at the xpath
        :param xpath: syntax for selecting nodes from within an XML document
        :return Response from PAN-OS
        """

        querystring = {"type": "config", "action": "get", "key": self.key, "xpath": xpath}

        response = self.make_request("SESSION.GET", querystring)
        output = self.get_output_with_exceptions(response)
        return output

    def set_(self, xpath: str, element: str) -> dict:
        """
        Creates a new element at the xpath
        :param xpath: a syntax for selecting nodes from within an XML document
        :param element: information on a object in XML format
        :return Response from PAN-OS
        """

        querystring = {"type": "config", "action": "set", "key": self.key, "xpath": xpath,
                       "element": element}

        response = self.make_request("SESSION.POST", querystring)
        output = self.get_output_with_exceptions(response)
        return output

    def show_(self, xpath: str) -> dict:
        """
        Returns the element at the xpath
        :param xpath: a syntax for selecting nodes from within an XML document
        :return Response from PAN-OS
        """

        querystring = {"type": "config", "action": "show", "key": self.key, "xpath": xpath}

        response = self.make_request("SESSION.GET", querystring)
        output = self.get_output_with_exceptions(response)
        return output

    def op(self, cmd: str) -> dict:
        querystring = {"type": "op", "key": self.key, "cmd": cmd}

        response = self.make_request("SESSION.GET", querystring)
        output = self.get_output_with_exceptions(response)
        return output

    def commit(self, action: str, cmd: str) -> dict:
        querystring = {"type": "commit", "action": action,
                       "key": self.key, "cmd": cmd}

        response = self.make_request("REQUESTS.GET", querystring)
        output = self.get_output_with_exceptions(response)
        return output

    def make_request(self, method, params):
        response = {"text": ""}
        try:
            if method == "SESSION.POST":
                response = self.session.post(self.url, params=params, verify=self.verify_cert)
            elif method == "SESSION.GET":
                response = self.session.get(self.url, params=params, verify=self.verify_cert)
            elif method == "REQUESTS.GET":
                response = requests.get(self.url, params=params, verify=self.verify_cert)
        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Call to Palo Alto Firewall API failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)

        return response

    @staticmethod
    def get_output_with_exceptions(response):
        if response.status_code == 401:
            raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD, data=response.text)
        if response.status_code == 403:
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED, data=response.text)
        if response.status_code == 404:
            raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
        if 400 <= response.status_code < 500:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        if response.status_code >= 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR)

        try:
            output = xmltodict.parse(response.text)
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
        except TypeError:
            raise PluginException(cause='The response from PAN-OS was not the correct data type.',
                                  assistance='Contact support for help.',
                                  data=response.text)
        except ValueError:
            raise PluginException(cause='The response from PAN-OS was not the correct form (XML).',
                                  assistance='Contact support for help.',
                                  data=response.text)
        except ParsingInterrupted:
            raise PluginException(cause='The response from PAN-OS was not the correct form (XML).',
                                  assistance='Contact support for help.',
                                  data=response.text)
        except SyntaxError:
            raise PluginException(cause='The response from PAN-OS was malformed.',
                                  assistance='Contact support for help.',
                                  data=response.text)
        except BaseException as e:
            raise PluginException(cause='An unknown error occurred when parsing the PAN-OS response.',
                                  assistance='Contact support for help.',
                                  data=f'{response.text}, error {e}')

        if output.get('response', {}).get('@status') == 'error':
            error = output['response']['msg']
            error = json.dumps(error)
            raise PluginException(
                cause='PAN-OS returned an error in response to the request.',
                assistance='Double that check inputs are valid. Contact support if this issue persists.',
                data=error
            )

        return output
