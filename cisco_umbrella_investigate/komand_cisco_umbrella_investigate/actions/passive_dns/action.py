import komand
from .schema import PassiveDnsInput, PassiveDnsOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException


class PassiveDns(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='passive_dns',
                description=Component.DESCRIPTION,
                input=PassiveDnsInput(),
                output=PassiveDnsOutput())

    def run(self, params={}):
        name = params.get(Input.NAME)
        resource_records = params.get(Input.RESOURCE_RECORDS)
        record_type = params.get(Input.RECORDTYPE)
        if record_type:
            record_type = record_type.replace(" ", "")
        try:
            response = self.connection.investigate.get_dns(
                name,
                resource_records=resource_records,
                record_type=record_type
            )
        except Exception as e:
            raise PluginException(
                preset=PluginException.Preset.UNKNOWN,
                data=e
            )
        if resource_records == "Timeline":
            return {
                Output.TIMELINE_DATA: response
            }
        else:
            return response
