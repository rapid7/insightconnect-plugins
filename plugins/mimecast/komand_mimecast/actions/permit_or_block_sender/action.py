import insightconnect_plugin_runtime
from .schema import PermitOrBlockSenderInput, PermitOrBlockSenderOutput, Output, Component

# Custom imports below
from komand_mimecast.util.util import Utils
from komand_mimecast.util.constants import DATA_FIELD


class PermitOrBlockSender(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="permit_or_block_sender",
            description=Component.DESCRIPTION,
            input=PermitOrBlockSenderInput(),
            output=PermitOrBlockSenderOutput(),
        )

    def run(self, params={}):
        data = {}
        for key, value in params.items():
            temp = Utils.normalize(key, value)
            data.update(temp)
        return {Output.RESPONSE: self.connection.client.permit_or_block_sender(data).get(DATA_FIELD, {})}
