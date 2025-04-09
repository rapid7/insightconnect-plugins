# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Return an object containing all of a user's factors for MFA"


class Input:
    USERID = "userId"


class Output:
    FACTORS = "factors"


class GetFactorsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "userId": {
      "type": "string",
      "title": "Okta User ID",
      "description": "User ID to get factors for",
      "order": 1
    }
  },
  "required": [
    "userId"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetFactorsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "factors": {
      "type": "array",
      "title": "Okta MFA Factors",
      "description": "Object containing all the factors of a user for MFA",
      "items": {
        "$ref": "#/definitions/factor"
      },
      "order": 1
    }
  },
  "definitions": {
    "factor": {
      "type": "object",
      "title": "factor",
      "properties": {
        "embedded": {
          "type": "object",
          "title": "Embedded",
          "description": "Embedded resources related to the Factor",
          "order": 1
        },
        "links": {
          "$ref": "#/definitions/factorLinks",
          "title": "Factor Links",
          "description": "Discoverable resources related to the Factor",
          "order": 2
        },
        "created": {
          "type": "string",
          "title": "Created",
          "description": "Timestamp when the factor was created",
          "order": 3
        },
        "factorType": {
          "type": "string",
          "title": "Factor Type",
          "description": "Type of the factor",
          "order": 4
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Unique key for the factor, a 20 character long system-generated ID",
          "order": 5
        },
        "lastUpdated": {
          "type": "string",
          "title": "Last Updated",
          "description": "Timestamp when the factor was last updated",
          "order": 6
        },
        "profile": {
          "type": "object",
          "title": "Profile",
          "description": "Profile credentials",
          "order": 7
        },
        "provider": {
          "type": "string",
          "title": "Factor Provider",
          "description": "Provider of the factor",
          "order": 8
        },
        "status": {
          "type": "string",
          "title": "Factor Status",
          "description": "Status of the factor",
          "order": 9
        },
        "vendorName": {
          "type": "string",
          "title": "Vendor Name",
          "description": "Factor Vendor Name (Same as provider but for On-Prem MFA it depends on Administrator Settings)",
          "order": 10
        },
        "verify": {
          "$ref": "#/definitions/factorVerificationObject",
          "title": "Verify",
          "description": "Specifies additional verification data for 'token' or 'token:hardware' factors",
          "order": 11
        }
      }
    },
    "factorLinks": {
      "type": "object",
      "title": "factorLinks",
      "properties": {
        "activate": {
          "$ref": "#/definitions/factorLink",
          "title": "Activate Link",
          "description": "Polls factor for completion of the activation of verification",
          "order": 1
        },
        "poll": {
          "$ref": "#/definitions/factorLink",
          "title": "Poll Link",
          "description": "Lifecycle action to transition the factor to ACTIVE status",
          "order": 2
        },
        "questions": {
          "$ref": "#/definitions/factorLink",
          "title": "Questions Link",
          "description": "List of questions for the question factor type",
          "order": 3
        },
        "resend": {
          "$ref": "#/definitions/factorLink",
          "title": "Resend Link",
          "description": "List of delivery options to resend activation or factor challenge",
          "order": 4
        },
        "self": {
          "$ref": "#/definitions/factorLink",
          "title": "Self Link",
          "description": "The actual factor",
          "order": 5
        },
        "send": {
          "$ref": "#/definitions/factorLink",
          "title": "Send Link",
          "description": "List of delivery options to send an activation or factor challenge",
          "order": 6
        },
        "verify": {
          "$ref": "#/definitions/factorLink",
          "title": "Verify Link",
          "description": "Verify the factor",
          "order": 7
        }
      }
    },
    "factorLink": {
      "type": "object",
      "title": "factorLink",
      "properties": {
        "href": {
          "type": "string",
          "title": "Href",
          "description": "Hyperlink to the resource",
          "order": 1
        },
        "hints": {
          "$ref": "#/definitions/hints",
          "title": "Hints",
          "description": "Hints for the hyperlink",
          "order": 2
        }
      }
    },
    "hints": {
      "type": "object",
      "title": "hints",
      "properties": {
        "allow": {
          "type": "array",
          "title": "Allowed Methods",
          "description": "Allowed Methods",
          "items": {
            "type": "string"
          },
          "order": 1
        }
      }
    },
    "factorVerificationObject": {
      "type": "object",
      "title": "factorVerificationObject",
      "properties": {
        "passCode": {
          "type": "string",
          "title": "Pass Code",
          "description": "OTP for next time window",
          "order": 1
        },
        "nextPassCode": {
          "type": "string",
          "title": "Next Pass Code",
          "description": "OTP for current time window",
          "order": 2
        }
      }
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
