import insightconnect_plugin_runtime
from .schema import CreateExemptionInput, CreateExemptionOutput, Input, Output, Component

# Custom imports below
from icon_rapid7_insightcloudsec.util.helpers import parse_date_from_datetime


class CreateExemption(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_exemption",
            description=Component.DESCRIPTION,
            input=CreateExemptionInput(),
            output=CreateExemptionOutput(),
        )

    def run(self, params={}):
        expiration_date = params.get(Input.EXPIRATIONDATE)
        json_data = {
            "approver": params.get(Input.APPROVER),
            "insight_id": params.get(Input.INSIGHTID),
            "insight_source": params.get(Input.INSIGHTSOURCE),
            "resource_ids": params.get(Input.RESOURCEIDS),
            "resource_type": params.get(Input.RESOURCETYPE),
            "start_date": parse_date_from_datetime(params.get(Input.STARTDATE)),
            "expiration_date": parse_date_from_datetime(expiration_date) if expiration_date else None,
            "notes": params.get(Input.NOTES),
        }
        return {Output.EXEMPTION: self.connection.api.create_exemption(json_data)}
