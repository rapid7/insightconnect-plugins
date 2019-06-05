import komand
from .schema import ListKeyboardLayoutsInput, ListKeyboardLayoutsOutput, Input, Output
# Custom imports below


class ListKeyboardLayouts(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_keyboard_layouts',
                description='Retrieve a list of available keyboard layouts for Windows analyzers',
                input=ListKeyboardLayoutsInput(),
                output=ListKeyboardLayoutsOutput())

    def run(self, params={}):
        keyboard_layouts = self.connection.api.server_keyboard_layouts()
        return {'keyboard_layouts': keyboard_layouts}
