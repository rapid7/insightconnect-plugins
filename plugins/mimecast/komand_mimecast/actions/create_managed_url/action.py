import insightconnect_plugin_runtime
import validators
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import CreateManagedUrlInput, CreateManagedUrlOutput, Component, Output, Input

# Custom imports below
from komand_mimecast.util.util import Utils
from komand_mimecast.util.constants import DATA_FIELD


class CreateManagedUrl(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_managed_url",
            description=Component.DESCRIPTION,
            input=CreateManagedUrlInput(),
            output=CreateManagedUrlOutput(),
        )

    def run(self, params={}):
        if not validators.url(params.get(Input.URL)):
            raise PluginException(
                cause="URL address is in invalid format.",
                assistance="Please check URL and try again.",
            )
        data = {}
        for key, value in params.items():
            temp = Utils.normalize(key, value)
            data.update(temp)
        return {Output.RESPONSE: self.connection.client.create_managed_url(data).get(DATA_FIELD, [])}
