import komand
from .schema import GetLogsInput, GetLogsOutput, Input, Output, Component
# Custom imports below


class GetLogs(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_logs',
            description=Component.DESCRIPTION,
            input=GetLogsInput(),
            output=GetLogsOutput())

    def run(self, params={}):
        mintime = params.get(Input.MINTIME, 1000000000000)  # Default to Sun Sep 09 2001 01:46:40 UTC

        PAGE_SIZE = 1000
        METADATA, NEXT_OFFSET, AUTHLOGS, TOTAL_OBJECTS = "metadata", "next_offset", "authlogs", "total_objects"

        authlogs = []
        try:
            # Get initial results
            results = self.connection.admin_api.get_authentication_log(api_version=2,
                                                                       mintime=mintime,
                                                                       limit=str(PAGE_SIZE))
            authlogs.extend(results[AUTHLOGS])

            # Set total_objects_left to amount reported by Duo, less the PAGE_SIZE since we have already made one call
            total_objects_left = results[METADATA][TOTAL_OBJECTS] - PAGE_SIZE

            # Set next_offset to next_offset provided by Duo to get next results page
            next_offset = results[METADATA][NEXT_OFFSET]
            while total_objects_left > 0:
                results = self.connection.admin_api.get_authentication_log(api_version=2,
                                                                           mintime=mintime,
                                                                           limit=str(PAGE_SIZE),
                                                                           next_offset=next_offset)

                # Set next offset and decrement total objects left to control loop
                next_offset = results[METADATA][NEXT_OFFSET]
                total_objects_left -= PAGE_SIZE
                authlogs.extend(results[AUTHLOGS])

            authlogs = komand.helper.clean(authlogs)
            return {Output.AUTHLOGS: authlogs}
        except KeyError as e:
            raise Exception(f"Error: API response was missing required fields necessary for proper functioning.") from e
