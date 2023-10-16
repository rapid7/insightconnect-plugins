import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import CreateUserInput, CreateUserOutput

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
        from_email = params.get("from_email")
        new_users_email = params.get("email")
        name = params.get("name")

        # optional
        dict_of_optional_fields = {
            "time_zone": params.get("time_zone", ""),
            "color": params.get("color", ""),
            "role": params.get("role", ""),
            "timezone": params.get("timezone", ""),
            "description": params.get("user_description", ""),
            "job_title": params.get("job_title", ""),
            "license": params.get("license", {}),
        }

        if from_email is None or new_users_email is None or name is None:
            self.logger.warning("Please ensure a valid 'from_email', 'new_users_email' and 'name' is provided")
            raise PluginException(
                cause="Missing required paramaters",
                assistance="Please ensure a valid 'from_email', 'new_users_email' and 'name' is provided",
            )

        response = self.connection.api.create_user(
            from_email=from_email,
            new_users_email=new_users_email,
            name=name,
            dict_of_optional_fields=dict_of_optional_fields,
        )

        return {"user": normalize_user(response.get("user", {}))}
