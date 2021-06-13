import komand
from .schema import SearchInput, SearchOutput, Output

# Custom imports below
from typing import Optional


class Search(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search", description="Search Zendesk", input=SearchInput(), output=SearchOutput()
        )

    def run(self, params={}):
        s_type = params.get("type")
        results = self.connection.client.search(params.get("item"), type=params.get("type").lower())
        objs = []
        if len(results) == 0:
            return {"error": "Could not find item"}

        for item in results:
            if s_type == "Organization" and results is not None:
                organization_obj = {
                    "created_at": item.created_at,
                    "details": item.details,
                    "external_id": self.convert_to_string(item.external_id),
                    "group_id": self.convert_to_string(item.group_id),
                    "id": self.convert_to_string(item.id),
                    "name": item.name,
                    "notes": item.notes,
                    "shared_comments": item.shared_comments,
                    "shared_tickets": item.shared_tickets,
                    "tags": item.tags,
                    "updated_at": item.updated_at,
                    "url": item.url,
                }
                objs.append(organization_obj)

            if s_type == "Ticket" and results is not None:
                ticket_obj = {
                    "assignee_id": self.convert_to_string(item.assignee_id),
                    "brand_id": self.convert_to_string(item.brand_id),
                    "collaborator_ids": self.convert_array(item.collaborator_ids),
                    "created_at": item.created_at,
                    "description": item.description,
                    "due_at": item.due_at,
                    "external_id": self.convert_to_string(item.external_id),
                    "forum_topic_id": self.convert_to_string(item.forum_topic_id),
                    "group_id": self.convert_to_string(item.group_id),
                    "has_incidents": item.has_incidents,
                    "id": item.id,
                    "organization_id": self.convert_to_string(item.organization_id),
                    "priority": item.priority,
                    "problem_id": self.convert_to_string(item.problem_id),
                    "raw_subject": item.raw_subject,
                    "recipient": self.convert_to_string(item.recipient),
                    "requester_id": self.convert_to_string(item.requester_id),
                    "sharing_agreement_ids": self.convert_array(item.sharing_agreement_ids),
                    "status": item.status,
                    "subject": item.subject,
                    "submitter_id": self.convert_to_string(item.submitter_id),
                    "tags": item.tags,
                    "type": item.type,
                    "updated_at": item.updated_at,
                    "url": item.url,
                }
                objs.append(ticket_obj)

            if s_type == "User" and results is not None:
                user_obj = {
                    "active": item.active,
                    "alias": item.alias,
                    "chat_only": item.chat_only,
                    "created_at": item.created_at,
                    "custom_role_id": self.convert_to_string(item.custom_role_id),
                    "details": item.details,
                    "email": item.email,
                    "external_id": self.convert_to_string(item.external_id),
                    "id": self.convert_to_string(item.id),
                    "last_login_at": item.last_login_at,
                    "locale": item.locale,
                    "locale_id": item.locale_id,
                    "moderator": item.moderator,
                    "name": item.name,
                    "notes": item.notes,
                    "only_private_comments": item.only_private_comments,
                    "organization_id": self.convert_to_string(item.organization_id),
                    "phone": item.phone,
                    "photo": item.photo,
                    "restricted_agent": item.restricted_agent,
                    "role": item.role,
                    "shared": item.shared,
                    "shared_agent": item.shared_agent,
                    "signature": item.signature,
                    "suspended": item.suspended,
                    "tags": item.tags,
                    "ticket_restriction": item.ticket_restriction,
                    "time_zone": item.time_zone,
                    "two_factor_auth_enabled": item.two_factor_auth_enabled,
                    "updated_at": item.updated_at,
                    "url": item.url,
                    "verified": item.verified,
                }
                objs.append(user_obj)
            if s_type == "Organization":
                return {Output.ORGANIZATIONS: komand.helper.clean(objs)}
            elif s_type == "Ticket":
                return {Output.TICKETS: komand.helper.clean(objs)}
            else:
                return {Output.USERS: komand.helper.clean(objs)}

    @staticmethod
    def convert_to_string(values: Optional[int]) -> Optional[str]:
        if not values:
            return None
        return str(values)

    @staticmethod
    def convert_array(values: Optional[list]) -> Optional[list]:
        converted_array = []
        for item in values:
            converted_array.append(str(item))
        return converted_array
