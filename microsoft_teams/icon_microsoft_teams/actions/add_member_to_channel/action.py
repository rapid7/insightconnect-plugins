import komand
from .schema import AddMemberToChannelInput, AddMemberToChannelOutput, Input, Output, Component
# Custom imports below
from icon_microsoft_teams.util.teams_utils import get_channels_from_microsoft
from icon_microsoft_teams.util.azure_ad_utils import get_user_info, get_group_id_from_name, add_user_to_channel


class AddMemberToChannel(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='add_member_to_channel',
            description=Component.DESCRIPTION,
            input=AddMemberToChannelInput(),
            output=AddMemberToChannelOutput()
        )

    def run(self, params={}):
        group_id = get_group_id_from_name(self.logger, self.connection, params.get(Input.GROUP_NAME))
        channels = get_channels_from_microsoft(self.logger, self.connection, group_id, params.get(Input.CHANNEL_NAME))

        return {
            Output.SUCCESS: add_user_to_channel(
                self.logger,
                self.connection,
                group_id,
                channels[0].get("id"),
                get_user_info(self.logger, self.connection, params.get(Input.MEMBER_LOGIN)).get("id")
            )
        }
