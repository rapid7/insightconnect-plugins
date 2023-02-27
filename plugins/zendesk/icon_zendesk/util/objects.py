from typing import Any, Dict

from zenpy.lib.api_objects import Organization, OrganizationMembership, Ticket, User


class Objects:
    @staticmethod
    def create_ticket_object(returned_ticket: Ticket) -> Dict[str, Any]:
        ticket_object = {
            "assignee_id": returned_ticket.assignee_id,
            "brand_id": returned_ticket.brand_id,
            "collaborator_ids": returned_ticket.collaborator_ids,
            "created_at": returned_ticket.created_at,
            "description": returned_ticket.description,
            "due_at": returned_ticket.due_at,
            "external_id": returned_ticket.external_id,
            "forum_topic_id": returned_ticket.forum_topic_id,
            "group_id": returned_ticket.group_id,
            "has_incidents": returned_ticket.has_incidents,
            "id": returned_ticket.id,
            "organization_id": returned_ticket.organization_id,
            "priority": returned_ticket.priority,
            "problem_id": returned_ticket.problem_id,
            "raw_subject": returned_ticket.raw_subject,
            "recipient": returned_ticket.recipient,
            "requester_id": returned_ticket.requester_id,
            "sharing_agreement_ids": returned_ticket.sharing_agreement_ids,
            "status": returned_ticket.status,
            "subject": returned_ticket.subject,
            "submitter_id": returned_ticket.submitter_id,
            "tags": returned_ticket.tags,
            "type": returned_ticket.type,
            "updated_at": returned_ticket.updated_at,
            "url": returned_ticket.url,
        }
        return ticket_object

    @staticmethod
    def create_user_object(user: User) -> Dict[str, Any]:
        user_object = {
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

        return user_object

    @staticmethod
    def create_organization_object(organisation: Organization) -> Dict[str, Any]:
        organization_object = {
            "created_at": organisation.created_at,
            "details": organisation.details,
            "external_id": organisation.external_id,
            "group_id": organisation.group_id,
            "id": organisation.id,
            "name": organisation.name,
            "notes": organisation.notes,
            "shared_comments": organisation.shared_comments,
            "shared_tickets": organisation.shared_tickets,
            "tags": organisation.tags,
            "updated_at": organisation.updated_at,
            "url": organisation.url,
        }
        return organization_object

    @staticmethod
    def create_membership_object(membership: OrganizationMembership) -> Dict[str, Any]:
        membership_object = {
            "id": membership.id,
            "user_id": membership.user_id,
            "organization_id": membership.organization_id,
            "default": membership.default,
            "created_at": membership.created_at,
            "updated_at": membership.updated_at,
        }
        return membership_object
