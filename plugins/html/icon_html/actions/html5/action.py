import insightconnect_plugin_runtime
from .schema import Html5Input, Html5Output, Input, Output, Component
from icon_html.util.api import HTMLConverter
from icon_html.util.helpers import encode_to_base64
from icon_html.util.strategies import ConvertToHTML, ConvertToHTML5


class Html5(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="html5",
            description=Component.DESCRIPTION,
            input=Html5Input(),
            output=Html5Output(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        document = params.get(Input.DOC, "")
        # END INPUT BINDING - DO NOT REMOVE

        converted_html = HTMLConverter(ConvertToHTML()).convert(document)
        converted_html5 = HTMLConverter(ConvertToHTML5()).convert(converted_html)
        return {
            Output.HTML5_CONTENTS: converted_html,
            Output.HTML5_FILE: encode_to_base64(converted_html5),
        }
