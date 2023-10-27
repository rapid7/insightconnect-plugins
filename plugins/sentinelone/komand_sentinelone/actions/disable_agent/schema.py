# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Disable agents that match a filter"


class Input:
    AGENT = "agent"
    EXPIRATIONTIME = "expirationTime"
    EXPIRATIONTIMEZONE = "expirationTimezone"
    FILTER = "filter"
    REBOOT = "reboot"


class Output:
    AFFECTED = "affected"


class DisableAgentInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent": {
      "type": "string",
      "title": "Agent",
      "description": "Agent to perform disable action on. Accepts IP address, MAC address, hostname, UUID or agent ID. Leave empty to perform action on all applicable Agents",
      "order": 1
    },
    "expirationTime": {
      "type": "string",
      "format": "date-time",
      "displayType": "date",
      "title": "Expiration Time",
      "description": "Agents will be re-enabled after this timestamp",
      "order": 4
    },
    "expirationTimezone": {
      "type": "string",
      "title": "Expiration Timezone",
      "description": "Timezone for the expiration timestamp. Set with expiration time",
      "default": "Central Standard Time (North America) [CST]",
      "enum": [
        "Australian Central Daylight Saving Time [ACDT]",
        "Australian Central Standard Time [ACST]",
        "Acre Time [ACT]",
        "Atlantic Daylight Time [ADT]",
        "Australian Eastern Daylight Saving Time [AEDT]",
        "Australian Eastern Standard Time [AEST]",
        "Australian Eastern Time [AET]",
        "Afghanistan Time [AFT]",
        "Alaska Daylight Time [AKDT]",
        "Alaska Standard Time [AKST]",
        "Alma-Ata Time [ALMT]",
        "Amazon Summer Time (Brazil) [AMST]",
        "Amazon Time (Brazil) [AMT]",
        "Armenia Time [AMT]",
        "Anadyr Time [ANAT]",
        "Aqtobe Time [AQTT]",
        "Argentina Time [ART]",
        "Arabia Standard Time [AST]",
        "Atlantic Standard Time [AST]",
        "Australian Western Standard Time [AWST]",
        "Azores Summer Time [AZOST]",
        "Azores Standard Time [AZOT]",
        "Azerbaijan Time [AZT]",
        "Brunei Time [BNT]",
        "British Indian Ocean Time [BIOT]",
        "Baker Island Time [BIT]",
        "Bolivia Time [BOT]",
        "Brasilia Summer Time [BRST]",
        "Brasilia Time [BRT]",
        "Bangladesh Standard Time [BST]",
        "Bougainville Standard Time [BST]",
        "Bhutan Time [BTT]",
        "Central Africa Time [CAT]",
        "Cocos Islands Time [CCT]",
        "Central Daylight Time (North America) [CDT]",
        "Cuba Daylight Time [CDT]",
        "Central European Summer Time [CEST]",
        "Central European Time [CET]",
        "Chatham Daylight Time [CHADT]",
        "Chatham Standard Time [CHAST]",
        "Choibalsan Standard Time [CHOT]",
        "Choibalsan Summer Time [CHOST]",
        "Chamorro Standard Time [CHST]",
        "Chuuk Time [CHUT]",
        "Clipperton Island Standard Time [CIST]",
        "Central Indonesia Time [WITA]",
        "Cook Island Time [CKT]",
        "Chile Summer Time [CLST]",
        "Chile Standard Time [CLT]",
        "Colombia Summer Time [COST]",
        "Colombia Time [COT]",
        "Central Standard Time (North America) [CST]",
        "China Standard Time [CST]",
        "Cuba Standard Time [CST]",
        "Central Time [CT]",
        "Cape Verde Time [CVT]",
        "Christmas Island Time [CXT]",
        "Davis Time [DAVT]",
        "Dumont dUrville Time [DDUT]",
        "AIX-specific equivalent of Central European Time [DFT]",
        "Easter Island Summer Time [EASST]",
        "Easter Island Standard Time [EAST]",
        "East Africa Time [EAT]",
        "Ecuador Time [ECT]",
        "Eastern Daylight Time (North America) [EDT]",
        "Eastern European Summer Time [EEST]",
        "Eastern European Time [EET]",
        "Eastern Greenland Summer Time [EGST]",
        "Eastern Greenland Time [EGT]",
        "Eastern Indonesian Time [WIT]",
        "Eastern Standard Time (North America) [EST]",
        "Further-eastern European Time [FET]",
        "Fiji Time [FJT]",
        "Falkland Islands Summer Time [FKST]",
        "Falkland Islands Time [FKT]",
        "Fernando de Noronha Time [FNT]",
        "Galapagos Time [GALT]",
        "Gambier Islands Time [GAMT]",
        "Georgia Standard Time [GET]",
        "French Guiana Time [GFT]",
        "Gilbert Island Time [GILT]",
        "Gambier Island Time [GIT]",
        "Greenwich Mean Time [GMT]",
        "South Georgia and the South Sandwich Islands Time [GST]",
        "Gulf Standard Time [GST]",
        "Guyana Time [GYT]",
        "Hawaii-Aleutian Daylight Time [HDT]",
        "Heure Avancee Europe Centrale French-language name for CEST [HAEC]",
        "Hawaii-Aleutian Standard Time [HST]",
        "Hong Kong Time [HKT]",
        "Heard and McDonald Islands Time [HMT]",
        "Hovd Time [HOVT]",
        "Indochina Time [ICT]",
        "International Day Line West time zone [IDLW]",
        "Israel Daylight Time [IDT]",
        "Indian Ocean Time [IOT]",
        "Iran Daylight Time [IRDT]",
        "Irkutsk Time [IRKT]",
        "Iran Standard Time [IRST]",
        "Indian Standard Time [IST]",
        "Irish Standard Time [IST]",
        "Israel Standard Time [IST]",
        "Japan Standard Time [JST]",
        "Kaliningrad Time [KALT]",
        "Kyrgyzstan Time [KGT]",
        "Kosrae Time [KOST]",
        "Krasnoyarsk Time [KRAT]",
        "Korea Standard Time [KST]",
        "Lord Howe Standard Time [LHST]",
        "Lord Howe Summer Time [LHST]",
        "Line Islands Time [LINT]",
        "Magadan Time [MAGT]",
        "Marquesas Islands Time [MART]",
        "Mawson Station Time [MAWT]",
        "Mountain Daylight Time (North America) [MDT]",
        "Middle European Time [MET]",
        "Middle European Summer Time [MEST]",
        "Marshall Islands Time [MHT]",
        "Macquarie Island Station Time [MIST]",
        "Marquesas Islands Time [MIT]",
        "Myanmar Standard Time [MMT]",
        "Moscow Time [MSK]",
        "Malaysia Standard Time [MST]",
        "Mountain Standard Time (North America) [MST]",
        "Mauritius Time [MUT]",
        "Maldives Time [MVT]",
        "Malaysia Time [MYT]",
        "New Caledonia Time [NCT]",
        "Newfoundland Daylight Time [NDT]",
        "Norfolk Island Time [NFT]",
        "Novosibirsk Time [NOVT]",
        "Nepal Time [NPT]",
        "Newfoundland Standard Time [NST]",
        "Newfoundland Time [NT]",
        "Niue Time [NUT]",
        "New Zealand Daylight Time [NZDT]",
        "New Zealand Standard Time [NZST]",
        "Omsk Time [OMST]",
        "Oral Time [ORAT]",
        "Pacific Daylight Time (North America) [PDT]",
        "Peru Time [PET]",
        "Kamchatka Time [PETT]",
        "Papua New Guinea Time [PGT]",
        "Phoenix Island Time [PHOT]",
        "Philippine Time [PHT]",
        "Pakistan Standard Time [PKT]",
        "Saint Pierre and Miquelon Daylight Time [PMDT]",
        "Saint Pierre and Miquelon Standard Time [PMST]",
        "Pohnpei Standard Time [PONT]",
        "Pacific Standard Time (North America) [PST]",
        "Philippine Standard Time [PST]",
        "Palau Time [PWT]",
        "Paraguay Summer Time [PYST]",
        "Paraguay Time [PYT]",
        "Reunion Time [RET]",
        "Rothera Research Station Time [ROTT]",
        "Sakhalin Island Time [SAKT]",
        "Samara Time [SAMT]",
        "South African Standard Time [SAST]",
        "Solomon Islands Time [SBT]",
        "Seychelles Time [SCT]",
        "Samoa Daylight Time [SDT]",
        "Singapore Time [SGT]",
        "Sri Lanka Standard Time [SLST]",
        "Srednekolymsk Time [SRET]",
        "Suriname Time [SRT]",
        "Samoa Standard Time [SST]",
        "Singapore Standard Time [SST]",
        "Showa Station Time [SYOT]",
        "Tahiti Time [TAHT]",
        "Thailand Standard Time [THA]",
        "French Southern and Antarctic Time [TFT]",
        "Tajikistan Time [TJT]",
        "Tokelau Time [TKT]",
        "Timor Leste Time [TLT]",
        "Turkmenistan Time [TMT]",
        "Turkey Time [TRT]",
        "Tonga Time [TOT]",
        "Tuvalu Time [TVT]",
        "Ulaanbaatar Summer Time [ULAST]",
        "Ulaanbaatar Standard Time [ULAT]",
        "Coordinated Universal Time [UTC]",
        "Uruguay Summer Time [UYST]",
        "Uruguay Standard Time [UYT]",
        "Uzbekistan Time [UZT]",
        "Venezuelan Standard Time [VET]",
        "Vladivostok Time [VLAT]",
        "Volgograd Time [VOLT]",
        "Vostok Station Time [VOST]",
        "Vanuatu Time [VUT]",
        "Wake Island Time [WAKT]",
        "West Africa Summer Time [WAST]",
        "West Africa Time [WAT]",
        "Western European Summer Time [WEST]",
        "Western European Time [WET]",
        "Western Indonesian Time [WIB]",
        "West Greenland Summer Time [WGST]",
        "West Greenland Time [WGT]",
        "Western Standard Time [WST]",
        "Yakutsk Time [YAKT]",
        "Yekaterinburg Time [YEKT]"
      ],
      "order": 3
    },
    "filter": {
      "type": "object",
      "title": "Filter",
      "description": "Filter to apply action on specified agents. Leave empty to perform action on all applicable Agents",
      "order": 5
    },
    "reboot": {
      "type": "boolean",
      "title": "Reboot",
      "description": "Set true to reboot the endpoint, false to skip rebooting",
      "default": false,
      "order": 2
    }
  },
  "required": [
    "reboot"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DisableAgentOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "affected": {
      "type": "integer",
      "title": "Affected",
      "description": "Number of entities affected by the requested operation",
      "order": 1
    }
  },
  "required": [
    "affected"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
