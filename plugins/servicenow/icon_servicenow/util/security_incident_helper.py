boolean_fields_to_convert = ["active", "risk_score_override"]
integer_fields_to_convert = [
    "business_criticality",
    "close_code",
    "priority",
    "risk_score",
    "state",
    "substate",
]


def convert_boolean_fields(security_incident_object: dict) -> dict:
    for field in boolean_fields_to_convert:
        if security_incident_object.get(field):
            security_incident_object[field] = security_incident_object.get(field) == "true"
    return security_incident_object


def convert_integer_fields(security_incident_object: dict) -> dict:
    for field in integer_fields_to_convert:
        if security_incident_object.get(field):
            security_incident_object[field] = int(security_incident_object.get(field))
    return security_incident_object


def convert_security_incident_fields(security_incident_object: dict) -> dict:
    convert_boolean_fields(security_incident_object)
    convert_integer_fields(security_incident_object)
    return security_incident_object


def remove_integer_fields_with_zero(parameters: dict) -> dict:
    parameters_copy = parameters.copy()
    for key, value in parameters.items():
        if not value and isinstance(value, int):
            parameters_copy.pop(key)
    return parameters_copy
