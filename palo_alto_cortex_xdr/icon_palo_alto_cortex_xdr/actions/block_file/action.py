import insightconnect_plugin_runtime
from .schema import BlockFileInput, BlockFileOutput, Input, Output, Component
# Custom imports below


class BlockFile(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='block_file',
                description=Component.DESCRIPTION,
                input=BlockFileInput(),
                output=BlockFileOutput())

    def run(self, params={}):
        file_hash = params.get(Input.FILE_HASH)
        comment = params.get(Input.COMMENT)
        incident_id = params.get(Input.INCIDENT_ID)

        if incident_id and incident_id < 1:  # Not sure if I need this, but just in case.
            incident_id = None

        return {Output.SUCCESS: self.connection.xdr_api.allow_or_block_file(file_hash,
                                                                            comment,
                                                                            incident_id,
                                                                            True)}
