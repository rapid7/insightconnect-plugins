import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import CreateUserInput, CreateUserOutput, Input, Output, Component

# Custom imports below
from komand_pagerduty.util.util import normalize_user


class CreateUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_user",
            description="Create a User",
            input=CreateUserInput(),
            output=CreateUserOutput(),
        )

    def run(self, params={}):
        """Trigger event"""

        # required
        from_email = params.get(Input.FROM_EMAIL)
        new_users_email = params.get(Input.EMAIL)
        name = params.get(Input.NAME)

        # optional
        dict_of_optional_fields = {
            "time_zone": params.get(Input.TIME_ZONE, ""),
            "color": params.get(Input.COLOR, ""),
            "role": params.get(Input.ROLE, ""),
            "description": params.get(Input.USER_DESCRIPTION, ""),
            "job_title": params.get(Input.JOB_TITLE, ""),
            "license": params.get(Input.LICENSE, {}),
        }

        response = self.connection.api.create_user(
            from_email=from_email,
            new_users_email=new_users_email,
            name=name,
            dict_of_optional_fields=dict_of_optional_fields,
        )

        return {Output.USER: normalize_user(response.get("user", {}))}
