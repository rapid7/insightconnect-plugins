from insightconnect_plugin_runtime import helper


def remove_null_and_clean(in_dict):
    for key in in_dict.keys():
        if in_dict.get(key) == "null":
            in_dict.pop(key)
    return helper.clean(in_dict)
