class Message:
    USER_CONTACT_CAUSE = "Contact information was not found in server's response."
    USER_CONTACT_ASSISTANCE = "Please check and verify if the user exists."
    USER_CONTACT_500_CAUSE = "Connection failed"
    USER_CONTACT_500_ASSISTANCE = "Please check out your connection"


def return_contact_information(input_dict: dict) -> dict:
    """return_contact_information. Function allows to map data that contains contact informations retrieved from
    Google API users().get()

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

    # def return_contact_information_name(users: list) -> list:
    #     """return_contact_information. Function allows to map data that contains contact informations retrieved from
    #     Google API users().list()
    #
    #     :param input_dict: Input dict as a response got from Google API
    #     :type input_dict: dict
    #
    #     :returns: Mapped dictionary that contains keys such as 'addresses', 'phones', and 'emails'
    #     :rtype: dict
    #     """
    # if input_dict.get("users") is None:
    #     return {"addresses": [], "phone_numbers": [], "email_addresses": []}
    # return list(map(return_contact_information, users))


def return_contact_informations_name(input_dict: dict) -> dict:
    """return_contact_informations. Function allows to map data that contains contact informations retrieved from
    Google API users().list()

    :param input_dict: Input dict as a response got from Google API
    :type input_dict: dict

    :returns: Mapped dictionary that contains keys such as 'addresses', 'phones', and 'emails'
    :rtype: dict
    """
    if input_dict.get("users") is None:
        return {"addresses": [], "phone_numbers": [], "email_addresses": []}
    for user in input_dict.get("users"):
        addresses_list = user.get("addresses", [])
        phones_list = [element.get("value") for element in user.get("phones", [])]
        emails_list = [element.get("address") for element in user.get("emails", [])]
        for address in addresses_list:
            if "streetAddress" in address:
                address["street"] = address.pop("streetAddress")
            if "postalCode" in address:
                address["postal_code"] = address.pop("postalCode")
        return {"addresses": addresses_list, "phone_numbers": phones_list, "email_addresses": emails_list}
