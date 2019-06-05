import komand
from .schema import UnsuspendUserInput, UnsuspendUserOutput, Input
# Custom imports below


class UnsuspendUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='unsuspend_user',
                description='Unsuspends a user account',
                input=UnsuspendUserInput(),
                output=UnsuspendUserOutput())

    def run(self, params={}):
        email = params.get(Input.EMAIL)
        service = self.connection.service

        user = service.users().update(userKey=email,
                                      body={
                                          "suspended": False
                                      }).execute()

        if "suspended" in user:
            return {"success": not user["suspended"]}
        else:
            raise Exception("Error: Suspend status was not found in the server response. "
                            "Please check and verify the status of the user.")
