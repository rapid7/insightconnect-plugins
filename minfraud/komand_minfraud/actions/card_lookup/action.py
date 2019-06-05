import komand
from .schema import CardLookupInput, CardLookupOutput
# Custom imports below
import minfraud


class CardLookup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='card_lookup',
                description='Query credit card info',
                input=CardLookupInput(),
                output=CardLookupOutput())

    def run(self, params={}):
        address = params.get('address')
        issuer_id_number = params.get('card_issuer_id_number')
        last_4_digits = params.get('card_last_4_digits')
        token = params.get('card_token')
        bank_name = params.get('card_bank_name')
        bank_phone_country_code = params.get('bank_phone_country_code')
        bank_phone_number = params.get('bank_phone_number')
        avs_result = params.get('avs_result')
        cvv_result = params.get('cvv_result')
        user = self.connection.user
        license = self.connection.license

        # Set client
        client = minfraud.Client(user, license)

        # define request
        request = {'device': {'ip_address': address}}
        credit_card = {}
        if issuer_id_number:
          credit_card['issuer_id_number'] = issuer_id_number
        if last_4_digits:
          credit_card['last_4_digits'] = last_4_digits
        if token:
          credit_card['token'] = token
        if bank_name:
          credit_card['bank_name'] = bank_name
        if bank_phone_country_code:
          credit_card['bank_phone_country_code'] = bank_phone_country_code
        if bank_phone_number:
          credit_card['bank_phone_number'] = bank_phone_number
        if avs_result:
          credit_card['avs_result'] = avs_result
        if cvv_result:
          credit_card['cvv_result'] = cvv_result

        # Add credit_card dict to request
        if credit_card:
          request['credit_card'] = credit_card
        else:
          self.logger.info('No credit card info provided')

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

        # Issuer info
        name = str(insights.credit_card.issuer.name)
        matches_provided_name = insights.credit_card.issuer.matches_provided_name
        phone_number = str(insights.credit_card.issuer.phone_number)
        matches_provided_phone_number = insights.credit_card.issuer.matches_provided_phone_number
        issuer = {'name': name,
          'matches_provided_name': matches_provided_name,
          'phone_number': phone_number,
          'matches_provided_phone_number': matches_provided_phone_number
          }

        # Clean issuer dict
        issuer = komand.helper.clean_dict(issuer)

        # Additional info
        brand = str(insights.credit_card.brand)
        country = str(insights.credit_card.country)
        is_issued_in_billing_address_country = insights.credit_card.is_issued_in_billing_address_country
        is_prepaid = insights.credit_card.is_prepaid
        type = insights.credit_card.type
        credit_card = {'brand': brand,
          'country': country,
          'is_issued_in_billing_address_country': is_issued_in_billing_address_country,
          'is_prepaid': is_prepaid,
          'type': type
          }

        # Clean additional dict
        credit_card = komand.helper.clean_dict(credit_card)

        # Combine dicts
        credit_card_result = {'issuer': issuer,
          'credit_card': credit_card
          }

        # Clean issuer_result dict
        credit_card_result = komand.helper.clean_dict(credit_card_result)

        return {'risk_score': risk_score, 'credit_card_result': credit_card_result}

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
