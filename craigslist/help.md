# Description

[Craigslist](https://www.craigslist.com) is provides local classifieds and forums for jobs, housing, for sale, personals, services, local community, and events.
This plugin allows searching for sale postings on Craigslist.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Search For Sale

This action is used to search the for sale section.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|category|string|None|True|Craigslist sales category|['antiques', 'appliances', 'arts+crafts', 'atv/utv/sno', 'auto parts', 'baby+kids', 'barter', 'beauty+hlth', 'bikes', 'boats', 'books', 'business', 'cars+trucks', 'cds/dvd/vhs', 'cell phones', 'clothes+acc', 'collectibles', 'computers', 'electronics', 'farm+garden', 'free', 'furniture', 'garage sale', 'general', 'heavy equip', 'household', 'jewelry', 'materials', 'motorcycles', 'music instr', 'photo+video', 'rvs+camp', 'sporting', 'tickets', 'tools', 'toys+games', 'trailers', 'video gaming', 'wanted']|
|section_filter|object|None|False|Craigslist has specific filters for each category. You can fine tune your search by entering a section specific filter as JSON e.g. { "max_price"\: 5000, "auto_size"\: "compact", "auto_paint"\: "blue" }|None|
|search_titles|boolean|False|False|Search the titles?|None|
|site|string|None|True|Craigslist site location|['columbusga', 'monterey', 'buenosaires', 'cincinnati', 'guelph', 'kamloops', 'merced', 'nottingham', 'brantford', 'stgeorge', 'roanoke', 'oslo', 'venice', 'lille', 'bismarck', 'farmington', 'wyoming', 'kootenays', 'sanantonio', 'pampanga', 'curitiba', 'columbiamo', 'appleton', 'delhi', 'chennai', 'sherbrooke', 'tulsa', 'wausa,', 'nanaimo', 'muskegon', 'southjersey', 'dothan', 'limaohio', 'syracuse', 'pueblo', 'norfolk', 'brisbane', 'puebla', 'cenla', 'alicante', 'plattsburgh', 'mumbai', 'bozeman', 'mattoon', 'cfl', 'siouxcity', 'lascruces', 'panamacity', 'quebec', 'rouen', 'copenhagen', 'augusta', 'princegeorge', 'newjersey', 'panama', 'rockies', 'greenville', 'annarbor', 'richmond', 'taipei', 'northmiss', 'fortlauderdale', 'racine', 'canarias', 'siouxfalls', 'harrisonburg', 'sarasota', 'capetown', 'guangzho,', 'okinawa', 'wuhan', 'leeds', 'hobart', 'newlondon', 'morgantown', 'chongqing', 'ukraine', 'bakersfield', 'spokane', 'juarez', 'lucknow', 'grandforks', 'dublin', 'elpaso', 'hiroshima', 'paris', 'christchurch', 'derby', 'capecod', 'brownsville', 'saguenay', 'shanghai', 'stockton', 'montpellier', 'sicily', 'nanjing', 'lima', 'florence', 'monterrey', 'onslow', 'battlecreek', 'quadcities', 'territories', 'eastmids', 'calgary', 'corvallis', 'brunswick', 'sarnia', 'wenatchee', 'centralmich', 'tuscarawas', 'glensfalls', 'asheville', 'mansfield', 'saltlakecity', 'ahmedabad', 'tampa', 'rockford', 'visalia', 'siskiyo,', 'salvador', 'tokyo', 'sanangelo', 'blacksburg', 'delrio', 'lakecharles', 'montevideo', 'westky', 'pretoria', 'newfoundland', 'beijing', 'texarkana', 'norwich', 'niagara', 'bend', 'acapulco', 'athensga', 'newhaven', 'csd', 'torino', 'hampshire', 'showlow', 'louisville', 'catskills', 'vancouver', 'kolkata', 'inlandempire', 'chillicothe', 'springfield', 'bajasur', 'edinburgh', 'seoul', 'mankato', 'faro', 'goldcoast', 'sardinia', 'swks', 'charleston', 'billings', 'southcoast', 'joplin', 'mendocino', 'hannover', 'killeen', 'guatemala', 'corpuschristi', 'sendai', 'lubbock', 'tijuana', 'yubasutter', 'sd', 'galveston', 'houston', 'tallahassee', 'casablanca', 'canberra', 'fresno', 'beaumont', 'washingtondc', 'auburn', 'helena', 'logan', 'modesto', 'milwaukee', 'sapporo', 'chihuahua', 'thumb', 'fairbanks', 'oneonta', 'denver', 'klamath', 'winnipeg', 'charlottesville', 'portoalegre', 'meridian', 'eugene', 'poconos', 'manila', 'zagreb', 'myrtlebeach', 'stcloud', 'harrisburg', 'stjoseph', 'oxford', 'bath', 'porto', 'kpr', 'susanville', 'hickory', 'yellowknife', 'missoula', 'detroit', 'eastky', 'saopaulo', 'stockholm', 'surat', 'rennes', 'redding', 'genoa', 'medford', 'zurich', 'cairo', 'osaka', 'milan', 'portland', 'eastnc', 'albanyga', 'hongkong', 'jerusalem', 'jackson', 'fortsmith', 'goldcountry', 'kuwait', 'texoma', 'pensacola', 'goa', 'hangzho,', 'mazatlan', 'terrehaute', 'kent', 'bacolod', 'fargo', 'smd', 'florencesc', 'quito', 'durban', 'lawrence', 'sfbay', 'sheffield', 'albuquerque', 'york', 'shreveport', 'scottsbluff', 'chatham', 'lynchburg', 'pune', 'desmoines', 'waterloo', 'cadiz', 'dunedin', 'bilbao', 'belleville', 'raleigh', 'cotedazur', 'santamaria', 'lewiston', 'austin', 'lasalle', 'macon', 'hyderabad', 'toulouse', 'humboldt', 'neworleans', 'roswell', 'bham', 'shenyang', 'olympic', 'colombia', 'cedarrapids', 'enid', 'gulfport', 'strasbourg', 'guanajuato', 'bologna', 'sandusky', 'charlestonwv', 'danville', 'muncie', 'geneva', 'pittsburgh', 'peoria', 'vermont', 'cornwall', 'hartford', 'honolul,', 'valencia', 'tehran', 'eauclaire', 'rapidcity', 'malaga', 'toronto', 'evansville', 'holland', 'richmondin', 'helsinki', 'youngstown', 'ventura', 'lausanne', 'tunis', 'prescott', 'vienna', 'charlotte', 'dalian', 'costarica', 'boston', 'sevilla', 'shoals', 'worcester', 'reno', 'wellington', 'tuscaloosa', 'junea,', 'jaipur', 'windsor', 'brighton', 'warsaw', 'rochester', 'abilene', 'parkersburg', 'wichitafalls', 'martinsburg', 'montgomery', 'eastco', 'clovis', 'beirut', 'yakima', 'santafe', 'santiago', 'dayton', 'victoria', 'liverpool', 'montana', 'littlerock', 'owensound', 'haifa', 'omaha', 'gadsden', 'mobile', 'hanford', 'seks', 'chicago', 'frederick', 'kaiserslautern', 'lakecity', 'istanbul', 'bordeaux', 'loire', 'madison', 'bellingham', 'cdo', 'victoriatx', 'manchester', 'nagoya', 'naga', 'baleares', 'westmd', 'maine', 'staugustine', 'ks,', 'ceb,', 'greenbay', 'treasure', 'basel', 'cookeville', 'lansing', 'perugia', 'darwin', 'boulder', 'ftmcmurray', 'palmsprings', 'baghdad', 'fayar', 'nwga', 'lethbridge', 'budapest', 'wilmington', 'lexington', 'kirksville', 'london', 'recife', 'wheeling', 'kitchener', 'bulgaria', 'kalamazoo', 'twintiers', 'reykjavik', 'prague', 'cologne', 'cairns', 'longisland', 'lisbon', 'roseburg', 'rmn', 'fortdodge', 'hattiesburg', 'lancaster', 'lyon', 'ocala', 'knoxville', 'londonon', 'dundee', 'newyork', 'toledo', 'reading', 'glasgow', 'yuma', 'losangeles', 'stlouis', 'nashville', 'boise', 'wv', 'akroncanton', 'grandrapids', 'butte', 'ames', 'bangkok', 'indore', 'winchester', 'leipzig', 'saskatoon', 'ntl', 'stuttgart', 'bristol', 'statesboro', 'lawton', 'hiltonhead', 'baltimore', 'pakistan', 'westslope', 'moscow', 'owensboro', 'meadville', 'masoncity', 'santodomingo', 'kerala', 'pv', 'reddeer', 'kokomo', 'hamilton', 'sierravista', 'fortaleza', 'bhubaneswar', 'naples', 'ramallah', 'odessa', 'chandigarh', 'kingston', 'huntsville', 'sunshine', 'nwct', 'williamsport', 'hamburg', 'atlanta', 'stillwater', 'sandiego', 'oklahomacity', 'coventry', 'brasilia', 'mohave', 'valdosta', 'natchez', 'bemidji', 'addisababa', 'slo', 'northplatte', 'xian', 'elmira', 'rio', 'barcelona', 'kenya', 'seattle', 'monroe', 'outerbanks', 'albany', 'salina', 'kelowna', 'managua', 'kalispell', 'comoxvalley', 'annapolis', 'guadalajara', 'zamboanga', 'jacksontn', 'bigbend', 'utica', 'ashtabula', 'carbondale', 'adelaide', 'chautauqua', 'indianapolis', 'columbia', 'singapore', 'zanesville', 'keys', 'sacramento', 'houma', 'sheboygan', 'nesd', 'brussels', 'caracas', 'lacrosse', 'chattanooga', 'daytona', 'dallas', 'iowacity', 'porthuron', 'rome', 'montreal', 'flint', 'ottumwa', 'aberdeen', 'savannah', 'nd', 'edmonton', 'winstonsalem', 'abbotsford', 'birmingham', 'hermosillo', 'auckland', 'mcallen', 'ithaca', 'belfast', 'fortwayne', 'fukuoka', 'clarksville', 'micronesia', 'newbrunswick', 'santabarbara', 'perth', 'cosprings', 'sydney', 'hat', 'heidelberg', 'springfieldil', 'grandisland', 'chambersburg', 'dubai', 'munich', 'amarillo', 'newcastle', 'jonesboro', 'grenoble', 'jacksonville', 'davaocity', 'semo', 'lincoln', 'moseslake', 'saginaw', 'miami', 'orlando', 'dusseldorf', 'johannesburg', 'veracruz', 'duluth', 'oaxaca', 'accra', 'jxn', 'chico', 'bucharest', 'brainerd', 'madrid', 'elko', 'malaysia', 'altoona', 'athens', 'lapaz', 'cleveland', 'halifax', 'batonrouge', 'regina', 'wollongong', 'delaware', 'luxembourg', 'marseilles', 'whitehorse', 'providence', 'caribbean', 'pei', 'cnj', 'columbus', 'dresden', 'bgky', 'bn', 'swva', 'northernwi', 'binghamton', 'barrie', 'bangalore', 'decatur', 'nmi', 'anchorage', 'collegestation', 'sanmarcos', 'melbourne', 'topeka', 'whistler', 'greatfalls', 'fingerlakes', 'greensboro', 'skagit', 'fortcollins', 'cambridge', 'chengd,', 'marshall', 'fredericksburg', 'essex', 'soo', 'provo', 'cardiff', 'amsterdam', 'essen', 'pullman', 'twinfalls', 'kansascity', 'nwks', 'bangladesh', 'waco', 'chambana', 'philadelphia', 'imperial', 'virgin', 'stpetersburg', 'tippecanoe', 'loz', 'bloomington', 'lasvegas', 'mexicocity', 'laredo', 'athensohio', 'monroemi', 'easttexas', 'troisrivieres', 'iloilo', 'swmi', 'bern', 'memphis', 'flagstaff', 'nuremberg', 'cariboo', 'skeena', 'jerseyshore', 'up', 'puertorico', 'tucson', 'jakarta', 'swv', 'ogden', 'sudbury', 'southbend', 'okaloosa', 'wichita', 'janesville', 'minneapolis', 'belohorizonte', 'salem', 'ottawa', 'erie', 'hudsonvalley', 'huntington', 'eastidaho', 'nh', 'pennstate', 'granada', 'peterborough', 'elsalvador', 'allentown', 'peace', 'gainesville', 'bremen', 'telaviv', 'potsdam', 'thunderbay', 'yucatan', 'easternshore', 'shenzhen', 'nacogdoches', 'phoenix', 'dubuque', 'devon', 'eastoregon', 'kenai', 'quincy', 'orangecounty', 'fortmyers', 'westernmass', 'scranton', 'frankfurt', 'lakeland', 'berlin', 'spacecoast', 'watertown', 'vietnam', 'lafayette', 'boone', 'oregoncoast', 'fayetteville', 'tricities', 'buffalo']|
|posted_today|boolean|False|False|Posted today?|None|
|has_image|boolean|False|False|Posting contains an image|None|
|query|string|None|False|Query string|None|
|search_distance|integer|None|False|Search distance in miles|None|
|zip_code|integer|None|False|Zipcode|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sale_posting|[]sale_posting|False|Item posting information|

Example output:

```

{
  "sale_posting": [
    {
      "name": "Marshall Half Stack MG100HCFX Guitar Amplifier Amp",
      "has_image": true,
      "url": "http://bn.craigslist.org/msg/d/marshall-half-stack-mg100hcfx/6294231281.html",
      "has_map": true,
      "price": "$400",
      "geotag": "N/A",
      "where": "Normal",
      "id": "6294231281",
      "datetime": "2017-09-05 14:58"
    },
    {
      "name": "Fender Pro Junior III - 15 Watt Tube Amp",
      "has_image": true,
      "url": "http://bn.craigslist.org/msg/d/fender-pro-junior-iii-15-watt/6243112613.html",
      "has_map": true,
      "price": "$260",
      "geotag": "N/A",
      "where": "N/A",
      "id": "6243112613",
      "datetime": "2017-08-25 12:56"
    },
    ...
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Craigslist](https://www.craigslist.org)
* [python-craigslist](https://pypi.python.org/pypi/python-craigslist/1.0.4)

