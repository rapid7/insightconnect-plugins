import insightconnect_plugin_runtime
import time
from .schema import (
    UsersAddedRemovedFromGroupInput,
    UsersAddedRemovedFromGroupOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_okta.util.helpers import clean
import re


class UsersAddedRemovedFromGroup(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="users_added_removed_from_group",
            description=Component.DESCRIPTION,
            input=UsersAddedRemovedFromGroupInput(),
            output=UsersAddedRemovedFromGroupOutput(),
        )

    def run(self, params={}):  # noqa: MC0001
        """Run the trigger"""
        group_list = params.get(Input.GROUPIDS)
        current_list = self.get_users_in_group_list(group_list)

        group_names = list()
        for group in group_list:
            response = self.connection.api_client.get_group(group_id=group)
            group_names.append(response.get("profile", {}).get("name", ""))

        while True:
            new_list = self.get_users_in_group_list(group_list)

            added = list()
            removed = list()
            for index, value in enumerate(group_list):
                added_users = []
                for new_user in new_list[index][value]:
                    found = False
                    for old_user in current_list[index][value]:
                        if new_user.get("id", "") == old_user.get("id", ""):
                            found = True

                    if not found:
                        added_users.append(new_user)

                removed_users = []
                for old_user in current_list[index][value]:
                    found = False
                    for new_user in new_list[index][value]:
                        if old_user.get("id", "") == new_user.get("id", ""):
                            found = True

                    if not found:
                        removed_users.append(old_user)

                if added_users:
                    added.append({"groupName": group_names[index], "groupId": value, "users": added_users})
                if removed_users:
                    removed.append(
                        {
                            "groupName": group_names[index],
                            "groupId": value,
                            "users": removed_users,
                        }
                    )

            if added and removed:
                self.logger.info("Users added and removed, sending to orchestrator.")
                self.send({Output.USERSADDEDTOGROUPS: added, Output.USERSREMOVEDFROMGROUPS: removed})
            elif added and not removed:
                self.logger.info("Users added, sending to orchestrator.")
                self.send({Output.USERSADDEDTOGROUPS: added, Output.USERSREMOVEDFROMGROUPS: []})
            elif removed and not added:
                self.logger.info("Users removed, sending to orchestrator.")
                self.send({Output.USERSREMOVEDFROMGROUPS: removed, Output.USERSADDEDTOGROUPS: []})

            current_list = new_list

            sleep_time = params.get(Input.INTERVAL, 300)
            self.logger.info(f"Loop complete, sleeping for {sleep_time}...")
            time.sleep(sleep_time)

    def get_users_in_group_list(self, group_list: list) -> list:
        current_list = []
        for group in group_list:
            current_list.append({group: self.get_users_in_group(group)})

        return current_list

    def get_users_in_group(self, group_id: str) -> list:
        returned_data = []
        response = self.connection.api_client.get_users_in_group(group_id=group_id)
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
            for user in data:
                user["links"] = user.pop("_links")
                if user.get("credentials") and user["credentials"].get("recovery_question"):
                    user["credentials"]["recoveryQuestion"] = user["credentials"].pop("recovery_question")
        except ValueError:
            raise PluginException(
                cause="Returned data was not in JSON format.",
                assistance="Double-check that group ID's are all valid.",
                data=response.text,
            )

        returned_data.extend(clean(data))
        return returned_data
