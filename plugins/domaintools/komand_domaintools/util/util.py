from domaintools.exceptions import (
    NotAuthorizedException,
    ServiceUnavailableException,
    BadRequestException,
    NotFoundException,
    InternalServerErrorException,
)
from insightconnect_plugin_runtime.exceptions import PluginException


def make_request(action, *args, **kwargs):
    try:
        response = action(*args, **kwargs)
        return response.data()
    except BadRequestException as e:
        action.logger.error(f"DomainToolsAPI: Bad Request: code {e.code}, reason {e.reason}")
    except ServiceUnavailableException as e:
        action.logger.error(f"DomainToolsAPI: Service Unavailable: code {e.code}, reason {e.reason}")
    except NotAuthorizedException as e:
        action.logger.error(f"DomainToolsAPI: Authorization Failed: code {e.code}, reason {e.reason}")
    except NotFoundException as e:
        action.logger.error(f"DomainToolsAPI: Action Not Found: code {e.code}, reason {e.reason}")
    except InternalServerErrorException as e:
        action.logger.error(f"DomainToolsAPI: Internal Server Error: code {e.code}, reason {e.reason}")

    raise PluginException(cause="DomainTools API Request Failed")
