def serialize(data, human=False):
    root_fields = [
        'host',
        'version',
        'http_address',
        'id',
        'name'
    ]
    if human:
        d = {k: '' for k in root_fields}
        d['result'] = {'text': str(data)}
    else:
        d = {k: data.pop(k) for k in root_fields}
        d['result'] = data
    return d


def check_types(valid_types, types_str):
    return [x for x in types_str.split(',') if x not in valid_types]
