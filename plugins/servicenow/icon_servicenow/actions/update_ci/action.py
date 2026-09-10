import insightconnect_plugin_runtime
from .schema import UpdateCiInput, UpdateCiOutput, Input, Output, Component

# Custom imports below
from icon_servicenow.util.validators import validate_record_identifier, validate_table_name


class UpdateCi(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_ci",
            description=Component.DESCRIPTION,
            input=UpdateCiInput(),
            output=UpdateCiOutput(),
        )

    def run(self, params={}):
        table = validate_table_name(params.get(Input.TABLE))
        system_id = validate_record_identifier(params.get(Input.SYSTEM_ID), "system ID")
        url = f"{self.connection.table_url}{table}/{system_id}"
        payload = params.get(Input.UPDATE_DATA)
        method = "put"

        response = self.connection.request.make_request(url, method, payload=payload)

        success = response.get("status", 0) in range(200, 299)

        return {Output.SUCCESS: success}
