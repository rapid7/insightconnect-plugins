import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below
from google.cloud import bigquery
from google.oauth2 import service_account


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params):
        self.logger.info(f"Connect: Connecting...")
        self.client = bigquery.Client(
            project=params.get(Input.PROJECT_ID),
            credentials=service_account.Credentials.from_service_account_info({
              "type": "service_account",
              "project_id": params.get(Input.PROJECT_ID),
              "private_key_id": params.get(Input.PRIVATE_KEY_ID),
              "private_key": params.get(Input.PRIVATE_KEY).get("privateKey").replace('\\n', "\n", -1),
              "client_email": params.get(Input.CLIENT_EMAIL),
              "client_id": params.get(Input.CLIENT_ID),
              "auth_uri": params.get(Input.AUTH_URI),
              "client_x509_cert_url": params.get(Input.CLIENT_X509_CERT_URL),
              "token_uri": params.get(Input.TOKEN_URI, "https://oauth2.googleapis.com/token"),
              "auth_provider_x509_cert_url": params.get(Input.AUTH_PROVIDER_X509_CERT_URL,
                                                        "https://www.googleapis.com/oauth2/v1/certs")
            })
        )

    def test(self):
        query_job = self.client.query('SELECT 1')
        return {
            "Success": len(query_job.result()) != 0
        }
