from typing import Union

from insightconnect_plugin_runtime.exceptions import PluginException
from zenpy.lib.exception import (
    APIException,
    RatelimitBudgetExceeded,
    RecordNotFoundException,
    SearchResponseLimitExceeded,
    TooManyValuesException,
    ZenpyCacheException,
    ZenpyException,
)

from icon_zendesk.util.messages import Messages


def detect_type_exception(error: Union[ZenpyException, APIException]) -> None:
    if issubclass(type(error), ZenpyException):
        detect_zenpy_exception(error)
    elif issubclass(type(error), APIException):
        detect_api_exception(error)
    else:
        raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)


def detect_zenpy_exception(error: ZenpyException) -> None:
    if type(error) is ZenpyCacheException:
        raise PluginException(cause=Messages.EXCEPTION_ZENPY_CACHE_CAUSE)
    elif type(error) is RatelimitBudgetExceeded:
        raise PluginException(cause=Messages.EXCEPTION_RATE_LIMIT_BUDGED_EXCEEDED_CAUSE)


def detect_api_exception(error: APIException) -> None:
    if type(error) is RecordNotFoundException:
        raise PluginException(
            cause=Messages.EXCEPTION_RECORD_NOT_FOUND_CAUSE,
            assistance=Messages.EXCEPTION_RECORD_NOT_FOUND_ASSISTANCE,
            data=error,
        )
    elif type(error) is TooManyValuesException:
        raise PluginException(
            cause=Messages.EXCEPTION_TOO_MANY_VALUES_CAUSE,
            assistance=Messages.EXCEPTION_TOO_MANY_VALUES_ASSISTANCE,
            data=error,
        )
    elif type(error) is SearchResponseLimitExceeded:
        raise PluginException(
            cause=Messages.EXCEPTION_SEARCH_RESPONSE_LIMIT_EXCEEDED_CAUSE,
            assistance=Messages.EXCEPTION_SEARCH_RESPONSE_LIMIT_EXCEEDED_ASSISTANCE,
            data=error,
        )
