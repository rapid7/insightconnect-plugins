import json

key_schema = json.loads(
    """
{
  "type": "object",
  "patternProperties": {
    "^.*$": {
      "anyOf": [{ "$ref": "#/definitions/AttributeValue" }]
    }
  },
  "additionalProperties": false,
  "definitions": {
    "AttributeValue": {
      "title": "AttributeValue",
      "type": "object",
      "properties": {
        "L": {
          "title": "L",
          "type": "array",
          "items": {
            "$ref": "#/definitions/AttributeValue"
          }
        },
        "S": {
          "title": "S",
          "type": "string"
        },
        "B": {
          "title": "B",
          "type": "string"
        },
        "BOOL": {
          "title": "Bool",
          "type": "boolean"
        },
        "BS": {
          "title": "Bs",
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "N": {
          "title": "N",
          "type": "string"
        },
        "NS": {
          "title": "Ns",
          "type": "array",
          "items": { "anyOf": [{ "type": "number" }, { "type": "integer" }] }
        },
        "NULL": { "title": "Null", "type": "boolean" },
        "SS": { "title": "Ss", "type": "array", "items": { "type": "string" } },
        "M": {
          "title": "M",
          "type": "object",
          "additionalProperties": { "$ref": "#/definitions/AttributeValue" }
        }
      },
      "additionalProperties": false
    }
  }
}
"""
)
