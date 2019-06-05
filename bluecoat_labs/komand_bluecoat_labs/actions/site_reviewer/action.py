import komand
from komand_bluecoat_labs.util import sitereview
from .schema import SiteReviewerInput, SiteReviewerOutput, Input, Output


class SiteReviewer(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='site_reviewer',
                description='Categorizes the given URL',
                input=SiteReviewerInput(),
                output=SiteReviewerOutput())

    def run(self, params={}):
        try:
            results = sitereview.main(params.get(Input.TARGET_URL))
            return {Output.SITE_REVIEW_RESULTS: results}
        except Exception:
            raise Exception("Unexpected issue occurred when reviewing site. Contact support for help")
