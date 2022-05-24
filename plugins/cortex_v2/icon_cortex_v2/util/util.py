tlp = {"WHITE": 0, "GREEN": 1, "AMBER": 2, "RED": 3}

def eq(field, value):
    # Based on https://github.com/TheHive-Project/Cortex4py/blob/2.1.0/cortex4py/query.py#L2
    return {'_field': field, '_value': value}
