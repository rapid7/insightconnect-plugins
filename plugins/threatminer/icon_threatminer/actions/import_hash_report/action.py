import insightconnect_plugin_runtime

from .schema import Component, ImportHashReportInput, ImportHashReportOutput, Input, Output

# Custom imports below


class ImportHashReport(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="import_hash_report",
            description=Component.DESCRIPTION,
            input=ImportHashReportInput(),
            output=ImportHashReportOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        query = params.get(Input.QUERY, "")
        # END INPUT BINDING - DO NOT REMOVE

        return {Output.RESPONSE: self.connection.api_client.import_hash(query, report=True)}
