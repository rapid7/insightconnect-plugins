import komand
from komand.exceptions import PluginException
from .schema import MoveEmailInput, MoveEmailOutput, Input, Output, Component
# Custom imports below
import requests
import json


class MoveEmail(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='move_email',
                description=Component.DESCRIPTION,
                input=MoveEmailInput(),
                output=MoveEmailOutput())

        self.MOVE_MESSAGE_ENDPOINT = "https://graph.microsoft.com/v1.0/{tenant}/users/{mailbox_id}/messages/{message_id}/move"
        self.GET_FOLDERS_ENDPOINT = "https://graph.microsoft.com/v1.0/{tenant}/users/{mailbox_id}/mailFolders"

    def run(self, params={}):
        folder_name = params.get(Input.FOLDER_NAME)
        message_id = params.get(Input.EMAIL_ID)
        mailbox_id = params.get(Input.MAILBOX_ID)

        destination_id = self.find_folder(folder_name, mailbox_id)

        result = self.move_message(message_id, mailbox_id, destination_id)
        return {Output.SUCCESS: result}

    def move_message(self, message_id: str, mailbox_id: str, destination_id: str) -> bool:
        headers = self.connection.get_headers(self.connection.get_auth_token())
        endpoint_formatted = self.MOVE_MESSAGE_ENDPOINT.format(tenant=self.connection.tenant,
                                                               mailbox_id=mailbox_id,
                                                               message_id=message_id)
        data = {
            "destinationId": destination_id
        }

        result = requests.post(endpoint_formatted, json=data, headers=headers)
        try:
            result.raise_for_status()
        except Exception as e:
            self.logger.error(f"Move Email failed. Exception was {e}")
            raise PluginException(cause="Move Email failed.",
                                  assistance=result.text)

        new_parent_folder = result.json().get('parentFolderId')
        return new_parent_folder == destination_id

    def find_folder(self, folder_name: str, mailbox_id: str) -> str:
        """
        Find the folder ID specified by the user

        :param folder_name: Folder name to look for e.g. Inbox, Phishy Stuff
        :param mailbox_id: The Mailbox ID to check for folders e.g. bob@hotmail.com
        :return:
        Mailbox ID (String)
        """

        headers = self.connection.get_headers(self.connection.get_auth_token())
        folders_endpoint_formatted = self.GET_FOLDERS_ENDPOINT.format(tenant=self.connection.tenant,
                                                                      mailbox_id=mailbox_id)
        try:
            request = requests.get(folders_endpoint_formatted, headers=headers)
            response = request.json()
            folders_list = response.get('value')

            # See if we have more than 10 folders, if so the API sends the link to get the next 10
            next_link = response.get('@odata.nextLink')
            while next_link:
                self.logger.info(f"Looking for additional folders: {next_link}")
                request = requests.get(next_link, headers=headers)
                response = request.json()
                folders_list.extend(response.get('value'))
                next_link = response.get('@odata.nextLink')
        except json.JSONDecodeError as j:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON,
                                  data=j)
        except Exception as e:
            raise PluginException(cause="Unable to get folders.",
                                  assistance="Folder name or connection settings may be incorrect, see following error for more information.",
                                  data=e)

        self.logger.info(f"Looking for {folder_name}")
        for folder in folders_list:
            self.logger.info(f"Checking {folder.get('displayName')}")
            if folder_name == folder.get("displayName"):
                self.logger.info("Folder found")
                return folder.get("id")

        # We either had a 0 length folder list, or the folder was not found
        raise PluginException(cause=f"Folder named {folder_name} was not found",
                              assistance=f"Please check the folder name and verify it exists in {mailbox_id}")
