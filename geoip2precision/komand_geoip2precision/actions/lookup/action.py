import komand
from .schema import LookupInput, LookupOutput
# Custom imports below
import geoip2.webservice


class Lookup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='lookup',
                description='Lookup IP address information',
                input=LookupInput(),
                output=LookupOutput())

    def run(self, params={}):
        address = params.get('address')
        user = self.connection.user
        license = self.connection.license

        # Set client
        client = geoip2.webservice.Client(user, license)

        try:
        # Make request to insights service
          response = client.insights(address)
        except geoip2.errors.AuthenticationError:
          self.logger.error('Authentication failed')
          raise
        except ValueError:
          self.logger.error('Invalid address provided')
          raise

        # Parse data from response
        asn = int(response.traits.autonomous_system_number)
        org = str(response.traits.autonomous_system_organization)
        domain = str(response.traits.domain)
        time_zone = str(response.location.time_zone)
        city = str(response.city.name)
        state = str(response.subdivisions.most_specific.iso_code)
        postal = int(response.postal.code)
        country = str(response.country.iso_code)
        registered_country = str(response.registered_country.iso_code)
        longitude = str(response.location.longitude)
        latitude = str(response.location.latitude)

        dic = {"address": address,
          "asn": asn,
          "org": org,
          "domain": domain,
          "time_zone": time_zone,
          "city": city,
          "state": state,
          "postal": postal,
          "country": country,
          "registered_country": registered_country,
          "longitude": longitude,
          "latitude": latitude,
        }   

        return dic

    def test(self):
        user = self.connection.user
        license = self.connection.license

        # Set client
        client = geoip2.webservice.Client(user, license)

        # Test user ID and license key
        try:
          response = client.insights() 
        except geoip2.errors.AuthenticationError: 
          self.logger.error('Invalid user ID or license key')
          raise
          
        return {}
