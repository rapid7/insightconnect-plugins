import komand
from .schema import ContainerKillInput, ContainerKillOutput
# Custom imports below
import docker


class ContainerKill(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='container_kill',
                description='Kill or send a signal to the container',
                input=ContainerKillInput(),
                output=ContainerKillOutput())

    def run(self, params={}):
        try:
            container = self.connection.docker_client.containers.get(params.get('id'))
            container.kill(signal=params.get('signal'))
        except (docker.errors.DockerException, docker.errors.APIError):
            self.logger.exception('Unable to kill container.')
            success = False
        else:
            success = True
        return {'success': success}

    def test(self):
        """TODO: Test action"""
        return {}
