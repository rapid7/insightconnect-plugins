import komand
from .schema import RemoveUserFromGroupInput, RemoveUserFromGroupOutput, Input, Output, Component
# Custom imports below
import requests
from komand_okta.util import helpers


class RemoveUserFromGroup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='remove_user_from_group',
            description=Component.DESCRIPTION,
            input=RemoveUserFromGroupInput(),
            output=RemoveUserFromGroupOutput())

    def run(self, params={}):
        """ Get the user by email """
        group_id = params.get(Input.GROUP_ID)
        email = params.get(Input.EMAIL)
        user_id = helpers.get_user_id(email, self.connection, self.logger)

        if user_id is None:
            return {Output.SUCCESS: False}

        """ Remove user from group by id"""
        url = requests.compat.urljoin(self.connection.okta_url, f'/api/v1/groups/{group_id}/users/{user_id}')
        response = self.connection.session.delete(url)

        return helpers.group_response(response, user_id)
