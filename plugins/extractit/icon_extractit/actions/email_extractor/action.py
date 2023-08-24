import insightconnect_plugin_runtime
from .schema import EmailExtractorInput, EmailExtractorOutput, Input, Output, Component

# Custom imports below
from icon_extractit.util.util import Regex
from icon_extractit.util.extractor import extract, clear_emails, fix_emails_suffix


class EmailExtractor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="email_extractor",
            description=Component.DESCRIPTION,
            input=EmailExtractorInput(),
            output=EmailExtractorOutput(),
        )

    def run(self, params={}):
        return {
            Output.EMAILS: fix_emails_suffix(
                clear_emails(extract(Regex.Email, params.get(Input.STR), params.get(Input.FILE)))
            )
        }
