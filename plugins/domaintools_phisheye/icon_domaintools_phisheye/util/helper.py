from domaintools.exceptions import (
    NotAuthorizedException,
    ServiceUnavailableException,
    BadRequestException,
    NotFoundException,
    InternalServerErrorException,
)
from insightconnect_plugin_runtime.exceptions import PluginException


class Helper:
    @staticmethod
    def make_request(action, logger, *args, **kwargs):
        try:
            response = action(*args, **kwargs)
            return response.data()
        except BadRequestException as error:
            cause = "DomainToolsAPI: Bad Request:"
            assistance = f"code {error.code}, reason {error.reason}"
        except ServiceUnavailableException as error:
            cause = "DomainToolsAPI: Service Unavailable:"
            assistance = f"code {error.code}, reason {error.reason}"
        except NotAuthorizedException as error:
            cause = "DomainToolsAPI: Authorization Failed:"
            assistance = f"code {error.code}, reason {error.reason}"
        except NotFoundException as error:
            cause = "DomainToolsAPI: Action Not Found:"
            assistance = f"code {error.code}, reason {error.reason}"
        except InternalServerErrorException as error:
            cause = "DomainToolsAPI: Internal Server Error:"
            assistance = f"code {error.code}, reason {error.reason}"

        logger.error(f"DomainToolsAPI: {cause} {assistance}")
        raise PluginException(cause=cause, assistance=assistance)
