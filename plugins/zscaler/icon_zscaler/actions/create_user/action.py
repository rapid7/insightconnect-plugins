import insightconnect_plugin_runtime
from .schema import CreateUserInput, CreateUserOutput, Input, Output, Component

# Custom imports below
from icon_zscaler.util.helpers import (
    clean_dict,
    remove_password_from_result,
    prepare_department,
    prepare_groups,
)


class CreateUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_user", description=Component.DESCRIPTION, input=CreateUserInput(), output=CreateUserOutput()
        )

    def run(self, params={}):
        self.logger.info("Creating new user...\n")

        parameters = {
            "name": params.get(Input.NAME),
            "email": params.get(Input.EMAIL),
            "groups": prepare_groups(self.connection.client.search_groups(), params.get(Input.GROUPNAMES)),
            "department": prepare_department(
                self.connection.client.search_department(params.get(Input.DEPARTMENTNAME)),
                params.get(Input.DEPARTMENTNAME),
            ),
            "comments": params.get(Input.COMMENTS),
            "tempAuthEmail": params.get(Input.TEMPAUTHEMAIL),
            "password": params.get(Input.PASSWORD),
        }

        return {Output.USER: remove_password_from_result(self.connection.client.create_user(clean_dict(parameters)))}
