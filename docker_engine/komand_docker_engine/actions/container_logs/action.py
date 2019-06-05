import komand
from .schema import ContainerLogsInput, ContainerLogsOutput
# Custom imports below
import docker


class ContainerLogs(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='container_logs',
                description='Retrieve container logs',
                input=ContainerLogsInput(),
                output=ContainerLogsOutput())

    def run(self, params={}):
        try:
            container = self.connection.docker_client.containers.get(params.get('id'))
            logs = str(container.logs())
        except (docker.errors.DockerException, docker.errors.APIError):
            raise
        else:
            return {'logs': logs}

    def test(self):
        """TODO: Test action"""
        return {}
