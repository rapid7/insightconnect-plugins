import komand
from .schema import GetFactorsInput, GetFactorsOutput, Input, Output, Component
# Custom imports below
import requests
from komand.exceptions import PluginException


class GetFactors(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_factors',
            description=Component.DESCRIPTION,
            input=GetFactorsInput(),
            output=GetFactorsOutput())

    def run(self, params={}):
        self.logger.info("Getting factors %s", params)
        user_id = params.get(Input.USER_ID)
        if not user_id:
            raise ValueError('user_id is required')
        okta_url = self.connection.okta_url

        url = requests.compat.urljoin(okta_url, f'/api/v1/users/{user_id}/factors')
        response = self.connection.session.get(url)
        if response.status_code == 401:
            self.logger.error('Okta: Invalid token or domain')
        data = response.json()

        for factor in data:
            if factor['factorType'] == "push":
                return factor

        raise PluginException(cause='Okta: An error occurred')
