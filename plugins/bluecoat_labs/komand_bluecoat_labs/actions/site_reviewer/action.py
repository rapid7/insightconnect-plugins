import insightconnect_plugin_runtime
from komand_bluecoat_labs.util import sitereview
from .schema import SiteReviewerInput, SiteReviewerOutput, Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException


class SiteReviewer(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="site_reviewer",
            description="Categorizes the given URL",
            input=SiteReviewerInput(),
            output=SiteReviewerOutput(),
        )

    def run(self, params={}):
        try:
            results = sitereview.main(params.get(Input.TARGET_URL))
            return {Output.SITE_REVIEW_RESULTS: results}
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
