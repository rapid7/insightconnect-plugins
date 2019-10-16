import komand
from .schema import GetEnterpriseGroupsInput, GetEnterpriseGroupsOutput, Input, Output, Component
# Custom imports below


class GetEnterpriseGroups(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_enterprise_groups',
                description=Component.DESCRIPTION,
                input=GetEnterpriseGroupsInput(),
                output=GetEnterpriseGroupsOutput())

    def run(self, params={}):
        client = self.connection.box_connection

        name = params.get(Input.GROUP_NAME)

        groups = client.groups()

        group_list = []

        # This doesn't resolve until you ask for groups, the objects that pop out are odd as well
        # thus we need translation code here
        for group in groups:
            group_object = {
                "type": group.type,
                "id": group.object_id,
                "name": group.name,
                "group_type": group.group_type
            }
            group_list.append(group_object)

        # If the user gave us a name, only return that group.
        # Put it in an array to normalize with the output
        if name:
            for group in group_list:
                if group.get("name") == name:
                    return {Output.GROUPS: komand.helper.clean([group])}

        return {Output.GROUPS: komand.helper.clean(group_list)}
    
