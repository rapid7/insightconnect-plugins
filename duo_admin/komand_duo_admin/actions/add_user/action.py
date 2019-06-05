import komand
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
        MAX_ALIASES = 4

        alias = params.get(Input.ALIAS)
        email = params.get(Input.EMAIL)
        firstname = params.get(Input.FIRSTNAME)
        lastname = params.get(Input.LASTNAME)
        notes = params.get(Input.NOTES)
        realname = params.get(Input.REALNAME)
        status = params.get(Input.STATUS)
        username = params.get(Input.USERNAME)

        if len(alias) > MAX_ALIASES:
            raise Exception("Alias parameter must contain 4 or less aliases")

        aliases = {}
        if alias:
            # Use enumerate with an offset of 1 to provide convenient indexing
            for index, value in enumerate(alias, 1):
                aliases[f"alias{index}"] = value

        try:
            # Dictionary splat the aliases
            resp = self.connection.admin_api.add_user(
                username=username,
                realname=realname,
                status=status,
                notes=notes,
                email=email,
                firstname=firstname,
                lastname=lastname,
                **aliases)
            resp = komand.helper.clean(resp)
            return {Output.RESPONSE: resp}
        except RuntimeError as e:
            self.logger.error("An error has occurred: {}".format(e))
            raise
