import komand
from .schema import DeviceLookupInput, DeviceLookupOutput
# Custom imports below
import minfraud


class DeviceLookup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='device_lookup',
                description='Query device info',
                input=DeviceLookupInput(),
                output=DeviceLookupOutput())

    def run(self, params={}):
        address = params.get('address')
        user_agent = params.get('user_agent')
        accept_language = params.get('accept_language')
        user = self.connection.user
        license = self.connection.license

        # Set client
        client = minfraud.Client(user, license)

        # Define request
        device = {'ip_address': address}
        if user_agent:
          device['user_agent'] = user_agent
        if accept_language:
          device['accept_language'] = accept_language

        try:
          # Generate request
          insights = client.insights({'device': device})
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

        return {'risk_score': risk_score,
          'ip_result': ip_result,
          'device_result': device_result
          }

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
