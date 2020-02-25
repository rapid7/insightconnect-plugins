import komand
from .schema import GetFactorsInput, GetFactorsOutput, Input, Output, Component
# Custom imports below
import requests
import json
from komand.exceptions import PluginException


class GetFactors(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_factors',
            description=Component.DESCRIPTION,
            input=GetFactorsInput(),
            output=GetFactorsOutput())

    def run(self, params={}):
        user_id = params.get(Input.USER_ID)

        try:
            okta_url = self.connection.okta_url
            url = requests.compat.urljoin(okta_url, f'/api/v1/users/{user_id}/factors')
            response = self.connection.session.get(url)
            if response.status_code not in range(200, 299):
                raise PluginException(
                    cause=f"Received HTTP {response.status_code} status code from Okta. Please verify your "
                          f"Okta server status and try again.",
                    assistance="If the issue persists please contact support.",
                    data=f"{response.status_code}, {response.text}"
                )
            data = response.json()

            return {Output.FACTORS: data}

        except (json.decoder.JSONDecodeError, TypeError):
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)
        except KeyError as e:
            raise PluginException(cause=f"An error has occurred retrieving data from the Okta API: {e}",
                                  assistance="It looks like some data in the factors returned didn't have what"
                                             " we expected. Does this user have MFA enabled?",
                                  data=data)
        except Exception as e:
            raise PluginException(cause=PluginException.Preset.UNKNOWN)
