import komand
import time
from .schema import (
    UsersAddedRemovedFromGroupInput,
    UsersAddedRemovedFromGroupOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
from komand.exceptions import PluginException
from komand_okta.util import helpers
import re


class UsersAddedRemovedFromGroup(komand.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="users_added_removed_from_group",
            description=Component.DESCRIPTION,
            input=UsersAddedRemovedFromGroupInput(),
            output=UsersAddedRemovedFromGroupOutput(),
        )

    def run(self, params={}):
        """Run the trigger"""
        group_list = params.get(Input.GROUP_IDS)
        okta_url = self.connection.okta_url
        current_list = self.get_users_in_group_list(group_list, okta_url)
        group_names = list()

        for group in group_list:
            # Get group names
            group_name_api = f"{okta_url}/api/v1/groups/{group}"
            response = self.connection.session.get(group_name_api)
            try:
                data = response.json()
            except ValueError:
                raise PluginException(
                    cause="Returned data was not in JSON format.",
                    assistance="Double check that group ID's are all valid.",
                    data=response.text,
                )
            helpers.raise_based_on_error_code(response)
            group_names.append(data["profile"]["name"])

        while True:
            new_list = self.get_users_in_group_list(group_list, okta_url)

            added = list()
            removed = list()
            for index, value in enumerate(group_list):

                # Find added group members
                added_users = []
                for new_user in new_list[index][value]:
                    found = False
                    for old_user in current_list[index][value]:
                        if new_user["id"] == old_user["id"]:
                            found = True

                    if not found:
                        added_users.append(new_user)

                # Find removed group members
                removed_users = []
                for old_user in current_list[index][value]:
                    found = False
                    for new_user in new_list[index][value]:
                        if old_user["id"] == new_user["id"]:
                            found = True

                    if not found:
                        removed_users.append(old_user)

                if added_users:
                    added.append({"group_name": group_names[index], "group_id": value, "users": added_users})
                if removed_users:
                    removed.append(
                        {
                            "group_name": group_names[index],
                            "group_id": value,
                            "users": removed_users,
                        }
                    )

            if added and removed:
                self.logger.info("Users added and removed, sending to orchestrator.")
                self.send({Output.USERS_ADDED_FROM_GROUPS: added, Output.USERS_REMOVED_FROM_GROUPS: removed})
            elif added and not removed:
                self.logger.info("Users added, sending to orchestrator.")
                self.send({Output.USERS_ADDED_FROM_GROUPS: added, Output.USERS_REMOVED_FROM_GROUPS: []})
            elif removed and not added:
                self.logger.info("Users removed, sending to orchestrator.")
                self.send({Output.USERS_REMOVED_FROM_GROUPS: removed, Output.USERS_ADDED_FROM_GROUPS: []})

            current_list = new_list

            sleep_time = params.get(Input.INTERVAL, 300)
            self.logger.info(f"Loop complete, sleeping for {sleep_time}...")
            time.sleep(sleep_time)

    def get_users_in_group_list(self, group_list, okta_url):
        current_list = []
        for group in group_list:
            current_list.append({group: self.get_users_in_group(f"{okta_url}/api/v1/groups/{group}/users")})

        return current_list

    def get_users_in_group(self, api_url):
        returned_data = []
        response = self.connection.session.get(api_url)
        next_link = None
        links = response.headers.get("Link", "").split(", ")
        for link in links:
            if 'rel="next"' in link:
                matched_link = re.match("<(.*?)>", link)
                if matched_link:
                    next_link = matched_link.group(1)

        if next_link:
            returned_data.extend(self.get_users_in_group(next_link))

        try:
            data = response.json()
        except ValueError:
            raise PluginException(
                cause="Returned data was not in JSON format.",
                assistance="Double-check that group ID's are all valid.",
                data=response.text,
            )

        helpers.raise_based_on_error_code(response)
        returned_data.extend(komand.helper.clean(data))
        return returned_data
