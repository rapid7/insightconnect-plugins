from typing import Union
from insightconnect_plugin_runtime.helper import return_non_empty


def clean(item_to_clean: Union[dict, list]) -> Union[dict, list]:
    if isinstance(item_to_clean, list):
        return [clean(item.copy()) for item in item_to_clean]
    if not isinstance(item_to_clean, dict):
        return item_to_clean
    return return_non_empty(item_to_clean.copy())
