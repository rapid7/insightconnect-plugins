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

        try:
            okta_url = self.connection.okta_url
            url = requests.compat.urljoin(okta_url, f"/api/v1/users/{user_id}/factors/{factor_id}/verify")
            response = self.connection.session.post(url)
            if response.status_code not in range(200, 299):
                raise PluginException(
                    cause=f"Received HTTP {response.status_code} status code from Okta. Please verify your "
                          f"Okta server status and try again.",
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
        except (json.decoder.JSONDecodeError, TypeError):
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)
        except KeyError as e:
            raise PluginException(cause=f"An error has occurred retrieving data from the Okta API: {e}",
                                  assistance="It looks like we didn't get data we were expecting back. Was "
                                             "the Factor ID supplied a push type and not something else, "
                                             "such as an SMS?",
                                  data=data)
        except Exception:
            raise PluginException(cause=PluginException.Preset.UNKNOWN)
