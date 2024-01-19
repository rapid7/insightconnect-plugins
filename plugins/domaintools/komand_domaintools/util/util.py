from domaintools.exceptions import (
    NotAuthorizedException,
    ServiceUnavailableException,
    BadRequestException,
    NotFoundException,
    InternalServerErrorException,
)
from insightconnect_plugin_runtime import PluginException


@staticmethod
def make_request(action, *args, **kwargs):
    try:
        response = action(*args, **kwargs)
        return response.data()
    except BadRequestException as exception:
        action.logger.error(f"DomainToolsAPI: Bad Request: code {exception.code}, reason {exception.reason}")
    except ServiceUnavailableException as exception:
        action.logger.error(f"DomainToolsAPI: Service Unavailable: code {exception.code}, reason {exception.reason}")
    except NotAuthorizedException as exception:
        action.logger.error(f"DomainToolsAPI: Authorization Failed: code {exception.code}, reason {exception.reason}")
    except NotFoundException as exception:
        action.logger.error(f"DomainToolsAPI: Action Not Found: code {exception.code}, reason {exception.reason}")
    except InternalServerErrorException as exception:
        action.logger.error(f"DomainToolsAPI: Internal Server Error: code {exception.code}, reason {exception.reason}")

    raise PluginException("DomainTools API Request Failed")
