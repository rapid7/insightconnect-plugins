import komand
from .schema import RemoveUserSiteAccessInput, RemoveUserSiteAccessOutput
# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_helper import ResourceHelper


class RemoveUserSiteAccess(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='remove_user_site_access',
                description='Remove site access from a user account',
                input=RemoveUserSiteAccessInput(),
                output=RemoveUserSiteAccessOutput())

    def run(self, params={}):
        resource_helper = ResourceHelper(self.connection.session, self.logger)
        endpoint = endpoints.User.user_sites(self.connection.console_url,
                                             params.get('user_id'), params.get('site_id'))
        self.logger.info("Using %s ..." % endpoint)

        response = resource_helper.resource_request(endpoint=endpoint, method='delete')

        return response
