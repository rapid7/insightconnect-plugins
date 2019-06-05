import komand
from .schema import ConnectionSchema
from netmiko import ConnectHandler
from os import path
import os
import base64


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.device = {}
        self.device_connect = None

    def connect_key(self, params={}):
        home_dir = (path.expanduser('~'))
        key_file = "{}/.ssh".format(home_dir)
        f = params.get('key').get('privateKey')
        fb = f.get('content')
        fb64 = base64.b64decode(fb)
        fb64 = fb64.decode("utf-8")
        if not path.exists(key_file):
            os.makedirs(key_file)
            os.chmod(key_file, 0o700)
        key_file_path = path.join(key_file, "id_rsa")
        with open(key_file_path, 'w+') as f:
            f.write(fb64)
        os.chmod(key_file_path, 0o600)
        self.logger.info("Establishing connection")
        device = {'device_type': params.get('device_type'), 'ip': params.get('host'),
                  'username': params.get('credentials').get('username'), 'use_keys': True, 'key_file': key_file_path,
                  'password': params.get('credentials').get('password'), 'port': params.get('port'),
                  'secret': params.get('secret').get('secretKey'), 'allow_agent': True, 'global_delay_factor': 4}
        self.device_connect = ConnectHandler(**device)
        return self.device_connect

    def connect_password(self, params={}):
        self.logger.info("Establishing connection")
        device = {'device_type': params.get('device_type'), 'ip': params.get('host'),
                  'username': params.get('credentials').get('username'), 'password': params.get('credentials').get('password'),
                  'port': params.get('port'), 'secret': params.get('secret').get('secretKey'), 'global_delay_factor': 4}
        self.device_connect = ConnectHandler(**device)
        return self.device_connect

    def client(self, host=None):
        if host:
            self.parameters['host'] = host
        if self.parameters.get('key'):
            self.logger.info("Using key...")
            self.logger.info(self.parameters)
            return self.connect_key(self.parameters)
        else:
            self.logger.info("Using password...")
            return self.connect_password(self.parameters)

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.client(params.get('host'))
