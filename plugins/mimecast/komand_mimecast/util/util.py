from typing import Dict, Any, Union

from komand_mimecast.util.constants import BASE_HOSTNAME_MAP, DEFAULT_REGION


class Utils:
    @staticmethod
    def prepare_base_url(region: str = DEFAULT_REGION) -> str:
        return f"https://{BASE_HOSTNAME_MAP.get(region)}.mimecast.com"

    @staticmethod
    def normalize(key: str, value: str) -> dict:
        if "_" not in key:
            if value and value != "none":
                return {key: value}
            return {}
        # pylint: disable=unnecessary-lambda
        chunks = list(filter(lambda c: len(c), key.split("_")))

        for i in range(1, len(chunks)):
            chunks[i] = chunks[i].capitalize()
        if value and value not in ("none", "None"):
            return {"".join(chunks): value}
        return {}

    @staticmethod
    def return_non_empty(input_dict: Dict[str, Any]) -> Union[Dict[Any, Any], Any]:
        """return_non_empty. Cleans up recursively the dictionary

        :param input_dict: Input dictionary
        :type input_dict: Dict[str, Any]

        :rtype: Union[Dict[Any, Any], None]
        """

        temp_dict = {}
        for key, value in input_dict.items():
            if value is not None and value != "" and value != []:
                if isinstance(value, dict):
                    return_dict = Utils.return_non_empty(value)
                    if return_dict:
                        temp_dict[key] = return_dict
                elif isinstance(value, list):
                    return_value = [
                        Utils.return_non_empty(element) if isinstance(element, dict) else element for element in value
                    ]
                    return_value = list(filter(None, return_value))
                    if return_value:
                        temp_dict[key] = return_value
                else:
                    temp_dict[key] = value
        return temp_dict
