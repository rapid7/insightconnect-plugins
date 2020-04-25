# Description

[Google Docs](https://developers.google.com/docs/api/reference/rest/v1/documents) is a online word processor. The plugin allows you to create and retrieve Google documents.

# Key Features

* Create Google documents
* Get Google documents

# Requirements

* A JWT with Google Docs permissions
* Google Docs API must be enabled

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials_file_contents|credential_secret_key|None|True|Copy and paste the contents of the credentials file provided by Google|None|None|

Example input:

```
"connection": {
  "credentials_file_contents": {
    "secretKey": "{\"type\":\"service_account\",\"project_id\":\"project-1111111111111\",\"private_key_id\": \"a1111aa111111aaa1111a1aa1aa111aa1a11aaaa1\",\"private_key\": \"-----BEGIN PRIVATE KEY-----\\\\nc29tZSBwcml2YXRlIGtleQ==\\\\n-----END PRIVATE KEY-----\\\\n\",\"client_email\": \"user@example.com\",\"client_id\": \"111111111111111111111\",\"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\"token_uri\": \"https://oauth2.googleapis.com/token\",\"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/test%40project-1111111111111.iam.gserviceaccount.com\"}"
  }
}
```

## Technical Details

### Actions

#### Append Line

This action is used to append line at end of document.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|content|string|None|True|Document content|None|None|
|document_id|string|None|True|Document ID|None|None|

Example input:

```
{
  "document_id": "1wLmF13vLaGrzsnPbwh6bjNg72jFhr8t4B6unBbfJi_q",
  "content": "Appended line"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|create_result|True|Append line result|

Example output:

```
{
  "result": {
    "replies": [
      {}
    ],
    "writeControl": {
      "requiredRevisionId": "ALm37BXuK4Riu0b1tbfv_hcbywo6sqKmArHp9GjZXy3xmRHAMG3p8C46LxZzMynRAoeC2_WSzDQrp4CGN7Gf"
    },
    "documentId": "1wLmF13vLaGrzsnPbwh6bjNg72jFhr8t4B6unBbfJi_q"
  }
}
```

#### Create Blank Document

This action is used to create a blank Google document.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|title|string|None|True|Document Title|None|None|

Example input:

```
{
  "title": "Test Blank Komand Doc"
}
```

##### Output

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

#### Create Document

This action is used to create a Google document.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|content|string|None|True|Document content|None|None|
|title|string|None|True|Document Title|None|None|

Example input:

```
{
  "content": "This is some text that should be in the body",
  "title": "Test Komand Doc"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|create_result|True|Document creation result|

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

#### Get Document

This action is used to get a Google document.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|document_id|string|None|True|Document ID|None|None|

Example input:

```
{
  "document_id": "1wLmF13vLaGrzsnPbwh6bjNg72jFhr8t4B6unBbfJi_q"
}
```

##### Output

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

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.1.0 - Add new action: append line at the end of file | Add example input
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Initial plugin

# Links

## References

* [Google Docs](https://developers.google.com/docs/api/reference/rest/v1/documents)

