import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
import oauth2client.service_account
import apiclient
import httplib2


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.service = None

    def connect(self, params):
        admin_user = params.get(Input.ADMIN_USER)
        client_email = params.get(Input.CLIENT_EMAIL)

        # JSON that will be used to connect to Google
        auth = {
            "type": "service_account",
            "admin_user": admin_user,
            "project_id": params.get(Input.PROJECT_ID),
            "private_key_id": params.get(Input.PRIVATE_KEY_ID),
            "private_key": params.get(Input.PRIVATE_KEY).get("privateKey"),
            "client_email": client_email,
            "client_id": params.get(Input.CLIENT_ID),
            "auth_uri": params.get(Input.AUTH_URI),
            "token_uri": params.get(Input.TOKEN_URI),
            "auth_provider_x509_cert_url": params.get(Input.AUTH_PROVIDER_X509_CERT_URL),
            "client_x509_cert_url": params.get(Input.CLIENT_X509_CERT_URL),
        }

        self.logger.info(f"Connecting {client_email} as {admin_user}")

        scopes = ["https://www.googleapis.com/auth/drive"]

        # Fix escaping issues in private_key
        if "\\n" in auth["private_key"]:
            auth["private_key"] = auth["private_key"].replace("\\n", "\n", -1)

        # Build a Google credentials object
        credentials = oauth2client.service_account.ServiceAccountCredentials.from_json_keyfile_dict(auth, scopes=scopes)

        # Delegate control to 'admin_user'
        delegated_credentials = credentials.create_delegated(admin_user)

        # Connect to Google Drive
        http = delegated_credentials.authorize(httplib2.Http())
        self.service = apiclient.discovery.build("drive", "v3", http=http)
