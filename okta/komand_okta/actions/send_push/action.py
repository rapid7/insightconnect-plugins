import komand
from .schema import SendPushInput, SendPushOutput, Input, Output, Component
# Custom imports below
import requests
import json
from komand.exceptions import PluginException


class SendPush(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='send_push',
            description=Component.DESCRIPTION,
            input=SendPushInput(),
            output=SendPushOutput())

    def run(self, params={}):
        user_id = params.get(Input.USER_ID)
        factor_id = params.get(Input.FACTOR_ID)

        if not user_id:
            raise PluginException(cause='user_id is required')
        elif not factor_id:
            raise PluginException(cause='factor_id is required')

        try:
            okta_url = self.connection.okta_url
            url = requests.compat.urljoin(okta_url, f'/api/v1/users/{user_id}/factors/{factor_id}/verify')
            response = self.connection.session.post(url)
            if response.status_code not in range(200, 299):
                raise PluginException(
                    cause="Received HTTP %d status code from Okta. Please verify your Okta server status and "
                          "try again.",
                    assistance="If the issue persists please contact support.",
                    data=f"{response.status_code}, {response.text}"
                )

            data = response.json()
            self.logger.info(data)

            poll_status = data['factorResult']
            link = data['_links']['poll']['href']

            # It times out after 60 seconds automatically
            while poll_status == "WAITING":
                poll_response = self.connection.session.get(link)
                poll_data = poll_response.json()
                poll_status = poll_data['factorResult']

            return {Output.FACTOR_STATUS: poll_status}
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
