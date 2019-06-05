import komand

def clean(object):
    cleaned = komand.helper.clean_list(object) if isinstance(object, list) else komand.helper.clean_dict(object)

    # The only *real* difference here is how we have to iterate through these different collection types
    if isinstance(cleaned, list):
        for key, value in enumerate(cleaned):
            if isinstance(value, list) or isinstance(value, dict):
                cleaned[key] = clean(value)
    elif isinstance(cleaned, dict):
        for key, value in cleaned.items():
            if isinstance(value, dict) or isinstance(value, list):
                cleaned[key] = clean(value)

    return cleaned
