import komand
from .schema import ConnectionSchema, Input
# Custom imports below
import jbxapi
from komand.exceptions import ConnectionTestException


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info('Connect: Connecting...')

        api_key = params.get('api_key').get('secretKey')
        api_url = params.get('url')
        if api_url is None:
            api_url = jbxapi.API_URL

        self.api = jbxapi.JoeSandbox(api_key, api_url)

        self.logger.info('Connect: Connected successfully')

    def test(self):
        try:
            self.api.list()
        except jbxapi.MissingParameterError as e:
            raise ConnectionTestException(
                cause=str(e),
                assistance='Please make sure that you are using Joe Sandbox '
                'according to the documentation.'
            )
        except jbxapi.InvalidParameterError as e:
            raise ConnectionTestException(
                cause=str(e),
                assistance='If the issue persists please contact support.'
            )
        except jbxapi.InvalidApiKeyError:
            raise ConnectionTestException(
                preset=ConnectionTestException.Preset.API_KEY
            )
        except jbxapi.ServerOfflineError:
            raise ConnectionTestException(
                preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE
            )
        except jbxapi.InternalServerError:
            raise ConnectionTestException(
                preset=ConnectionTestException.Preset.SERVER_ERROR
            )
        except jbxapi.PermissionError:
            raise ConnectionTestException(
                preset=ConnectionTestException.Preset.UNAUTHORIZED
            )
        except jbxapi.ApiError as e:
            raise ConnectionTestException(
                cause='An error occured: ' + str(e),
                assistance='If the issue persists please contact support.'
            )
