import komand
from .schema import NetworkGetInput, NetworkGetOutput
# Custom imports below
import docker
from ... import helper


class NetworkGet(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='network_get',
                description='Get a Docker network by ID',
                input=NetworkGetInput(),
                output=NetworkGetOutput())

    def run(self, params={}):
        try:
            network = self.connection.docker_client.networks.get(params.get('id'))
        except (docker.errors.DockerException, docker.errors.APIError):
            raise
        else:
            return {'network': helper.network_to_json(network)}

    def test(self):
        """TODO: Test action"""
        return {}
