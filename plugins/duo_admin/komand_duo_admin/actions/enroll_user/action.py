import insightconnect_plugin_runtime
from .schema import EnrollUserInput, EnrollUserOutput, Input, Output, Component


# Custom imports below
from komand_duo_admin.util.helpers import clean


class EnrollUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="enroll_user",
            description=Component.DESCRIPTION,
            input=EnrollUserInput(),
            output=EnrollUserOutput(),
        )

    def run(self, params={}):
        time_to_expiration = params.get(Input.TIMETOEXPIRATION)

        data = {
            "username": params.get(Input.USERNAME),
            "email": params.get(Input.EMAIL),
            "valid_secs": str(time_to_expiration) if time_to_expiration and time_to_expiration > 0 else None,
        }
        return {
            Output.SUCCESS: True if self.connection.admin_api.enroll_user(clean(data)).get("stat") == "OK" else False
        }
