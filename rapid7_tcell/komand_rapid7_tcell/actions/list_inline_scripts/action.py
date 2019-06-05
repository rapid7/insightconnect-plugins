import komand
from .schema import ListInlineScriptsInput, ListInlineScriptsOutput
# Custom imports below


class ListInlineScripts(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_inline_scripts',
                description='Fetch details for all seen inline scripts (matching the provided criteria)',
                input=ListInlineScriptsInput(),
                output=ListInlineScriptsOutput())

    def run(self, params={}):
        app_id = params.get('app_id')
        from_ = params.get('from')
        to = params.get('to')
        per_page = params.get('per_page', 10)
        page = params.get('page', 1)

        inline_scripts = self.connection.api.list_inline_scripts(
            app_id, from_, to, per_page, page
        )
        if inline_scripts is None:
            inline_scripts = {'total': 0, 'inline_scripts': []}

        return inline_scripts

    def test(self):
        return {}
