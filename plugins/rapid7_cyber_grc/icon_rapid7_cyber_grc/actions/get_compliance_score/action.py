import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetComplianceScoreInput, GetComplianceScoreOutput, Input, Output, Component

# Custom imports below
from ...util.compliance import framework_scores


class GetComplianceScore(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_compliance_score",
            description=Component.DESCRIPTION,
            input=GetComplianceScoreInput(),
            output=GetComplianceScoreOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        control_set_id = params.get(Input.CONTROL_SET_ID)
        # END INPUT BINDING - DO NOT REMOVE

        frameworks, unscored = framework_scores(self.connection.client, control_set_id)
        if unscored:
            self.logger.info(
                f"{len(unscored)} control set(s) have no scores in Cyber GRC yet and are not included: "
                f"{', '.join(str(set_id) for set_id in unscored)}"
            )

        return {Output.FRAMEWORKS: frameworks, Output.OVERALL: self._overall(frameworks)}

    @staticmethod
    def _overall(frameworks):
        """Mean of the per framework scores.

        Cyber GRC has no tenant wide score to read, so this is the plugin's own roll up.
        It is an unweighted mean: every framework counts once regardless of how many
        controls it holds, which is what a framework by framework dashboard shows.
        """
        if not frameworks:
            return {"compliance": 0.0, "automated_controls_percentage": 0.0, "framework_count": 0}
        return {
            "compliance": round(sum(f["compliance"] for f in frameworks) / len(frameworks), 2),
            "automated_controls_percentage": round(
                sum(f["automated_controls_percentage"] for f in frameworks) / len(frameworks), 2
            ),
            "framework_count": len(frameworks),
        }
