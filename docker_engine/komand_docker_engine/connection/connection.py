import komand
from .schema import ConnectionSchema
# Custom imports below
import docker
from .. import helper


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.docker_client = None

    def connect(self, params={}):
        client_cert = (
            helper.key_to_file(params.get('client_cert').get('secretKey')),
            helper.key_to_file(params.get('client_key').get('secretKey'))
        )
        ca_cert = helper.key_to_file(params.get('ca_cert').get('secretKey'))
        tls_config = docker.tls.TLSConfig(
            client_cert=client_cert,
            ca_cert=ca_cert
        )
        base_url = params.get('url')

        try:
            self.logger.info("Connect: Connecting to {}".format(base_url))
            self.docker_client = docker.DockerClient(
                base_url=base_url,
                tls=tls_config,
                version=params.get('api_version')
            )
        except docker.errors.DockerException:
            raise
        else:
            self.logger.info("Connect: Connected to {} successfully.".format(base_url))
