import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
import pypandoc
import base64
import re
from .schema import Html5Input, Html5Output, Input, Output


class Html5(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="html5",
            description="Convert HTML to HTML5",
            input=Html5Input(),
            output=Html5Output(),
        )

    def run(self, params={}):
        tag_parser = "(?i)<\/?\w+((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[^'\">\s]+))?)+\s*|\s*)\/?>"  # noqa: W605
        tags = re.findall(tag_parser, params.get(Input.DOC))

        if not tags:
            raise PluginException(cause="Invalid input.", assistance="Input must be of type HTML.")

        try:
            output = pypandoc.convert_text(params.get(Input.DOC), "html", format="md")
            new_output = pypandoc.convert(output, "html5", format="md")
        except RuntimeError as error:
            raise PluginException(cause="Pypandoc Runtime Error: ", assistance="Check stack trace log", data=error)

        file_ = base64.b64encode(new_output.encode("utf-8")).decode()
        return {Output.HTML5_CONTENTS: output, Output.HTML5_FILE: file_}
