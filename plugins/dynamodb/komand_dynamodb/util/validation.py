from jsonschema import validate, ValidationError
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.action import Action
from typing import Dict, Callable


def additional_argument_validator(param_name: str, schema: Dict) -> Callable:
    """
    additional_argument_validator A decorator factory which allows adding an extra
    input validation step to the run method inside an Action

    :param param_name: parameter inside params argument to be validated
    :param schema: json schema for validating the parameter

    :return: the decorator function that enables validation
    """

    def _decorator(method: Callable) -> Callable:
        def validated_method(self: Action, params: Dict) -> Dict:
            parameter = params.get(param_name)
            if parameter:
                try:
                    validate(parameter, schema=schema)
                except ValidationError as validation_error:
                    raise PluginException(
                        cause=f"Extra input validation failed on {param_name}",
                        assistance=f"Please check if {param_name} is of correct format",
                        data=validation_error.cause,
                    )
            result = method(self, params)
            return result

        return validated_method

    return _decorator
