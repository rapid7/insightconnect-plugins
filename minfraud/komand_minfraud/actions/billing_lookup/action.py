import komand
from .schema import BillingLookupInput, BillingLookupOutput
# Custom imports below
import minfraud


class BillingLookup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='billing_lookup',
                description='Query billing address info',
                input=BillingLookupInput(),
                output=BillingLookupOutput())

    def run(self, params={}):
        address = params.get('address')
        billing_first_name = params.get('billing_first_name')
        billing_last_name = params.get('billing_last_name')
        billing_company = params.get('billing_company')
        billing_address = params.get('billing_address')
        billing_address_2 = params.get('billing_address_2')
        billing_city = params.get('billing_city')
        billing_region = params.get('billing_region')
        billing_country = params.get('billing_country')
        billing_postal = params.get('billing_postal')
        billing_phone_number = params.get('billing_phone_number')
        billing_phone_country_code = params.get('billing_phone_country_code')
        user = self.connection.user
        license = self.connection.license

        # Set client
        client = minfraud.Client(user, license)

        # define request
        request = {'device': {'ip_address': address}}
        billing = {}
        if billing_first_name:
          billing['first_name'] = billing_first_name
        if billing_last_name:
          billing['last_name'] = billing_last_name
        if billing_company:
          billing['company'] = billing_company
        if billing_address:
          billing['address'] = billing_address
        if billing_address_2:
          billing['address_2'] = billing_address_2
        if billing_city:
          billing['city'] = billing_city
        if billing_region:
          billing['region'] = billing_region
        if billing_country:
          billing['country'] = billing_country
        if billing_postal:
          billing['postal'] = billing_postal
        if billing_phone_number:
          billing['phone_number'] = billing_phone_number
        if billing_phone_country_code:
          billing['phone_country_code'] = billing_phone_country_code

        # Add billing dict to request
        if billing:
          request['billing'] = billing
        else:
          self.logger.info('No billing info provided')

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

        # Billing info
        is_postal_in_city = insights.billing_address.is_postal_in_city
        latitude = str(insights.billing_address.latitude)
        longitude = str(insights.billing_address.longitude)
        distance_to_ip_location = insights.billing_address.distance_to_ip_location
        # TO-DO - change to is_in_ip_country
        is_ip_in_country = insights.billing_address.is_in_ip_country
        billing_result = {'is_postal_in_city': is_postal_in_city,
          'latitude': latitude,
          'longitude': longitude,
          'distance_to_ip_location': distance_to_ip_location,
          'is_ip_in_country': is_ip_in_country
          }

        # Clean billing dict
        billing_result = komand.helper.clean_dict(billing_result)

        return {'risk_score': risk_score, 'billing_result': billing_result}

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
