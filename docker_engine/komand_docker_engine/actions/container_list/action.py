import komand
from .schema import ContainerListInput, ContainerListOutput
# Custom imports below
import docker
from ... import helper


class ContainerList(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='container_list',
                description='List available Docker containers',
                input=ContainerListInput(),
                output=ContainerListOutput())

    def run(self, params={}):
        try:
            containers = self.connection.docker_client.containers.list()
        except (docker.errors.DockerException, docker.errors.APIError):
            raise
        else:
            return {'containers': list(map(helper.container_to_json, containers))}

    def test(self):
        """TODO: Test action"""
        return {}
