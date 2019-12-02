import komand
from .schema import RiskDetectionInput, RiskDetectionOutput, Input, Output, Component

# Custom imports below
from icon_azure_ad_admin.util.komand_clean_with_nulls import remove_null_and_clean
from komand.exceptions import PluginException
import time
import requests
import json


class RiskDetection(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='risk_detection',
                description=Component.DESCRIPTION,
                input=RiskDetectionInput(),
                output=RiskDetectionOutput())
        self.risk_level = ""
        self.found = {}

    def initialize(self):
        new_risks = self.get_risks()

        try:
            result = new_risks['value']
        except KeyError:
            raise PluginException(cause='Unexpected output format.',
                                  assistance='The output from Azure Active Directory was not in the expected format. Please contact support for help.',
                                  data=result)

        for risk in result:
            self.found[risk.get('id')] = True

    def get_risks(self):
        headers = self.connection.get_headers(self.connection.get_auth_token())

        if self.risk_level and self.risk_level != "all":
            risk_detect_endpoint = f"https://graph.microsoft.com/beta/{self.connection.tenant}/riskDetections?$filter=riskLevel eq '{self.risk_level}'"
        else:
            risk_detect_endpoint = f"https://graph.microsoft.com/beta/{self.connection.tenant}/riskDetections"

        new_risks = requests.get(risk_detect_endpoint, headers=headers)

        if not new_risks.status_code == 200:
            raise PluginException(
                cause=f"Risk Detections returned an unexpected response: {new_risks.status_code}",
                assistance="Please contact support for help.",
                data=new_risks.text)

        try:
            return new_risks.json()
        except json.decoder.JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=new_risks)

    def poll(self):
        new_risks = self.get_risks()

        try:
            result = remove_null_and_clean(new_risks['value'])
        except KeyError:
            raise PluginException(cause='Unexpected output format.',
                                  assistance='The output from Azure Active Directory was not in the expected format. Please contact support for help.',
                                  data=new_risks)

        for risk in result:
            if risk.get('id') not in self.found:
                self.found[risk.get('id')] = True
                self.send({Output.RISK: risk})

    def run(self, params={}):
        self.risk_level = params.get(Input.RISK_LEVEL)
        self.frequency = params.get(Input.FREQUENCY, 60)
        self.initialize()
        while True:
            self.poll()
            time.sleep(self.frequency)
