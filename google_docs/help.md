# Google Docs

## About

[Google Docs](https://developers.google.com/docs/api/reference/rest/v1/documents) allows you to manage and edit Google documents.

## Actions

### Create Blank Document

This action is used to create a blank Google document.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|title|string|None|True|Document Title|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|document|document|True|Created Document|

Example output:

```
{
  "document": {
    "title": "Test Blank Komand Doc",
    "body": {
      "content": [
        {
          "endIndex": 1,
          "sectionBreak": {
            "sectionStyle": {
              "columnSeparatorStyle": "NONE",
              "contentDirection": "LEFT_TO_RIGHT"
            }
          }
        },
        {
          "startIndex": 1,
          "endIndex": 2,
          "paragraph": {
            "elements": [
              {
                "startIndex": 1,
                "endIndex": 2,
                "textRun": {
                  "content": "\n",
                  "textStyle": {}
                }
              }
            ],
            "paragraphStyle": {
              "namedStyleType": "NORMAL_TEXT",
              "direction": "LEFT_TO_RIGHT"
            }
          }
        }
      ]
    },
    "documentStyle": {
      "background": {
        "color": {}
      },
      "pageNumberStart": 1,
      "marginTop": {
        "magnitude": 72,
        "unit": "PT"
      },
      "marginBottom": {
        "magnitude": 72,
        "unit": "PT"
      },
      "marginRight": {
        "magnitude": 72,
        "unit": "PT"
      },
      "marginLeft": {
        "magnitude": 72,
        "unit": "PT"
      },
      "pageSize": {
        "height": {
          "magnitude": 792,
          "unit": "PT"
        },
        "width": {
          "magnitude": 612,
          "unit": "PT"
        }
      }
    },
    "namedStyles": {
      "styles": [
        {
          "namedStyleType": "NORMAL_TEXT",
          "textStyle": {
            "bold": false,
            "italic": false,
            "underline": false,
            "strikethrough": false,
            "smallCaps": false,
            "backgroundColor": {},
            "foregroundColor": {
              "color": {
                "rgbColor": {}
              }
            },
            "fontSize": {
              "magnitude": 11,
              "unit": "PT"
            },
            "weightedFontFamily": {
              "fontFamily": "Arial",
              "weight": 400
            },
            "baselineOffset": "NONE"
          },
          "paragraphStyle": {
            "namedStyleType": "NORMAL_TEXT",
            "alignment": "START",
            "lineSpacing": 115,
            "direction": "LEFT_TO_RIGHT",
            "spacingMode": "COLLAPSE_LISTS",
            "spaceAbove": {
              "unit": "PT"
            },
            "spaceBelow": {
              "unit": "PT"
            },
            "borderBetween": {
              "color": {},
              "width": {
                "unit": "PT"
              },
              "padding": {
                "unit": "PT"
              },
              "dashStyle": "SOLID"
            },
            "borderTop": {
              "color": {},
              "width": {
                "unit": "PT"
              },
              "padding": {
                "unit": "PT"
              },
              "dashStyle": "SOLID"
            },
            "borderBottom": {
              "color": {},
              "width": {
                "unit": "PT"
              },
              "padding": {
                "unit": "PT"
              },
              "dashStyle": "SOLID"
            },
            "borderLeft": {
              "color": {},
              "width": {
                "unit": "PT"
              },
              "padding": {
                "unit": "PT"
              },
              "dashStyle": "SOLID"
            },
            "borderRight": {
              "color": {},
              "width": {
                "unit": "PT"
              },
              "padding": {
                "unit": "PT"
              },
              "dashStyle": "SOLID"
            },
            "indentFirstLine": {
              "unit": "PT"
            },
            "indentStart": {
              "unit": "PT"
            },
            "indentEnd": {
              "unit": "PT"
            },
            "keepLinesTogether": false,
            "keepWithNext": false,
            "avoidWidowAndOrphan": true,
            "shading": {
              "backgroundColor": {}
            }
          }
        },
        {
          "namedStyleType": "HEADING_1",
          "textStyle": {
            "fontSize": {
              "magnitude": 20,
              "unit": "PT"
            }
          },
          "paragraphStyle": {
            "namedStyleType": "NORMAL_TEXT",
            "direction": "LEFT_TO_RIGHT",
            "spaceAbove": {
              "magnitude": 20,
              "unit": "PT"
            },
            "spaceBelow": {
              "magnitude": 6,
              "unit": "PT"
            },
            "keepLinesTogether": true,
            "keepWithNext": true
          }
        },
        {
          "namedStyleType": "HEADING_2",
          "textStyle": {
            "bold": false,
            "fontSize": {
              "magnitude": 16,
              "unit": "PT"
            }
          },
          "paragraphStyle": {
            "namedStyleType": "NORMAL_TEXT",
            "direction": "LEFT_TO_RIGHT",
            "spaceAbove": {
              "magnitude": 18,
              "unit": "PT"
            },
            "spaceBelow": {
              "magnitude": 6,
              "unit": "PT"
            },
            "keepLinesTogether": true,
            "keepWithNext": true
          }
        },
        {
          "namedStyleType": "HEADING_3",
          "textStyle": {
            "bold": false,
            "foregroundColor": {
              "color": {
                "rgbColor": {
                  "red": 0.2627451,
                  "green": 0.2627451,
                  "blue": 0.2627451
                }
              }
            },
            "fontSize": {
              "magnitude": 14,
              "unit": "PT"
            }
          },
          "paragraphStyle": {
            "namedStyleType": "NORMAL_TEXT",
            "direction": "LEFT_TO_RIGHT",
            "spaceAbove": {
              "magnitude": 16,
              "unit": "PT"
            },
            "spaceBelow": {
              "magnitude": 4,
              "unit": "PT"
            },
            "keepLinesTogether": true,
            "keepWithNext": true
          }
        },
        {
          "namedStyleType": "HEADING_4",
          "textStyle": {
            "foregroundColor": {
              "color": {
                "rgbColor": {
                  "red": 0.4,
                  "green": 0.4,
                  "blue": 0.4
                }
              }
            },
            "fontSize": {
              "magnitude": 12,
              "unit": "PT"
            }
          },
          "paragraphStyle": {
            "namedStyleType": "NORMAL_TEXT",
            "direction": "LEFT_TO_RIGHT",
            "spaceAbove": {
              "magnitude": 14,
              "unit": "PT"
            },
            "spaceBelow": {
              "magnitude": 4,
              "unit": "PT"
            },
            "keepLinesTogether": true,
            "keepWithNext": true
          }
        },
        {
          "namedStyleType": "HEADING_5",
          "textStyle": {
            "foregroundColor": {
              "color": {
                "rgbColor": {
                  "red": 0.4,
                  "green": 0.4,
                  "blue": 0.4
                }
              }
            },
            "fontSize": {
              "magnitude": 11,
              "unit": "PT"
            }
          },
          "paragraphStyle": {
            "namedStyleType": "NORMAL_TEXT",
            "direction": "LEFT_TO_RIGHT",
            "spaceAbove": {
              "magnitude": 12,
              "unit": "PT"
            },
            "spaceBelow": {
              "magnitude": 4,
              "unit": "PT"
            },
            "keepLinesTogether": true,
            "keepWithNext": true
          }
        },
        {
          "namedStyleType": "HEADING_6",
          "textStyle": {
            "italic": true,
            "foregroundColor": {
              "color": {
                "rgbColor": {
                  "red": 0.4,
                  "green": 0.4,
                  "blue": 0.4
                }
              }
            },
            "fontSize": {
              "magnitude": 11,
              "unit": "PT"
            }
          },
          "paragraphStyle": {
            "namedStyleType": "NORMAL_TEXT",
            "direction": "LEFT_TO_RIGHT",
            "spaceAbove": {
              "magnitude": 12,
              "unit": "PT"
            },
            "spaceBelow": {
              "magnitude": 4,
              "unit": "PT"
            },
            "keepLinesTogether": true,
            "keepWithNext": true
          }
        },
        {
          "namedStyleType": "TITLE",
          "textStyle": {
            "fontSize": {
              "magnitude": 26,
              "unit": "PT"
            }
          },
          "paragraphStyle": {
            "namedStyleType": "NORMAL_TEXT",
            "direction": "LEFT_TO_RIGHT",
            "spaceAbove": {
              "unit": "PT"
            },
            "spaceBelow": {
              "magnitude": 3,
              "unit": "PT"
            },
            "keepLinesTogether": true,
            "keepWithNext": true
          }
        },
        {
          "namedStyleType": "SUBTITLE",
          "textStyle": {
            "italic": false,
            "foregroundColor": {
              "color": {
                "rgbColor": {
                  "red": 0.4,
                  "green": 0.4,
                  "blue": 0.4
                }
              }
            },
            "fontSize": {
              "magnitude": 15,
              "unit": "PT"
            },
            "weightedFontFamily": {
              "fontFamily": "Arial",
              "weight": 400
            }
          },
          "paragraphStyle": {
            "namedStyleType": "NORMAL_TEXT",
            "direction": "LEFT_TO_RIGHT",
            "spaceAbove": {
              "unit": "PT"
            },
            "spaceBelow": {
              "magnitude": 16,
              "unit": "PT"
            },
            "keepLinesTogether": true,
            "keepWithNext": true
          }
        }
      ]
    },
    "revisionId": "AOV_f4_6TbAXNLqEHuln5ayjQnUXQhPiInTuPKc66XgI86IWROm6LJUFjwwAeagTgeASRbRR1Cl0SiKtmAi14w",
    "suggestionsViewMode": "SUGGESTIONS_INLINE",
    "documentId": "1q6n-6JUd1TfzBXGJ_RbBqQOljLbl7j6ioeU5y64IXu0"
  }
}
```

### Create Document

This action is used to create a Google document.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|content|string|None|False|Document Content|None|
|title|string|None|True|Document Title|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|string|True|Document Creation Result|

Example output:

```
{
  "result": {
    "replies": [
      {}
    ],
    "writeControl": {
      "requiredRevisionId": "AOV_f49mLnIJFgmk7psTgc5_PVg2kWLko70CMGdjFnBIbYCh-GbEZKXhRH2nMrmLgLu-ZTVF8VnzwHIpxg8v5g"
    },
    "documentId": "1LuCjmLbV_-LVihVa2OPOuvcGnIS4nmG0J84Wfw58Gy4"
  }
}
```

### Get Document

This action is used to get a Google document.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|document_id|string|None|True|Document ID|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|document|document|True|Document Object|

Example output:

```
{
  "document": {
    "title": "Test Komand Doc",
    "body": {
      "content": [
        {
          "endIndex": 1,
          "sectionBreak": {
            "sectionStyle": {
              "columnSeparatorStyle": "NONE",
              "contentDirection": "LEFT_TO_RIGHT"
            }
          }
        },
        {
          "startIndex": 1,
          "endIndex": 46,
          "paragraph": {
            "elements": [
              {
                "startIndex": 1,
                "endIndex": 46,
                "textRun": {
                  "content": "This is some text that should be in the body\n",
                  "textStyle": {}
                }
              }
            ],
            "paragraphStyle": {
              "namedStyleType": "NORMAL_TEXT",
              "direction": "LEFT_TO_RIGHT"
            }
          }
        }
      ]
    },
    "documentStyle": {
      "background": {
        "color": {}
      },
      "pageNumberStart": 1,
      "marginTop": {
        "magnitude": 72,
        "unit": "PT"
      },
      "marginBottom": {
        "magnitude": 72,
        "unit": "PT"
      },
      "marginRight": {
        "magnitude": 72,
        "unit": "PT"
      },
      "marginLeft": {
        "magnitude": 72,
        "unit": "PT"
      },
      "pageSize": {
        "height": {
          "magnitude": 792,
          "unit": "PT"
        },
        "width": {
          "magnitude": 612,
          "unit": "PT"
        }
      }
    },
    "namedStyles": {
      "styles": [
        {
          "namedStyleType": "NORMAL_TEXT",
          "textStyle": {
            "bold": false,
            "italic": false,
            "underline": false,
            "strikethrough": false,
            "smallCaps": false,
            "backgroundColor": {},
            "foregroundColor": {
              "color": {
                "rgbColor": {}
              }
            },
            "fontSize": {
              "magnitude": 11,
              "unit": "PT"
            },
            "weightedFontFamily": {
              "fontFamily": "Arial",
              "weight": 400
            },
            "baselineOffset": "NONE"
          },
          "paragraphStyle": {
            "namedStyleType": "NORMAL_TEXT",
            "alignment": "START",
            "lineSpacing": 115,
            "direction": "LEFT_TO_RIGHT",
            "spacingMode": "COLLAPSE_LISTS",
            "spaceAbove": {
              "unit": "PT"
            },
            "spaceBelow": {
              "unit": "PT"
            },
            "borderBetween": {
              "color": {},
              "width": {
                "unit": "PT"
              },
              "padding": {
                "unit": "PT"
              },
              "dashStyle": "SOLID"
            },
            "borderTop": {
              "color": {},
              "width": {
                "unit": "PT"
              },
              "padding": {
                "unit": "PT"
              },
              "dashStyle": "SOLID"
            },
            "borderBottom": {
              "color": {},
              "width": {
                "unit": "PT"
              },
              "padding": {
                "unit": "PT"
              },
              "dashStyle": "SOLID"
            },
            "borderLeft": {
              "color": {},
              "width": {
                "unit": "PT"
              },
              "padding": {
                "unit": "PT"
              },
              "dashStyle": "SOLID"
            },
            "borderRight": {
              "color": {},
              "width": {
                "unit": "PT"
              },
              "padding": {
                "unit": "PT"
              },
              "dashStyle": "SOLID"
            },
            "indentFirstLine": {
              "unit": "PT"
            },
            "indentStart": {
              "unit": "PT"
            },
            "indentEnd": {
              "unit": "PT"
            },
            "keepLinesTogether": false,
            "keepWithNext": false,
            "avoidWidowAndOrphan": true,
            "shading": {
              "backgroundColor": {}
            }
          }
        },
        {
          "namedStyleType": "HEADING_1",
          "textStyle": {
            "fontSize": {
              "magnitude": 20,
              "unit": "PT"
            }
          },
          "paragraphStyle": {
            "namedStyleType": "NORMAL_TEXT",
            "direction": "LEFT_TO_RIGHT",
            "spaceAbove": {
              "magnitude": 20,
              "unit": "PT"
            },
            "spaceBelow": {
              "magnitude": 6,
              "unit": "PT"
            },
            "keepLinesTogether": true,
            "keepWithNext": true
          }
        },
        {
          "namedStyleType": "HEADING_2",
          "textStyle": {
            "bold": false,
            "fontSize": {
              "magnitude": 16,
              "unit": "PT"
            }
          },
          "paragraphStyle": {
            "namedStyleType": "NORMAL_TEXT",
            "direction": "LEFT_TO_RIGHT",
            "spaceAbove": {
              "magnitude": 18,
              "unit": "PT"
            },
            "spaceBelow": {
              "magnitude": 6,
              "unit": "PT"
            },
            "keepLinesTogether": true,
            "keepWithNext": true
          }
        },
        {
          "namedStyleType": "HEADING_3",
          "textStyle": {
            "bold": false,
            "foregroundColor": {
              "color": {
                "rgbColor": {
                  "red": 0.2627451,
                  "green": 0.2627451,
                  "blue": 0.2627451
                }
              }
            },
            "fontSize": {
              "magnitude": 14,
              "unit": "PT"
            }
          },
          "paragraphStyle": {
            "namedStyleType": "NORMAL_TEXT",
            "direction": "LEFT_TO_RIGHT",
            "spaceAbove": {
              "magnitude": 16,
              "unit": "PT"
            },
            "spaceBelow": {
              "magnitude": 4,
              "unit": "PT"
            },
            "keepLinesTogether": true,
            "keepWithNext": true
          }
        },
        {
          "namedStyleType": "HEADING_4",
          "textStyle": {
            "foregroundColor": {
              "color": {
                "rgbColor": {
                  "red": 0.4,
                  "green": 0.4,
                  "blue": 0.4
                }
              }
            },
            "fontSize": {
              "magnitude": 12,
              "unit": "PT"
            }
          },
          "paragraphStyle": {
            "namedStyleType": "NORMAL_TEXT",
            "direction": "LEFT_TO_RIGHT",
            "spaceAbove": {
              "magnitude": 14,
              "unit": "PT"
            },
            "spaceBelow": {
              "magnitude": 4,
              "unit": "PT"
            },
            "keepLinesTogether": true,
            "keepWithNext": true
          }
        },
        {
          "namedStyleType": "HEADING_5",
          "textStyle": {
            "foregroundColor": {
              "color": {
                "rgbColor": {
                  "red": 0.4,
                  "green": 0.4,
                  "blue": 0.4
                }
              }
            },
            "fontSize": {
              "magnitude": 11,
              "unit": "PT"
            }
          },
          "paragraphStyle": {
            "namedStyleType": "NORMAL_TEXT",
            "direction": "LEFT_TO_RIGHT",
            "spaceAbove": {
              "magnitude": 12,
              "unit": "PT"
            },
            "spaceBelow": {
              "magnitude": 4,
              "unit": "PT"
            },
            "keepLinesTogether": true,
            "keepWithNext": true
          }
        },
        {
          "namedStyleType": "HEADING_6",
          "textStyle": {
            "italic": true,
            "foregroundColor": {
              "color": {
                "rgbColor": {
                  "red": 0.4,
                  "green": 0.4,
                  "blue": 0.4
                }
              }
            },
            "fontSize": {
              "magnitude": 11,
              "unit": "PT"
            }
          },
          "paragraphStyle": {
            "namedStyleType": "NORMAL_TEXT",
            "direction": "LEFT_TO_RIGHT",
            "spaceAbove": {
              "magnitude": 12,
              "unit": "PT"
            },
            "spaceBelow": {
              "magnitude": 4,
              "unit": "PT"
            },
            "keepLinesTogether": true,
            "keepWithNext": true
          }
        },
        {
          "namedStyleType": "TITLE",
          "textStyle": {
            "fontSize": {
              "magnitude": 26,
              "unit": "PT"
            }
          },
          "paragraphStyle": {
            "namedStyleType": "NORMAL_TEXT",
            "direction": "LEFT_TO_RIGHT",
            "spaceAbove": {
              "unit": "PT"
            },
            "spaceBelow": {
              "magnitude": 3,
              "unit": "PT"
            },
            "keepLinesTogether": true,
            "keepWithNext": true
          }
        },
        {
          "namedStyleType": "SUBTITLE",
          "textStyle": {
            "italic": false,
            "foregroundColor": {
              "color": {
                "rgbColor": {
                  "red": 0.4,
                  "green": 0.4,
                  "blue": 0.4
                }
              }
            },
            "fontSize": {
              "magnitude": 15,
              "unit": "PT"
            },
            "weightedFontFamily": {
              "fontFamily": "Arial",
              "weight": 400
            }
          },
          "paragraphStyle": {
            "namedStyleType": "NORMAL_TEXT",
            "direction": "LEFT_TO_RIGHT",
            "spaceAbove": {
              "unit": "PT"
            },
            "spaceBelow": {
              "magnitude": 16,
              "unit": "PT"
            },
            "keepLinesTogether": true,
            "keepWithNext": true
          }
        }
      ]
    },
    "revisionId": "AOV_f4-ihmBtXazmNI3atxs6q__f_v95KD8CRRYr0A0r_JW6AvszrkUOTHGYc2duYLspaHXPvjnJWyIymNLAQQ",
    "suggestionsViewMode": "SUGGESTIONS_INLINE",
    "documentId": "1WTLf8-9swLvSJHQoyJyk-VCiU1ptTucJDrL4gZBUQ7Q"
  }
}
```

## Triggers

_This plugin does not contain any triggers._

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials_file_contents|credential_secret_key|None|True|Copy and paste the contents of the credentials file from google|None|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

## Workflows

Examples:

* Create document
* Get document

## Versions

* 1.0.0 - Initial plugin

## References

* [Google Docs](https://developers.google.com/docs/api/reference/rest/v1/documents)

## Custom Output Types

### create_result

|Name|Type|Required|Description|
|----|----|--------|-----------|
|documentId|string|False|Document ID|
|replies|[]object|False|Replies|
|writeControl|object|False|Write control|

### document

|Name|Type|Required|Description|
|----|----|--------|-----------|
|body|object|False|Body|
|documentId|string|False|Document ID|
|documentStyle|object|False|Document Style|
|namedStyles|object|False|Named styles|
|revisionId|string|False|Revision ID|
|suggestionsViewMode|string|False|Suggestions view mode|
|title|string|False|Title|