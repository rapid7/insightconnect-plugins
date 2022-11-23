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

    def run(self, params={}):
        full_name = params.get(Input.FULL_NAME)
        try:

            # Generate response with full_name input
            print('1')
            response = (
                self.connection.service.users().list(customer="my_customer", query=f"name:'{full_name}'").execute()
            )
            # Print Response so we can see what's going on
            #   print(f"RESPONSE: {response}")
            # If 'users' exists in the response, then run return_contact_information_name on it
            #   if 'users' in response.keys():
            print('2')
            if 'users' in response.keys():
                print('3')
                return {Output.CONTACT: return_contact_information_name(response)}
            # Otherwise, if "name" is NOT found, then throw the user not found messages
            # else:
            #     raise PluginException(cause=Message.USER_CONTACT_CAUSE_USER_NOT_FOUND,
            #                           assistance=Message.USER_CONTACT_ASSISTANCE_USER_NOT_FOUND)
            else:
                print(response)
                raise PluginException(data=response)

        # Handles all errors
        except Exception as error:
            print('5')
            print("THIS IS THE SECOND EXCEPT EXCEPTION AS ERROR")
            print(error)
            print(type(error))
            print(len(str(error)))
            # If error is 400
            # if '400' in str(error):
            raise PluginException(cause=Message.USER_CONTACT_CAUSE_USER_NOT_FOUND,
                                  assistance=Message.USER_CONTACT_ASSISTANCE_USER_NOT_FOUND, data=error)

        # except Exception as exception:
        #     logging.info("YO HEPHZI, THIS IS THE 'except Exception as exception' SECTION")
        #     print(exception)
