# Description

[Craigslist](https://www.craigslist.org/) provides local classifieds and forums for jobs, housing, for
  sale, personals, services, local community, and events. Using the Craigslist plugin for Rapid7 InsightConnect,
organizations can monitor their brand as well as automate searches for lost or stolen assets.

# Key Features

* Monitor the For Sale section

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Search for Sale

This action is used to search the for sale section.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|category|string|None|True|Craigslist sales category|['antiques', 'appliances', 'arts+crafts', 'atv/utv/sno', 'auto parts', 'baby+kids', 'barter', 'beauty+hlth', 'bikes', 'boats', 'books', 'business', 'cars+trucks', 'cds/dvd/vhs', 'cell phones', 'clothes+acc', 'collectibles', 'computers', 'electronics', 'farm+garden', 'free', 'furniture', 'garage sale', 'general', 'heavy equip', 'household', 'jewelry', 'materials', 'motorcycles', 'music instr', 'photo+video', 'rvs+camp', 'sporting', 'tickets', 'tools', 'toys+games', 'trailers', 'video gaming', 'wanted']|
|has_image|boolean|False|False|Posting contains an image|None|
|posted_today|boolean|False|False|Is posted today|None|
|query|string|None|False|Query string|None|
|search_distance|integer|None|False|Search distance in miles|None|
|search_titles|boolean|False|False|Search the titles|None|
|section_filter|object|None|False|Craigslist has specific filters for each category. You can fine tune your search by entering a section specific filter as JSON e.g. { "max_price": 5000, "auto_size": "compact", "auto_paint": "blue" }|None|
|site|string|None|True|Craigslist site location|['columbusga', 'monterey', 'buenosaires', 'cincinnati', 'guelph', 'kamloops', 'merced', 'nottingham', 'brantford', 'stgeorge', 'roanoke', 'oslo', 'venice', 'lille', 'bismarck', 'farmington', 'wyoming', 'kootenays', 'sanantonio', 'pampanga', 'curitiba', 'columbiamo', 'appleton', 'delhi', 'chennai', 'sherbrooke', 'tulsa', 'wausa,', 'nanaimo', 'muskegon', 'southjersey', 'dothan', 'limaohio', 'syracuse', 'pueblo', 'norfolk', 'brisbane', 'puebla', 'cenla', 'alicante', 'plattsburgh', 'mumbai', 'bozeman', 'mattoon', 'cfl', 'siouxcity', 'lascruces', 'panamacity', 'quebec', 'rouen', 'copenhagen', 'augusta', 'princegeorge', 'newjersey', 'panama', 'rockies', 'greenville', 'annarbor', 'richmond', 'taipei', 'northmiss', 'fortlauderdale', 'racine', 'canarias', 'siouxfalls', 'harrisonburg', 'sarasota', 'capetown', 'guangzho,', 'okinawa', 'wuhan', 'leeds', 'hobart', 'newlondon', 'morgantown', 'chongqing', 'ukraine', 'bakersfield', 'spokane', 'juarez', 'lucknow', 'grandforks', 'dublin', 'elpaso', 'hiroshima', 'paris', 'christchurch', 'derby', 'capecod', 'brownsville', 'saguenay', 'shanghai', 'stockton', 'montpellier', 'sicily', 'nanjing', 'lima', 'florence', 'monterrey', 'onslow', 'battlecreek', 'quadcities', 'territories', 'eastmids', 'calgary', 'corvallis', 'brunswick', 'sarnia', 'wenatchee', 'centralmich', 'tuscarawas', 'glensfalls', 'asheville', 'mansfield', 'saltlakecity', 'ahmedabad', 'tampa', 'rockford', 'visalia', 'siskiyo,', 'salvador', 'tokyo', 'sanangelo', 'blacksburg', 'delrio', 'lakecharles', 'montevideo', 'westky', 'pretoria', 'newfoundland', 'beijing', 'texarkana', 'norwich', 'niagara', 'bend', 'acapulco', 'athensga', 'newhaven', 'csd', 'torino', 'hampshire', 'showlow', 'louisville', 'catskills', 'vancouver', 'kolkata', 'inlandempire', 'chillicothe', 'springfield', 'bajasur', 'edinburgh', 'seoul', 'mankato', 'faro', 'goldcoast', 'sardinia', 'swks', 'charleston', 'billings', 'southcoast', 'joplin', 'mendocino', 'hannover', 'killeen', 'guatemala', 'corpuschristi', 'sendai', 'lubbock', 'tijuana', 'yubasutter', 'sd', 'galveston', 'houston', 'tallahassee', 'casablanca', 'canberra', 'fresno', 'beaumont', 'washingtondc', 'auburn', 'helena', 'logan', 'modesto', 'milwaukee', 'sapporo', 'chihuahua', 'thumb', 'fairbanks', 'oneonta', 'denver', 'klamath', 'winnipeg', 'charlottesville', 'portoalegre', 'meridian', 'eugene', 'poconos', 'manila', 'zagreb', 'myrtlebeach', 'stcloud', 'harrisburg', 'stjoseph', 'oxford', 'bath', 'porto', 'kpr', 'susanville', 'hickory', 'yellowknife', 'missoula', 'detroit', 'eastky', 'saopaulo', 'stockholm', 'surat', 'rennes', 'redding', 'genoa', 'medford', 'zurich', 'cairo', 'osaka', 'milan', 'portland', 'eastnc', 'albanyga', 'hongkong', 'jerusalem', 'jackson', 'fortsmith', 'goldcountry', 'kuwait', 'texoma', 'pensacola', 'goa', 'hangzho,', 'mazatlan', 'terrehaute', 'kent', 'bacolod', 'fargo', 'smd', 'florencesc', 'quito', 'durban', 'lawrence', 'sfbay', 'sheffield', 'albuquerque', 'york', 'shreveport', 'scottsbluff', 'chatham', 'lynchburg', 'pune', 'desmoines', 'waterloo', 'cadiz', 'dunedin', 'bilbao', 'belleville', 'raleigh', 'cotedazur', 'santamaria', 'lewiston', 'austin', 'lasalle', 'macon', 'hyderabad', 'toulouse', 'humboldt', 'neworleans', 'roswell', 'bham', 'shenyang', 'olympic', 'colombia', 'cedarrapids', 'enid', 'gulfport', 'strasbourg', 'guanajuato', 'bologna', 'sandusky', 'charlestonwv', 'danville', 'muncie', 'geneva', 'pittsburgh', 'peoria', 'vermont', 'cornwall', 'hartford', 'honolul,', 'valencia', 'tehran', 'eauclaire', 'rapidcity', 'malaga', 'toronto', 'evansville', 'holland', 'richmondin', 'helsinki', 'youngstown', 'ventura', 'lausanne', 'tunis', 'prescott', 'vienna', 'charlotte', 'dalian', 'costarica', 'boston', 'sevilla', 'shoals', 'worcester', 'reno', 'wellington', 'tuscaloosa', 'junea,', 'jaipur', 'windsor', 'brighton', 'warsaw', 'rochester', 'abilene', 'parkersburg', 'wichitafalls', 'martinsburg', 'montgomery', 'eastco', 'clovis', 'beirut', 'yakima', 'santafe', 'santiago', 'dayton', 'victoria', 'liverpool', 'montana', 'littlerock', 'owensound', 'haifa', 'omaha', 'gadsden', 'mobile', 'hanford', 'seks', 'chicago', 'frederick', 'kaiserslautern', 'lakecity', 'istanbul', 'bordeaux', 'loire', 'madison', 'bellingham', 'cdo', 'victoriatx', 'manchester', 'nagoya', 'naga', 'baleares', 'westmd', 'maine', 'staugustine', 'ks,', 'ceb,', 'greenbay', 'treasure', 'basel', 'cookeville', 'lansing', 'perugia', 'darwin', 'boulder', 'ftmcmurray', 'palmsprings', 'baghdad', 'fayar', 'nwga', 'lethbridge', 'budapest', 'wilmington', 'lexington', 'kirksville', 'london', 'recife', 'wheeling', 'kitchener', 'bulgaria', 'kalamazoo', 'twintiers', 'reykjavik', 'prague', 'cologne', 'cairns', 'longisland', 'lisbon', 'roseburg', 'rmn', 'fortdodge', 'hattiesburg', 'lancaster', 'lyon', 'ocala', 'knoxville', 'londonon', 'dundee', 'newyork', 'toledo', 'reading', 'glasgow', 'yuma', 'losangeles', 'stlouis', 'nashville', 'boise', 'wv', 'akroncanton', 'grandrapids', 'butte', 'ames', 'bangkok', 'indore', 'winchester', 'leipzig', 'saskatoon', 'ntl', 'stuttgart', 'bristol', 'statesboro', 'lawton', 'hiltonhead', 'baltimore', 'pakistan', 'westslope', 'moscow', 'owensboro', 'meadville', 'masoncity', 'santodomingo', 'kerala', 'pv', 'reddeer', 'kokomo', 'hamilton', 'sierravista', 'fortaleza', 'bhubaneswar', 'naples', 'ramallah', 'odessa', 'chandigarh', 'kingston', 'huntsville', 'sunshine', 'nwct', 'williamsport', 'hamburg', 'atlanta', 'stillwater', 'sandiego', 'oklahomacity', 'coventry', 'brasilia', 'mohave', 'valdosta', 'natchez', 'bemidji', 'addisababa', 'slo', 'northplatte', 'xian', 'elmira', 'rio', 'barcelona', 'kenya', 'seattle', 'monroe', 'outerbanks', 'albany', 'salina', 'kelowna', 'managua', 'kalispell', 'comoxvalley', 'annapolis', 'guadalajara', 'zamboanga', 'jacksontn', 'bigbend', 'utica', 'ashtabula', 'carbondale', 'adelaide', 'chautauqua', 'indianapolis', 'columbia', 'singapore', 'zanesville', 'keys', 'sacramento', 'houma', 'sheboygan', 'nesd', 'brussels', 'caracas', 'lacrosse', 'chattanooga', 'daytona', 'dallas', 'iowacity', 'porthuron', 'rome', 'montreal', 'flint', 'ottumwa', 'aberdeen', 'savannah', 'nd', 'edmonton', 'winstonsalem', 'abbotsford', 'birmingham', 'hermosillo', 'auckland', 'mcallen', 'ithaca', 'belfast', 'fortwayne', 'fukuoka', 'clarksville', 'micronesia', 'newbrunswick', 'santabarbara', 'perth', 'cosprings', 'sydney', 'hat', 'heidelberg', 'springfieldil', 'grandisland', 'chambersburg', 'dubai', 'munich', 'amarillo', 'newcastle', 'jonesboro', 'grenoble', 'jacksonville', 'davaocity', 'semo', 'lincoln', 'moseslake', 'saginaw', 'miami', 'orlando', 'dusseldorf', 'johannesburg', 'veracruz', 'duluth', 'oaxaca', 'accra', 'jxn', 'chico', 'bucharest', 'brainerd', 'madrid', 'elko', 'malaysia', 'altoona', 'athens', 'lapaz', 'cleveland', 'halifax', 'batonrouge', 'regina', 'wollongong', 'delaware', 'luxembourg', 'marseilles', 'whitehorse', 'providence', 'caribbean', 'pei', 'cnj', 'columbus', 'dresden', 'bgky', 'bn', 'swva', 'northernwi', 'binghamton', 'barrie', 'bangalore', 'decatur', 'nmi', 'anchorage', 'collegestation', 'sanmarcos', 'melbourne', 'topeka', 'whistler', 'greatfalls', 'fingerlakes', 'greensboro', 'skagit', 'fortcollins', 'cambridge', 'chengd,', 'marshall', 'fredericksburg', 'essex', 'soo', 'provo', 'cardiff', 'amsterdam', 'essen', 'pullman', 'twinfalls', 'kansascity', 'nwks', 'bangladesh', 'waco', 'chambana', 'philadelphia', 'imperial', 'virgin', 'stpetersburg', 'tippecanoe', 'loz', 'bloomington', 'lasvegas', 'mexicocity', 'laredo', 'athensohio', 'monroemi', 'easttexas', 'troisrivieres', 'iloilo', 'swmi', 'bern', 'memphis', 'flagstaff', 'nuremberg', 'cariboo', 'skeena', 'jerseyshore', 'up', 'puertorico', 'tucson', 'jakarta', 'swv', 'ogden', 'sudbury', 'southbend', 'okaloosa', 'wichita', 'janesville', 'minneapolis', 'belohorizonte', 'salem', 'ottawa', 'erie', 'hudsonvalley', 'huntington', 'eastidaho', 'nh', 'pennstate', 'granada', 'peterborough', 'elsalvador', 'allentown', 'peace', 'gainesville', 'bremen', 'telaviv', 'potsdam', 'thunderbay', 'yucatan', 'easternshore', 'shenzhen', 'nacogdoches', 'phoenix', 'dubuque', 'devon', 'eastoregon', 'kenai', 'quincy', 'orangecounty', 'fortmyers', 'westernmass', 'scranton', 'frankfurt', 'lakeland', 'berlin', 'spacecoast', 'watertown', 'vietnam', 'lafayette', 'boone', 'oregoncoast', 'fayetteville', 'tricities', 'buffalo']|
|zip_code|integer|None|False|Zipcode|None|

Example input:

```
{
    "category": "music instr",
    "has_image": true,
    "posted_today": false,
    "query": "amp",
    "search_distance": 20,
    "search_titles": true,
    "section_filter": {},
    "site": "bn",
    "zip_code": 61736
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sale_posting|[]sale_posting|False|Item posting information|

Example output:

```
{
  "sale_posting": [
    {
      "datetime": "2020-03-29 08:32",
      "geotag": "N/A",
      "has_image": true,
      "id": "7095410530",
      "last_updated": "2020-03-29 08:32",
      "name": "1965 Ampeg Gemini I amp",
      "price": "$0",
      "repost_of": "7072730013",
      "url": "https://bn.craigslist.org/msg/d/bloomington-1965-ampeg-gemini-amp/7095410530.html",
      "where": "N/A"
    },
    {
      "datetime": "2020-03-29 08:32",
      "geotag": "N/A",
      "has_image": true,
      "id": "7095412414",
      "last_updated": "2020-03-29 08:32",
      "name": "Victoria 35310 Tweed Bandmaster amp",
      "price": "$0",
      "repost_of": "7072561348",
      "url": "https://bn.craigslist.org/msg/d/bloomington-victoria-tweed-bandmaster/7095412414.html",
      "where": "N/A"
    },
    {
      "datetime": "2020-03-29 08:26",
      "geotag": "N/A",
      "has_image": true,
      "id": "7084092503",
      "last_updated": "2020-03-29 08:26",
      "name": "Vintage Fender Bronco amp (aka Vibro Champ)",
      "price": "$550",
      "repost_of": "7060256964",
      "url": "https://bn.craigslist.org/msg/d/bloomington-vintage-fender-bronco-amp/7084092503.html",
      "where": "N/A"
    },
    {
      "datetime": "2020-02-22 20:15",
      "geotag": "N/A",
      "has_image": true,
      "id": "7080659514",
      "last_updated": "2020-02-22 20:15",
      "name": "Cube amp",
      "price": "$40",
      "repost_of": "N/A",
      "url": "https://bn.craigslist.org/msg/d/lexington-cube-amp/7080659514.html",
      "where": "Chenoa"
    }
  ]
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.2 - Change docker image from `komand/python-2-plugin:2` to `komand/python-3-37-slim-plugin:3` to reduce plugin image size | Use input and output constants | Added "f" strings | Add test | Add example input
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Craigslist](https://www.craigslist.org/)
* [python-craigslist](https://pypi.python.org/pypi/python-craigslist/1.0.4)

