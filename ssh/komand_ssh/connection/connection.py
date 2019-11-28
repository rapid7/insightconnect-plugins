import komand
from .schema import ConnectionSchema

# Custom imports below
import base64
import paramiko
import io


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect_key(self, params):
        self.logger.info("connecting via key")

        key = base64.b64decode(params.get('key').get('privateKey')).strip().decode("utf-8")
        fd = io.StringIO(key)
        k = paramiko.RSAKey.from_private_key(fd, password=params.get('password').get('secretKey'))

        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.load_system_host_keys()

        s.connect(
          params.get('host'), 
          params.get('port'), 
          username=params.get('username').get('secretKey'),
          pkey=k
        )
        return s

    def connect_password(self, params):
        self.logger.info("connecting via password")
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.load_system_host_keys()
        s.connect(
          params.get('host'),
          params.get('port'), 
          params.get('username').get('secretKey'), 
          params.get('password').get('secretKey')
        )
        return s

    def client(self, host=None):
        if host:
            self.parameters['host'] = host
        if self.parameters.get('use_key'):
            return self.connect_key(self.parameters)
        else:
            return self.connect_password(self.parameters)

    def connect(self, params):
        self.logger.info("connecting")
        self.host = params.get('host')

    def test(self):
        client = self.client(self.host)
        client.close()

        return {"connection": "successful"}
