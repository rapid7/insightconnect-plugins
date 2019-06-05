import komand
from .schema import ShippingLookupInput, ShippingLookupOutput
# Custom imports below
import minfraud


class ShippingLookup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='shipping_lookup',
                description='Query shipping address info',
                input=ShippingLookupInput(),
                output=ShippingLookupOutput())

    def run(self, params={}):
        address = params.get('address')
        shipping_first_name = params.get('shipping_first_name')
        shipping_last_name = params.get('shipping_last_name')
        shipping_company = params.get('shipping_company')
        shipping_address = params.get('shipping_address')
        shipping_address_2 = params.get('shipping_address_2')
        shipping_city = params.get('shipping_city')
        shipping_region = params.get('shipping_region')
        shipping_country = params.get('shipping_country')
        shipping_postal = params.get('shipping_postal')
        shipping_phone_number = params.get('shipping_phone_number')
        shipping_phone_country_code = params.get('shipping_phone_country_code')
        shipping_delivery_speed = params.get('shipping_delivery_speed')
        user = self.connection.user
        license = self.connection.license

        # Set client
        client = minfraud.Client(user, license)

        # define request
        request = {'device': {'ip_address': address}}
        shipping = {}
        if shipping_first_name:
          shipping['first_name'] = shipping_first_name
        if shipping_last_name:
          shipping['last_name'] = shipping_last_name
        if shipping_company:
          shipping['company'] = shipping_company
        if shipping_address:
          shipping['address'] = shipping_address
        if shipping_address_2:
          shipping['address_2'] = shipping_address_2
        if shipping_city:
          shipping['city'] = shipping_city
        if shipping_region:
          shipping['region'] = shipping_region
        if shipping_country:
          shipping['country'] = shipping_country
        if shipping_postal:
          shipping['postal'] = shipping_postal
        if shipping_phone_number:
          shipping['phone_number'] = shipping_phone_number
        if shipping_phone_country_code:
          shipping['phone_country_code'] = shipping_phone_country_code
        if shipping_delivery_speed != "none":
          shipping['delivery_speed'] = shipping_delivery_speed

        # Add shipping dict to request
        if shipping:
          request['shipping'] = shipping
        else:
          self.logger.info('No shipping info provided')

        try:
          # Generate Request
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

        # Shipping info
        is_high_risk = insights.shipping_address.is_high_risk
        is_postal_in_city = insights.shipping_address.is_postal_in_city
        latitude = str(insights.shipping_address.latitude)
        longitude = str(insights.shipping_address.longitude)
        distance_to_ip_location = insights.shipping_address.distance_to_ip_location
        distance_to_billing_address = insights.shipping_address.distance_to_billing_address
        is_in_ip_country = insights.shipping_address.is_in_ip_country
        shipping_result = {'is_high_risk': is_high_risk,
          'is_postal_in_city': is_postal_in_city,
          'latitude': latitude,
          'longitude': longitude,
          'distance_to_ip_location': distance_to_ip_location,
          'distance_to_billing_address': distance_to_billing_address,
          'is_in_ip_country': is_in_ip_country
          }

        # Clean shipping dict
        shipping_result = komand.helper.clean_dict(shipping_result)

        return {'risk_score': risk_score, 'shipping_result': shipping_result}

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
