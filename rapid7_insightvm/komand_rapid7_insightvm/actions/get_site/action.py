import komand
from .schema import GetSiteInput, GetSiteOutput
# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_helper import ResourceHelper


class GetSite(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_site',
                description='Get a site by ID',
                input=GetSiteInput(),
                output=GetSiteOutput())

    def run(self, params={}):
        resource_helper = ResourceHelper(self.connection.session, self.logger)
        site_id = params.get("id")
        endpoint = endpoints.Site.sites(self.connection.console_url, site_id)
        self.logger.info("Using %s ..." % endpoint)
        site = resource_helper.resource_request(endpoint)

        return {"site": site}
