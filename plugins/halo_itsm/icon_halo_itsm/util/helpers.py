"""Helpers for transforming Halo ITSM API responses to plugin output format."""


def _drop_none(data: dict) -> dict:
    """Omit keys Halo did not return. The output schema declares typed fields
    (e.g. string), so a None value fails SDK output validation with
    "None is not of type 'string'"; no ticket/action fields are required, so
    omitting them is valid."""
    return {key: value for key, value in data.items() if value is not None}


def clean_ticket(raw_ticket: dict) -> dict:
    """Extract relevant ticket fields from a raw Halo ITSM API response."""
    if not raw_ticket:
        return {}

    return _drop_none(
        {
            "id": raw_ticket.get("id"),
            "summary": raw_ticket.get("summary"),
            "details": raw_ticket.get("details"),
            "status_id": raw_ticket.get("status_id"),
            "priority_id": raw_ticket.get("priority_id"),
            "tickettype_id": raw_ticket.get("tickettype_id"),
            "category_1": raw_ticket.get("category_1"),
            "category_2": raw_ticket.get("category_2"),
            "impact": raw_ticket.get("impact"),
            "urgency": raw_ticket.get("urgency"),
            "user_id": raw_ticket.get("user_id"),
            "user_name": raw_ticket.get("user_name"),
            "agent_id": raw_ticket.get("agent_id"),
            "agent_name": raw_ticket.get("agent_name"),
            "team": raw_ticket.get("team"),
            "dateoccurred": raw_ticket.get("dateoccurred"),
            "datecreated": raw_ticket.get("datecreated"),
            "lastupdate": raw_ticket.get("lastupdate"),
            "closeddate": raw_ticket.get("closeddate"),
            "client_id": raw_ticket.get("client_id"),
            "client_name": raw_ticket.get("client_name"),
            "site_id": raw_ticket.get("site_id"),
            "sla_id": raw_ticket.get("sla_id"),
        }
    )


def clean_action(raw_action: dict) -> dict:
    """Extract relevant action fields from a raw Halo ITSM API response."""
    if not raw_action:
        return {}

    return _drop_none(
        {
            "id": raw_action.get("id"),
            "ticket_id": raw_action.get("ticket_id"),
            "who": raw_action.get("who"),
            "note": raw_action.get("note"),
            "hiddenfromuser": raw_action.get("hiddenfromuser"),
            "outcome": raw_action.get("outcome"),
            "actiondate": raw_action.get("actiondate") or raw_action.get("datetime"),  # Halo returns "datetime"
        }
    )
