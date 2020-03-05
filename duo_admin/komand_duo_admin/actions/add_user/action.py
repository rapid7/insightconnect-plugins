import komand
from komand.exceptions import PluginException
from .schema import AddUserInput, AddUserOutput, Input, Output, Component
# Custom imports below


class AddUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_user",
            description=Component.DESCRIPTION,
            input=AddUserInput(),
            output=AddUserOutput())

    def run(self, params={}):
        max_aliases = 4

        alias = params.get(Input.ALIAS)
        email = params.get(Input.EMAIL)
        first_name = params.get(Input.FIRSTNAME)
        last_name = params.get(Input.LASTNAME)
        notes = params.get(Input.NOTES)
        real_name = params.get(Input.REALNAME)
        status = params.get(Input.STATUS)
        username = params.get(Input.USERNAME)

        if len(alias) > max_aliases:
            raise PluginException(
                cause="Invalid input",
                assistance="Alias parameter must contain 4 or less aliases"
            )

        aliases = {}
        if alias:
            for index, value in enumerate(alias, 1):
                aliases[f"alias{index}"] = value

        try:
            resp = self.connection.admin_api.add_user(
                username=username,
                realname=real_name,
                status=status,
                notes=notes,
                email=email,
                firstname=first_name,
                lastname=last_name,
                **aliases)
            resp = komand.helper.clean(resp)
            return {Output.RESPONSE: resp}
        except RuntimeError as e:
            self.logger.error(f"An error has occurred: {str(e)}")
            raise PluginException(
                preset=PluginException.Preset.INVALID_JSON,
                data=f"An error has occurred: {str(e)}"
            )
