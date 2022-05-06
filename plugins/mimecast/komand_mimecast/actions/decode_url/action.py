import insightconnect_plugin_runtime
from .schema import DecodeUrlInput, DecodeUrlOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_mimecast.util.constants import DATA_FIELD, URL_FIELD, FAIL_FIELD


class DecodeUrl(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="decode_url",
            description=Component.DESCRIPTION,
            input=DecodeUrlInput(),
            output=DecodeUrlOutput(),
        )

    def run(self, params={}):
        data = {URL_FIELD: params.get(Input.ENCODED_URL)}
        response = self.connection.client.decode_url(data)
        try:
            if not response.get(DATA_FIELD)[0]["success"]:
                raise PluginException(
                    cause=f"The URL {params.get(Input.ENCODED_URL)} could not be decoded.",
                    assistance="Please ensure that it is a Mimecast encoded URL.",
                    data=response.get(FAIL_FIELD),
                )
        except KeyError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response)
        except IndexError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response)

        try:
            output = response[DATA_FIELD][0][URL_FIELD]
        except KeyError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response)
        except IndexError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response)
        return {Output.DECODED_URL: output}
