import komand
from .schema import EmailLookupInput, EmailLookupOutput
# Custom imports below
import minfraud


class EmailLookup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='email_lookup',
                description='Query email info',
                input=EmailLookupInput(),
                output=EmailLookupOutput())

    def run(self, params={}):
        address = params.get('address')
        domain = params.get('domain')
        email = params.get('email')
        user = self.connection.user
        license = self.connection.license

        # Set client
        client = minfraud.Client(user, license)

        # Define request
        request = {'device': {'ip_address': address}}
        email_dic = {}
        if domain:
          email_dic['domain'] = domain
        if email:
          email_dic['address'] = email

        # Add email_dic to request
        if email_dic:
          request['email'] = email_dic
        else:
          self.logger.info('No email info provided')

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

        #TO-DO - rename email to email_result
        # Email info
        is_free = insights.email.is_free
        is_high_risk = insights.email.is_high_risk
        email_result = {'is_free': is_free,
          'is_high_risk': is_high_risk
          }

        # Clean email dict
        email_result = komand.helper.clean_dict(email_result)

        return {'risk_score': risk_score, 'email_result': email_result}

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
