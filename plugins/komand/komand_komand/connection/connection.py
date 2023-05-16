import insightconnect_plugin_runtime
from .schema import ConnectionSchema
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom import below
import requests


class KomandCredentials(object):
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.credentials = None

    def get_job(self, uid):
        self.logger.debug("fetching job: %s", uid)
        url = self.credentials.base_url + "/v2/jobs/" + uid
        response = self.session().get(url)
        if response.status_code != requests.codes.ok:
            self.logger.error("Failure to get job bad status code : " + str(response.status_code) + str(response.text))
            return None

        job = response.json()

        return job

    def lookup_workflow_name(self, name):
        url = self.credentials.base_url + "/v2/workflows?status=active&minimum=true"
        response = self.session().get(url)

        if response.status_code != requests.codes.ok:
            raise PluginException(
                cause="Unexpected Error",
                assistane=f"Response: {str(response.status_code) + str(response.text)}"
            )
        workflows = r.json()["workflows"]

        for workflow in workflows:
            if workflow["name"] == name:
                return workflow["workflow_uid"]

        return None

    def _get_session_token(self):
        """Obtains a session token via /sessions endpoint using user credentials"""

        self.logger.info("Getting session token for user...")

        url = self.credentials.base_url + "/v2/sessions"
        auth_payload = {
            "user_name": self.credentials.username,
            "user_secret": self.credentials.password,
        }

        auth_response = requests.post(url=url, json=auth_payload)
        auth_response.raise_for_status()

        try:
            token = auth_response.json()["token"]
        except KeyError as error:
            self.logger.error(f"Error obtaining session token: {error}")
        else:
            self.logger.info("Got token!")
            return token

    def session(self):
        """Returns a requests session pre-populated with necessary token"""
        session = requests.Session()
        session.cookies.set(name="jwt", value=self._get_session_token())

        return session

    def connect(self, params):
        self.credentials = KomandCredentials(
            base_url=params["url"],
            username=params["credentials"]["username"],
            password=params["credentials"]["password"],
        )
