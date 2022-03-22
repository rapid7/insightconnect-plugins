import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
import googleapiclient.discovery
from googleapiclient.errors import HttpError
from google.oauth2 import service_account


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.auth = None
        self.service = None
        self.scopes = ["https://www.googleapis.com/auth/admin.directory.user"]
        self.credentials = None
        self.read_only = False

    def connect(self, params):
        admin_user = params.get(Input.ADMIN_USER)
        project_id = params.get(Input.PROJECT_ID)
        private_key_id = params.get(Input.PRIVATE_KEY_ID)
        private_key = params.get(Input.PRIVATE_KEY).get("privateKey")
        client_email = params.get(Input.CLIENT_EMAIL)
        client_id = params.get(Input.CLIENT_ID)
        client_x509_cert_url = params.get(Input.CLIENT_X509_CERT_URL)
        auth_uri = params.get(Input.AUTH_URI)
        token_uri = params.get(Input.TOKEN_URI)
        auth_provider_x509_cert_url = params.get(Input.AUTH_PROVIDER_X509_CERT_URL)
        self.scopes = [params.get(Input.OAUTH_SCOPE, "https://www.googleapis.com/auth/admin.directory.user")]
        if self.scopes == ["https://www.googleapis.com/auth/admin.directory.user.readonly"]:
            self.read_only = True
        self.logger.info(f"Using OAuth scope ({self.scopes}) for connections")

        # JSON that will be used to connect to Google
        auth = {
            "type": "service_account",
            "project_id": project_id,
            "private_key_id": private_key_id,
            "private_key": private_key,
            "client_email": client_email,
            "client_id": client_id,
            "auth_uri": auth_uri,
            "token_uri": token_uri,
            "auth_provider_x509_cert_url": auth_provider_x509_cert_url,
            "client_x509_cert_url": client_x509_cert_url,
        }

        # Fix escaping issues in private_key
        if "\\n" in auth["private_key"]:
            auth["private_key"] = auth["private_key"].replace("\\n", "\n", -1)

        # Build a Google credentials object
        self.credentials = service_account.Credentials.from_service_account_info(auth, scopes=self.scopes)

        # Delegate to admin user
        self.configure_delegation(admin_user)

    def configure_delegation(self, user):
        """
        set_delegation modifies the self.service attribute to be delegated for the provided
        user. This ensures that delegation can be performed for any user in an action when using
        domain-wide delegation on a service account
        :param user: user email which should be delegated, if None will use the service account user
        :return user: user string value to be used in API requests
        """
        self.logger.info(f"Impersonating user {user}")

        # Delegate control to user
        delegated_credentials = self.credentials.with_subject(user)

        # Discovery caching isn't supported in this version of the client, but the default is
        # to have it on so it needs to bbe explicitly turned off
        self.service = googleapiclient.discovery.build(
            "admin", "directory_v1", credentials=delegated_credentials, cache_discovery=False
        )

    def test(self):
        try:
            # Test the service account using the discovery API
            # which doesn't require an OAuth scope
            service = googleapiclient.discovery.build(
                "discovery", "v1", credentials=self.credentials, cache_discovery=False
            )
            service.apis().list(name="admin", preferred=True).execute()
            return {"success": True}
        except HttpError as e:
            raise ConnectionTestException(
                cause=f"Failed to retrieve Admin SDK API info via the provided service account, API error: {e}",
                assistance="Verify the input service credentials and the permissions on the service account.",
            )
