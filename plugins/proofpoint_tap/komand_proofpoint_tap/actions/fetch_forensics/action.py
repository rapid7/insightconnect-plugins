import insightconnect_plugin_runtime
from .schema import FetchForensicsInput, FetchForensicsOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_proofpoint_tap.util.helpers import clean


class FetchForensics(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="fetch_forensics",
            description=Component.DESCRIPTION,
            input=FetchForensicsInput(),
            output=FetchForensicsOutput(),
        )

    def run(self, params={}):
        threat_id = params.get(Input.THREATID)
        campaign_id = params.get(Input.CAMPAIGNID)
        include_campaign_forensics = params.get(Input.INCLUDECAMPAIGNFORENSICS, False)

        if threat_id and campaign_id:
            raise PluginException(
                cause="Both Campaign ID and Threat ID were provided.",
                assistance="Only one of the following two parameters can be used: Campaign ID or Threat ID.",
            )
        if not threat_id and not campaign_id:
            raise PluginException(
                cause="One of the following inputs must be provided.",
                assistance="Please enter either Threat ID or Campaign ID.",
            )

        result = clean(
            self.connection.client.get_forensics(
                {
                    "threatId": threat_id if threat_id else None,
                    "campaignId": campaign_id if campaign_id else None,
                    "includeCampaignForensics": include_campaign_forensics if threat_id else None,
                }
            )
        )

        for i, report in enumerate(result.get("reports", [])):
            for j, forensic in enumerate(report.get("forensics", [])):
                blacklisted = forensic.get("what", {}).get("blacklisted")
                if blacklisted:
                    result["reports"][i]["forensics"][j]["what"]["blacklisted"] = bool(blacklisted)

        return {Output.GENERATED: result.get("generated"), Output.REPORTS: result.get("reports", [])}
