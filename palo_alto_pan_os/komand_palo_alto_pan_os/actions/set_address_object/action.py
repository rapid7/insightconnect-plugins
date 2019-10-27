import komand
from .schema import SetAddressObjectInput, SetAddressObjectOutput, Input, Output
from komand.exceptions import PluginException
# Custom imports below


class SetAddressObject(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='set_address_object',
                description='Create a new address object',
                input=SetAddressObjectInput(),
                output=SetAddressObjectOutput())

    def run(self, params={}):
        address = params.get(Input.ADDRESS)
        object_type = params.get(Input.TYPE)
        name = params.get(Input.OBJECT_NAME)
        description = params.get(Input.OBJECT_DESCRIPTION)
        tag_list = params.get(Input.TAGS)

        # create tags XML
        tag = ''
        if tag_list:
            tag_list = tag_list.split(',')
            for item in tag_list:
                tag = tag + f'<member>{item}</member>'

        # create object type XML
        object_type = object_type.lower()
        address = f'<{object_type}>{address}</{object_type}>'

        xpath = f"/config/devices/entry/vsys/entry/address/entry[@name='test{name}']"
        element = address
        if description:
            element = f'{element}<description>{description}</description>'
        if tag:
            element = f'{element}<tag>{tag}</tag>'

        output = self.connection.request.set_(xpath=xpath, element=element)
        try:
            return {Output.MESSAGE: output['response']['msg'],
                    Output.STATUS: output['response']['@status'],
                    Output.CODE: output['response']['@code']}
        except KeyError:
            raise PluginException(cause='The output did not contain expected keys.',
                                  assistance='Contact support for help.',
                                  data=output)
