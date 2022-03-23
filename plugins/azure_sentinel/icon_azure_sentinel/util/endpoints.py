COMMON_URI = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/"


class Endpoint:
    GETINCIDENT = COMMON_URI + "incidents/{}?api-version={}"
    CREATEINCIDENT = COMMON_URI + "incidents/{}?api-version={}"
    LISTINCIDENTS = COMMON_URI + "incidents?api-version={}"
    DELETEINCIDENT = COMMON_URI + "incidents/{}?api-version={}"
    LISTALERTS = COMMON_URI + "incidents/{}/alerts?api-version={}"
    LISTBOOKMARKS = COMMON_URI + "incidents/{}/bookmarks?api-version={}"
    LISTENTITIES = COMMON_URI + "incidents/{}/entities?api-version={}"
    # Comment related URLs
    GETCOMMENT = COMMON_URI + "incidents/{}/comments/{}?api-version={}"
    LISTCOMMENTS = COMMON_URI + "incidents/{}/comments?api-version={}"
    CREATEUPDATECOMMENT = COMMON_URI + "incidents/{}/comments/{}?api-version={}"
    DELETECOMMENT = COMMON_URI + "incidents/{}/comments/{}?api-version={}"
    # Threat Intelligence Indicator related URLs
    CREATEINDICATOR = COMMON_URI + "threatIntelligence/main/createIndicator?api-version={}"
    GETINDICATOR = COMMON_URI + "threatIntelligence/main/indicators/{}?api-version={}"
    UPDATEINDICATOR = COMMON_URI + "threatIntelligence/main/indicators/{}?api-version={}"
    DELETEINDICATOR = COMMON_URI + "threatIntelligence/main/indicators/{}?api-version={}"
    QUERYINDICATORS = COMMON_URI + "threatIntelligence/main/queryIndicators?api-version={}"
    APPENDTAGS = COMMON_URI + "threatIntelligence/main/indicators/{}/appendTags?api-version={}"
    REPLACETAGS = COMMON_URI + "threatIntelligence/main/indicators/{}/replaceTags?api-version={}"
