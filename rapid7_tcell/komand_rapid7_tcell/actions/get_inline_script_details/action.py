import komand
from .schema import GetInlineScriptDetailsInput, GetInlineScriptDetailsOutput
# Custom imports below


class GetInlineScriptDetails(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_inline_script_details',
                description='Fetch details for the inline script with the given ID',
                input=GetInlineScriptDetailsInput(),
                output=GetInlineScriptDetailsOutput())

    def run(self, params={}):
        app_id = params.get('app_id')
        inline_script_id = params.get('inline_script_id')

        inline_script = self.connection.api.get_inline_script_details(
            app_id, inline_script_id
        )

        return {'inline_script': inline_script}

    def test(self):
        return {}
