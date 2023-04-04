STUB_URL_API = "This is a url"
STUB_ADD_NOTE_PARAMETERS = {
    "category": "category",
    "notes": "notes",
    "source": "source",
    "summary": "summary",
    "incident_number_good": 12345,
    "incident_number_bad": 54321,
}
STUB_CREATE_INCIDENT_PARAMETERS = {
    "assignee": "identifier",
    "category": "category",
    "customer": "identifier",
    "description": "description",
    "impact": "impact",
    "source": "source",
    "status": "status",
    "summary": "summary",
    "type": "type",
    "urgency": "urgency",
}
STUB_CREATE_SERVICE_REQUEST_PARAMETERS = {
    "customer": "identifier",
    "description": "description",
    "service_request_template": "identifier",
    "service_request_template_not_unique": "identifier_not_unique",
    "service_request_template_none": "no_identifier",
    "status": "status",
    "urgency": "urgency",
}
STUB_DELETE_INCIDENT_PARAMETERS = {
    "good_id": 12345,
    "bad_id": 54321,
    "odd_id": 15243
}
STUB_GET_INCIDENT_PARAMETERS = {"good_id": 12345, "bad_id": 54321}
STUB_NEW_INCIDENT_PARAMETERS = {}