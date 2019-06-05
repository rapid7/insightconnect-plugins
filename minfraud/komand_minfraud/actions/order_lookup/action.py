import komand
from .schema import OrderLookupInput, OrderLookupOutput
# Custom imports below
import minfraud


class OrderLookup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='order_lookup',
                description='Query order info',
                input=OrderLookupInput(),
                output=OrderLookupOutput())

    def run(self, params={}):
        address = params.get('address')
        order_amount = params.get('order_amount')
        order_currency = params.get('order_currency')
        order_discount_code = params.get('order_discount_code')
        order_affiliate_id = params.get('order_affiliate_id')
        order_subaffiliate_id = params.get('order_subaffiliate_id')
        order_referrer_uri = params.get('order_referrer_uri')
        order_is_gift = params.get('order_is_gift')
        order_has_gift_message = params.get('order_has_gift_message')
        user = self.connection.user
        license = self.connection.license

        # Set client
        client = minfraud.Client(user, license)

        # Define request
        request = {'device': {'ip_address': address}}
        order = {}
        if order_amount:
          order['amount'] = float(order_amount)
        if order_currency:
          order['currency'] = order_currency
        if order_discount_code:
          order['discount_code'] = order_discount_code
        if order_affiliate_id:
          order['affiliate_id'] = order_affiliate_id
        if order_subaffiliate_id:
          order['subaffiliate_id'] = order_subaffiliate_id
        if order_referrer_uri:
          order['referrer_uri'] = order_referrer_uri
        order['is_gift'] = order_is_gift
        order['has_gift_message'] = order_has_gift_message

        # Add order dic to request
        request['order'] = order

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
