API = "https://api.services.mimecast.com"
DATA_FIELD = "data"
META_FIELD = "meta"
PAGINATION_FIELD = "pagination"
TRACKED_EMAILS_FIELD = "trackedEmails"
TRACKED_EMAILS_ADVANCED_OPTIONS = "advancedTrackAndTraceOptions"
IS_LAST_TOKEN_FIELD = "isLastToken"  # nosec
ID_FIELD = "id"
DOMAIN_FIELD = "domain"
EMAIL_FIELD = "emailAddress"
URL_FIELD = "url"
FAIL_FIELD = "fail"
STATUS_FIELD = "status"
GROUP_MEMBER_ALREADY_EXISTS_ERROR = "err_folder_group_member_already_exists"
XDK_BINDING_EXPIRED_ERROR = "err_xdk_binding_expired"
INVALID_SIEM_TOKEN = "err_audit_siem_invalid_token"  # nosec
MANAGED_URL_EXISTS_ERROR = "err_managed_url_exists_code"
CODE = "code"
FOLDER_EMAIL_NOT_FOUND_ERROR = "err_folder_email_address_not_found"
MANAGED_URL_NOT_FOUND_ERROR = "err_managed_url_not_found"
DEVELOPER_KEY_ERROR = "err_developer_key"
FIELD_VALIDATION_ERROR = "err_validation_null"
VALIDATION_BLANK_ERROR = "err_validation_blank"
INVALID_REGION = "err_audit_log_incorrect_region"
VALIDATION_INVALID_EMAIL_ADDRESS_ERROR = "err_validation_invalid_email_address"
BASIC_ASSISTANCE_MESSAGE = "Please check input and try again."
BASIC_ASSISTANCE_MESSAGE_CONNECTION = "Please check input connection and try again."
TRACKED_EMAILS_ADVANCED_CAUSE = "One of fields `Send From`, `Send To`, `Subject`, `Sender IP` must not be empty."
TRACKED_EMAILS_REQUIRED_CAUSE = (
    "Either one of `Send From`, `Send To`, `Subject`, `Sender IP` fields, or `Message ID` must not be empty."
)
TRACKED_EMAILS_ASSISTANCE = "Please fill the necessary fields with data, and try again."
ERROR_CASES = {
    XDK_BINDING_EXPIRED_ERROR: "AccessKey has expired.",
    MANAGED_URL_EXISTS_ERROR: "The managed URL already exists; to update it, delete and recreate.",
    GROUP_MEMBER_ALREADY_EXISTS_ERROR: "Group member already exists.",
    FOLDER_EMAIL_NOT_FOUND_ERROR: "Error email address not found.",
    MANAGED_URL_NOT_FOUND_ERROR: "Managed URL not found.",
    DEVELOPER_KEY_ERROR: "Connection headers has not been configured.",
    VALIDATION_INVALID_EMAIL_ADDRESS_ERROR: "Email address is not valid.",
    INVALID_SIEM_TOKEN: "The SIEM token is invalid",
}
RATE_LIMIT_ASSISTANCE = "Task will resume collection of logs after the rate limiting period has expired."
