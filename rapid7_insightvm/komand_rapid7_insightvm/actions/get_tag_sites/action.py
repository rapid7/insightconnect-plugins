import komand
from .schema import GetTagSitesInput, GetTagSitesOutput
# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_helper import ResourceHelper


class GetTagSites(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_tag_sites',
                description='Get site IDs associated with a tag',
                input=GetTagSitesInput(),
                output=GetTagSitesOutput())

    def run(self, params={}):
        resource_helper = ResourceHelper(self.connection.session, self.logger)
        tag_id = params.get("id")
        endpoint = endpoints.Tag.tag_sites(self.connection.console_url, tag_id)
        self.logger.info("Using %s ..." % endpoint)

        response = resource_helper.resource_request(endpoint=endpoint)

        if 'resources' in response:
            return {"site_ids": response['resources']}
        else:
            return {"site_ids": []}
