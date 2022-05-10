import datetime

from typing import Any, Dict, List, Union, Callable, Tuple


def return_non_empty(input_dict: Dict[str, Any]) -> Dict[Any, Any]:
    """return_non_empty. Cleans up recusively the dictionary

    :param input_dict:
    :type input_dict: Dict[str, Any]
    :rtype: Dict[Any, Any]
    """
    temp_dict = {}
    for key, value in input_dict.items():
        if value is not None and value != "":
            if isinstance(value, dict):
                return_dict = return_non_empty(value)
                if return_dict:
                    temp_dict[key] = return_dict
            elif isinstance(value, list):
                if len(value) > 0:
                    temp_dict[key] = value
            else:
                temp_dict[key] = value
    return temp_dict


def map_output(input_dict: Dict[str, Any]) -> Dict[Any, Any]:
    etag = input_dict.get("etag")
    if etag:
        input_dict["etag"] = etag.replace('"', "")
    return input_dict


def map_output_for_list(input_dict: List[Dict]) -> List[Dict]:
    output_list = []
    for element in input_dict:
        output_list.append(map_output(element))
    return output_list


def generate_query_params(
    status: str,
    created_time: Union[datetime.datetime, None] = None,
    last_update_time: Union[datetime.datetime, None] = None,
    assigned_to: Union[str, None] = None,
) -> Union[dict, None]:
    """generate_query_params. Generates query params for Get New Incidents trigger

    :param status: Input status of incidents
    :type status: str

    :param created_time: Time of creation ago of incidents as datetime.datetime object
    :type created_time: datetime.datetime

    :param last_update_time: Time of last update of incidents as datetime.datetime object
    :type last_update_time: datetime.datetime

    :param assigned_to: Member to be assigned to an incident
    :type assigned_to: str

    :rtype: dict
    """

    filter_status = f"properties/status eq '{status}'" if status != "All" else ""
    filter_created_time = f"properties/createdTimeUtc ge {created_time.isoformat()}Z" if created_time else ""
    filter_last_update_time = (
        f"properties/lastModifiedTimeUtc ge {last_update_time.isoformat()}Z" if last_update_time else ""
    )
    filter_assigned_to = f"properties/owner/assignedTo eq '{assigned_to}'" if assigned_to else ""

    filter_parameters = (filter_status, filter_created_time, filter_last_update_time, filter_assigned_to)
    if not any(filter_parameters):
        return None
    filter_output = ""
    for filter_parameter in filter_parameters:
        if filter_parameter:
            filter_output += filter_parameter + " and "
    if len(filter_output) > 2 and filter_output.split(" ")[-2] == "and":
        filter_output = filter_output[:-5]
    return {"filter": filter_output}


def request_execution_time(func: Callable) -> Callable:
    """request_execution_time. Measures time of request

    :param func: Function to be decorated
    :type func: Callable

    :rtype: Tuple[dict, float]
    """

    def _wrap(*args, **kwargs):
        start_request_time = datetime.datetime.now()
        response = func(*args, **kwargs)
        end_request_time = datetime.datetime.now()
        return response, end_request_time - start_request_time

    return _wrap
