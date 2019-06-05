import komand
from .schema import GetFileRuleInput, GetFileRuleOutput, Input, Output, Component
from komand.exceptions import PluginException
# Custom imports below
import requests

class GetFileRule(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_file_rule',
                description=Component.DESCRIPTION,
                input=GetFileRuleInput(),
                output=GetFileRuleOutput())

    def run(self, params={}):
        file_rule_id = params.get(Input.FILE_RULE_ID)

        self.logger.info(f"Getting file rule {file_rule_id}")

        url = f"{self.connection.host}/api/bit9platform/v1/fileRule/{file_rule_id}"
        r = self.connection.session.get(url, verify=self.connection.verify)

        try:
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            self.logger.info(f"Call to Carbon Black raised exception: {e}")
            raise PluginException(cause="Call to Carbon Black failed",
                                  assistance=r.text)

        result = komand.helper.clean(r.json())

        return {Output.FILE_RULE: result}
