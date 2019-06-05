import komand
from .schema import ConnectionSchema
# Custom imports below
import urllib
import tempfile
from boxsdk import JWTAuth, Client


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.box_connection = None

    def store_tokens(self, access_token, refresh_token):
        r_token = refresh_token
        a_token = access_token

    def connect(self, params={}):
        client_id = params.get('client_id')
        client_secret = params.get('client_secret').get("secretKey")
        enterprise_id = params.get('enterprise_id')
        jwt_key_id = params.get('jwt_key_id')
        password = params.get('rsa_password').get("secretKey").encode()
        private_key = params.get('private_key').get("secretKey")

        self.logger.info("Connect: Connecting..")

        # Fix escaping issues in private_key
        if '\\n' in private_key:
            private_key = private_key.replace('\\n', "\n", -1)

        # Try to connect with the legacy code
        try:

            # store private key
            parsed_private_key = urllib.parse.unquote_plus(private_key)
            f = tempfile.NamedTemporaryFile('w')
            f.write(parsed_private_key)
            f.seek(0)

            auth = JWTAuth(client_id=client_id,
                           client_secret=client_secret,
                           enterprise_id=enterprise_id,
                           jwt_key_id=jwt_key_id,
                           rsa_private_key_file_sys_path=f.name,
                           store_tokens=self.store_tokens,
                           rsa_private_key_passphrase=password
                           )
            self.box_connection = Client(auth)
            access_token = auth.authenticate_instance()

            self.logger.info("Connect: Connection successful")
            f.close()

        # if legacy connection fails try to connect with new code
        except ValueError:

            # store private key
            f = tempfile.NamedTemporaryFile('w')
            f.write(private_key)
            f.seek(0)

            auth = JWTAuth(client_id=client_id,
                           client_secret=client_secret,
                           enterprise_id=enterprise_id,
                           jwt_key_id=jwt_key_id,
                           rsa_private_key_file_sys_path=f.name,
                           rsa_private_key_passphrase=password
                           )
            self.box_connection = Client(auth)
            access_token = auth.authenticate_instance()

            self.logger.info("Connect: Connection successful")
            f.close()
