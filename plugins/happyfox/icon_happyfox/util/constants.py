sort_by = {
    "assignee username ascending": "assigneea",
    "assignee username descending": "assigneed",
    "category ascending": "categorya",
    "category descending": "categoryd",
    "contact ID ascending": "clienta",
    "contact ID descending": "clientd",
    "due date": "due",
    "last updated ascending": "updatea",
    "last updated descending": "updated",
    "priority order ascending": "prioritya",
    "priority order descending": "priorityd",
    "status order ascending": "statusa",
    "status order descending": "statusd",
    "subject in alphabetical order ascending": "subjecta",
    "subject in alphabetical order descending": "subjectd",
    "ticket creation date ascending": "createa",
    "ticket creation date descending": "created",
    "ticket ID ascending": "ticketa",
    "ticket ID descending": "ticketd",
    "ticket last modified date ascending": "last_modifieda",
    "ticket last modified date descending": "last_modifiedd",
    "unresponded tickets first": "unresponded",
}


class Cause:
    CUSTOM_FIELD_NOT_FOUND = "The custom field '{key}' does not exist or is not available for the specified category."
    NO_TEXT_AND_HTML = "Text and HTML field not provided. One of these fields is required to create a ticket."
    NOT_FOUND = "Resource not found."
    SERVER_ERROR = "Server error occurred."


class Assistance:
    CUSTOM_FIELD_NOT_FOUND = "Custom fields that are available: {available_custom_fields}"
    NO_TEXT_AND_HTML = "Please provide a Text or HTML field and try again."
    NOT_FOUND = (
        "Verify your input is correct and not malformed and try again. If the issue persists, please contact support."
    )
    SERVER_ERROR = "Verify your plugin connection inputs are correct and not malformed and try again. If the issue persists, please contact support."


class TextCase:
    SNAKE_CASE = "snake_case"
    CAMEL_CASE = "camel_case"
