import komand
from .schema import AddPermissionSetToUserInput, AddPermissionSetToUserOutput
# Custom imports below


class AddPermissionSetToUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_permission_set_to_user',
                description='Adds permission set(s) to specified user',
                input=AddPermissionSetToUserInput(),
                output=AddPermissionSetToUserOutput())

    def run(self, params={}):
        try:
            mc = self.connection.client
            out = mc.run('core.addPermSetsForUser', params["user"], params["permission_set"])
            return {"message": out}
        except Exception as e:
            self.logger.error("Could not add specified permission set to specified user. Error: " + str(e))
            raise

    def test(self):
        try:
            mc = self.connection.client
            if mc.epo.getVersion():
                return {"message": True}
        except Exception:
            self.logger.error("An unexpected error occurred during the API request")
            raise
