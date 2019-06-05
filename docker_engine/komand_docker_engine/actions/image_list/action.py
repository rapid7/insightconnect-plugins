import komand
from .schema import ImageListInput, ImageListOutput
# Custom imports below
import docker
from ... import helper


class ImageList(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='image_list',
                description='List available Docker images',
                input=ImageListInput(),
                output=ImageListOutput())

    def run(self, params={}):
        try:
            images = self.connection.docker_client.images.list()
        except (docker.errors.DockerException, docker.errors.APIError):
            raise
        else:
            return {'images': list(map(helper.image_to_json, images))}

    def test(self):
        """TODO: Test action"""
        return {}
