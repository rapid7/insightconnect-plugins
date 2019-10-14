import komand
from .schema import GetGroupByNameInput, GetGroupByNameOutput, Input, Output, Component
# Custom imports below
from icon_azure_ad_admin.util.get_group import get_group


class GetGroupByName(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_group_by_name',
                description=Component.DESCRIPTION,
                input=GetGroupByNameInput(),
                output=GetGroupByNameOutput())

    def run(self, params={}):
        group_name = params.get(Input.NAME)

        self.logger.info(f"Getting group named: {group_name}")

        group_output = get_group(self.connection, group_name)

        # Komand clean doesn't take care of null
        for key in group_output.keys():
            if group_output.get(key) == 'null':
                group_output.pop(key)

        return {Output.GROUP: komand.helper.clean(group_output)}
