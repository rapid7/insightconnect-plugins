import insightconnect_plugin_runtime
from .schema import ShowUserInput, ShowUserOutput, Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import zenpy


class ShowUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="show_user",
            description="Retrieve user information",
            input=ShowUserInput(),
            output=ShowUserOutput(),
        )

    def run(self, params={}):
        try:
            user = self.connection.client.users(id=params.get(Input.USER_ID))
        except zenpy.lib.exception.APIException as e:
            self.logger.debug(e)
            raise PluginException(
                cause=f"User ID {params.get(Input.USER_ID)} not found in Zendesk.",
                assistance="Make sure the input user ID is correct.",
            )
        user_obj = {
            "active": user.active,
            "alias": user.alias,
            "chat_only": user.chat_only,
            "created_at": user.created_at,
            "custom_role_id": user.custom_role_id,
            "details": user.details,
            "email": user.email,
            "external_id": user.external_id,
            "id": user.id,
            "last_login_at": user.last_login_at,
            "locale": user.locale,
            "locale_id": user.locale_id,
            "moderator": user.moderator,
            "name": user.name,
            "notes": user.notes,
            "only_private_comments": user.only_private_comments,
            "organization_id": user.organization_id,
            "phone": user.phone,
            "photo": user.photo,
            "restricted_agent": user.restricted_agent,
            "role": user.role,
            "shared": user.shared,
            "shared_agent": user.shared_agent,
            "signature": user.signature,
            "suspended": user.suspended,
            "tags": user.tags,
            "ticket_restriction": user.ticket_restriction,
            "time_zone": user.time_zone,
            "two_factor_auth_enabled": user.two_factor_auth_enabled,
            "updated_at": user.updated_at,
            "url": user.url,
            "verified": user.verified,
        }
        return {Output.USER: user_obj}

    def test(self):
        try:
            test = self.connection.client.users.me().email
            return {"success": test}
        except:
            raise
