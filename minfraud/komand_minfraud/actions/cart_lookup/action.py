import komand
from .schema import CartLookupInput, CartLookupOutput
# Custom imports below
import minfraud


class CartLookup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='cart_lookup',
                description='Query shopping cart info',
                input=CartLookupInput(),
                output=CartLookupOutput())

    def run(self, params={}):
        address = params.get('address')
        item_category = params.get('item_category')
        item_id = params.get('item_id')
        quantity = params.get('quantity')
        price = params.get('price')
        user = self.connection.user
        license = self.connection.license

        # Set client
        client = minfraud.Client(user, license)

        # Define request
        request = {'device': {'ip_address': address}}
        shopping_cart = {}
        if item_category:
          shopping_cart['category'] = item_category
        if item_id:
          shopping_cart['item_id'] = item_id
        if quantity:
          shopping_cart['quantity'] = quantity
        if price:
          shopping_cart['price'] = float(price)

        # Add shopping_cart dic to request
        if shopping_cart:
          shopping_cart = [shopping_cart]
          request['shopping_cart'] = shopping_cart
        else:
          self.logger.info('No shopping cart info provided')

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
