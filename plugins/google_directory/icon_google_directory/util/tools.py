class Message:
    USER_CONTACT_CAUSE = "Contact information was not found in server's response."
    USER_CONTACT_ASSISTANCE = "Please check and verify if the user exists."


def return_contact_informations(input_dict: dict) -> dict:
    """return_contact_informations. Function allows to map data that contains contact informations retrieved from Google API users().get()

    :param input_dict: Input dict as a response got from Google API
    :type input_dict: dict

    :returns: Mapped dictionary that contains keys such as 'addresses', 'phones', and 'emails'
    :rtype: dict
    """

    addresses_list = input_dict.get("addresses", [])
    phones_list = [element.get("value") for element in input_dict.get("phones", [])]
    emails_list = [element.get("address") for element in input_dict.get("emails", [])]
    for address in addresses_list:
        if "streetAddress" in address:
            address["street"] = address.pop("streetAddress")
        if "postalCode" in address:
            address["postal_code"] = address.pop("postalCode")
    return {"addresses": addresses_list, "phone_numbers": phones_list, "email_addresses": emails_list}
