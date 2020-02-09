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
        if not user_id:
            raise PluginException(cause='user_id is required')

        try:
            okta_url = self.connection.okta_url
            url = requests.compat.urljoin(okta_url, f'/api/v1/users/{user_id}/factors')
            response = self.connection.session.get(url)
            if response.status_code not in range(200, 299):
                raise PluginException(
                    cause="Received HTTP %d status code from Okta. Please verify your Okta server status and "
                          "try again.",
                    assistance="If the issue persists please contact support.",
                    data=f"{response.status_code}, {response.text}"
                )
            data = response.json()

            for factor in data:
                if factor['factorType'] == "push":
                    return {Output.FACTORS: factor}

        except json.decoder.JSONDecodeError:
            raise PluginException(
                cause="Received an unexpected response from Okta ",
                assistance="(non-JSON or no response was received).",
                data=response.text
            )
        except TypeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)
        except KeyError as e:
            raise PluginException(cause='Key error has occured: %s' % e)
        except Exception as e:
            raise PluginException(cause='There was an error attempting to connect to the Okta API: %s' % e)
