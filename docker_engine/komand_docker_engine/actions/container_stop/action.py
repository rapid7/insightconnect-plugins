import komand
from .schema import ContainerStopInput, ContainerStopOutput

# Custom imports below
import docker


class ContainerStop(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="container_stop",
            description="Stop a container by ID",
            input=ContainerStopInput(),
            output=ContainerStopOutput(),
        )

    def run(self, params={}):
        try:
            container = self.connection.docker_client.containers.get(params.get("id"))
            container.stop(timeout=params.get("timeout"))
        except (docker.errors.DockerException, docker.errors.APIError):
            self.logger.exception("Unable to stop container.")
            success = False
        else:
            success = True
        return {"success": success}

    def test(self):
        """TODO: Test action"""
        return {}
