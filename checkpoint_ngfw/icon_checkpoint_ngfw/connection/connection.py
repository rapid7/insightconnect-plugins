import komand
from .schema import ConnectionSchema, Input
# Custom imports below
from komand.exceptions import PluginException, ConnectionTestException
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.username = params.get(Input.USERNAME_PASSWORD, {}).get("username")
        self.password = params.get(Input.USERNAME_PASSWORD, {}).get("password")

        self.ssl_verify = params.get(Input.SSL_VERIFY)
        self.server_ip = params.get(Input.SERVER)
        self.server_port = params.get(Input.PORT)

        self.server_and_port = f"https://{self.server_ip}:{self.server_port}"

        self.get_sid()

    def get_sid(self):
        url = f"{self.server_and_port}/web_api/login"
        payload = {
            "user": self.username,
            "password": self.password
        }

        request = requests.post(url, json=payload, verify=self.ssl_verify)

        try:
            request.raise_for_status()
        except Exception:
            # The errors returned by this api aren't very good
            # It's a 400 with some error text.
            raise PluginException(cause="There was problem authenticating with Check Point NGFW.",
                                  assistance="Check the server IP address, port, username, and password defined in "
                                             "your plugin connection",
                                  data=request.text)

        self.sid = request.json().get("sid")

    def publish(self):
        url = f"{self.server_and_port}/web_api/publish"
        payload = {}  # Yes, the API requires an empty json object
        headers = self.get_headers()

        request = requests.post(url, json=payload, headers=headers, verify=self.ssl_verify)
        try:
            request.raise_for_status()
        except Exception as e:
            # The errors returned by this api aren't very good
            # It's a 400 with some error text.
            raise PluginException(cause="There was problem publishing to Checkpoint NGFW.",
                                  assistance=request.text,
                                  data=e)

    def logout(self):
        url = f"{self.server_and_port}/web_api/logout"
        payload = {}
        headers = self.get_headers()

        request = requests.post(url, json=payload, headers=headers, verify=self.ssl_verify)
        try:
            request.raise_for_status()
        except Exception as e:
            # The errors returned by this api aren't very good
            # It's a 400 with some error text.
            raise PluginException(cause="There was problem logging out.",
                                  assistance=request.text,
                                  data=e)

    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "X-chkp-sid": self.sid
        }

    def discard_all_sessions(self):
        """
        This method will get all open sessions, discard all of them, then get a new session ID.
        This is a last ditch effort when you need to fix this:
        'Runtime error: An object is locked by another session.'
        """

        url = f"{self.server_and_port}/web_api/show-sessions"
        headers = self.get_headers()
        payload = {
            "limit": 20,  # This will make 20 calls to the API at most, if there are more sessions than that its trouble
            "view-published-sessions": False
        }
        request = requests.post(url, json=payload, headers=headers, verify=self.ssl_verify)
        try:
            request.raise_for_status()
        except Exception as e:
            # The errors returned by this api aren't very good
            # It's a 400 with some error text.
            raise PluginException(cause="There was problem publishing to Checkpoint NGFW.",
                                  assistance=request.text,
                                  data=e)

        url_discard = f"{self.server_and_port}/web_api/discard"
        sessions = request.json().get("objects")
        for session in sessions:
            uid = session.get("uid")
            discard_payload = {
                "uid": uid
            }

            requests.post(url_discard, json=discard_payload, headers=headers, verify=self.ssl_verify)

        self.publish() # Yes, you have to publish that you are not publishing
        self.logout()

        self.get_sid()

    def post_and_publish(self, headers, discard_other_sessions, payload, url):
        result = requests.post(url, headers=headers, json=payload, verify=self.ssl_verify)
        # This gets odd. If you try to publish a change while someone else is working on a change it will fail
        # I give the user an option to discard all sessions, however, I don't want to do that unless I have to
        # as it's an expensive operation (could take a couple minutes)
        # So, try to make the change, if it's locked, see if we need to discard all sessions and try to make the
        # call again.
        try:
            result.raise_for_status()
        except Exception:
            self.logger.warning(result.text)
            if "object is locked" in result.text:
                if discard_other_sessions:
                    self.discard_all_sessions()
                    result = requests.post(url, headers=headers, json=payload, verify=self.ssl_verify)

            # try to see if we still have a bad request
            try:
                result.raise_for_status()
            except Exception as e:
                raise PluginException(cause=f"Call to {url} failed.",
                                      assistance=result.text,
                                      data=e)

        self.publish()
        self.logout()

        return result

    def test(self):
        if not self.sid:
            raise ConnectionTestException(cause=f"Unable to authenticate to the Check Point server at: "
                                                f"{self.server_ip}:{self.server_port}",
                                          assistance="Please check your connection settings and try again.")
        return {"success": True}


