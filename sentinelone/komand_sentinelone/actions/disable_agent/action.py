import insightconnect_plugin_runtime
from .schema import DisableAgentInput, DisableAgentOutput, Input, Output, Component

# Custom imports below


class DisableAgent(insightconnect_plugin_runtime.Action):
    TIMEZONES_MAP = {
        "GMT +00:00": [
            "Azores Summer Time [AZOST]",
            "Coordinated Universal Time [UTC]",
            "Eastern Greenland Summer Time [EGST]",
            "Greenwich Mean Time [GMT ]",
            "Western European Time [WET]",
        ],
        "GMT +01:00": [
            "AIX-specific equivalent of Central European Time [DFT]",
            "Central European Time [CET]",
            "Irish Standard Time [IST]",
            " Middle European Time [MET]",
            "West Africa Time [WAT]",
            "Western European Summer Time [WEST]",
        ],
        "GMT +02:00": [
            "Central Africa Time [CAT]",
            "Central European Summer Time [CEST]",
            "Eastern European Time [EET]",
            "Heure Avancée Europe Centrale French-language name for CEST [HAEC]",
            "Israel Standard Time [IST]",
            "Kaliningrad Time [KALT]",
            "Middle European Summer Time [MEST]",
            "South African Standard Time [SAST]",
            "West Africa Summer Time [WAST]",
        ],
        "GMT +03:00": [
            "Arabia Standard Time [AST]",
            "East Africa Time [EAT]",
            "Eastern European Summer Time [EEST]",
            "Further-eastern European Time [FET]",
            "Indian Ocean Time [IOT]",
            "Israel Daylight Time [IDT]",
            "Moscow Time [MSK]",
            "Showa Station Time [SYOT]",
            "Turkey Time [TRT]",
        ],
        "GMT +03:30": ["Iran Standard Time [IRST]"],
        "GMT +04:00": [
            "Armenia Time [AMT]",
            "Azerbaijan Time [AZT]",
            "Georgia Standard Time [GET]",
            "Gulf Standard Time [GST]",
            "Mauritius Time [MUT]",
            "Réunion Time [RET]",
            "Samara Time [SAMT]",
            "Seychelles Time [SCT]",
            "Volgograd Time [VOLT]",
        ],
        "GMT +04:30": ["Afghanistan Time [AFT]", "Iran Daylight Time [IRDT]"],
        "GMT +05:00": [
            "Aqtobe Time [AQTT]",
            "French Southern and Antarctic Time [TFT]",
            "Heard and McDonald Islands Time [HMT]",
            "Maldives Time [MVT]",
            "Mawson Station Time [MAWT]",
            "Oral Time [ORAT]",
            "Pakistan Standard Time [PKT]",
            "Tajikistan Time [TJT]",
            "Turkmenistan Time [TMT]",
            "Uzbekistan Time [UZT]",
            "Yekaterinburg Time [YEKT]",
        ],
        "GMT +05:30": ["Indian Standard Time [IST]", "Sri Lanka Standard Time [SLST]"],
        "GMT +05:45": ["Nepal Time [NPT]"],
        "GMT +06:00": [
            "Alma-Ata Time [ALMT]",
            "Bangladesh Standard Time [BST]",
            "Bhutan Time [BTT]",
            "British Indian Ocean Time [BIOT]",
            "Kyrgyzstan Time [KGT]",
            "Omsk Time [OMST]",
            "Vostok Station Time [VOST]",
        ],
        "GMT +06:30": ["Cocos Islands Time [CCT]", "Myanmar Standard Time [MMT]"],
        "GMT +07:00": [
            "Christmas Island Time [CXT]",
            "Davis Time [DAVT]",
            "Hovd Time [HOVT]",
            "Indochina Time [ICT]",
            "Krasnoyarsk Time [KRAT]",
            "Novosibirsk Time [NOVT]",
            "Thailand Standard Time [THA]",
            "Western Indonesian Time [WIB]",
        ],
        "GMT +08:00": [
            "Australian Western Standard Time [AWST]",
            "Brunei Time [BNT]",
            "Central Indonesia Time [WITA]",
            "China Standard Time [CST]",
            "Choibalsan Standard Time [CHOT]",
            "Hong Kong Time [HKT]",
            "Irkutsk Time [IRKT]",
            "Malaysia Standard Time [MST]",
            "Malaysia Time [MYT]",
            "Philippine Standard Time [PST]",
            "Philippine Time [PHT]",
            "Singapore Standard Time [SST]",
            "Singapore Time [SGT]",
            "Ulaanbaatar Standard Time [ULAT]",
            "Western Standard Time [WST]",
        ],
        "GMT +09:00": [
            "Choibalsan Summer Time [CHOST]",
            "Eastern Indonesian Time [WIT]",
            "Japan Standard Time [JST]",
            "Korea Standard Time [KST]",
            "Palau Time [PWT]",
            "Timor Leste Time [TLT]",
            "Ulaanbaatar Summer Time [ULAST]",
            "Yakutsk Time [YAKT]",
        ],
        "GMT +09:30": ["Australian Central Standard Time [ACST]"],
        "GMT +10:00": [
            "Australian Eastern Standard Time [AEST]",
            "Australian Eastern Time [AET]",
            "Chamorro Standard Time [CHST]",
            "Chuuk Time [CHUT]",
            "Dumont dUrville Time [DDUT]",
            "Papua New Guinea Time [PGT]",
            "Vladivostok Time [VLAT]",
        ],
        "GMT +10:30": ["Australian Central Daylight Saving Time [ACDT]", "Lord Howe Standard Time [LHST]"],
        "GMT +11:00": [
            "Australian Eastern Daylight Saving Time [AEDT]",
            "Bougainville Standard Time [BST]",
            "Kosrae Time [KOST]",
            "Lord Howe Summer Time [LHST]",
            "Macquarie Island Station Time [MIST]",
            "New Caledonia Time [NCT]",
            "Norfolk Island Time [NFT]",
            "Pohnpei Standard Time [PONT]",
            "Sakhalin Island Time [SAKT]",
            "Solomon Islands Time [SBT]",
            "Srednekolymsk Time [SRET]",
            "Vanuatu Time [VUT]",
        ],
        "GMT +12:00": [
            "Anadyr Time [ANAT]",
            "Fiji Time [FJT]",
            "Gilbert Island Time [GILT]",
            "Kamchatka Time [PETT]",
            "Magadan Time [MAGT]",
            "Marshall Islands Time [MHT]",
            "New Zealand Standard Time [NZST]",
            "Tuvalu Time [TVT]",
            "Wake Island Time [WAKT]",
        ],
        "GMT +12:45": ["Chatham Standard Time [CHAST]"],
        "GMT +13:00": [
            "New Zealand Daylight Time [NZDT]",
            "Phoenix Island Time [PHOT]",
            "Tokelau Time [TKT]",
            "Tonga Time [TOT]",
        ],
        "GMT +13:45": ["Chatham Daylight Time [CHADT]"],
        "GMT +14:00": ["Line Islands Time [LINT]"],
        "GMT -01:00": ["Azores Standard Time [AZOT]", "Cape Verde Time [CVT]", "Eastern Greenland Time [EGT]"],
        "GMT -02:00": [
            "Brasília Summer Time [BRST]",
            "Fernando de Noronha Time [FNT]",
            "Saint Pierre and Miquelon Daylight Time [PMDT]",
            "South Georgia and the South Sandwich Islands Time [GST]",
            "Uruguay Summer Time [UYST]",
            "West Greenland Summer Time [WGST]",
        ],
        "GMT -02:30": ["Newfoundland Daylight Time [NDT]"],
        "GMT -03:00": [
            "Amazon Summer Time (Brazil) [AMST]",
            "Argentina Time [ART]",
            "Atlantic Daylight Time [ADT]",
            "Brasília Time [BRT]",
            "Chile Summer Time [CLST]",
            "Falkland Islands Summer Time [FKST]",
            "French Guiana Time [GFT]",
            "Paraguay Summer Time [PYST]",
            "Rothera Research Station Time [ROTT]",
            "Saint Pierre and Miquelon Standard Time [PMST]",
            "Suriname Time [SRT]",
            "Uruguay Standard Time [UYT]",
            "West Greenland Time [WGT]",
        ],
        "GMT -03:30": ["Newfoundland Standard Time [NST]", "Newfoundland Time [NT]"],
        "GMT -04:00": [
            "Amazon Time (Brazil) [AMT]",
            "Atlantic Standard Time [AST]",
            "Bolivia Time [BOT]",
            "Chile Standard Time [CLT]",
            "Colombia Summer Time [COST]",
            "Cuba Daylight Time [CDT]",
            "Eastern Daylight Time (North America) [EDT]",
            "Falkland Islands Time [FKT]",
            "Guyana Time [GYT]",
            "Paraguay Time [PYT]",
            "Venezuelan Standard Time [VET]",
        ],
        "GMT -05:00": [
            "Acre Time [ACT]",
            "Central Daylight Time (North America) [CDT]",
            "Colombia Time [COT]",
            "Cuba Standard Time [CST]",
            "Easter Island Summer Time [EASST]",
            "Eastern Standard Time (North America) [EST]",
            "Ecuador Time [ECT]",
            "Peru Time [PET]",
        ],
        "GMT -06:00": [
            "Central Standard Time (North America) [CST]",
            "Central Time [CT]",
            "Easter Island Standard Time [EAST]",
            "Galápagos Time [GALT]",
            "Mountain Daylight Time (North America) [MDT]",
        ],
        "GMT -07:00": ["Mountain Standard Time (North America) [MST]", "Pacific Daylight Time (North America) [PDT]"],
        "GMT -08:00": [
            "Alaska Daylight Time [AKDT]",
            "Clipperton Island Standard Time [CIST]",
            "Pacific Standard Time (North America) [PST]",
        ],
        "GMT -09:00": [
            "Alaska Standard Time [AKST]",
            "Gambier Island Time [GIT]",
            "Gambier Islands Time [GAMT]",
            "Hawaii–Aleutian Daylight Time [HDT]",
        ],
        "GMT -09:30": ["Marquesas Islands Time [MART]", "Marquesas Islands Time [MIT]"],
        "GMT -10:00": [
            "Cook Island Time [CKT]",
            "Hawaii–Aleutian Standard Time [HST]",
            "Samoa Daylight Time [SDT]",
            "Tahiti Time [TAHT]",
        ],
        "GMT -11:00": ["Niue Time [NUT]", "Samoa Standard Time [SST]"],
        "GMT -12:00": ["Baker Island Time [BIT]", "International Day Line West time zone [IDLW]"],
    }

    def __init__(self):
        super(self.__class__, self).__init__(
            name="disable_agent",
            description=Component.DESCRIPTION,
            input=DisableAgentInput(),
            output=DisableAgentOutput(),
        )

    def run(self, params={}):
        expiration_timezone = params.get(Input.EXPIRATION_TIMEZONE)
        expiration_time = params.get(Input.EXPIRATION_TIME)
        agent = params.get(Input.AGENT)
        user_filter = params.get(Input.FILTER, {})
        data = {"shouldReboot": params.get(Input.REBOOT)}

        if expiration_time:
            for timezone, timezone_list in DisableAgent.TIMEZONES_MAP.items():
                if expiration_timezone in timezone_list:
                    expiration_timezone = timezone
                    break
                else:
                    expiration_timezone = "GMT +06:00"

            data["expirationTimezone"] = expiration_timezone
            data["expiration"] = expiration_time

        if agent:
            user_filter["uuid"] = self.connection.client.get_agent_uuid(agent)

        return {Output.AFFECTED: self.connection.disable_agent(data, user_filter).get("data", {}).get("affected", 0)}
