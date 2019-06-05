import komand
from .schema import EventLookupInput, EventLookupOutput
# Custom imports below
import minfraud


class EventLookup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='event_lookup',
                description='Query event info',
                input=EventLookupInput(),
                output=EventLookupOutput())

    def run(self, params={}):
        address = params.get('address')
        transaction_id = params.get('transaction_id')
        shop_id = params.get('shop_id')
        time = params.get('time')
        event_type = params.get('event_type')
        user = self.connection.user
        license = self.connection.license

        # Set client
        client = minfraud.Client(user, license)

        # Define request
        request = {'device': {'ip_address': address}}
        event = {}
        if transaction_id:
          event['transaction_id'] = transaction_id
        if shop_id:
          event['shop_id'] = shop_id
        if time:
          event['time'] = time
        if event_type != "none":
          event['type'] = event_type

        # Add event dic to request
        # TO-DO - raise exception "if not event"
        if event:
          request['event'] = event
        else:
          self.logger.info('No event info provided')

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
