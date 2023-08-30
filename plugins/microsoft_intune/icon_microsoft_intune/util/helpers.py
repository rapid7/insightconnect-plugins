KEY_NAMES_EXCEPTIONS = {"azureADDeviceId": "azure_ad_device_id", "azureADRegistered": "azure_ad_registered"}


def handle_key_names_exceptions(output_object: dict) -> dict:
    for key, value in KEY_NAMES_EXCEPTIONS.items():
        field_value = output_object.get(key)
        if field_value:
            output_object[value] = field_value
            del output_object[key]
    return output_object
