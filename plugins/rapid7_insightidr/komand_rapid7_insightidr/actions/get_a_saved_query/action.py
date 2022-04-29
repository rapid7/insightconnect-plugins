import uuid

import komand
from .schema import GetASavedQueryInput, GetASavedQueryOutput, Input, Output, Component
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
from komand_rapid7_insightidr.util.endpoints import Queries
from komand.exceptions import PluginException
from uuid import UUID
from validators import uuid
# Custom imports below


class GetASavedQuery(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_a_saved_query',
            description=Component.DESCRIPTION,
            input=GetASavedQueryInput(),
            output=GetASavedQueryOutput())

    def run(self, params={}):
        query_id = params.get(Input.QUERY_ID)
        if not uuid(query_id):
            raise PluginException(
                cause="Query ID field did not contain a valid UUID.",
                assistance="Please enter a valid UUID value in the Query ID field.",
                data=f"Query ID: {query_id}"
            )
        request = ResourceHelper(self.connection.session, self.logger)
        response = request.resource_request(Queries.get_query_by_id(self.connection.url, query_id),
                                            "get")
        return {Output.SAVED_QUERY: response}
