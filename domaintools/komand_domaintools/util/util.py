from domaintools.exceptions import (
    NotAuthorizedException, ServiceUnavailableException,
    BadRequestException, NotFoundException, InternalServerErrorException
)

@staticmethod
def make_request(action, *args, **kwargs):
    try:
        response = action(*args, **kwargs)
        return response.data()
    except BadRequestException as e:
        action.logger.error("DomainToolsAPI: Bad Request: code {}, reason {}".format(e.code, e.reason))
    except ServiceUnavailableException as e:
        action.logger.error("DomainToolsAPI: Service Unavailable: code {}, reason {}".format(e.code, e.reason))
    except NotAuthorizedException as e:
        action.logger.error("DomainToolsAPI: Authorization Failed: code {}, reason {}".format(e.code, e.reason))
    except NotFoundException as e:
        action.logger.error("DomainToolsAPI: Action Not Found: code {}, reason {}".format(e.code, e.reason))
    except InternalServerErrorException as e:
        action.logger.error("DomainToolsAPI: Internal Server Error: code {}, reason {}".format(e.code, e.reason))

    raise Exception('DomainTools API Request Failed')
