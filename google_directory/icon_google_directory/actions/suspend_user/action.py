import komand
from .schema import SuspendUserInput, SuspendUserOutput, Input
# Custom imports below


class SuspendUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='suspend_user',
                description='Suspends a user account',
                input=SuspendUserInput(),
                output=SuspendUserOutput())

    def run(self, params={}):
        email = params.get(Input.EMAIL)
        service = self.connection.service

        user = service.users().update(userKey=email,
                                      body={
                                          "suspended": True
                                      }).execute()

        if "suspended" in user:
            return {"success": user["suspended"]}
        else:
            raise Exception("Error: Suspend status was not found in the server response. "
                            "Please check and verify the status of the user.")
