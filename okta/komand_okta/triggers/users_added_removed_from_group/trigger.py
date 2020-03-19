import komand
import time
from .schema import UsersAddedRemovedFromGroupInput, UsersAddedRemovedFromGroupOutput, Input, Output, Component
# Custom imports below
import itertools
from komand.exceptions import PluginException


class UsersAddedRemovedFromGroup(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='users_added_removed_from_group',
                description=Component.DESCRIPTION,
                input=UsersAddedRemovedFromGroupInput(),
                output=UsersAddedRemovedFromGroupOutput())

    def run(self, params={}):
        """Run the trigger"""
        group_list = params.get(Input.GROUP_IDS)
        okta_url = self.connection.okta_url
        current_list = list()
        group_names = list()
        for group in group_list:
            api = f"{okta_url}/api/v1/groups/{group}/users"
            # Build a reference list to check for updates against
            response = self.connection.session.get(api)
            if response.status_code() in range(400, 499):
                raise PluginException(cause="Okta returned a 4xx status code",
                                      assistance="Ensure that the secretKey key is both valid and correct")
            if response.status_code() in range(500, 599)
                raise PluginException(cause="Okta returned a 5xx status code",
                                      assistance="Ensure that the okta URL key is  correct")
            try:
                data = response.json()
                data = komand.helper.clean(data)
            except ValueError:
                raise PluginException(cause='Returned data was not in JSON format',
                                      assistance="Double check that group ID's are all valid",
                                      data=response.text)
            current_list.append({group: data})

            # Get group names
            group_name_api = f"{okta_url}/api/v1/groups/{group}"
            response = self.connection.session.get(group_name_api)
            if response.status_code() in range(400, 499):
                raise PluginException(cause="Okta returned a 4xx status code",
                                      assistance="Ensure that the secretKey key is both valid and correct")
            if response.status_code() in range(500, 599)
                raise PluginException(cause="Okta returned a 5xx status code",
                                      assistance="Ensure that the okta URL key is  correct")
            try:
                data = response.json()
            except ValueError:
                raise PluginException(cause='Returned data was not in JSON format',
                                      assistance="Double check that group ID's are all valid",
                                      data=response.text)
            group_names.append(data["profile"]["name"])

        while True:
            new_list = list()
            for group in group_list:
                api = f"{okta_url}/api/v1/groups/{group}/users"

                response = self.connection.session.get(api)
                if response.status_code() in range(400, 499):
                    raise PluginException(cause="Okta returned a 4xx status code",
                                          assistance="Ensure that the secretKey key is both valid and correct")
                if response.status_code() in range(500, 599)
                    raise PluginException(cause="Okta returned a 5xx status code",
                                          assistance="Ensure that the okta URL key is  correct")
                try:
                    data = response.json()
                except ValueError:
                    raise PluginException(cause='Returned data was not in JSON format',
                                          assistance="Double check that group ID's are all valid",
                                          data=response.text)
                data = komand.helper.clean(data)
                new_list.append({group: data})

            added = list()
            removed = list()
            for index, value in enumerate(group_list):
                added_users = list(
                    itertools.filterfalse(lambda user: user in current_list[index][value], new_list[index][value]))
                removed_users = list(
                    itertools.filterfalse(lambda user: user in new_list[index][value], current_list[index][value]))
                if added_users:
                    added.append({"group_name": group_names[index], "group_id": value, "users": added_users})
                if removed_users:
                    removed.append({"group_name": group_names[index], "group_id": value, "users": removed_users})

            if added and removed:
                self.send({Output.USERS_ADDED_FROM_GROUPS: added, Output.USERS_REMOVED_FROM_GROUPS: removed})
            elif added and not removed:
                self.send({Output.USERS_ADDED_FROM_GROUPS: added})
            elif removed and not added:
                self.send({Output.USERS_REMOVED_FROM_GROUPS: removed})

                current_list = new_list
            time.sleep(params.get(Input.INTERVAL, 300))
