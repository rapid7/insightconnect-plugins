import komand
from .schema import ConnectionSchema
from komand.exceptions import ConnectionTestException
# Custom imports below
from dxlclient.broker import Broker
from dxlclient.client import DxlClient
from dxlclient.client_config import DxlClientConfig


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        broker_ca, client_crt, client_key, address = params.get('broker_ca').get('privateKey'), \
                                                     params.get('client_crt').get('privateKey'), \
                                                     params.get('client_key').get('privateKey'), \
                                                     params.get('host')

        # Fix escaping issues in keys
        broker_ca = self.fix_escaping_issues(broker_ca)
        client_crt = self.fix_escaping_issues(client_crt)
        client_key = self.fix_escaping_issues(client_key)

        # Create temp files for certificates
        with open('broker_ca', 'w') as broker_ca_file:
            broker_ca_file.write(broker_ca)
        with open('client_crt', 'w') as client_crt_file:
            client_crt_file.write(client_crt)
        with open('client_key', 'w') as client_key_file:
            client_key_file.write(client_key)

        self.config = DxlClientConfig(
            broker_ca_bundle=broker_ca_file.name,
            cert_file=client_crt_file.name,
            private_key=client_key_file.name,
            brokers=[Broker.parse('ssl://{}'.format(address))])

        self.logger.info("Connect: Connecting...")

    def test(self):
        try:
            with DxlClient(self.config) as dxl_client:
                # Connect to the fabric
                dxl_client.connect()
            return True
        except:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE)

    def fix_escaping_issues(self, crt: str)-> str:
        # Fix \n being replaced by \\n
        if '\\n' in crt:
            crt = crt.replace('\\n', '\n', -1)

        # Fix \n being replaced by \s
        certlist = crt.split()
        newcert = certlist.pop(0)
        for line in certlist:
            if line == 'CERTIFICATE-----':
                newcert = newcert + ' ' + line
            elif line == 'PRIVATE':
                newcert = newcert + ' ' + line
            elif line == 'KEY-----':
                newcert = newcert + ' ' + line
            else:
                newcert = newcert + '\n' + line
        newcert = newcert + '\n'
        return newcert
