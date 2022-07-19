class Item:
    ID = "id"

    def get_all_attributes(self):
        return [self.__getattribute__(name) for name in dir(self) if not name.startswith("_")]


class Response(Item):
    REQUEST = "request"
    REQUESTS = "requests"
    NOTES = "notes"
    NOTE = "note"
    RESPONSE_STATUS = "response_status"
    RESOLUTION = "resolution"


class ResponseStatus:
    STATUS = "status"
    STATUS_CODE = "status_code"


class Note(Item):
    LAST_UPDATED_BY = "last_updated_by"
    ADDED_TIME = "added_time"
    LAST_UPDATED_TIME = "last_updated_time"
    ADDED_BY = "added_by"
    SHOW_TO_REQUESTER = "show_to_requester"


class Request(Item):
    SUBJECT = "subject"
    REQUESTER = "requester"
    DESCRIPTION = "description"
    REQUEST_TYPE = "request_type"
    IMPACT = "impact"
    STATUS = "status"
    MODE = "mode"
    LEVEL = "level"
    URGENCY = "urgency"
    PRIORITY = "priority"
    SERVICE_CATEGORY = "service_category"
    ASSETS = "assets"
    SITE = "site"
    GROUP = "group"
    TECHNICIAN = "technician"
    CATEGORY = "category"
    SUBCATEGORY = "subcategory"
    ITEM = "item"
    EMAIL_IDS_TO_NOTIFY = "email_ids_to_notify"
    IS_FCR = "is_fcr"
    UDF_FIELDS = "udf_fields"
    CREATED_TIME = "created_time"
    DUE_BY_TIME = "due_by_time"
    CREATED_BY = "created_by"
    IS_SERVICE_REQUEST = "is_service_request"
    HAS_NOTES = "has_notes"
    IS_OVERDUE = "is_overdue"


class Time:
    DISPLAY_VALUE = "display_value"


class User(Item):
    NAME = "name"
    IS_VIPUSER = "is_vipuser"


class Priority(Item):
    NAME = "name"


class Status(Item):
    NAME = "name"


class Resolution:
    CONTENT = "content"
