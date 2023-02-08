class Cause:
    INVALID_REQUEST = "Invalid details provided."
    INVALID_AUTH_DATA = "Invalid client ID or secret provided."
    NOT_FOUND = "Resource not found."
    TOO_MANY_REQUESTS = "API limit error."
    SERVER_ERROR = "Server error occurred."


class Assistance:
    VERIFY_INPUT = (
        "Verify your input is correct and not malformed and try again. If the issue persists, please contact support."
    )
    VERIFY_AUTH = "Verify your client ID and secret are correct. If the issue persists, please contact support."
    SERVER_ERROR = "Verify your plugin connection inputs are correct and not malformed and try again. If the issue persists, please contact support."


class ValueType:
    INTEGER = "integer"
    STRING = "string"


class Member:
    TYPE = "type"
    ACCESS_ALL = "accessAll"
    EXTERNAL_ID = "externalId"
    COLLECTIONS = "collections"
    EMAIL = "email"
