INCIDENT_STATUS = {
    "First Line Incident": "firstLine",
    "Second Line Incident": "secondLine",
    "Partial Incident": "partial",
}

INCIDENT_FIELDS_WITH_ITEM_ID = ["branch", "location", "operator", "operatorGroup", "sla", "supplier"]
INCIDENT_FIELDS_WITH_ITEM_NAME = [
    "budgetHolder",
    "callType",
    "category",
    "closureCode",
    "department",
    "duration",
    "entryType",
    "impact",
    "majorCallObject",
    "object",
    "personExtraFieldA",
    "personExtraFieldB",
    "priority",
    "processingStatus",
    "subcategory",
    "urgency",
]
INCIDENT_FIELDS_WITH_EMAIL = ["callerLookup"]
INCIDENT_FIELDS_WITH_NUMBER = ["mainIncident"]
SKIP_FIELDS = ["id", "number"]


class Cause:
    INVALID_REQUEST = "The parameters of the request were malformed."
    INVALID_CREDENTIALS = "Invalid credentials."
    NOT_ENOUGH_PERMISSIONS = "No permission to access the data."
    NOT_FOUND = "Resource not found."
    CONNECTION_ERROR = "Connection error."


class Assistance:
    VERIFY_INPUT = "Please verify inputs and if the issue persists, contact support."
    VERIFY_CREDENTIALS = "Please verify connection credentials and if the issue persists, contact support."
