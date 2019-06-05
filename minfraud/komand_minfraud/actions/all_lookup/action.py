import komand
from .schema import AllLookupInput, AllLookupOutput
# Custom imports below
import json
import minfraud


class AllLookup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='all_lookup',
                description='Query any info',
                input=AllLookupInput(),
                output=AllLookupOutput())

    def run(self, params={}):
        address = params.get('address')
        user_agent = params.get('user_agent')
        accept_language = params.get('accept_language')
        domain = params.get('domain')
        email = params.get('email')
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
        issuer_id_number = params.get('card_issuer_id_number')
        last_4_digits = params.get('card_last_4_digits')
        token = params.get('card_token')
        bank_name = params.get('card_bank_name')
        bank_phone_country_code = params.get('bank_phone_country_code')
        bank_phone_number = params.get('bank_phone_number')
        avs_result = params.get('avs_result')
        cvv_result = params.get('cvv_result')
        transaction_id = params.get('transaction_id')
        shop_id = params.get('shop_id')
        time = params.get('time')
        event_type = params.get('event_type')
        user_id = params.get('user_id')
        username_md5 = params.get('username_md5')
        item_category = params.get('item_category')
        item_id = params.get('item_id')
        quantity = params.get('quantity')
        price = params.get('price')
        order_amount = params.get('order_amount')
        order_currency = params.get('order_currency')
        order_discount_code = params.get('order_discount_code')
        order_affiliate_id = params.get('order_affiliate_id')
        order_subaffiliate_id = params.get('order_subaffiliate_id')
        order_referrer_uri = params.get('order_referrer_uri')
        order_is_gift = params.get('order_is_gift')
        order_has_gift_message = params.get('order_has_gift_message')
        payment_processor = params.get('payment_processor')
        payment_was_authorized = params.get('payment_was_authorized')
        payment_decline_code = params.get('payment_delince_code')
        user = self.connection.user
        license = self.connection.license

        # Set client
        client = minfraud.Client(user, license)

        # Initiate request dict
        request = {}

        # Initiate all_result dict
        all_result = {}

        ################################
        # Device Request
        ###############################
        # Define device request
        device = {}
        device['ip_address'] = address
        if user_agent:
          device['user_agent'] = user_agent
        if accept_language:
          device['accept_language'] = accept_language

        request['device'] = device

        ###############################
        # Email Request
        ##############################
        # Define email request
        email_dic = {}
        if domain:
          email_dic['domain'] = domain
        if email:
          email_dic['address'] = email

        if email_dic:
          request['email'] = email_dic

        ###############################
        # Billing Request
        ##############################
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

        if billing:
          request['billing'] = billing

        ################################
        # Shipping Request
        ###############################
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

        if shipping:
          request['shipping'] = shipping

        ################################
        # Card Request
        ###############################
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

        if credit_card:
          request['credit_card'] = credit_card

        ################################
        # Event Request
        ###############################
        event = {}
        if transaction_id:
          event['transaction_id'] = transaction_id
        if shop_id:
          event['shop_id'] = shop_id
        if time:
          event['time'] = time
        if event_type != "none":
          event['type'] = event_type

        if event:
          request['event'] = event

        ################################
        # Account Request
        ###############################
        account = {}
        if user_id:
          account['user_id'] = user_id
        if username_md5:
          account['username_md5'] = username_md5

        if account:
          request['account'] = account


        ################################
        # Cart Request
        ###############################
        shopping_cart = {}
        if item_category:
          shopping_cart['category'] = item_category
        if item_id:
          shopping_cart['item_id'] = item_id
        if quantity:
          shopping_cart['quantity'] = quantity
        if price:
          shopping_cart['price'] = float(price)

        if shopping_cart:
          shopping_cart = [shopping_cart]
          request['shopping_cart'] = shopping_cart

        ################################
        # Order Request
        ###############################
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

        request['order'] = order

        ################################
        # Payment Request
        ###############################
        payment = {}
        if payment_processor != "none":
          payment['processor'] = payment_processor
        if payment_decline_code:
          payment['decline_code'] = payment_decline_code
        payment['was_authorized'] = payment_was_authorized

        request['payment'] = payment


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

        ###############################
        # Gather Device Data
        ##############################
        # IP portion of response
        ip = insights.ip_address

        # Overall risk score
        risk_score = str(insights.risk_score)

        # Risk score for IP
        risk = str(ip.risk)

        # City info
        confidence = ip.city.confidence
        geoname_id = ip.city.geoname_id
        name = str(ip.city.name)
        city = {'confidence': confidence,
          'geoname_id': geoname_id,
          'name': name
          }

        # Continent info
        code = str(ip.continent.code)
        geoname_id = ip.continent.geoname_id
        name = str(ip.continent.name)
        continent = {'code': code,
          'geoname_id': geoname_id,
          'name': name
          }

        # Country info
        confidence = ip.country.confidence
        geoname_id = ip.country.geoname_id
        name = str(ip.country.name)
        is_high_risk = ip.country.is_high_risk
        iso_code = str(ip.country.iso_code)
        country = {'confidence': confidence,
          'geoname_id': geoname_id,
          'name': name,
          'is_high_risk': is_high_risk,
          'iso_code': iso_code
          }

        # Location info
        accuracy_radius = ip.location.accuracy_radius
        average_income = ip.location.average_income
        population_density = ip.location.population_density
        latitude = str(ip.location.latitude)
        local_time = str(ip.location.local_time)
        longitude = str(ip.location.longitude)
        metro_code = ip.location.metro_code
        time_zone = str(ip.location.time_zone)
        location = {'accuracy_radius': accuracy_radius,
          'avergae_income': average_income,
          'population_density': population_density,
          'latitude': latitude,
          'local_time': local_time,
          'longitude': longitude,
          'metro_code': metro_code,
          'time_zone': time_zone
          }

        # Postal info
        code = int(ip.postal.code)
        confidence = ip.postal.confidence
        postal = {'code': code,
          'confidence': confidence
          }

        # Registered country info
        geoname_id = ip.registered_country.geoname_id
        iso_code = str(ip.registered_country.iso_code)
        name = str(ip.registered_country.name)
        registered_country = {'geoname_id': geoname_id,
          'iso_code': iso_code,
          'name': name
          }

        # Represented country info
        geoname_id = ip.represented_country.geoname_id
        iso_code = str(ip.represented_country.iso_code)
        name = str(ip.represented_country.name)
        _type = str(ip.represented_country.type)
        represented_country = {'geoname_id': geoname_id,
          'iso_code': iso_code,
          'name': name,
          '_type': _type
          }

        # Subdivisions info
        iso_code = str(ip.subdivisions.most_specific.iso_code)
        confidence = ip.subdivisions.most_specific.confidence
        geoname_id = ip.subdivisions.most_specific.geoname_id
        name = str(ip.subdivisions.most_specific.name)
        subdivisions = {'confidence': confidence,
          'geoname_id': geoname_id,
          'iso_code': iso_code,
          'name': name
          }

        # Traits info
        autonomous_system_number = ip.traits.autonomous_system_number
        autonomous_system_organization = str(ip.traits.autonomous_system_organization)
        domain = str(ip.traits.domain)
        is_anonymous_proxy = ip.traits.is_anonymous_proxy
        is_satellite_provider = ip.traits.is_satellite_provider
        isp = str(ip.traits.isp)
        ip_address = str(ip.traits.ip_address)
        organization = str(ip.traits.organization)
        user_type = str(ip.traits.user_type)
        traits = {'autonomous_system_number': autonomous_system_number,
          'autonomous_system_organization': autonomous_system_organization,
          'domain': domain,
          'is_anonymous_proxy': is_anonymous_proxy,
          'is_satellite_provider': is_satellite_provider,
          'isp': isp,
          'ip_address': ip_address,
          'organization': organization,
          'user_type': user_type
          }

        # Device info
        confidence = insights.device.confidence
        id = insights.device.id
        last_seen = insights.device.last_seen
        device_result = {'confidence': confidence,
          'id': id,
          'last_seen': last_seen
          }

        # Clean device dict
        device_result = komand.helper.clean_dict(device_result)

        # Set result dict
        ip_result = {'risk': risk,
          'city': city,
          'continent': continent,
          'country': country,
          'location': location,
          'postal': postal,
          'registered_country': registered_country,
          'represented_country': represented_country,
          'subdivisions': subdivisions,
          'traits': traits
          }

        # Clean dict
        for k, v in ip_result.items():
          if k != "risk":
            ip_result[k] = komand.helper.clean_dict(ip_result[k])

        all_result['ip_result'] = ip_result
        all_result['device_result'] = device_result

        ###################################
        # Gather email data
        ##################################
        is_free = insights.email.is_free
        is_high_risk = insights.email.is_high_risk
        email_result = {'is_free': is_free,
          'is_high_risk': is_high_risk
          }

        # Clean email dict
        email_result = komand.helper.clean_dict(email_result)

        all_result['email_result'] = email_result


        ###################################
        # Gather billing data
        ##################################
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

        all_result['billing_result'] = billing_result


        ###################################
        # Gather shipping data
        ##################################
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

        all_result['shipping_result'] = shipping_result

        ###################################
        # Gather card data
        ##################################
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

        all_result['credit_card_result'] = credit_card_result

        return {'all_result': all_result, 'risk_score': risk_score}

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
