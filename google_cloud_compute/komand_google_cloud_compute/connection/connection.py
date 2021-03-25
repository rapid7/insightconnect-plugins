import insightconnect_plugin_runtime
import oauth2client.service_account
from googleapiclient import discovery
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException

from .schema import ConnectionSchema

# Custom imports below
from ..util.api import GoogleCloudComputeAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params={}):
        # JSON that will be used to connect to Google
        auth = {
            "type": "service_account",
            "project_id": params.get("project_id"),
            "private_key_id": params.get("private_key_id"),
            "private_key": params.get("private_key").get("privateKey"),
            "client_email": params.get("client_email"),
            "client_id": params.get("client_id"),
            "auth_uri": params.get("auth_uri"),
            "token_uri": params.get("token_uri"),
            "auth_provider_x509_cert_url": params.get("auth_provider_x509_cert_url"),
            "client_x509_cert_url": params.get("client_x509_cert_url"),
        }

        scopes = ["https://www.googleapis.com/auth/compute"]

        # Fix escaping issues in private_key
        private_key = auth["private_key"]

        if "\\n" in private_key:
            auth["private_key"] = private_key.replace("\\n", "\n", -1)

        # Build a Google credentials object
        credentials = oauth2client.service_account.ServiceAccountCredentials.from_json_keyfile_dict(auth, scopes=scopes)

        self.client = GoogleCloudComputeAPI(
            discovery.build("compute", "v1", credentials=credentials), params.get("project_id")
        )

    def test(self):
        try:
            return {"success": self.client.list_zones()["id"]}
        except PluginException as e:
            raise ConnectionTestException(cause=e.cause, assistance=e.assistance, data=e.data)
