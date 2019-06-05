import komand
from .schema import PaymentLookupInput, PaymentLookupOutput
# Custom imports below
import minfraud


class PaymentLookup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='payment_lookup',
                description='Query payment info',
                input=PaymentLookupInput(),
                output=PaymentLookupOutput())

    def run(self, params={}):
        address = params.get('address')
        payment_processor = params.get('payment_processor')
        payment_was_authorized = params.get('payment_was_authorized')
        payment_decline_code = params.get('payment_delince_code')
        user = self.connection.user
        license = self.connection.license

        # Set client
        client = minfraud.Client(user, license)

        # Define request
        request = {'device': {'ip_address': address}}
        payment = {}
        if payment_processor != "none":
          payment['processor'] = payment_processor
        if payment_decline_code:
          payment['decline_code'] = payment_decline_code
        payment['was_authorized'] = payment_was_authorized

        # Add payment dic to request
        request['payment'] = payment

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
