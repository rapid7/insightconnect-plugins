# Description

Timestamps, timezones, and Datetimes can be difficult to work with, especially when dealing with different locales on different systems. The Datetime InsightConnect plugin manipulates timestamps using Python's [Maya](https://pypi.org/project/maya/) library, which makes the simple things much easier while admitting that time is an illusion (timezones doubly so).

# Key Features

* Convert a Datetime to an Epoch and vice versa
* Convert a Datetime to a specified format
* Determine the elapsed time between two dates
* Convert date from localtime to UTC
* Convert date from UTC to localtime

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Get Future Time

This action is used to calculate a new delta timestamp from parameters and a timestamp. The default base timestamp uses the current time to calculate a new delta timestamp. User can also provide different timestamp then the current time eg. 2020-01-01T10:20:30.0Z. New delta timestamp is computed by adding the amount of time units specified by user to the base timestamp. Obtained timestamp is converted to the time zone selected by the user. Default time zone is set up as UTC. Action returns RFC3339 compliant timestamp eg. 2020-02-02T10:20:30.0Z.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|base_timestamp|date|None|False|Timestamp used for calculating a new delta timestamp eg. 2020-07-02T21:20:33.0Z, to use current time leave base timestamp parameter empty|None|2020-07-02 21:20:33|
|time_amount|integer|None|True|The amount of time units to add to the base timestamp to get the future time|[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]|20|
|time_unit|string|None|True|Units of time used for the future timestamp calculation|['Seconds', 'Minutes', 'Hours', 'Days', 'Weeks', 'Months']|Days|
|time_zone|string|UTC|True|List of zones|['Africa/Abidjan', 'Africa/Accra', 'Africa/Addis_Ababa', 'Africa/Algiers', 'Africa/Asmara', 'Africa/Asmera', 'Africa/Bamako', 'Africa/Bangui', 'Africa/Banjul', 'Africa/Bissau', 'Africa/Blantyre', 'Africa/Brazzaville', 'Africa/Bujumbura', 'Africa/Cairo', 'Africa/Casablanca', 'Africa/Ceuta', 'Africa/Conakry', 'Africa/Dakar', 'Africa/Dar_es_Salaam', 'Africa/Djibouti', 'Africa/Douala', 'Africa/El_Aaiun', 'Africa/Freetown', 'Africa/Gaborone', 'Africa/Harare', 'Africa/Johannesburg', 'Africa/Juba', 'Africa/Kampala', 'Africa/Khartoum', 'Africa/Kigali', 'Africa/Kinshasa', 'Africa/Lagos', 'Africa/Libreville', 'Africa/Lome', 'Africa/Luanda', 'Africa/Lubumbashi', 'Africa/Lusaka', 'Africa/Malabo', 'Africa/Maputo', 'Africa/Maseru', 'Africa/Mbabane', 'Africa/Mogadishu', 'Africa/Monrovia', 'Africa/Nairobi', 'Africa/Ndjamena', 'Africa/Niamey', 'Africa/Nouakchott', 'Africa/Ouagadougou', 'Africa/Porto-Novo', 'Africa/Sao_Tome', 'Africa/Timbuktu', 'Africa/Tripoli', 'Africa/Tunis', 'Africa/Windhoek', 'America/Adak', 'America/Anchorage', 'America/Anguilla', 'America/Antigua', 'America/Araguaina', 'America/Argentina/Buenos_Aires', 'America/Argentina/Catamarca', 'America/Argentina/ComodRivadavia', 'America/Argentina/Cordoba', 'America/Argentina/Jujuy', 'America/Argentina/La_Rioja', 'America/Argentina/Mendoza', 'America/Argentina/Rio_Gallegos', 'America/Argentina/Salta', 'America/Argentina/San_Juan', 'America/Argentina/San_Luis', 'America/Argentina/Tucuman', 'America/Argentina/Ushuaia', 'America/Aruba', 'America/Asuncion', 'America/Atikokan', 'America/Atka', 'America/Bahia', 'America/Bahia_Banderas', 'America/Barbados', 'America/Belem', 'America/Belize', 'America/Blanc-Sablon', 'America/Boa_Vista', 'America/Bogota', 'America/Boise', 'America/Buenos_Aires', 'America/Cambridge_Bay', 'America/Campo_Grande', 'America/Cancun', 'America/Caracas', 'America/Catamarca', 'America/Cayenne', 'America/Cayman', 'America/Chicago', 'America/Chihuahua', 'America/Coral_Harbour', 'America/Cordoba', 'America/Costa_Rica', 'America/Creston', 'America/Cuiaba', 'America/Curacao', 'America/Danmarkshavn', 'America/Dawson', 'America/Dawson_Creek', 'America/Denver', 'America/Detroit', 'America/Dominica', 'America/Edmonton', 'America/Eirunepe', 'America/El_Salvador', 'America/Ensenada', 'America/Fort_Wayne', 'America/Fortaleza', 'America/Glace_Bay', 'America/Godthab', 'America/Goose_Bay', 'America/Grand_Turk', 'America/Grenada', 'America/Guadeloupe', 'America/Guatemala', 'America/Guayaquil', 'America/Guyana', 'America/Halifax', 'America/Havana', 'America/Hermosillo', 'America/Indiana/Indianapolis', 'America/Indiana/Knox', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Tell_City', 'America/Indiana/Vevay', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Indianapolis', 'America/Inuvik', 'America/Iqaluit', 'America/Jamaica', 'America/Jujuy', 'America/Juneau', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Knox_IN', 'America/Kralendijk', 'America/La_Paz', 'America/Lima', 'America/Los_Angeles', 'America/Louisville', 'America/Lower_Princes', 'America/Maceio', 'America/Managua', 'America/Manaus', 'America/Marigot', 'America/Martinique', 'America/Matamoros', 'America/Mazatlan', 'America/Mendoza', 'America/Menominee', 'America/Merida', 'America/Metlakatla', 'America/Mexico_City', 'America/Miquelon', 'America/Moncton', 'America/Monterrey', 'America/Montevideo', 'America/Montreal', 'America/Montserrat', 'America/Nassau', 'America/New_York', 'America/Nipigon', 'America/Nome', 'America/Noronha', 'America/North_Dakota/Beulah', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/Ojinaga', 'America/Panama', 'America/Pangnirtung', 'America/Paramaribo', 'America/Phoenix', 'America/Port-au-Prince', 'America/Port_of_Spain', 'America/Porto_Acre', 'America/Porto_Velho', 'America/Puerto_Rico', 'America/Rainy_River', 'America/Rankin_Inlet', 'America/Recife', 'America/Regina', 'America/Resolute', 'America/Rio_Branco', 'America/Rosario', 'America/Santa_Isabel', 'America/Santarem', 'America/Santiago', 'America/Santo_Domingo', 'America/Sao_Paulo', 'America/Scoresbysund', 'America/Shiprock', 'America/Sitka', 'America/St_Barthelemy', 'America/St_Johns', 'America/St_Kitts', 'America/St_Lucia', 'America/St_Thomas', 'America/St_Vincent', 'America/Swift_Current', 'America/Tegucigalpa', 'America/Thule', 'America/Thunder_Bay', 'America/Tijuana', 'America/Toronto', 'America/Tortola', 'America/Vancouver', 'America/Virgin', 'America/Whitehorse', 'America/Winnipeg', 'America/Yakutat', 'America/Yellowknife', 'Antarctica/Casey', 'Antarctica/Davis', 'Antarctica/DumontDUrville', 'Antarctica/Macquarie', 'Antarctica/Mawson', 'Antarctica/McMurdo', 'Antarctica/Palmer', 'Antarctica/Rothera', 'Antarctica/South_Pole', 'Antarctica/Syowa', 'Antarctica/Vostok', 'Arctic/Longyearbyen', 'Asia/Aden', 'Asia/Almaty', 'Asia/Amman', 'Asia/Anadyr', 'Asia/Aqtau', 'Asia/Aqtobe', 'Asia/Ashgabat', 'Asia/Ashkhabad', 'Asia/Baghdad', 'Asia/Bahrain', 'Asia/Baku', 'Asia/Bangkok', 'Asia/Beirut', 'Asia/Bishkek', 'Asia/Brunei', 'Asia/Calcutta', 'Asia/Choibalsan', 'Asia/Chongqing', 'Asia/Chungking', 'Asia/Colombo', 'Asia/Dacca', 'Asia/Damascus', 'Asia/Dhaka', 'Asia/Dili', 'Asia/Dubai', 'Asia/Dushanbe', 'Asia/Gaza', 'Asia/Harbin', 'Asia/Hebron', 'Asia/Ho_Chi_Minh', 'Asia/Hong_Kong', 'Asia/Hovd', 'Asia/Irkutsk', 'Asia/Istanbul', 'Asia/Jakarta', 'Asia/Jayapura', 'Asia/Jerusalem', 'Asia/Kabul', 'Asia/Kamchatka', 'Asia/Karachi', 'Asia/Kashgar', 'Asia/Kathmandu', 'Asia/Katmandu', 'Asia/Kolkata', 'Asia/Krasnoyarsk', 'Asia/Kuala_Lumpur', 'Asia/Kuching', 'Asia/Kuwait', 'Asia/Macao', 'Asia/Macau', 'Asia/Magadan', 'Asia/Makassar', 'Asia/Manila', 'Asia/Muscat', 'Asia/Nicosia', 'Asia/Novokuznetsk', 'Asia/Novosibirsk', 'Asia/Omsk', 'Asia/Oral', 'Asia/Phnom_Penh', 'Asia/Pontianak', 'Asia/Pyongyang', 'Asia/Qatar', 'Asia/Qyzylorda', 'Asia/Rangoon', 'Asia/Riyadh', 'Asia/Saigon', 'Asia/Sakhalin', 'Asia/Samarkand', 'Asia/Seoul', 'Asia/Shanghai', 'Asia/Singapore', 'Asia/Taipei', 'Asia/Tashkent', 'Asia/Tbilisi', 'Asia/Tehran', 'Asia/Tel_Aviv', 'Asia/Thimbu', 'Asia/Thimphu', 'Asia/Tokyo', 'Asia/Ujung_Pandang', 'Asia/Ulaanbaatar', 'Asia/Ulan_Bator', 'Asia/Urumqi', 'Asia/Vientiane', 'Asia/Vladivostok', 'Asia/Yakutsk', 'Asia/Yekaterinburg', 'Asia/Yerevan', 'Atlantic/Azores', 'Atlantic/Bermuda', 'Atlantic/Canary', 'Atlantic/Cape_Verde', 'Atlantic/Faeroe', 'Atlantic/Faroe', 'Atlantic/Jan_Mayen', 'Atlantic/Madeira', 'Atlantic/Reykjavik', 'Atlantic/South_Georgia', 'Atlantic/St_Helena', 'Atlantic/Stanley', 'Australia/ACT', 'Australia/Adelaide', 'Australia/Brisbane', 'Australia/Broken_Hill', 'Australia/Canberra', 'Australia/Currie', 'Australia/Darwin', 'Australia/Eucla', 'Australia/Hobart', 'Australia/LHI', 'Australia/Lindeman', 'Australia/Lord_Howe', 'Australia/Melbourne', 'Australia/NSW', 'Australia/North', 'Australia/Perth', 'Australia/Queensland', 'Australia/South', 'Australia/Sydney', 'Australia/Tasmania', 'Australia/Victoria', 'Australia/West', 'Australia/Yancowinna', 'Brazil/Acre', 'Brazil/DeNoronha', 'Brazil/East', 'Brazil/West', 'CET', 'CST6CDT', 'Canada/Atlantic', 'Canada/Central', 'Canada/East-Saskatchewan', 'Canada/Eastern', 'Canada/Mountain', 'Canada/Newfoundland', 'Canada/Pacific', 'Canada/Saskatchewan', 'Canada/Yukon', 'Chile/Continental', 'Chile/EasterIsland', 'Cuba', 'EET', 'EST', 'EST5EDT', 'Egypt', 'Eire', 'Etc/GMT', 'Etc/GMT+0', 'Etc/GMT+1', 'Etc/GMT+10', 'Etc/GMT+11', 'Etc/GMT+12', 'Etc/GMT+2', 'Etc/GMT+3', 'Etc/GMT+4', 'Etc/GMT+5', 'Etc/GMT+6', 'Etc/GMT+7', 'Etc/GMT+8', 'Etc/GMT+9', 'Etc/GMT-0', 'Etc/GMT-1', 'Etc/GMT-10', 'Etc/GMT-11', 'Etc/GMT-12', 'Etc/GMT-13', 'Etc/GMT-14', 'Etc/GMT-2', 'Etc/GMT-3', 'Etc/GMT-4', 'Etc/GMT-5', 'Etc/GMT-6', 'Etc/GMT-7', 'Etc/GMT-8', 'Etc/GMT-9', 'Etc/GMT0', 'Etc/Greenwich', 'Etc/UCT', 'Etc/UTC', 'Etc/Universal', 'Etc/Zulu', 'Europe/Amsterdam', 'Europe/Andorra', 'Europe/Athens', 'Europe/Belfast', 'Europe/Belgrade', 'Europe/Berlin', 'Europe/Bratislava', 'Europe/Brussels', 'Europe/Bucharest', 'Europe/Budapest', 'Europe/Chisinau', 'Europe/Copenhagen', 'Europe/Dublin', 'Europe/Gibraltar', 'Europe/Guernsey', 'Europe/Helsinki', 'Europe/Isle_of_Man', 'Europe/Istanbul', 'Europe/Jersey', 'Europe/Kaliningrad', 'Europe/Kiev', 'Europe/Lisbon', 'Europe/Ljubljana', 'Europe/London', 'Europe/Luxembourg', 'Europe/Madrid', 'Europe/Malta', 'Europe/Mariehamn', 'Europe/Minsk', 'Europe/Monaco', 'Europe/Moscow', 'Europe/Nicosia', 'Europe/Oslo', 'Europe/Paris', 'Europe/Podgorica', 'Europe/Prague', 'Europe/Riga', 'Europe/Rome', 'Europe/Samara', 'Europe/San_Marino', 'Europe/Sarajevo', 'Europe/Simferopol', 'Europe/Skopje', 'Europe/Sofia', 'Europe/Stockholm', 'Europe/Tallinn', 'Europe/Tirane', 'Europe/Tiraspol', 'Europe/Uzhgorod', 'Europe/Vaduz', 'Europe/Vatican', 'Europe/Vienna', 'Europe/Vilnius', 'Europe/Volgograd', 'Europe/Warsaw', 'Europe/Zagreb', 'Europe/Zaporozhye', 'Europe/Zurich', 'GB', 'GB-Eire', 'GMT', 'GMT+0', 'GMT-0', 'GMT0', 'Greenwich', 'HST', 'Hongkong', 'Iceland', 'Indian/Antananarivo', 'Indian/Chagos', 'Indian/Christmas', 'Indian/Cocos', 'Indian/Comoro', 'Indian/Kerguelen', 'Indian/Mahe', 'Indian/Maldives', 'Indian/Mauritius', 'Indian/Mayotte', 'Indian/Reunion', 'Iran', 'Israel', 'Jamaica', 'Japan', 'Kwajalein', 'Libya', 'MET', 'MST', 'MST7MDT', 'Mexico/BajaNorte', 'Mexico/BajaSur', 'Mexico/General', 'NZ', 'NZ-CHAT', 'Navajo', 'PRC', 'PST8PDT', 'Pacific/Apia', 'Pacific/Auckland', 'Pacific/Chatham', 'Pacific/Chuuk', 'Pacific/Easter', 'Pacific/Efate', 'Pacific/Enderbury', 'Pacific/Fakaofo', 'Pacific/Fiji', 'Pacific/Funafuti', 'Pacific/Galapagos', 'Pacific/Gambier', 'Pacific/Guadalcanal', 'Pacific/Guam', 'Pacific/Honolulu', 'Pacific/Johnston', 'Pacific/Kiritimati', 'Pacific/Kosrae', 'Pacific/Kwajalein', 'Pacific/Majuro', 'Pacific/Marquesas', 'Pacific/Midway', 'Pacific/Nauru', 'Pacific/Niue', 'Pacific/Norfolk', 'Pacific/Noumea', 'Pacific/Pago_Pago', 'Pacific/Palau', 'Pacific/Pitcairn', 'Pacific/Pohnpei', 'Pacific/Ponape', 'Pacific/Port_Moresby', 'Pacific/Rarotonga', 'Pacific/Saipan', 'Pacific/Samoa', 'Pacific/Tahiti', 'Pacific/Tarawa', 'Pacific/Tongatapu', 'Pacific/Truk', 'Pacific/Wake', 'Pacific/Wallis', 'Pacific/Yap', 'Poland', 'Portugal', 'ROC', 'ROK', 'Singapore', 'Turkey', 'UCT', 'US/Alaska', 'US/Aleutian', 'US/Arizona', 'US/Central', 'US/East-Indiana', 'US/Eastern', 'US/Hawaii', 'US/Indiana-Starke', 'US/Michigan', 'US/Mountain', 'US/Pacific', 'US/Pacific-New', 'US/Samoa', 'UTC', 'Universal', 'W-SU', 'WET', 'Zulu']|UTC|

Example input:

```
{
  "base_timestamp": "2020-07-02T21:20:33.0Z",
  "time_amount": 20,
  "time_unit": "Days",
  "time_zone": "UTC"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|timestamp|date|True|New timestamp|

Example output:

```
{
  "timestamp": "2020-07-22T21:20:33.0Z"
}
```

#### To UTC

This action is used to convert time from localtime to UTC.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|base_time|date|None|True|Datetime to convert, eg. 22 Jul 2020 21:20:33. Milliseconds is not supported|None|22 Jul 2020 21:20:33|
|timezone|string|None|True|Timezone to convert from localtime|None|US/Eastern|

Example input:

```
{
  "base_time": "22 Jul 2020 21:20:33",
  "timezone": "US/Eastern"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|converted_date|date|True|Date in UTC|

Example output:

```
{
  "converted_date": "2020-07-23T01:20:33.0Z"
}

```

#### To Localtime

This action is used to convert time from UTC to localtime.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|base_time|date|None|True|Datetime to convert, eg. 22 Jul 2020 21:20:33. Milliseconds is not supported|None|22 Jul 2020 21:20:33|
|timezone|string|None|True|Timezone to convert from UTC to localtime|None|US/Eastern|

Example input:

```
{
  "base_time": "22 Jul 2020 21:20:33",
  "timezone": "US/Eastern"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|converted_date|date|True|Date in localtime|

Example output:

```
{
  "converted_date": "2020-07-22T17:20:33.0Z"
}
```

#### Get Datetime

This action is used to get the current Datetime in a specified format.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|format_string|string|%d %b %Y %H:%M:%S|True|Format string for the output|None|%d %b %Y %H:%M:%S|
|use_rfc3339_format|boolean|None|True|Use RFC3339 format (eg. 2017-10-24T18:27:36.23Z). This is the most compatible date format for timestamp manipulation. Enabling this will override the format string input|None|True|

Example input:

```
{
  "format_string": "%d %b %Y %H:%M:%S",
  "use_rfc3339_format": true
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|datetime|string|True|Datetime|
|epoch_timestamp|integer|True|Epoch timestamp|

Example output:

```

{
  "datetime": "2017-10-26T04:04:36.91Z",
  "epoch_timestamp": 1508990676
}

```

#### Subtract from Datetime

This action is used to subtract Datetime units from a Datetime.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|base_time|date|None|True|Datetime from which to subtract from|None|22 Jul 2020 21:20:33|
|days|integer|0|True|How many days to subtract from the specified Datetime|None|0|
|hours|integer|0|True|How many hours to subtract from the specified Datetime|None|0|
|minutes|integer|0|True|How many minutes to subtract from the specified Datetime|None|0|
|months|integer|0|True|How many months to subtract from the specified Datetime|None|0|
|seconds|integer|0|True|How many seconds to subtract from the specified Datetime|None|0|
|years|integer|0|True|How many years to subtract from the specified Datetime|None|0|

Example input:

```
{
  "base_time": "22 Jul 2020 21:20:33",
  "days": 0,
  "hours": 0,
  "minutes": 0,
  "months": 0,
  "seconds": 0,
  "years": 0
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|date|date|True|The Datetime after subtraction|

Example output:

```

{
  "date": "2015-08-13T13:21:10.42Z"
}

```

#### Add to Datetime

This action is used to add Datetime units to a Datetime.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|base_time|date|None|True|Datetime with which to add to|None|22 Jul 2020 21:20:33|
|days|integer|0|True|How many days to add to the specified Datetime|None|0|
|hours|integer|0|True|How many hours to add to the specified Datetime|None|0|
|minutes|integer|0|True|How many minutes to add to the specified Datetime|None|0|
|months|integer|0|True|How many months to add to the specified Datetime|None|0|
|seconds|integer|0|True|How many seconds to add to the specified Datetime|None|0|
|years|integer|0|True|How many years to add to the specified Datetime|None|0|

Example input:

```
{
  "base_time": "22 Jul 2020 21:20:33",
  "days": 0,
  "hours": 0,
  "minutes": 0,
  "months": 0,
  "seconds": 0,
  "years": 0
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|date|date|True|The Datetime after addition|

Example output:

```

{
  "date": "2015-08-13T13:21:10.42Z"
}

```

#### Date from Epoch

This action is used to convert an epoch as an integer to a Datetime.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|epoch|number|None|True|Epoch as integer or float|None|1595452833|

Example input:

```
{
  "epoch": 1595452833
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|date|date|True|Datetime after epoch conversion|

Example output:

```

{
  "date": "2017-11-14T21:07:53.00Z"
}

```

#### Epoch from Date

This action is used to convert a Datetime to an epoch.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|datetime|date|None|True|Date in RFC3339 format|None|22 Jul 2020 21:09:09|

Example input:

```
{
  "datetime": "22 Jul 2020 21:09:09"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|epoch|integer|True|Epoch after conversion|

Example output:

```

{
  "epoch": 1521045250
}

```

#### Time Elapsed

This action is used to find the difference between two Datetime inputs.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|first_time|date|None|True|First date|None|2020-07-22 21:20:33|
|result_unit|string|None|True|Time unit of measurement for result|['Years', 'Months', 'Days', 'Hours', 'Minutes', 'Seconds']|Years|
|second_time|date|None|True|Second date|None|2022-07-22 21:20:33|

Example input:

```
{
  "first_time": "2020-07-22T21:20:33.0Z",
  "result_unit": "Years",
  "second_time": "2022-07-22T21:20:33.0Z"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|difference|integer|True|Quantity of time difference|
|time_unit|string|True|Time unit of measurement|

Example output:

```

{
  "difference": 4
  "unit": "Months"
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 2.2.0 - Add new action Get Future Time
* 2.1.1 - Update to latest plugin runtime with support for gevent worker class
* 2.1.0 - New actions To UTC and To Localtime
* 2.0.6 - Update to v4 Python plugin runtime
* 2.0.5 - New spec and help.md format for the Extension Library | Changed const string in params.get to Input constants | Update to use the `komand/python-3-37-slim-plugin:3` Docker image to reduce plugin size
* 2.0.4 - Update plugin tag from `utility` to `utilities` for Marketplace searchability
* 2.0.3 - Fixed issue where connection test failed
* 2.0.2 - Fixed issue where action Date from Epoch will not accept floats
* 2.0.1 - Fixed issue where action Epoch from Date may return a float and not an integer
* 2.0.0 - Bug fix for epoch type
* 1.0.0 - Add action: Time Elapsed | Support web server mode
* 0.5.0 - Add action: Epoch from Date
* 0.4.1 - Bug fix for CI tool incorrectly uploading plugins
* 0.4.0 - Add action: Date from Epoch
* 0.3.1 - SSL bug fix in SDK
* 0.3.0 - Update Get Datetime: Add output for epoch timestamp
* 0.2.1 - Update Get Datetime: Add option to output in RFC3339 format for greater compatibility
* 0.2.0 - Add actions: Add to Datetime, Subtract from Datetime
* 0.1.0 - Initial plugin

# Links

## References

* [Python Time](https://docs.python.org/3/library/time.html#time.strftime)

