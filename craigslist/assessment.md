## Assessment
### Run

<details>

```
{
  "body": {
    "log": "rapid7/Craigslist:1.0.2. Step name: for_sale\nFilter: {'search_titles': True, 'posted_today': False, 'has_image': True, 'query': 'amp', 'search_distance': 20, 'zip_code': 61736}\nTranslated category: msa\n",
    "meta": {},
    "output": {
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
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/craigslist:1.0.2 --debug run < tests/for_sale.json
</summary>
</details>

<details>

```
{
  "body": {
    "log": "rapid7/Craigslist:1.0.2. Step name: for_sale\nFilter: {'search_titles': True, 'posted_today': False, 'has_image': True, 'query': '', 'search_distance': 20, 'zip_code': 61736, 'condition': 'like new', 'max_price': 1000}\nTranslated category: msa\n",
    "meta": {},
    "output": {
      "sale_posting": [
        {
          "datetime": "2020-03-26 18:40",
          "geotag": "N/A",
          "has_image": true,
          "id": "7099430178",
          "last_updated": "2020-03-26 18:40",
          "name": "Trombone",
          "price": "$150",
          "repost_of": "6531130969",
          "url": "https://bn.craigslist.org/msg/d/bloomington-trombone/7099430178.html",
          "where": "N/A"
        },
        {
          "datetime": "2020-02-24 19:32",
          "geotag": "N/A",
          "has_image": true,
          "id": "7081832881",
          "last_updated": "2020-02-24 19:32",
          "name": "Used Piano",
          "price": "$100",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/bloomington-used-piano/7081832881.html",
          "where": "Bloomington"
        },
        {
          "datetime": "2020-03-28 20:38",
          "geotag": "N/A",
          "has_image": true,
          "id": "7100419875",
          "last_updated": "2020-03-28 20:38",
          "name": "Fender Squier J Bass",
          "price": "$200",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/normal-fender-squier-bass/7100419875.html",
          "where": "Bloomington"
        },
        {
          "datetime": "2020-02-22 00:38",
          "geotag": "N/A",
          "has_image": true,
          "id": "7080112670",
          "last_updated": "2020-02-22 00:38",
          "name": "Epiphone AJ Acoustic/Electric Guitar",
          "price": "$300",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/bloomington-epiphone-aj-acoustic/7080112670.html",
          "where": "N/A"
        },
        {
          "datetime": "2020-02-22 11:05",
          "geotag": "N/A",
          "has_image": true,
          "id": "7080308027",
          "last_updated": "2020-02-22 11:05",
          "name": "Direct Boxes",
          "price": "$10",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/bloomington-direct-boxes/7080308027.html",
          "where": "Bloomington"
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
          "datetime": "2020-03-29 08:27",
          "geotag": "N/A",
          "has_image": true,
          "id": "7086698426",
          "last_updated": "2020-03-29 08:27",
          "name": "Vintage Guild T100-DP Hollowbody (aka: the \"Slim Jim\")",
          "price": "$0",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/bloomington-vintage-guild-t100-dp/7086698426.html",
          "where": "N/A"
        },
        {
          "datetime": "2020-03-29 08:26",
          "geotag": "N/A",
          "has_image": true,
          "id": "7086706697",
          "last_updated": "2020-03-29 08:26",
          "name": "Gibson Les Pauls",
          "price": "$0",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/bloomington-gibson-les-pauls/7086706697.html",
          "where": "N/A"
        },
        {
          "datetime": "2020-03-06 09:56",
          "geotag": "N/A",
          "has_image": true,
          "id": "7088331015",
          "last_updated": "2020-03-06 09:56",
          "name": "Ultimate Support SP-100 Air-Powered Series Speaker Pole",
          "price": "$80",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/bloomington-ultimate-support-sp-100-air/7088331015.html",
          "where": "Bloomington"
        },
        {
          "datetime": "2020-03-29 08:28",
          "geotag": "N/A",
          "has_image": true,
          "id": "7090783945",
          "last_updated": "2020-03-29 08:28",
          "name": "Vintage Electro-Voice Mic Lot - nice harp mics!",
          "price": "$0",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/bloomington-vintage-electro-voice-mic/7090783945.html",
          "where": "N/A"
        },
        {
          "datetime": "2020-03-29 08:29",
          "geotag": "N/A",
          "has_image": true,
          "id": "7090792127",
          "last_updated": "2020-03-29 08:29",
          "name": "Vintage Hammond M-3 Tube Organ - the Baby B-3!",
          "price": "$150",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/bloomington-vintage-hammond-3-tube/7090792127.html",
          "where": "N/A"
        },
        {
          "datetime": "2020-03-14 14:24",
          "geotag": "N/A",
          "has_image": true,
          "id": "7093339051",
          "last_updated": "2020-03-14 14:24",
          "name": "Yamaha 6'1\" C3 Grand Piano",
          "price": "$0",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msd/d/bloomington-yamaha-61-c3-grand-piano/7093339051.html",
          "where": "Bloomington"
        },
        {
          "datetime": "2020-03-15 22:39",
          "geotag": "N/A",
          "has_image": true,
          "id": "7094044532",
          "last_updated": "2020-03-15 22:39",
          "name": "J. Reynolds Sunburst Strat w/bag",
          "price": "$100",
          "repost_of": "7065620600",
          "url": "https://bn.craigslist.org/msg/d/bloomington-reynolds-sunburst-strat-bag/7094044532.html",
          "where": "Bloomington"
        },
        {
          "datetime": "2020-03-29 08:29",
          "geotag": "N/A",
          "has_image": true,
          "id": "7095405297",
          "last_updated": "2020-03-29 08:29",
          "name": "Propellerhead Reason 10 Recording Software \u0026 Focusrite Plug Ins",
          "price": "$0",
          "repost_of": "7073376128",
          "url": "https://bn.craigslist.org/msg/d/bloomington-propellerhead-reason-10/7095405297.html",
          "where": "N/A"
        },
        {
          "datetime": "2020-03-29 08:42",
          "geotag": "N/A",
          "has_image": true,
          "id": "7095409370",
          "last_updated": "2020-03-29 08:42",
          "name": "The Loar LM-700 Mandolin, F5 copy, case \u0026 other upgrades",
          "price": "$0",
          "repost_of": "7073386675",
          "url": "https://bn.craigslist.org/msg/d/bloomington-the-loar-lm-700-mandolin-f5/7095409370.html",
          "where": "N/A"
        },
        {
          "datetime": "2020-03-29 08:31",
          "geotag": "N/A",
          "has_image": true,
          "id": "7095409530",
          "last_updated": "2020-03-29 08:31",
          "name": "Pedals Galore",
          "price": "$0",
          "repost_of": "7073364739",
          "url": "https://bn.craigslist.org/msg/d/bloomington-pedals-galore/7095409530.html",
          "where": "N/A"
        },
        {
          "datetime": "2020-03-29 08:31",
          "geotag": "N/A",
          "has_image": true,
          "id": "7095409642",
          "last_updated": "2020-03-29 08:31",
          "name": "Custom pedal board with vintage case",
          "price": "$50",
          "repost_of": "7073358944",
          "url": "https://bn.craigslist.org/msg/d/bloomington-custom-pedal-board-with/7095409642.html",
          "where": "N/A"
        },
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
          "datetime": "2020-03-29 08:33",
          "geotag": "N/A",
          "has_image": true,
          "id": "7097794603",
          "last_updated": "2020-03-29 08:33",
          "name": "Strymon Blue Sky Reverberator pedal",
          "price": "$255",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/bloomington-strymon-blue-sky/7097794603.html",
          "where": "N/A"
        },
        {
          "datetime": "2020-03-27 15:57",
          "geotag": "N/A",
          "has_image": true,
          "id": "7099839070",
          "last_updated": "2020-03-27 15:57",
          "name": "Phonic 15” 3-way PA speakers",
          "price": "$300",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/bloomington-phonic-15-3-way-pa-speakers/7099839070.html",
          "where": "N/A"
        },
        {
          "datetime": "2020-03-29 11:30",
          "geotag": "N/A",
          "has_image": true,
          "id": "7100587707",
          "last_updated": "2020-03-29 11:30",
          "name": "Ibanez PC15-VS Acoustic Guitar",
          "price": "$125",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/bloomington-ibanez-pc15-vs-acoustic/7100587707.html",
          "where": "N/A"
        },
        {
          "datetime": "2020-03-29 13:09",
          "geotag": "N/A",
          "has_image": true,
          "id": "7100636980",
          "last_updated": "2020-03-29 13:09",
          "name": "Epiphone Les Paul Custom Pro",
          "price": "$480",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/bloomington-epiphone-les-paul-custom-pro/7100636980.html",
          "where": "N/A"
        },
        {
          "datetime": "2020-03-29 14:23",
          "geotag": "N/A",
          "has_image": true,
          "id": "7100675309",
          "last_updated": "2020-03-29 14:23",
          "name": "Digitech Ventura Vibe Pedal",
          "price": "$80",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/bloomington-digitech-ventura-vibe-pedal/7100675309.html",
          "where": "N/A"
        },
        {
          "datetime": "2020-03-28 11:53",
          "geotag": "N/A",
          "has_image": true,
          "id": "7100167340",
          "last_updated": "2020-03-28 11:53",
          "name": "Drum Set",
          "price": "$300",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/bloomington-drum-set/7100167340.html",
          "where": "Bloomington"
        },
        {
          "datetime": "2020-02-21 14:18",
          "geotag": "N/A",
          "has_image": true,
          "id": "7079819011",
          "last_updated": "2020-02-21 14:18",
          "name": "Guitar pedals loopers, beat buddy",
          "price": "$1",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/bloomington-guitar-pedals-loopers-beat/7079819011.html",
          "where": "Bloomington,  Illinois"
        },
        {
          "datetime": "2020-03-14 13:58",
          "geotag": "N/A",
          "has_image": true,
          "id": "7093317130",
          "last_updated": "2020-03-14 13:58",
          "name": "Cecilio Violin with accessories",
          "price": "$200",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/farmer-city-cecilio-violin-with/7093317130.html",
          "where": "N/A"
        },
        {
          "datetime": "2020-03-10 12:58",
          "geotag": "N/A",
          "has_image": true,
          "id": "7076296554",
          "last_updated": "2020-03-10 12:58",
          "name": "2x12 Cabinet Celestion Greenback",
          "price": "$280",
          "repost_of": "7030327349",
          "url": "https://bn.craigslist.org/msg/d/normal-2x12-cabinet-celestion-greenback/7076296554.html",
          "where": "N/A"
        },
        {
          "datetime": "2020-02-16 06:30",
          "geotag": "N/A",
          "has_image": true,
          "id": "7076296643",
          "last_updated": "2020-02-16 06:30",
          "name": "Crest X20r rack mount mixer",
          "price": "$580",
          "repost_of": "7030338985",
          "url": "https://bn.craigslist.org/msg/d/normal-crest-x20r-rack-mount-mixer/7076296643.html",
          "where": "N/A"
        },
        {
          "datetime": "2020-02-21 13:17",
          "geotag": "N/A",
          "has_image": true,
          "id": "7079769093",
          "last_updated": "2020-02-21 13:17",
          "name": "Taylor GA3e-12 string guitar",
          "price": "$799",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/normal-taylor-ga3e-12-string-guitar/7079769093.html",
          "where": "N/A"
        },
        {
          "datetime": "2020-02-27 20:45",
          "geotag": "N/A",
          "has_image": true,
          "id": "7083777516",
          "last_updated": "2020-02-27 20:45",
          "name": "Antique upright piano",
          "price": "$1",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/normal-antique-upright-piano/7083777516.html",
          "where": "Normal"
        },
        {
          "datetime": "2020-02-29 14:13",
          "geotag": "N/A",
          "has_image": true,
          "id": "7084811896",
          "last_updated": "2020-02-29 14:13",
          "name": "Squier Standard Stratocaster Electric Guitar",
          "price": "$150",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/normal-squier-standard-stratocaster/7084811896.html",
          "where": "Normal"
        },
        {
          "datetime": "2020-03-14 13:00",
          "geotag": "N/A",
          "has_image": true,
          "id": "7093275365",
          "last_updated": "2020-03-14 13:00",
          "name": "Recording King RD-G6",
          "price": "$149",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/normal-recording-king-rd-g6/7093275365.html",
          "where": "N/A"
        },
        {
          "datetime": "2020-03-14 13:09",
          "geotag": "N/A",
          "has_image": true,
          "id": "7093282355",
          "last_updated": "2020-03-14 13:09",
          "name": "Kremona 3/4 size nylon string guitar",
          "price": "$199",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/normal-kremona-3-4-size-nylon-string/7093282355.html",
          "where": "N/A"
        },
        {
          "datetime": "2020-03-14 13:22",
          "geotag": "N/A",
          "has_image": true,
          "id": "7093292114",
          "last_updated": "2020-03-14 13:22",
          "name": "Eastman E1SS-LTD acoustic guitar",
          "price": "$899",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/normal-eastman-e1ss-ltd-acoustic-guitar/7093292114.html",
          "where": "N/A"
        },
        {
          "datetime": "2020-03-14 13:42",
          "geotag": "N/A",
          "has_image": true,
          "id": "7093306313",
          "last_updated": "2020-03-14 13:42",
          "name": "Short Mountain handmade acoustic guitar",
          "price": "$799",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/normal-short-mountain-handmade-acoustic/7093306313.html",
          "where": "N/A"
        },
        {
          "datetime": "2020-03-18 17:07",
          "geotag": "N/A",
          "has_image": true,
          "id": "7095520850",
          "last_updated": "2020-03-18 17:07",
          "name": "Yamaha oboe 211",
          "price": "$475",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/normal-yamaha-oboe-211/7095520850.html",
          "where": "Normal"
        },
        {
          "datetime": "2020-03-18 17:50",
          "geotag": "N/A",
          "has_image": true,
          "id": "7095541832",
          "last_updated": "2020-03-18 17:50",
          "name": "Buescher Aristocrat Alto Saxophone",
          "price": "$200",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/normal-buescher-aristocrat-alto/7095541832.html",
          "where": "Normal"
        },
        {
          "datetime": "2020-03-18 18:25",
          "geotag": "N/A",
          "has_image": true,
          "id": "7095557898",
          "last_updated": "2020-03-18 18:25",
          "name": "Yamaha Trumpet Ytr-2320",
          "price": "$95",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/normal-yamaha-trumpet-ytr-2320/7095557898.html",
          "where": "Normal"
        },
        {
          "datetime": "2020-03-20 16:08",
          "geotag": "N/A",
          "has_image": true,
          "id": "7096512246",
          "last_updated": "2020-03-20 16:08",
          "name": "Taylor Academy 12 acoustic guitar",
          "price": "$450",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/normal-taylor-academy-12-acoustic-guitar/7096512246.html",
          "where": "N/A"
        },
        {
          "datetime": "2020-03-27 12:04",
          "geotag": "N/A",
          "has_image": true,
          "id": "7097365682",
          "last_updated": "2020-03-27 12:04",
          "name": "Congas set of 3",
          "price": "$799",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/normal-congas-set-of-3/7097365682.html",
          "where": "Normal"
        },
        {
          "datetime": "2020-03-27 12:04",
          "geotag": "N/A",
          "has_image": true,
          "id": "7097372194",
          "last_updated": "2020-03-27 12:04",
          "name": "Gibraltar Drum Rack",
          "price": "$175",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/normal-gibraltar-drum-rack/7097372194.html",
          "where": "Normal"
        },
        {
          "datetime": "2020-03-27 12:04",
          "geotag": "N/A",
          "has_image": true,
          "id": "7097374673",
          "last_updated": "2020-03-27 12:04",
          "name": "LP Tito Puente Timbalites",
          "price": "$275",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/normal-lp-tito-puente-timbalites/7097374673.html",
          "where": "Normal"
        },
        {
          "datetime": "2020-03-27 12:04",
          "geotag": "N/A",
          "has_image": true,
          "id": "7097377194",
          "last_updated": "2020-03-27 12:04",
          "name": "Remo Tubanos",
          "price": "$300",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/normal-remo-tubanos/7097377194.html",
          "where": "Normal"
        },
        {
          "datetime": "2020-03-25 22:00",
          "geotag": "N/A",
          "has_image": true,
          "id": "7099013929",
          "last_updated": "2020-03-25 22:00",
          "name": "Huge selection of used Kawai \u0026 Yamaha upright pianos!",
          "price": "$0",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msd/d/normal-huge-selection-of-used-kawai/7099013929.html",
          "where": "Normal"
        },
        {
          "datetime": "2020-03-29 08:32",
          "geotag": "N/A",
          "has_image": true,
          "id": "7095412259",
          "last_updated": "2020-03-29 08:32",
          "name": "Vintage Kalamazoo amps - Model One \u0026 Model Two",
          "price": "$0",
          "repost_of": "7072571136",
          "url": "https://bn.craigslist.org/msg/d/bloomington-vintage-kalamazoo-amps/7095412259.html",
          "where": "N/A"
        },
        {
          "datetime": "2020-03-26 22:17",
          "geotag": "N/A",
          "has_image": true,
          "id": "7099496361",
          "last_updated": "2020-03-26 22:17",
          "name": "PDP hi-hat stand",
          "price": "$35",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/normal-pdp-hi-hat-stand/7099496361.html",
          "where": "Normal"
        },
        {
          "datetime": "2020-02-22 20:12",
          "geotag": "N/A",
          "has_image": true,
          "id": "7080658332",
          "last_updated": "2020-02-22 20:12",
          "name": "Prelude trumpet",
          "price": "$125",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/lexington-prelude-trumpet/7080658332.html",
          "where": "Chenoa"
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
        },
        {
          "datetime": "2020-03-28 22:19",
          "geotag": "N/A",
          "has_image": true,
          "id": "7094027683",
          "last_updated": "2020-03-28 22:19",
          "name": "Tama Bass Drum  with kick pedal",
          "price": "$60",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/clinton-tama-bass-drum-with-kick-pedal/7094027683.html",
          "where": "Clinton"
        },
        {
          "datetime": "2020-03-28 22:19",
          "geotag": "N/A",
          "has_image": true,
          "id": "7094028698",
          "last_updated": "2020-03-28 22:19",
          "name": "Pearl kick pedal and cymbal stand",
          "price": "$50",
          "repost_of": "N/A",
          "url": "https://bn.craigslist.org/msg/d/clinton-pearl-kick-pedal-and-cymbal/7094028698.html",
          "where": "Clinton"
        }
      ]
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/craigslist:1.0.2 --debug run < tests/for_sale_section_filter.json
</summary>
</details>

### Test

Autogenerate with:
<details>

```
{
  "body": {
    "log": "rapid7/Craigslist:1.0.2. Step name: for_sale\nSuccessful request to https://www.craigslist.org/about/\n",
    "meta": {},
    "output": {
      "success": "https://www.craigslist.org/about/"
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/craigslist:1.0.2 --debug test < tests/for_sale.json
</summary>
</details>

Autogenerate with:
<details>

```
{
  "body": {
    "log": "rapid7/Craigslist:1.0.2. Step name: for_sale\nSuccessful request to https://www.craigslist.org/about/\n",
    "meta": {},
    "output": {
      "success": "https://www.craigslist.org/about/"
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/craigslist:1.0.2 --debug test < tests/for_sale_section_filter.json
</summary>
</details>

Autogenerate with:
<details>

```
[*] Use ``make menu`` for available targets
[*] Including available Makefiles: ../tools/Makefiles/Helpers.mk ../tools/Makefiles/Colors.mk
--
[*] Running validators
[*] Validating plugin at .

[*] Running Integration Validators...
[*] Executing validator HelpValidator
[*] Executing validator ChangelogValidator
[*] Executing validator RequiredKeysValidator
[*] Executing validator UseCaseValidator
[*] Executing validator SpecPropertiesValidator
[*] Executing validator SpecVersionValidator
[*] Executing validator FilesValidator
[*] Executing validator TagValidator
[*] Executing validator DescriptionValidator
[*] Executing validator TitleValidator
[*] Executing validator VendorValidator
[*] Executing validator DefaultValueValidator
[*] Executing validator IconValidator
[*] Executing validator RequiredValidator
[*] Executing validator VersionValidator
[*] Executing validator DockerfileParentValidator
[*] Executing validator LoggingValidator
[*] Executing validator ProfanityValidator
Validator ProfanityValidator failed!
plugin.spec.yaml contains banned word: virgin.
[*] Executing validator AcronymValidator
[*] Executing validator JSONValidator
[*] Executing validator OutputValidator
[*] Executing validator RegenerationValidator
[*] Executing validator HelpInputOutputValidator
[*] Executing validator SupportValidator
[*]Plugin failed validation!

----
[*] Total time elapsed: 347.39599999999996ms

[*] Validating spec with js-yaml
[SUCCESS] Passes js-yaml spec check


[*] Validating markdown...
[SUCCESS] Passes markdown linting

[*] Validating python files for style...
[SUCCESS] Passes flake8 linting

[*] Validating python files for security vulnerabilities...
[main]  INFO    profile include tests: None
[main]  INFO    profile exclude tests: None
[main]  INFO    cli include tests: None
[main]  INFO    cli exclude tests: None
[main]  INFO    running on Python 3.7.6
Run started:2020-03-29 23:44:29.751527

Test results:
        No issues identified.

Code scanned:
        Total lines of code: 1058
        Total lines skipped (#nosec): 0

Run metrics:
        Total issues (by severity):
                Undefined: 0.0
                Low: 0.0
                Medium: 0.0
                High: 0.0
        Total issues (by confidence):
                Undefined: 0.0
                Low: 0.0
                Medium: 0.0
                High: 0.0
Files skipped (0):
[SUCCESS] Passes bandit security checks

```

<summary>
make validate
</summary>
</details>

Autogenerate with:
<details>

```
[*] Validating plugin with all validators at .

[*] Running Integration Validators...
[*] Executing validator HelpValidator
[*] Executing validator ChangelogValidator
[*] Executing validator RequiredKeysValidator
[*] Executing validator UseCaseValidator
[*] Executing validator SpecPropertiesValidator
[*] Executing validator SpecVersionValidator
[*] Executing validator FilesValidator
[*] Executing validator TagValidator
[*] Executing validator DescriptionValidator
[*] Executing validator TitleValidator
[*] Executing validator VendorValidator
[*] Executing validator DefaultValueValidator
[*] Executing validator IconValidator
[*] Executing validator RequiredValidator
[*] Executing validator VersionValidator
[*] Executing validator DockerfileParentValidator
[*] Executing validator LoggingValidator
[*] Executing validator ProfanityValidator
Validator ProfanityValidator failed!
plugin.spec.yaml contains banned word: virgin.
[*] Executing validator AcronymValidator
[*] Executing validator JSONValidator
[*] Executing validator OutputValidator
[*] Executing validator RegenerationValidator
[*] Executing validator HelpInputOutputValidator
[*] Executing validator SupportValidator
[*] Executing validator ExceptionValidator
[*] Executing validator CredentialsValidator
[*] Executing validator PasswordValidator
[*] Executing validator PrintValidator
[*] Executing validator ConfidentialValidator
[*] Executing validator DockerValidator
[*] Executing validator URLValidator
[*]Plugin failed validation!

----
[*] Total time elapsed: 14060.138ms

```

<summary>
icon-validate --all .
</summary>
</details>