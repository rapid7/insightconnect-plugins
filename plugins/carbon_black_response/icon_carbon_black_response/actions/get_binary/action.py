import insightconnect_plugin_runtime
from .schema import GetBinaryInput, GetBinaryOutput

# Custom imports below
from cbapi.response.models import Binary


class GetBinary(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_binary",
            description="Retrieve a binary by its Hash",
            input=GetBinaryInput(),
            output=GetBinaryOutput(),
        )

    def run(self, params={}):
        try:
            binary = self.connection.carbon_black.select(Binary, params["hash"])
        except Exception as ex:
            self.logger.error("Failed to retrieve binary: %s", ex)
            raise ex
        return {"binary": str(binary.file.read())}

    def test(self):
        if self.connection.test():
            return {}
