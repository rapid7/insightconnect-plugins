import komand
from .schema import RetrieveSecurityPoliciesInput, RetrieveSecurityPoliciesOutput


class RetrieveSecurityPolicies(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='retrieve_security_policies',
                description='Lists all security policies',
                input=RetrieveSecurityPoliciesInput(),
                output=RetrieveSecurityPoliciesOutput())

    def run(self, params={}):
        action = "security_policies"
        if params.get("id"):
            action = action + "/" + params.get("id")

        r = self.connection.connector.get(action)

        self.connection.connector.raise_error_when_not_in_status(200)
        if 'data' not in r and params.get("id"):
            data = [r]
        elif 'data' not in r:
            self.connection.connector.raise_error("Empty argument attack_group_ID")
        else:
            data = r['data']

        for k, val in enumerate(data):
            if "request_limits" not in data[k]:
                data[k]["request_limits"] = ""
            if "double_decoding" not in data[k]:
                data[k]["double_decoding"] = ""
            if 'id' not in data[k]:
                data[k]["id"] = data[k]["name"]
            if "default_character_set" not in data[k]:
                data[k]["default_character_set"] = ""
            if "limit_checks" not in data[k] or data[k]["limit_checks"] == "no":
                data[k]["limit_checks"] = False
            else:
                data[k]["limit_checks"] = True

            del data[k]["json key profile"]

        return {"policies": data}

    def test(self):
        return {"policies": [{
            "allowed_acls": 0,
            "apply_double_decoding": "",
            "default_character_set": "",
            "character": "",
            "cloaking": {},
            "cookie_protection": "",
            "cookie_security": {
                "allowUnrecognizedCookies": "",
                "cookieMaxAge": 0,
                "cookieReplayProtectionType": "",
                "cookies_exempted": [],
                "customHeaders": [],
                "daysAllowed": 0,
                "http_only": "no",
                "secureCookie": 0,
                "tamperProofMode": ""
            },
            "data_theft_protection": [],
            "disallowed_acls": 0,
            "id": "",
            "limit_checks": False,
            "double_decoding": "no",
            "name": "",
            "parameter_protection": {
                "allowedFileUploadType": "",
                "base64DecodeParameterValue": "",
                "blockedAttackTypes": [],
                "customBlockedAttackTypes": [],
                "deniedMetaCharacters": "",
                "enable": "no",
                "exceptionPatterns": [],
                "fileUploadMimeTypes": [],
                "fileUpload_extensions": [],
                "ignoreParameters": [],
                "maximumInstances": 0,
                "maximumParameterValueLength": 0,
                "maximumUploadFileSize": 0
            },
            "parameter_protection_status": "",
            "request_limits": {
                "enable": "no",
                "maxCookieNameLength": 0,
                "maxCookieValueLength": 0,
                "maxHeaderNameLength": 0,
                "maxHeaderValueLength": 0,
                "maxNumberOfCookies": 0,
                "maxNumberOfHeaders": 0,
                "maxQueryLength": 0,
                "maxRequestLength": 0,
                "maxRequestLineLength": 0,
                "maxURLLength": 0
            },
            "url_normalization": {
                "defaultCharset": "",
                "detectResponseCharset": "",
                "double_decoding": "no",
                "parameter_separators": ""
            },
            "url_protection": {
                "allowedContentTypes": [],
                "allowedMethods": [],
                "blockedAttackTypes": [],
                "csrfPrevention": "",
                "custom_blockedAttackTypes": [],
                "enable": "no",
                "exceptionPatterns": [],
                "maxContentLength": 0,
                "maxParameters": 0,
                "maximumParameterNameLength": 0,
                "maximumUploadFiles": 0
            },
            "url_protection_status": "no"
        }]}
