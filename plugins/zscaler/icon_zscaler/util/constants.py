URL_CATEGORORIES_NAMES = {
    "Military": "MILITARY",
    "Dynamic DNS Host": "DYNAMIC_DNS",
    "Newly Revived Domains": "NEWLY_REVIVED_DOMAINS",
    "Other Adult Material": "OTHER_ADULT_MATERIAL",
    "Adult Themes": "ADULT_THEMES",
    "Lingerie/Bikini": "LINGERIE_BIKINI",
    "Nudity": "NUDITY",
    "Pornography": "PORNOGRAPHY",
    "Body Art": "SEXUALITY",
    "Adult Sex Education": "ADULT_SEX_EDUCATION",
    "K-12 Sex Education": "K_12_SEX_EDUCATION",
    "Social Networking Adult": "SOCIAL_ADULT",
    "Other Business and Economy": "OTHER_BUSINESS_AND_ECONOMY",
    "Corporate Marketing": "CORPORATE_MARKETING",
    "Finance": "FINANCE",
    "Professional Services": "PROFESSIONAL_SERVICES",
    "Classifieds": "CLASSIFIEDS",
    "Online Trading, Brokerage, Insurance": "TRADING_BROKARAGE_INSURANCE",
    "Other Drugs": "OTHER_DRUGS",
    "Marijuana": "MARIJUANA",
    "Other Education": "OTHER_EDUCATION",
    "Continuing Education/Colleges": "CONTINUING_EDUCATION_COLLEGES",
    "History": "HISTORY",
    "K-12": "K_12",
    "Reference Sites": "REFERENCE_SITES",
    "Science/Tech": "SCIENCE_AND_TECHNOLOGY",
    "Other Entertainment/Recreation": "OTHER_ENTERTAINMENT_AND_RECREATION",
    "Entertainment": "ENTERTAINMENT",
    "Television/Movies": "TELEVISION_AND_MOVIES",
    "Music and Audio Streaming": "MUSIC",
    "Video Streaming": "STREAMING_MEDIA",
    "Radio": "RADIO_STATIONS",
    "Gambling": "GAMBLING",
    "Online and Other Games": "OTHER_GAMES",
    "Social Networking Games": "SOCIAL_NETWORKING_GAMES",
    "Other Government and Politics": "OTHER_GOVERNMENT_AND_POLITICS",
    "Government": "GOVERNMENT",
    "Politics": "POLITICS",
    "Health": "HEALTH",
    "Other Illegal or Questionable": "OTHER_ILLEGAL_OR_QUESTIONABLE",
    "Copyright Infringement": "COPYRIGHT_INFRINGEMENT",
    "Computer Hacking": "COMPUTER_HACKING",
    "Questionable": "QUESTIONABLE",
    "Profanity": "PROFANITY",
    "Mature Humor": "MATURE_HUMOR",
    "Anonymizer": "ANONYMIZER",
    "Other Information Technology": "OTHER_INFORMATION_TECHNOLOGY",
    "Translators": "TRANSLATORS",
    "Image Host": "IMAGE_HOST",
    "FileHost": "FILE_HOST",
    "Shareware Download": "SHAREWARE_DOWNLOAD",
    "Advertising": "WEB_BANNERS",
    "Web Host": "WEB_HOST",
    "Web Search": "WEB_SEARCH",
    "Portals": "PORTALS",
    "Safe Search Engine": "SAFE_SEARCH_ENGINE",
    "CDN": "CDN",
    "Operating System and Software Updates": "OSS_UPDATES",
    "DNS Over HTTPS Services": "DNS_OVER_HTTPS",
    "Other Internet Communication": "OTHER_INTERNET_COMMUNICATION",
    "Internet Services": "INTERNET_SERVICES",
    "Discussion Forum": "DISCUSSION_FORUMS",
    "Online Chat": "ONLINE_CHAT",
    "Webmail": "EMAIL_HOST",
    "Blogs": "BLOG",
    "Peer-to-Peer Site": "P2P_COMMUNICATION",
    "Remote Access Tools": "REMOTE_ACCESS",
    "Web Conferencing": "WEB_CONFERENCING",
    "Zscaler Proxy IPs": "ZSPROXY_IPS",
    "Job/Employment Search": "JOB_SEARCH",
    "Militancy/Hate and Extremism": "MILITANCY_HATE_AND_EXTREMISM",
    "Other Miscellaneous": "OTHER_MISCELLANEOUS",
    "Miscellaneous or Unknown": "MISCELLANEOUS_OR_UNKNOWN",
    "Newly Registered and Observed Domains": "NEWLY_REG_DOMAINS",
    "Non Categorizable": "NON_CATEGORIZABLE",
    "News and Media": "NEWS_AND_MEDIA",
    "Other Religion": "OTHER_RELIGION",
    "Traditional Religion": "TRADITIONAL_RELIGION",
    "Cult": "CULT",
    "Alt/New Age": "ALT_NEW_AGE",
    "Other Security": "OTHER_SECURITY",
    "Spyware/Adware": "ADWARE_OR_SPYWARE",
    "Custom Encrypted Content": "ENCR_WEB_CONTENT",
    "Other Shopping and Auctions": "OTHER_SHOPPING_AND_AUCTIONS",
    "Online Shopping": "SPECIALIZED_SHOPPING",
    "Real Estate": "REAL_ESTATE",
    "Online Auctions": "ONLINE_AUCTIONS",
    "Other Social and Family Issues": "OTHER_SOCIAL_AND_FAMILY_ISSUES",
    "Social Issues": "SOCIAL_ISSUES",
    "Family Issues": "FAMILY_ISSUES",
    "Other Society and Lifestyle": "OTHER_SOCIETY_AND_LIFESTYLE",
    "Art/Culture": "ART_CULTURE",
    "Lifestyle": "ALTERNATE_LIFESTYLE",
    "Hobbies/Leisure": "HOBBIES_AND_LEISURE",
    "Dining/Restaurant": "DINING_AND_RESTAURANT",
    "Alcohol/Tobacco": "ALCOHOL_TOBACCO",
    "Social Networking": "SOCIAL_NETWORKING",
    "Special Interests/Social Organizations": "SPECIAL_INTERESTS",
    "Sports": "SPORTS",
    "Tasteless": "TASTELESS",
    "Travel": "TRAVEL",
    "User-Defined": "USER_DEFINED",
    "Vehicles": "VEHICLES",
    "Violence": "VIOLENCE",
    "Weapons/Bomb": "WEAPONS_AND_BOMBS",
}

URL_CATEGORY_UPDATE_ACTIONS = {"Add to the list": "ADD_TO_LIST", "Remove from the list": "REMOVE_FROM_LIST"}


class Cause:
    INVALID_DETAILS = "Invalid details provided."
    RESOURCE_NOT_FOUND = "Resource not found."
    GROUP_NOT_FOUND = "Group not found."
    DEPARTMENT_NOT_FOUND = "Department not found."
    CATEGORY_NOT_FOUND = "URL Category not found."
    URL_LIST_NOT_PROVIDED = "URL list not provided."
    TOKEN_EXPIRED = "OAuth 2.0 bearer token has expired or is invalid."
    RATE_LIMITED = "API rate limit exceeded."
    INSUFFICIENT_PERMISSIONS = "Insufficient permissions to perform this action."
    SERVER_ERROR = "Zscaler API encountered an internal server error."
    SERVICE_UNAVAILABLE = "Zscaler API service is temporarily unavailable."


class Assistance:
    VERIFY_INPUT = (
        "Verify your input is correct and not malformed and try again. If the issue persists, please contact support."
    )
    REAUTHENTICATE = (
        "The OAuth 2.0 token has expired. The plugin will attempt to re-authenticate automatically. "
        "If the issue persists, verify that the client_id and private_key are correct and not revoked."
    )
    RATE_LIMIT_WAIT = (
        "The API rate limit has been exceeded. Wait for the rate limit window to reset before retrying. "
        "Check the Retry-After header for timing guidance."
    )
    CHECK_PERMISSIONS = (
        "Verify that the API client has the required permissions for this operation in the ZIdentity portal. "
        "Ensure the correct scopes are assigned to the client credentials."
    )
    CONTACT_SUPPORT = (
        "An internal server error occurred on the Zscaler side. If the issue persists, contact Zscaler support."
    )
    RETRY_LATER = (
        "The Zscaler API service is temporarily unavailable. Retry the request after a short delay. "
        "If the issue persists, check the Zscaler status page or contact support."
    )


HTTP_ERROR_MAP = {
    400: {"cause": Cause.INVALID_DETAILS, "assistance": Assistance.VERIFY_INPUT},
    401: {"cause": Cause.TOKEN_EXPIRED, "assistance": Assistance.REAUTHENTICATE},
    403: {"cause": Cause.INSUFFICIENT_PERMISSIONS, "assistance": Assistance.CHECK_PERMISSIONS},
    404: {"cause": Cause.RESOURCE_NOT_FOUND, "assistance": Assistance.VERIFY_INPUT},
    429: {"cause": Cause.RATE_LIMITED, "assistance": Assistance.RATE_LIMIT_WAIT},
    500: {"cause": Cause.SERVER_ERROR, "assistance": Assistance.CONTACT_SUPPORT},
    503: {"cause": Cause.SERVICE_UNAVAILABLE, "assistance": Assistance.RETRY_LATER},
}
