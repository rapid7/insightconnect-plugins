import insightconnect_plugin_runtime
from .schema import DlCreateInput, DlCreateOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class DlCreate(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="dlCreate",
            description=Component.DESCRIPTION,
            input=DlCreateInput(),
            output=DlCreateOutput(),
        )

    def run(self, params={}):
        # Required data
        data = {
            "access": params.get(Input.ACCESS),
            "isGlobal": params.get(Input.ISGLOBAL),
            "name": params.get(Input.NAME),
        }

        # Optional Data
        destination = params.get(Input.DESTINATION, "")
        dest_type = params.get(Input.TYPE)
        comment = params.get(Input.COMMENT, "")

        # Destination is a required field when specifying, but not overall,
        # raise exception when not specifying destination but other inputs
        if (comment or dest_type) and not destination:
            raise PluginException(
                cause="Comment or Type selected without destination",
                assistance="Specify a destination in order to use type or comment inputs",
            )

        if destination:
            destinations = [
                {
                    "destination": destination,
                    "type": dest_type,
                    "comment": comment,
                }
            ]
            data["destinations"] = destinations

        # POST request
        result = self.connection.client.create_destination_list(data=data)
        result = {key: value for key, value in result.items() if value is not None}

        return {Output.SUCCESS: result}
