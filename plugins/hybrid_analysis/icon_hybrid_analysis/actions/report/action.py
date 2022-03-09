import validators

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
from .schema import ReportInput, ReportOutput, Input, Component


class Report(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="report", description=Component.DESCRIPTION, input=ReportInput(), output=ReportOutput()
        )

    def run(self, params={}):
        hash_to_get_report = params.get(Input.HASH)
        if not validators.sha256(hash_to_get_report):
            raise PluginException(
                cause="Provided hash is not supported.",
                assistance="The API only supports SHA256 hashes. Please check the provided hash and try again.",
            )
        return insightconnect_plugin_runtime.helper.clean(self.connection.api.report(hash_to_get_report))
