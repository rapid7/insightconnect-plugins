MAX_ALIASES_NUMBER: int = 4


class Cause:
    INVALID_AUTH_DATA = "Invalid signature."
    INVALID_INPUT = "Incorrect input."
    INVALID_REQUEST = "Invalid details provided."
    NOT_FOUND = "Resource not found."
    SERVER_ERROR = "Server error occurred."
    USER_NOT_FOUND = "User not found."


class Assistance:
    ALIASES_NUMBER_EXCEEDED = f"Alias parameter must contain {MAX_ALIASES_NUMBER} or less aliases."
    INVALID_INPUT = "Please check that your input is correct and try again.\nIncorrect input: '{given_input}'.\nPossible inputs: {possible_inputs}."
    SERVER_ERROR = "Verify your plugin connection inputs are correct and not malformed and try again. If the issue persists, please contact support."
    USER_NOT_FOUND = "Please check if the given username is correct and try again."
    VERIFY_AUTH = "Verify your integration key and secret are correct. If the issue persists, please contact support."
    VERIFY_INPUT = (
        "Verify your input is correct and not malformed and try again. If the issue persists, please contact support."
    )
    RATE_LIMIT = "Task will resume collection of logs after the rate limiting period has expired."


class PossibleInputs:
    possible_factors = [
        "duo_push",
        "phone_call",
        "u2f_token",
        "hardware_token",
        "bypass_code",
        "sms_passcode",
        "duo_mobile_passcode",
        "yubikey_code",
        "passcode",
        "digipass_go_7_token",
        "not_available",
        "sms_refresh",
        "remembered_device",
        "trusted_network",
    ]
    possible_reasons = [
        "user_marked_fraud",
        "deny_unenrolled_user",
        "error",
        "locked_out",
        "user_disabled",
        "user_cancelled",
        "invalid_passcode",
        "no_response",
        "no_keys_pressed",
        "call_timed_out",
        "location_restricted",
        "factor_restricted",
        "platform_restricted",
        "version_restricted",
        "rooted_device",
        "no_screen_lock",
        "touch_id_disabled",
        "no_disk_encryption",
        "anonymous_ip",
        "out_of_date",
        "denied_by_policy",
        "software_restricted",
        "no_duo_certificate_present",
        "user_provided_invalid_certificate",
        "could_not_determine_if_endpoint_was_trusted",
        "invalid_management_certificate_collection_state",
        "no_referring_hostname_provided",
        "invalid_referring_hostname_provided",
        "no_web_referer_match",
        "endpoint_failed_google_verification",
        "endpoint_is_not_trusted",
        "invalid_device",
        "anomalous_push",
        "endpoint_is_not_in_management_system",
        "no_activated_duo_mobile_account",
        "allow_unenrolled_user",
        "bypass_user",
        "trusted_network",
        "remembered_device",
        "trusted_location",
        "user_approved",
        "valid_passcode",
        "allowed_by_policy",
        "allow_unenrolled_user_on_trusted_network",
        "user_not_in_permitted_group",
    ]
    possible_results = ["success", "denied", "fraud"]
    possible_event_types = ["authentication", "enrollment"]
