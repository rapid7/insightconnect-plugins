
def set_field_values(template, field_values, dirty=True):
    """Creates a new business object from a template using the field_values to provide key, value mapping"""
    buisness_object = []
    for bo_field in template["fields"]:
        if bo_field["name"] in field_values:
            # Set each dirty field to True if set to Flase the field will not be included in the request
            if dirty:
                bo_field["dirty"] = True
            bo_field["value"] = field_values.pop(bo_field["name"])
        buisness_object.append(bo_field)
    return buisness_object
