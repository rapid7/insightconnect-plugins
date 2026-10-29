import insightconnect_plugin_runtime
from .schema import GetVersionStatusInput, GetVersionStatusOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_endoflife_ai.util import helper


class GetVersionStatus(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_version_status",
            description=Component.DESCRIPTION,
            input=GetVersionStatusInput(),
            output=GetVersionStatusOutput(),
        )

    def run(self, params={}):
        product = helper.path_segment(params.get(Input.PRODUCT), lowercase=True)
        version = helper.path_segment(params.get(Input.VERSION))
        if not product or not version:
            raise PluginException(
                cause="Product and version are both required.",
                assistance="Provide a product slug such as nodejs and a release cycle such as 20.",
            )

        self.logger.info(f"Looking up {product} {version}")
        status_code, json_ = helper.request_json(self.connection, "GET", f"/v1/score/{product}/{version}")

        if status_code == 404:
            return {Output.FOUND: False, Output.MESSAGE: helper.error_message(json_)}

        out = helper.score_to_output(json_)
        out[Output.FOUND] = True
        return insightconnect_plugin_runtime.helper.clean(out)
