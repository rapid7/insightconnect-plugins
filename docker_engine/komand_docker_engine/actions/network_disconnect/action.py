import komand
from .schema import NetworkDisconnectInput, NetworkDisconnectOutput
# Custom imports below
import docker


class NetworkDisconnect(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='network_disconnect',
                description='Disconnect a container from a network by ID',
                input=NetworkDisconnectInput(),
                output=NetworkDisconnectOutput())

    def run(self, params={}):
        try:
            network = self.connection.docker_client.networks.get(params.get('network_id'))
            network.disconnect(params.get('container_id'))
        except (docker.errors.DockerException, docker.errors.APIError):
            self.logger.exception('Unable to disconnect container from network.')
            success = False
        else:
            success = True
        return {'success': success}

    def test(self):
        """TODO: Test action"""
        return {}
