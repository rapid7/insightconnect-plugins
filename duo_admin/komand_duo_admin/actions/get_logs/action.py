import komand
from komand.exceptions import PluginException
from .schema import GetLogsInput, GetLogsOutput, Input, Output, Component


# Custom imports below


class GetLogs(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_logs',
            description=Component.DESCRIPTION,
            input=GetLogsInput(),
            output=GetLogsOutput())

        self.METADATA, self.NEXT_OFFSET, self.AUTH_LOGS, self.TOTAL_OBJECTS = "metadata", "next_offset", "authlogs", "total_objects"
        self.PAGE_SIZE = 1000

    def run(self, params={}):
        min_time = params.get(Input.MINTIME, 1000000000000)

        auth_logs = []
        try:
            results = self.connection.admin_api.get_authentication_log(
                api_version=2,
                mintime=min_time,
                limit=str(self.PAGE_SIZE)
            )
            auth_logs.extend(results[self.AUTH_LOGS])

            total_objects_left = results[self.METADATA][self.TOTAL_OBJECTS] - self.PAGE_SIZE

            next_offset = results[self.METADATA][self.NEXT_OFFSET]
            while total_objects_left > 0:
                results = self.connection.admin_api.get_authentication_log(
                    api_version=2,
                    mintime=min_time,
                    limit=str(self.PAGE_SIZE),
                    next_offset=next_offset
                )

                next_offset = results[self.METADATA][self.NEXT_OFFSET]
                total_objects_left -= self.PAGE_SIZE
                auth_logs.extend(results[self.AUTH_LOGS])

            auth_logs = komand.helper.clean(auth_logs)
            return {Output.AUTHLOGS: auth_logs}
        except KeyError as e:
            raise PluginException(
                preset=PluginException.Preset.SERVER_ERROR,
                data=f"Error: API response was missing required fields necessary for proper functioning. {str(e)}"
            )
