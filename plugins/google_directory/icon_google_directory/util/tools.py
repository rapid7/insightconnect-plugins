import logging


class Message:
    USER_CONTACT_CAUSE_USER_NOT_FOUND = "Contact information was not found in server's response."
    USER_CONTACT_ASSISTANCE_USER_NOT_FOUND = "Please check and verify if the user exists."
    USER_CONTACT_CAUSE = "Something went wrong"
    USER_CONTACT_ASSISTANCE = "Please check the logs for further information and contact the Insight Connect team if " \
                              "the error persists "


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


def return_contact_information_name(input_dict: dict) -> dict:
    """return_contact_informations. Function allows to map data that contains contact informations retrieved from
    Google API users().list()

    :param input_dict: Input dict as a response got from Google API
    :type input_dict: dict

    :returns: Mapped dictionary that contains keys such as 'addresses', 'phones', and 'emails'
    :rtype: dict
    """
    if input_dict.get("users") is None:
        return {"name": None}
    for user in input_dict.get("users"):
        name = user.get("name").get("fullName")
        addresses_list = user.get("addresses", [])
        phones_list = [element.get("value") for element in user.get("phones", [])]
        emails_list = [element.get("address") for element in user.get("emails", [])]
        for address in addresses_list:
            if "streetAddress" in address:
                address["street"] = address.pop("streetAddress")
            if "postalCode" in address:
                address["postal_code"] = address.pop("postalCode")
        return {"name": name, "addresses": addresses_list, "phone_numbers": phones_list, "email_addresses": emails_list}


def handle_service_error(error) -> dict:
    if error:
        logging.info("Hey hephzi this is what you're looking for" + str(error))
        message = {"cause": "User was not found",
                   "assistance": "A user was not found with the passed search parameters",
                   "data": error}
    else:
        message = {"cause": "Something went wrong",
                   "assistance": "Please check the logs for further information and contact the Insight Connect team "
                                 "if the error persists",
                   "data": error}
    return message
