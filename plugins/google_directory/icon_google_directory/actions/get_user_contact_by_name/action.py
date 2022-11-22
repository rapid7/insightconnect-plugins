import logging

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import GetUserContactByNameInput, GetUserContactByNameOutput, Input, Output, Component

# Custom imports below
from icon_google_directory.util.tools import return_contact_information_name, Message


class GetUserContactByName(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_user_contact_by_name",
            description=Component.DESCRIPTION,
            input=GetUserContactByNameInput(),
            output=GetUserContactByNameOutput(),
        )

    # def run(self, params={}):
    #     full_name = params.get(Input.FULL_NAME)
    #     try:
    #         response = (
    #             self.connection.service.users().list(customer="my_customer", query=f"name:'{full_name}'").execute()
    #         )
    #         return {Output.CONTACT: return_contact_information_name(response)}
    #     except Exception as exception:
    #         error = handle_service_error(exception)
    #         raise PluginException(cause=error.get("cause"), assistance=error.get("assistance"),
    #                               data=error.get("data"))

    def run(self, params={}):
        full_name = params.get(Input.FULL_NAME)
        try:
            # Generate response with full_name input
            response = (
                self.connection.service.users().list(customer="my_customer", query=f"name:'{full_name}'").execute()
            )
            print(f"RESPONSE: {response}")
            # If name exists in the response, then run return_contact_information_name on it
            if 'users' in response.keys():
                return {Output.CONTACT: return_contact_information_name(response)}

            # Otherwise, if "name" is NOT found, then throw the user not found messages
            else:
                # raise PluginException(cause=Message.USER_CONTACT_CAUSE_USER_NOT_FOUND,
                #                       assistance=Message.USER_CONTACT_ASSISTANCE_USER_NOT_FOUND)
                raise Exception()

        # Handles all errors
        except Exception as error:
            print(error)
            print(type(error))
            print(len(str(error)))
            # If error is 400
            if '400' in str(error):
                raise PluginException(cause=Message.USER_CONTACT_CAUSE_USER_NOT_FOUND,
                                      assistance=Message.USER_CONTACT_ASSISTANCE_USER_NOT_FOUND)

        # except Exception as exception:
        #     logging.info("YO HEPHZI, THIS IS THE 'except Exception as exception' SECTION")
        #     error = handle_service_error(exception)
        #     raise PluginException(cause=error.get("cause"), assistance=error.get("assistance"), data=exception)
