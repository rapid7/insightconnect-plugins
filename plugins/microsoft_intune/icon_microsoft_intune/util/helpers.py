KEY_NAMES_EXCEPTIONS = {"azureADDeviceId": "azure_ad_device_id", "azureADRegistered": "azure_ad_registered"}


def handle_key_names_exceptions(output_object: dict) -> dict:
    for key in KEY_NAMES_EXCEPTIONS.keys():
        if output_object.get(key):
            output_object[KEY_NAMES_EXCEPTIONS[key]] = output_object.get(key)
            del output_object[key]
    return output_object
