import komand
from .schema import SetAddressObjectInput, SetAddressObjectOutput, Input, Output
# Custom imports below


class SetAddressObject(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='set_address_object',
                description='Create a new address object',
                input=SetAddressObjectInput(),
                output=SetAddressObjectOutput())

    def run(self, params={}):
        address = params.get('address')
        object_type = params.get('type')
        name = params.get('object_name')
        description = params.get('object_description')
        tag_list = params.get('tags')

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
            return {"message": output['response']['msg'],
                    "status": output['response']['@status'],
                    "code": output['response']['@code']}
        except KeyError:
            self.logger.error('The output did not contain a proper response.')
            self.logger.error(output)
            raise
