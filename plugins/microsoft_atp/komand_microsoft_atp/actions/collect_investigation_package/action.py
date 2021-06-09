import insightconnect_plugin_runtime
from .schema import CollectInvestigationPackageInput, CollectInvestigationPackageOutput, Input, Output, Component

# Custom imports below


class CollectInvestigationPackage(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="collect_investigation_package",
            description=Component.DESCRIPTION,
            input=CollectInvestigationPackageInput(),
            output=CollectInvestigationPackageOutput(),
        )

    def run(self, params={}):
        self.logger.info("Running...")
        comment = params.get(Input.COMMENT)
        if not comment:
            comment = "Investigation package collected via InsightConnect"
        return {
            Output.COLLECT_INVESTIGATION_PACKAGE_RESPONSE: insightconnect_plugin_runtime.helper.clean(
                self.connection.client.collect_investigation_package(
                    self.connection.client.find_machine_id(params.get(Input.MACHINE)), comment
                )
            )
        }
