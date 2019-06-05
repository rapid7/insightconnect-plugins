import komand
from .schema import AccountLookupInput, AccountLookupOutput
# Custom imports below
import minfraud


class AccountLookup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='account_lookup',
                description='Query account info',
                input=AccountLookupInput(),
                output=AccountLookupOutput())

    def run(self, params={}):
        address = params.get('address')
        user_id = params.get('user_id')
        username_md5 = params.get('username_md5')
        user = self.connection.user
        license = self.connection.license

        # Set client
        client = minfraud.Client(user, license)

        # Define request
        request = {'device': {'ip_address': address}}
        account = {}
        if user_id:
          account['user_id'] = user_id
        if username_md5:
          account['username_md5'] = username_md5

        # Add account dic to request
        if account:
          request['account'] = account
        else:
          self.logger.info('No account info provided')

        try:
        # Generate request
          insights = client.insights(request)
        except minfraud.AuthenticationError:
          self.logger.error('Authentication failed')
          raise
        except minfraud.InsufficientFundsError:
          self.logger.error('Insufficient funds')
          raise
        except minfraud.InvalidRequestError:
          self.logger.error('Invalid request')
          raise
        except minfraud.HttpError:
          self.logger.error('Unexpected HTTP error occurred')
          raise
        except minfraud.MinFraudError:
          self.logger.error('Unexpected content received from server')
          raise

        # Overall risk score
        risk_score = str(insights.risk_score)
        return {'risk_score': risk_score}

    def test(self):
        user = self.connection.user
        license = self.connection.license

        # Set client
        client = minfraud.Client(user, license)

        # Define request
        request = {'device': {'ip_address': '8.8.8.8'}}

        try:
        # Generate request
          insights = client.insights(request)
        except minfraud.AuthenticationError:
          self.logger.error('Authentication failed')
          raise
        except minfraud.InsufficientFundsError:
          self.logger.error('Insufficient funds')
          raise
        return {}
