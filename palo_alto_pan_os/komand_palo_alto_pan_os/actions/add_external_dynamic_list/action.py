import komand
from .schema import AddExternalDynamicListInput, AddExternalDynamicListOutput
from komand.exceptions import PluginException
# Custom imports below
from komand_palo_alto_pan_os.util import util


class AddExternalDynamicList(komand.Action):

    _LIST_TYPE_KEY = {'Predefined IP List': '',
                      'IP List': 'ip',
                      'Domain List': 'domain',
                      'URL List': 'url'}
    _REPEAT_KEY = {'Five Minute': 'five-minute',
                   'Hourly': 'hourly',
                   'Daily': 'daily',
                   'Weekly': 'weekly'}

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_external_dynamic_list',
                description='Add an external dynamic list',
                input=AddExternalDynamicListInput(),
                output=AddExternalDynamicListOutput())

    def run(self, params={}):
        add = util.ExternalList()
        name = params.get('name')
        list_type = params.get('list_type')
        description = params.get('description')
        source = params.get('source')
        repeat = params.get('repeat')
        time = params.get('time')
        day = params.get('day')

        xpath = "/config/devices/entry/vsys/entry/external-list/entry[@name='{}']".format(name)
        element = add.element_for_create_external_list(self._LIST_TYPE_KEY[list_type],
                                                       description,
                                                       source,
                                                       self._REPEAT_KEY[repeat],
                                                       time,
                                                       day.lower)

        output = self.connection.request.set_(xpath=xpath, element=element)
        try:
            status = output['response']['@status']
            code = output['response']['@code']
            message = output['response']['msg']
            return {"status": status, 'code': code, 'message': message}
        except KeyError:
            raise PluginException(cause='The output did not contain expected keys.',
                                  assistance='Contact support for help.',
                                  data=output)
