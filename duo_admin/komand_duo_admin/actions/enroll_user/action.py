import komand
from .schema import EnrollUserInput, EnrollUserOutput, Input, Output, Component
# Custom imports below


class EnrollUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='enroll_user',
                description=Component.DESCRIPTION,
                input=EnrollUserInput(),
                output=EnrollUserOutput())

    def run(self, params={}):
        username = params.get(Input.USERNAME)
        email = params.get(Input.EMAIL)
        expiration = params.get(Input.TIME_TO_EXPIRATION)

        try:
            self.connection.admin_api.enroll_user(username=username,
                                                  email=email,
                                                  valid_secs=expiration)
        except RuntimeError:
            return {Output.SUCCESS: False}

        return {Output.SUCCESS: True}
