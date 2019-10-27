import komand
from .schema import DecodeUrlInput, DecodeUrlOutput, Input, Output, Component
# Custom imports below
from komand_mimecast.util import util
from komand.exceptions import PluginException


class DecodeUrl(komand.Action):
    # URI for Decode URL
    _URI = '/api/ttp/url/decode-url'

    def __init__(self):
        super(self.__class__, self).__init__(
                name='decode_url',
                description=Component.DESCRIPTION,
                input=DecodeUrlInput(),
                output=DecodeUrlOutput())

    def run(self, params={}):
        # Import variables from connection
        url = self.connection.url
        username = self.connection.username
        password = self.connection.password
        access_key = self.connection.access_key
        secret_key = self.connection.secret_key
        app_id = self.connection.app_id
        app_key = self.connection.app_key
        auth_type = self.connection.auth_type

        # Generate payload dictionary
        data = {"url": params.get(Input.ENCODED_URL)}

        mimecast_request = util.MimecastRequests()
        response = mimecast_request.mimecast_post(url=url, uri=DecodeUrl._URI, username=username,
                                                  password=password, auth_type=auth_type,
                                                  access_key=access_key, secret_key=secret_key,
                                                  app_id=app_id, app_key=app_key, data=data)
        # Logout
        logout = util.Authentication()
        logout_result = logout.logout(url=url, username=username, password=password,
                                      auth_type=auth_type, access_key=access_key,
                                      secret_key=secret_key, app_id=app_id, app_key=app_key)

        try:
            # Test for logout fail
            if logout_result['fail']:
                self.logger.error(logout_result['fail'])
                try:
                    raise PluginException(cause='Could not log out.',
                                          assistance='Contact support for help.',
                                          data='Status code is {}, see log for details'.format(response['meta']['status']))
                except KeyError:
                    raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                          data=response)

        except KeyError:
            # Unknown key error
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=logout_result)
        try:
            if not response['data'][0]['success']:
                raise PluginException(cause=f'The URL {params.get(Input.ENCODED_URL)} could not be decoded.',
                                      assistance='Please ensure that it is a Mimecast encoded URL',
                                      data=response['fail'])
        except KeyError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response)
        except IndexError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response)

        try:
            output = response['data'][0]['url']
        except KeyError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response)
        except IndexError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response)
        return {Output.DECODED_URL: output}
