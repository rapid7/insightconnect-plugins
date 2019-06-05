import komand
from .schema import ContainerRemoveInput, ContainerRemoveOutput
# Custom imports below
import docker


class ContainerRemove(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='container_remove',
                description='Remove a container by ID',
                input=ContainerRemoveInput(),
                output=ContainerRemoveOutput())

    def run(self, params={}):
        try:
            container = self.connection.docker_client.containers.get(params.get('id'))
            container.remove(
                v=params.get('v'),
                link=params.get('link'),
                force=params.get('force')
            )
        except (docker.errors.DockerException, docker.errors.APIError):
            self.logger.exception('Unable to remove container.')
            success = False
        else:
            success = True
        return {'success': success}

    def test(self):
        """TODO: Test action"""
        return {}
