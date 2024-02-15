from insightconnect_plugin_runtime.exceptions import PluginException

from domaintools.exceptions import (
    NotAuthorizedException,
    ServiceUnavailableException,
    BadRequestException,
    NotFoundException,
    InternalServerErrorException,
)
import logging

def make_request(action, *args, **kwargs):
    try:
        response = action(*args, **kwargs)
        logging.info("RESPONSE-----")
        logging.info(response)
        logging.info("END-----")
        return response.data()
    except BadRequestException as exception:
        raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=f"DomainToolsAPI: Bad Request: code "
                                                                              f"{exception.code}, reason "
                                                                              f"{exception.reason}")
    except ServiceUnavailableException as exception:
        raise PluginException(preset=PluginException.Preset.SERVICE_UNAVAILABLE, data=f"DomainToolsAPI: Service "
                                                                                      f"Unavailable: code "
                                                                                      f"{exception.code}, reason "
                                                                                      f"{exception.reason}")
    except NotAuthorizedException as exception:
        raise PluginException(preset=PluginException.Preset.UNAUTHORIZED, data=f"DomainToolsAPI: Authorization "
                                                                               f"Failed: code {exception.code}, "
                                                                               f"reason {exception.reason}")
    except NotFoundException as exception:
        raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=f"DomainToolsAPI: Action Not Found: code "
                                                                            f"{exception.code}, reason "
                                                                            f"{exception.reason}")
    except InternalServerErrorException as exception:
        raise PluginException(preset=PluginException.Preset.UNKNOWN, data=f"DomainToolsAPI: Internal Server Error: code"
                                                                          f" {exception.code}, "
                                                                          f"reason {exception.reason}")
    except Exception as exception:
        raise PluginException(preset=PluginException.Preset.UNKNOWN, data=f"DomainTools API Request Failed: {response}")
