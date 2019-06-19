import komand
from .schema import GetUserTokensInput, GetUserTokensOutput
# Custom imports below
from komand_wigle.util.utils import clear_empty_values


class GetUserTokens(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_user_tokens',
                description='Get all authorization tokens for the logged-in user',
                input=GetUserTokensInput(),
                output=GetUserTokensOutput())

    def run(self, params={}):
        self.logger.info('GetUserTokens: Fetching tokens ...')
        params = clear_empty_values(params)
        token_type = params.get('type', None)
        response = self.connection.call_api(
            'get', 'profile/apiToken', params={'type': token_type}
        )
        if isinstance(response, dict):
            return {'tokens': response['result']}
        else:
            return {'tokens': []}

    def test(self):
        return {
          'tokens': [
            {
              "authName": "AID5945ddaae0f0aec31e334e3be768e815",
              "token": "2f3e1b24382059f9ebc5eb518c4ecf50",
              "status": "STATUS_ACTIVE",
              "type": "API",
              "personId": 221291
            }
          ]
        }
