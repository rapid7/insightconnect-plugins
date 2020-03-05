import komand
from .schema import ResetFactorsInput, ResetFactorsOutput, Input, Output, Component
# Custom imports below
import requests
from komand_okta.util import helpers
from komand.exceptions import PluginException


class ResetFactors(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='reset_factors',
            description=Component.DESCRIPTION,
            input=ResetFactorsInput(),
            output=ResetFactorsOutput())

    def run(self, params={}):
        """ Get the user by email """
        email = params.get(Input.EMAIL)
        okta_url = self.connection.okta_url
        user_id = helpers.get_user_id(email, self.connection, self.logger)

        if user_id is None:
            return {Output.SUCCESS: False}

        """ Get enrolled factors by user id """
        url = requests.compat.urljoin(okta_url, f'/api/v1/users/{user_id}/factors')
        response = self.connection.session.get(url)
        data = response.json()

        """ Reset all factors """
        for factor in data:
            factor_id = factor['id']
            url = requests.compat.urljoin(okta_url, f'/api/v1/users/{user_id}/factors/{factor_id}')
            response = self.connection.session.delete(url)

            if response.status_code != 204:
                data = response.json()
                error_code = data['errorCode']
                error_summary = data['errorSummary']
                self.logger.error(f'Okta: {response.status_code} error. Error code: {error_code}. {error_summary}')
                raise PluginException(cause='Reset factors error', assistance=data['errorSummary'])

        return {Output.EMAIL: email, Output.USER_ID: user_id, Output.SUCCESS: True}
