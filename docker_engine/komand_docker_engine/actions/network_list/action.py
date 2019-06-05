import komand
from .schema import NetworkListInput, NetworkListOutput
# Custom imports below
import docker
from ... import helper


class NetworkList(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='network_list',
                description='List available Docker networks',
                input=NetworkListInput(),
                output=NetworkListOutput())

    def run(self, params={}):
        try:
            networks = self.connection.docker_client.networks.list()
        except (docker.errors.DockerException, docker.errors.APIError):
            raise
        else:
            return {'networks': list(map(helper.network_to_json, networks))}

    def test(self):
        """TODO: Test action"""
        return {}
