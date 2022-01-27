from insightconnect_plugin_runtime.exceptions import PluginException


class InputDataValidator:
    PARAMS_CHAR_LIMITING = {
        "message": 130,
        "alias": 512,
        "description": 15000,
        "responders": 50,
        "visibleTo": 50,
        "actions": (10, 50),
        "tags": (20, 50),
        "details": 8000,
        "entity": 512,
        "source": 100,
        "user": 100,
        "note": 25000,
    }

    EXCEPTION_MESSAGE_LIMIT = 'Limit of maximum input characters for parameter "{parameter_name}" has been exceeded (maximum {parameter_type} {maximum})'
    EXCEPTION_MESSAGE_REQUIRED = "No required parameter has been entered"
    PARAMS_CHAR_REQUIRED = "message"

    def validate(self, data: dict) -> None:

        for key, value in data.items():
            if key in self.PARAMS_CHAR_REQUIRED and value is None:
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=self.EXCEPTION_MESSAGE_REQUIRED)

            if key in self.PARAMS_CHAR_LIMITING:
                if isinstance(self.PARAMS_CHAR_LIMITING.get(key), tuple) and value is not None:
                    self._is_valid_input(value, self.PARAMS_CHAR_LIMITING.get(key)[0], key, "elements")

                    for element in value:
                        self._is_valid_input(element, self.PARAMS_CHAR_LIMITING.get(key)[1], key, "characters")

                if isinstance(self.PARAMS_CHAR_LIMITING.get(key), int) and value is not None:
                    self._is_valid_input(value, self.PARAMS_CHAR_LIMITING.get(key), key, "characters")

    def _is_valid_input(self, value: str, max_char: int, parameter_name: str, parameter_type: str) -> None:
        if self._check_params_limit(value, max_char):
            raise PluginException(
                preset=PluginException.Preset.UNKNOWN,
                data=self._exception_message(parameter_name, parameter_type, max_char),
            )

    def _check_params_limit(self, value: str, max_char: int) -> bool:
        return max_char < len(value)

    def _exception_message(self, parameter_name: str, parameter_type: str, max_char: int) -> str:
        return self.EXCEPTION_MESSAGE_LIMIT.format(
            parameter_name=parameter_name, parameter_type=parameter_type, maximum=max_char
        )
