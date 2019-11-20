import komand
from .schema import FindGroupsInput, FindGroupsOutput, Input, Output, Component
# Custom imports below
from komand_mimecast.util import util
from komand.exceptions import PluginException


class FindGroups(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='find_groups',
                description=Component.DESCRIPTION,
                input=FindGroupsInput(),
                output=FindGroupsOutput())

    def run(self, params={}):
        # Import variables from connection
        url = self.connection.url
        uri = self.connection.FIND_GROUPS_URI
        access_key = self.connection.access_key
        secret_key = self.connection.secret_key
        app_id = self.connection.app_id
        app_key = self.connection.app_key

        query = params.get(Input.QUERY)
        source = params.get(Input.SOURCE)
        if query:
            data = {'query': query, 'source': source}
        else:
            data = {'source': source}

        # Mimecast request
        mimecast_request = util.MimecastRequests()
        response = mimecast_request.mimecast_post(url=url, uri=uri,
                                                  access_key=access_key, secret_key=secret_key,
                                                  app_id=app_id, app_key=app_key, data=data)

        try:
            output = response['data'][0]['folders']
        except KeyError:
            self.logger.error(response)
            raise PluginException(cause='Unexpected output format.',
                                  assistance='The output from Mimecast was not in the expected format. Please contact support for help.',
                                  data=response)

        return {Output.GROUPS: output}
