import insightconnect_plugin_runtime
from .schema import CreateScheduleInput, CreateScheduleOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper
from komand_rapid7_insightappsec.util.endpoints import Schedules


class CreateSchedule(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_schedule",
            description=Component.DESCRIPTION,
            input=CreateScheduleInput(),
            output=CreateScheduleOutput(),
        )

    def run(self, params={}):
        frequency = params.get(Input.FREQUENCY)
        rrule = params.get(Input.RRULE)
        json_data = {
            "name": params.get(Input.NAME),
            "scan_config": {"id": params.get(Input.SCANCONFIGID)},
            "enabled": params.get(Input.ENABLED),
            "first_start": params.get(Input.FIRSTSTART),
            "last_start": params.get(Input.LASTSTART),
        }

        if not frequency and not rrule:
            raise PluginException(
                cause="Frequency and recurrence rule are not provided.",
                assistance="Please provide the frequency or recurrence rule and try again.",
            )
        if rrule:
            json_data["rrule"] = rrule.upper()
        else:
            json_data["frequency"] = frequency

        request = ResourceHelper(self.connection.session, self.logger)
        request.resource_request(Schedules.schedule(self.connection.url), "POST", payload=json_data)
        return {Output.SUCCESS: True}
