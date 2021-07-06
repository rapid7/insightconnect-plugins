com = {
    'extend': None,

    'domain_name': r'Domain Name:\s?(.+)',
    'registrar': r'Registrar:\s?(.+)',
    'registrant': r'Registrant:?\s{0,}(?:[^\n][\n]?){0,}?\s{0,}Name(?:[^:]{0,}):\s?(.+)',
    'registrant_cc': r'Registrant:?\s{0,}(?:[^\n][\n]?){0,}?\s{0,}Country(?:[^:]{0,}):\s?(.+)',

    'creation_date': r'Creation Date:\s?(.+)',
    'expiration_date': r'Expiration Date:\n|Expiration Date:\s?(.+)',
    'updated_date': r'Updated Date:\s?(.+)',

    'name_servers': r'Name Server:\s*(.+)\s*',
    'status': r'Status:\s?(.+)',
    'emails': r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    # Komand additions
    'registry_domain_id': r'Registry Domain ID:\s?(.+)',
    'registrar_whois_server': r'Registrar WHOIS Server:\s?(.+)',
    'registrar_url': r'Registrar URL:\s?(.+)',
    'registrar_iana_id': r'Registrar IANA ID:\s(.+)',
    'registrar_abuse_contact_email': r'Registrar Abuse Contact Email:\s(.+)',
    'registrar_abuse_contact_phone': r'Registrar Abuse Contact Phone:\s(.+)',
    'domain_status': r'Domain Status:\s(.+)',
    'dnssec': r'DNSSEC:\s(.+)'
}

net = {
    'extend': 'com',
}

org = {
    'extend': 'com',

    'creation_date': r'Creat(?:ed On|ion Date):\s?(.+)',
    'expiration_date': r'(?:Registry\s)?Expir(?:y|ation) Date:\s?(.+)',
    'updated_date': r'(?:Last\s)?Updated (?:On|Date):\s?(.+)',

    'registrar': r'(?:Registrar|Sponsoring Registrar):\s?(.+)',
    'registrant': r'Registrant Organization:\s?(.+)',

    'status': r'Status:\s?(.+)',
}

uk = {
    'extend': 'com',

    'registrant': r'Registrant:\n\s*(.+)',
    'registrant_cc': r'Registrant\'s address:\s+(?:[^\n][\n]?)+\n(.+)\n\n',

    'creation_date': r'Registered on:\s?(.+)',
    'expiration_date': r'Expiry date: \s?(.+)',
    'updated_date': r'Last updated:\s*(.+)',

    'name_servers': r'Name servers:\n?(.+)\n?(.+)\n?(.+)\n?(.+)',
    'status': r'Registration status:\n\s*(.+)',
}

pl = {
    'extend': 'uk',

    'registrant_cc' : r'location:\s?(.+)',
    'creation_date': r'\ncreated:\s*(.+)\n',
    'updated_date': r'\nlast modified:\s*(.+)\n',
    'expiration_date': r'\noption expiration date:\s*(.+)\n',

    'name_servers': r'\nnameservers:\s*(.+)\n\s*(.+)\n',
    'status': r'\nStatus:\n\s*(.+)',
}

ru = {
    'extend': 'com',

    'domain_name': r'domain:\s*(.+)',

    'creation_date': r'\ncreated:\s*(.+)',
    'expiration_date': r'\npaid-till:\s*(.+)',

    'name_servers': r'\nnserver:\s*(.+)',
    'status': r'\nstate:\s*(.+)',
}

su = {
    'extend': 'ru',
}

ru_rf = {
    'extend': 'ru',
}

lv = {
    'extend': 'ru',

    'registrar': r'\[Registrar\]?\s{0,}(?:[^\n][\n]?){0,}?\s{0,}Name(?:[^:]{0,}):\s?(.+)',
    'creation_date': r'Registered:\s*(.+)\n',
    'updated_date': r'Updated:\s*(.+)\n',

    'status': r'Status:\s?(.+)',
}

jp = {
    'domain_name': r'\[Domain Name\]\s?(.+)',
    'registrar': None,
    'registrant': r'\[Registrant\]\s?(.+)',
    'registrant_cc' : None,

    'creation_date': r'\[Created on\]\s?(.+)',
    'expiration_date': r'\[Expires on\]\s?(.+)',
    'updated_date': r'\[Last Updated\]\s?(.+)',

    'name_servers': r'\[Name Server\]\s*(.+)',
    'status': r'\[Status\]\s?(.+)',
    'emails': r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

co_jp = {
    'extend': 'jp',

    'creation_date': r'\[Registered Date\]\s?(.+)',
    'expiration_date': r'\[State\].+\((.+)\)',
    'updated_date': r'\[Last Update\]\s?(.+)',
}

de = {
    'extend': 'com',
    'domain_name': r'\ndomain:\s*(.+)',
    'registrant_cc': r'CountryCode:\s?(.+)',
    'updated_date': r'\nChanged:\s?(.+)',
    'name_servers': r'Nserver:\s*(.+)',
}

at = {
    'extend': 'com',
    'domain_name': r'domain:\s?(.+)',
    'updated_date': r'changed:\s?(.+)',
    'name_servers': r'nserver:\s*(.+)',
}

eu = {
    'extend': 'com',

    'domain_name': r'Domai(?:n|n Name):\s?(.+)',
    'registrar': r'Name:\s?(.+)',
    'name_servers': r'Name(?: servers| Server):\s(?:\s(.+)\s(.+)\s(.+)\s(.+)|(.+))',
}

cc = {
    'extend': 'com',
}

biz = {
    'extend': 'org',

    'creation_date': r'Domain Registration Date:\s?(.+)',
    'expiration_date': r'Domain Expiration Date:\s?(.+)',
    'updated_date': r'Domain Last Updated Date:\s?(.+)',

    'status': None,
}

info = {
    'extend': 'org'
}

online = {
    'extend': 'org',

    'status': r'Domain Status:\s?(.+)'
}

name = {
    'extend': 'com',

    'status': r'Domain Status:\s?(.+)',
}

us = {
    'extend': 'biz',
}

me = {
    'extend': 'org',
}

co = {
    'extend': 'biz',

    'status': r'Status:\s?(.+)',
}

be = {
    'extend': 'pl',

    'domain_name': r'\nDomain:\s*(.+)',
    'registrar': r'(?:Company\s)?Name:\n?(.+)',

    'creation_date': r'Registered:\s*(.+)\n',

    'status': r'Status:\s?(.+)',
}

nz = {
    'extend': None,

    'domain_name': r'domain_name:\s?(.+)',
    'registrar': r'registrar_name:\s?(.+)',
    'registrant': r'registrant_contact_name:\s?(.+)',
    'registrant_cc': r'registrant_contact_country:\s?([^\(]+).+',

    'creation_date': r'domain_dateregistered:\s?(.+)',
    'expiration_date': r'domain_datebilleduntil:\s?(.+)',
    'updated_date': r'domain_datelastmodified:\s?(.+)',

    'name_servers': r'ns_name_[0-9]{2}:\s?(.+)',
    'status': r'query_status:\s?(.+)',
    'emails': r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

cz = {
    'extend': 'com',

    'domain_name': r'Domain:\s?(.+)',
    'registrar': r'registrar:\s?(.+)',
    'registrant': r'registrant:\s?(.+)',

    'creation_date': r'registered:\s?(.+)',
    'expiration_date': r'expire:\s?(.+)',
    'updated_date': r'changed:\s?(.+)',

    'name_servers': r'nserver:\s*(.+) ',
}

it = {
    'extend': 'com',

    'domain_name': r'Domain:\s?(.+)',
    'registrar': r'Registrar\s*Organization:\s*(.+)',
    'registrant_cc': None,

    'creation_date': r'Created:\s?(.+)',
    'expiration_date': r'Expire Date:\s?(.+)',
    'updated_date': r'Last Update:\s?(.+)',

    'name_servers': r'Nameservers\s?(.+)\s?(.+)\s?(.+)\s?(.+)',
    'emails': None,
    'status': r'Status:\s?(.+)',
}

fr = {
    'extend': 'com',

    'domain_name': r'domain:\s?(.+)',
    'registrar': r'registrar:\s*(.+)',
    'registrant': r'contact:\s?(.+)',
    'registrant_cc': r'country:\s?(.+)',

    'creation_date': r'created:\s?(.+)',
    'expiration_date': r'Expiry Date:\s?(.+)',
    'updated_date': r'last-update:\s?(.+)',

    'name_servers': r'nserver:\s*(.+)',
    'status': r'status:\s?(.+)',
}

kg = {
    'extend': 'com',

    'domain_name': r'Domain \s?(.+)',
    'creation_date': r'Record created:\s?(.+)',
    'expiration_date': r'Record expires on \s?(.+)',
}

vc = {
    'extend': 'com',
}

fm = {
    'extend': 'com',

    'domain_name': r'Query: \s?(.+)',
    'creation_date': r'Created: \s?(.+)',
    'expiration_date': r'Expires: \s?(.+)'
}

tv = {
    'extend': 'com',
    'domain_name': r'Domain Name: \s?(.+)',

    'creation_date': r'Creation Date: \s?(.+)',
    'expiration_date': r'Registry Expiry Date: \s?(.+)'
}

edu = {
    'extend': 'com',
    'domain_name': r'Domain Name: \s?(.+)',

    'creation_date': r'Domain record activated: \s?(.+)',
    'expiration_date': r'Domain expires: \s?(.+)',
    'updated_date': r'Domain record last updated: \s?(.+)',
}

ca = {
    'extend': 'com',

    'domain_name': r'Domain name: \s?(.+)',
    'creation_date': r'Creation date: \s?(.+)',
    'expiration_date': r'Expiry date: \s?(.+)',
    'updated_date': r'Updated date: \s?(.+)',
}

cn = {
    'extend': 'com',

    'registrant': r'Registrant:\s?(.+)',
    'registrant_cc': None,

    'creation_date': r'Registration Date:\s?(.+)',
    'updated_date': None,

    'emails': r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

hk = {
    'extend': None,

    'domain_name': r'Domain Name:\s?(.+)',
    'registrar': r'Registrar Name:\s?(.+)',
    'registrant': r'Company English Name\(?.+\)?:\s?(.+)',
    'registrant_cc': r'Country:\s?(.+)',

    'creation_date': r'Domain Name Commencement Date:\s?(.+)',
    'expiration_date': r'Expiry Date:\s?(.+)',
    'updated_date': None,

    'name_servers': r'Name Servers Information:\s*(.+)\s*',
    'status': r'Domain Status:\s?(.+)',
    'emails': r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

kr = {
    'extend': None,

    'domain_name': r'Domain Name\s+:\s?(.+)',
    'registrar': None,
    'registrant': r'Registrant\s+:\s?(.+)',
    'registrant_cc': None,

    'creation_date': r'Registered Date\s+:\s?(.+)',
    'expiration_date': r'Expiration Date\s+:\s?(.+)',
    'updated_date': r'Last Updated Date\s+:\s?(.+)',

    'name_servers': r'Host Name\s+:\s?(.+)',
    'emails': r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

bo = {
    'extend': None,

    'domain_name': r'Dominio:\s?(.+)',
    'registrar': None,
    'registrant': r'TITULAR:?\s{0,}(?:[^\n][\n]?){0,}?\s{0,}Organizacion(?:[^:]{0,}):\s?(.+)',
    'registrant_cc': r'TITULAR:?\s{0,}(?:[^\n][\n]?){0,}?\s{0,}Pais(?:[^:]{0,}):\s?(.+)',

    'creation_date': r'Fecha de registro:\s?(.+)',
    'expiration_date': r'Fecha de vencimiento:\s?(.+)',
    'updated_date': None,

    'name_servers': None,
    'status': None,
    'emails': r's/([\w.-]+)(\sen\s)([\w.-]+\.[\w]{2,4})/\1@\3/',
}

md = {
    'extend': None,

    'domain_name': r'Domain name:\s?(.+)',
    'registrar': None,
    'registrant': r'Registrant:\s?(.+)',
    'registrant_cc': None,

    'creation_date': r'Created:\s?(.+)',
    'expiration_date': r'Expiration date:\s?(.+)',
    'updated_date': None,

    'name_servers': r'Name server:\s?(.+)',
}

st = {
    'extend': 'com',

    'status': r'Status:\s?(.+)',
    'creation_date': r'Creation Date:\s?(.+)',
    'expiration_date': r'Expiration Date:\s?(.+)',
    'updated_date': r'Updated Date:\s?(.+)',
}
aarp = {
  'extend': 'com',
}
abarth = {
  'extend': 'com',
}
abbott = {
  'extend': 'com',
}
abbvie = {
  'extend': 'com',
}
abc = {
  'extend': 'com',
}
abogado = {
  'extend': 'com',
}
abudhabi = {
  'extend': 'com',
}
academy = {
  'extend': 'com',
}
accountant = {
  'extend': 'com',
}
accountants = {
  'extend': 'com',
}
ac = {
  'extend': 'com',
}
aco = {
  'extend': 'com',
}
active = {
  'extend': 'com',
}
actor = {
  'extend': 'com',
}
adac = {
  'extend': 'com',
}
ads = {
  'extend': 'com',
}
adult = {
  'extend': 'com',
}
aeg = {
  'extend': 'com',
}
ae = {
  'extend': 'com',
}
aero = {
  'extend': 'com',
}
afamilycompany = {
  'extend': 'com',
}
af = {
  'extend': 'com',
}
afl = {
  'extend': 'com',
}
africa = {
  'extend': 'com',
}
agakhan = {
  'extend': 'com',
}
agency = {
  'extend': 'com',
}
ag = {
  'extend': 'com',
}
aigo = {
  'extend': 'com',
}
ai = {
  'extend': 'com',
}
airbus = {
  'extend': 'com',
}
airforce = {
  'extend': 'com',
}
airtel = {
  'extend': 'com',
}
akdn = {
  'extend': 'com',
}
alfaromeo = {
  'extend': 'com',
}
alibaba = {
  'extend': 'com',
}
alipay = {
  'extend': 'com',
}
allfinanz = {
  'extend': 'com',
}
allstate = {
  'extend': 'com',
}
ally = {
  'extend': 'com',
}
alsace = {
  'extend': 'com',
}
alstom = {
  'extend': 'com',
}
americanfamily = {
  'extend': 'com',
}
amfam = {
  'extend': 'com',
}
android = {
  'extend': 'com',
}
anquan = {
  'extend': 'com',
}
anz = {
  'extend': 'com',
}
aol = {
  'extend': 'com',
}
apartments = {
  'extend': 'com',
}
app = {
  'extend': 'com',
}
apple = {
  'extend': 'com',
}
aquarelle = {
  'extend': 'com',
}
archi = {
  'extend': 'com',
}
ar = {
  'extend': 'com',
}
army = {
  'extend': 'com',
}
arpa = {
  'extend': 'com',
}
arte = {
  'extend': 'com',
}
art = {
  'extend': 'com',
}
# as is Python keyword
#as = {
#  'extend': 'com',
#}
asda = {
  'extend': 'com',
}
asia = {
  'extend': 'com',
}
associates = {
  'extend': 'com',
}
attorney = {
  'extend': 'com',
}
auction = {
  'extend': 'com',
}
audi = {
  'extend': 'com',
}
audio = {
  'extend': 'com',
}
au = {
  'extend': 'com',
}
auspost = {
  'extend': 'com',
}
auto = {
  'extend': 'com',
}
autos = {
  'extend': 'com',
}
avianca = {
  'extend': 'com',
}
aw = {
  'extend': 'com',
}
ax = {
  'extend': 'com',
}
baidu = {
  'extend': 'com',
}
band = {
  'extend': 'com',
}
bank = {
  'extend': 'com',
}
barcelona = {
  'extend': 'com',
}
barclaycard = {
  'extend': 'com',
}
barclays = {
  'extend': 'com',
}
barefoot = {
  'extend': 'com',
}
bargains = {
  'extend': 'com',
}
bar = {
  'extend': 'com',
}
basketball = {
  'extend': 'com',
}
bauhaus = {
  'extend': 'com',
}
bayern = {
  'extend': 'com',
}
bbc = {
  'extend': 'com',
}
bbt = {
  'extend': 'com',
}
bbva = {
  'extend': 'com',
}
bcg = {
  'extend': 'com',
}
bcn = {
  'extend': 'com',
}
beats = {
  'extend': 'com',
}
beauty = {
  'extend': 'com',
}
beer = {
  'extend': 'com',
}
bentley = {
  'extend': 'com',
}
berlin = {
  'extend': 'com',
}
bestbuy = {
  'extend': 'com',
}
best = {
  'extend': 'com',
}
bet = {
  'extend': 'com',
}
bg = {
  'extend': 'com',
}
bid = {
  'extend': 'com',
}
bike = {
  'extend': 'com',
}
bingo = {
  'extend': 'com',
}
bio = {
  'extend': 'com',
}
bj = {
  'extend': 'com',
}
blackfriday = {
  'extend': 'com',
}
black = {
  'extend': 'com',
}
blanco = {
  'extend': 'com',
}
blockbuster = {
  'extend': 'com',
}
blog = {
  'extend': 'com',
}
blue = {
  'extend': 'com',
}
bms = {
  'extend': 'com',
}
bmw = {
  'extend': 'com',
}
bn = {
  'extend': 'com',
}
bnl = {
  'extend': 'com',
}
bnpparibas = {
  'extend': 'com',
}
boats = {
  'extend': 'com',
}
boehringer = {
  'extend': 'com',
}
bofa = {
  'extend': 'com',
}
bom = {
  'extend': 'com',
}
bond = {
  'extend': 'com',
}
boo = {
  'extend': 'com',
}
boots = {
  'extend': 'com',
}
bosch = {
  'extend': 'com',
}
bostik = {
  'extend': 'com',
}
boston = {
  'extend': 'com',
}
boutique = {
  'extend': 'com',
}
box = {
  'extend': 'com',
}
bradesco = {
  'extend': 'com',
}
br = {
    'extend': 'com',
    'domain_name':              r'domain:\s?(.+)',
    'registrar':                'nic.br',
    'registrant':               None,
    'owner':                    r'owner:\s?(.+)',
    'creation_date':            r'created:\s?(.+)',
    'expiration_date':          r'expires:\s?(.+)',
    'updated_date':             r'changed:\s?(.+)',
    'name_servers':             r'nserver:\s*(.+)',
    'status':                   r'status:\s?(.+)',
}
bridgestone = {
  'extend': 'com',
}
broadway = {
  'extend': 'com',
}
broker = {
  'extend': 'com',
}
brother = {
  'extend': 'com',
}
brussels = {
  'extend': 'com',
}
budapest = {
  'extend': 'com',
}
bugatti = {
  'extend': 'com',
}
builders = {
  'extend': 'com',
}
build = {
  'extend': 'com',
}
business = {
  'extend': 'com',
}
buy = {
  'extend': 'com',
}
bw = {
  'extend': 'com',
}
by = {
  'extend': 'com',
}
bzh = {
  'extend': 'com',
}
cab = {
  'extend': 'com',
}
cafe = {
  'extend': 'com',
}
cal = {
  'extend': 'com',
}
camera = {
  'extend': 'com',
}
cam = {
  'extend': 'com',
}
camp = {
  'extend': 'com',
}
cancerresearch = {
  'extend': 'com',
}
canon = {
  'extend': 'com',
}
capetown = {
  'extend': 'com',
}
capital = {
  'extend': 'com',
}
capitalone = {
  'extend': 'com',
}
cards = {
  'extend': 'com',
}
career = {
  'extend': 'com',
}
careers = {
  'extend': 'com',
}
care = {
  'extend': 'com',
}
car = {
  'extend': 'com',
}
cars = {
  'extend': 'com',
}
casa = {
  'extend': 'com',
}
case = {
  'extend': 'com',
}
caseih = {
  'extend': 'com',
}
cash = {
  'extend': 'com',
}
casino = {
  'extend': 'com',
}
catering = {
  'extend': 'com',
}
catholic = {
  'extend': 'com',
}
cat = {
  'extend': 'com',
}
cba = {
  'extend': 'com',
}
cbs = {
  'extend': 'com',
}
ceb = {
  'extend': 'com',
}
center = {
  'extend': 'com',
}
ceo = {
  'extend': 'com',
}
cern = {
  'extend': 'com',
}
cfa = {
  'extend': 'com',
}
cfd = {
  'extend': 'com',
}
cf = {
  'extend': 'com',
}
chanel = {
  'extend': 'com',
}
channel = {
  'extend': 'com',
}
chat = {
  'extend': 'com',
}
cheap = {
  'extend': 'com',
}
ch = {
  'extend': 'com',
}
chintai = {
  'extend': 'com',
}
christmas = {
  'extend': 'com',
}
chrome = {
  'extend': 'com',
}
chrysler = {
  'extend': 'com',
}
church = {
  'extend': 'com',
}
ci = {
  'extend': 'com',
}
cipriani = {
  'extend': 'com',
}
cityeats = {
  'extend': 'com',
}
city = {
  'extend': 'com',
}
claims = {
  'extend': 'com',
}
cleaning = {
  'extend': 'com',
}
cl = {
  'extend': 'com',
}
click = {
  'extend': 'com',
}
clinic = {
  'extend': 'com',
}
clinique = {
  'extend': 'com',
}
clothing = {
  'extend': 'com',
}
cloud = {
  'extend': 'com',
}
club = {
  'extend': 'com',
}
clubmed = {
  'extend': 'com',
}
coach = {
  'extend': 'com',
}
codes = {
  'extend': 'com',
}
coffee = {
  'extend': 'com',
}
college = {
  'extend': 'com',
}
cologne = {
  'extend': 'com',
}
comcast = {
  'extend': 'com',
}
commbank = {
  'extend': 'com',
}
community = {
  'extend': 'com',
}
company = {
  'extend': 'com',
}
compare = {
  'extend': 'com',
}
computer = {
  'extend': 'com',
}
comsec = {
  'extend': 'com',
}
condos = {
  'extend': 'com',
}
construction = {
  'extend': 'com',
}
consulting = {
  'extend': 'com',
}
contact = {
  'extend': 'com',
}
contractors = {
  'extend': 'com',
}
cookingchannel = {
  'extend': 'com',
}
cooking = {
  'extend': 'com',
}
cool = {
  'extend': 'com',
}
coop = {
  'extend': 'com',
}
corsica = {
  'extend': 'com',
}
country = {
  'extend': 'com',
}
coupons = {
  'extend': 'com',
}
courses = {
  'extend': 'com',
}
creditcard = {
  'extend': 'com',
}
credit = {
  'extend': 'com',
}
creditunion = {
  'extend': 'com',
}
cr = {
  'extend': 'com',
}
cricket = {
  'extend': 'com',
}
cruise = {
  'extend': 'com',
}
cruises = {
  'extend': 'com',
}
csc = {
  'extend': 'com',
}
cuisinella = {
  'extend': 'com',
}
cx = {
  'extend': 'com',
}
cymru = {
  'extend': 'com',
}
cyou = {
  'extend': 'com',
}
dabur = {
  'extend': 'com',
}
dad = {
  'extend': 'com',
}
dance = {
  'extend': 'com',
}
data = {
  'extend': 'com',
}
date = {
  'extend': 'com',
}
dating = {
  'extend': 'com',
}
datsun = {
  'extend': 'com',
}
day = {
  'extend': 'com',
}
dclk = {
  'extend': 'com',
}
dds = {
  'extend': 'com',
}
deals = {
  'extend': 'com',
}
degree = {
  'extend': 'com',
}
delivery = {
  'extend': 'com',
}
deloitte = {
  'extend': 'com',
}
delta = {
  'extend': 'com',
}
democrat = {
  'extend': 'com',
}
dental = {
  'extend': 'com',
}
dentist = {
  'extend': 'com',
}
design = {
  'extend': 'com',
}
desi = {
  'extend': 'com',
}
dev = {
  'extend': 'com',
}
diamonds = {
  'extend': 'com',
}
diet = {
  'extend': 'com',
}
digital = {
  'extend': 'com',
}
direct = {
  'extend': 'com',
}
directory = {
  'extend': 'com',
}
discount = {
  'extend': 'com',
}
dish = {
  'extend': 'com',
}
diy = {
  'extend': 'com',
}
dk = {
  'extend': 'com',
}
dm = {
  'extend': 'com',
}
docs = {
  'extend': 'com',
}
doctor = {
  'extend': 'com',
}
dodge = {
  'extend': 'com',
}
dog = {
  'extend': 'com',
}
doha = {
  'extend': 'com',
}
domains = {
  'extend': 'com',
}
doosan = {
  'extend': 'com',
}
dot = {
  'extend': 'com',
}
download = {
  'extend': 'com',
}
drive = {
  'extend': 'com',
}
dtv = {
  'extend': 'com',
}
dubai = {
  'extend': 'com',
}
duck = {
  'extend': 'com',
}
dunlop = {
  'extend': 'com',
}
durban = {
  'extend': 'com',
}
dvag = {
  'extend': 'com',
}
dvr = {
  'extend': 'com',
}
dz = {
  'extend': 'com',
}
eat = {
  'extend': 'com',
}
ec = {
  'extend': 'com',
}
eco = {
  'extend': 'com',
}
edeka = {
  'extend': 'com',
}
education = {
  'extend': 'com',
}
ee = {
  'extend': 'com',
}
email = {
  'extend': 'com',
}
emerck = {
  'extend': 'com',
}
energy = {
  'extend': 'com',
}
engineer = {
  'extend': 'com',
}
engineering = {
  'extend': 'com',
}
enterprises = {
  'extend': 'com',
}
epson = {
  'extend': 'com',
}
equipment = {
  'extend': 'com',
}
ericsson = {
  'extend': 'com',
}
erni = {
  'extend': 'com',
}
es = {
  'extend': 'com',
}
esq = {
  'extend': 'com',
}
estate = {
  'extend': 'com',
}
esurance = {
  'extend': 'com',
}
eurovision = {
  'extend': 'com',
}
eus = {
  'extend': 'com',
}
events = {
  'extend': 'com',
}
exchange = {
  'extend': 'com',
}
expert = {
  'extend': 'com',
}
exposed = {
  'extend': 'com',
}
express = {
  'extend': 'com',
}
extraspace = {
  'extend': 'com',
}
fage = {
  'extend': 'com',
}
fail = {
  'extend': 'com',
}
fairwinds = {
  'extend': 'com',
}
faith = {
  'extend': 'com',
}
family = {
  'extend': 'com',
}
fan = {
  'extend': 'com',
}
fans = {
  'extend': 'com',
}
farm = {
  'extend': 'com',
}
fashion = {
  'extend': 'com',
}
fedex = {
  'extend': 'com',
}
feedback = {
  'extend': 'com',
}
ferrari = {
  'extend': 'com',
}
fiat = {
  'extend': 'com',
}
fidelity = {
  'extend': 'com',
}
fido = {
  'extend': 'com',
}
fi = {
  'extend': 'com',
}
film = {
  'extend': 'com',
}
final = {
  'extend': 'com',
}
finance = {
  'extend': 'com',
}
financial = {
  'extend': 'com',
}
firestone = {
  'extend': 'com',
}
firmdale = {
  'extend': 'com',
}
fish = {
  'extend': 'com',
}
fishing = {
  'extend': 'com',
}
fit = {
  'extend': 'com',
}
fitness = {
  'extend': 'com',
}
flights = {
  'extend': 'com',
}
florist = {
  'extend': 'com',
}
flowers = {
  'extend': 'com',
}
flsmidth = {
  'extend': 'com',
}
fly = {
  'extend': 'com',
}
foodnetwork = {
  'extend': 'com',
}
foo = {
  'extend': 'com',
}
football = {
  'extend': 'com',
}
forex = {
  'extend': 'com',
}
forsale = {
  'extend': 'com',
}
forum = {
  'extend': 'com',
}
foundation = {
  'extend': 'com',
}
fresenius = {
  'extend': 'com',
}
frl = {
  'extend': 'com',
}
frogans = {
  'extend': 'com',
}
frontdoor = {
  'extend': 'com',
}
fujitsu = {
  'extend': 'com',
}
fujixerox = {
  'extend': 'com',
}
fund = {
  'extend': 'com',
}
fun = {
  'extend': 'com',
}
furniture = {
  'extend': 'com',
}
futbol = {
  'extend': 'com',
}
fyi = {
  'extend': 'com',
}
gal = {
  'extend': 'com',
}
gallery = {
  'extend': 'com',
}
gallo = {
  'extend': 'com',
}
gallup = {
  'extend': 'com',
}
game = {
  'extend': 'com',
}
games = {
  'extend': 'com',
}
garden = {
  'extend': 'com',
}
gbiz = {
  'extend': 'com',
}
gd = {
  'extend': 'com',
}
gdn = {
  'extend': 'com',
}
gea = {
  'extend': 'com',
}
gent = {
  'extend': 'com',
}
genting = {
  'extend': 'com',
}
george = {
  'extend': 'com',
}
gf = {
  'extend': 'com',
}
ggee = {
  'extend': 'com',
}
gg = {
  'extend': 'com',
}
gift = {
  'extend': 'com',
}
gifts = {
  'extend': 'com',
}
gi = {
  'extend': 'com',
}
gives = {
  'extend': 'com',
}
giving = {
  'extend': 'com',
}
glade = {
  'extend': 'com',
}
glass = {
  'extend': 'com',
}
gle = {
  'extend': 'com',
}
gl = {
  'extend': 'com',
}

# global is python keyword
#global = {
#  'extend': 'com',
#}
globo = {
  'extend': 'com',
}
gmail = {
  'extend': 'com',
}
gmbh = {
  'extend': 'com',
}
gmx = {
  'extend': 'com',
}
godaddy = {
  'extend': 'com',
}
gold = {
  'extend': 'com',
}
goldpoint = {
  'extend': 'com',
}
golf = {
  'extend': 'com',
}
goodhands = {
  'extend': 'com',
}
goodyear = {
  'extend': 'com',
}
goog = {
  'extend': 'com',
}
google = {
  'extend': 'com',
}
goo = {
  'extend': 'com',
}
gop = {
  'extend': 'com',
}
gov = {
  'extend': 'com',
}
gq = {
  'extend': 'com',
}
graphics = {
  'extend': 'com',
}
gratis = {
  'extend': 'com',
}
green = {
  'extend': 'com',
}
gripe = {
  'extend': 'com',
}
group = {
  'extend': 'com',
}
gs = {
  'extend': 'com',
}
guge = {
  'extend': 'com',
}
guide = {
  'extend': 'com',
}
guitars = {
  'extend': 'com',
}
guru = {
  'extend': 'com',
}
gy = {
  'extend': 'com',
}
hamburg = {
  'extend': 'com',
}
hangout = {
  'extend': 'com',
}
haus = {
  'extend': 'com',
}
hdfcbank = {
  'extend': 'com',
}
hdfc = {
  'extend': 'com',
}
healthcare = {
  'extend': 'com',
}
help = {
  'extend': 'com',
}
helsinki = {
  'extend': 'com',
}
here = {
  'extend': 'com',
}
hermes = {
  'extend': 'com',
}
hgtv = {
  'extend': 'com',
}
hiphop = {
  'extend': 'com',
}
hisamitsu = {
  'extend': 'com',
}
hitachi = {
  'extend': 'com',
}
hiv = {
  'extend': 'com',
}
hkt = {
  'extend': 'com',
}
hm = {
  'extend': 'com',
}
hn = {
  'extend': 'com',
}
hockey = {
  'extend': 'com',
}
holdings = {
  'extend': 'com',
}
holiday = {
  'extend': 'com',
}
homedepot = {
  'extend': 'com',
}
homes = {
  'extend': 'com',
}
honda = {
  'extend': 'com',
}
horse = {
  'extend': 'com',
}
hospital = {
  'extend': 'com',
}
host = {
  'extend': 'com',
}
hosting = {
  'extend': 'com',
}
house = {
  'extend': 'com',
}
how = {
  'extend': 'com',
}
hr = {
  'extend': 'com',
}
ht = {
  'extend': 'com',
}
hughes = {
  'extend': 'com',
}
hu = {
  'extend': 'com',
}
hyundai = {
  'extend': 'com',
}
ibm = {
  'extend': 'com',
}
icbc = {
  'extend': 'com',
}
ice = {
  'extend': 'com',
}
icu = {
  'extend': 'com',
}
id = {
  'extend': 'com',
}
ie = {
  'extend': 'com',
}
ifm = {
  'extend': 'com',
}
iinet = {
  'extend': 'com',
}
ikano = {
  'extend': 'com',
}
il = {
  'extend': 'com',
}
imamat = {
  'extend': 'com',
}
im = {
  'extend': 'com',
}
immobilien = {
  'extend': 'com',
}
immo = {
  'extend': 'com',
}
#Using "IN" as "in" is a keyword in python
IN = {
    'extend': 'com',
}
industries = {
  'extend': 'com',
}
infiniti = {
  'extend': 'com',
}
ing = {
  'extend': 'com',
}
ink = {
  'extend': 'com',
}
institute = {
  'extend': 'com',
}
insurance = {
  'extend': 'com',
}
insure = {
  'extend': 'com',
}
international = {
  'extend': 'com',
}
int = {
  'extend': 'com',
}
investments = {
  'extend': 'com',
}
io = {
  'extend': 'com',
}
iq = {
  'extend': 'com',
}
ir = {
  'extend': 'com',
}
irish = {
  'extend': 'com',
}
iselect = {
  'extend': 'com',
}
# is is a Python keyword
#is = {
#  'extend': 'com',
#}
ismaili = {
  'extend': 'com',
}
istanbul = {
  'extend': 'com',
}
ist = {
  'extend': 'com',
}
itv = {
  'extend': 'com',
}
iveco = {
  'extend': 'com',
}
jaguar = {
  'extend': 'com',
}
java = {
  'extend': 'com',
}
jcb = {
  'extend': 'com',
}
jcp = {
  'extend': 'com',
}
jeep = {
  'extend': 'com',
}
je = {
  'extend': 'com',
}
jewelry = {
  'extend': 'com',
}
jio = {
  'extend': 'com',
}
jll = {
  'extend': 'com',
}
jobs = {
  'extend': 'com',
}
joburg = {
  'extend': 'com',
}
juegos = {
  'extend': 'com',
}
juniper = {
  'extend': 'com',
}
kaufen = {
  'extend': 'com',
}
kddi = {
  'extend': 'com',
}
ke = {
  'extend': 'com',
}
kerryhotels = {
  'extend': 'com',
}
kerrylogistics = {
  'extend': 'com',
}
kerryproperties = {
  'extend': 'com',
}
kfh = {
  'extend': 'com',
}
kia = {
  'extend': 'com',
}
ki = {
  'extend': 'com',
}
kim = {
  'extend': 'com',
}
kitchen = {
  'extend': 'com',
}
kiwi = {
  'extend': 'com',
}
kn = {
  'extend': 'com',
}
koeln = {
  'extend': 'com',
}
komatsu = {
  'extend': 'com',
}
kosher = {
  'extend': 'com',
}
krd = {
  'extend': 'com',
}
kred = {
  'extend': 'com',
}
kuokgroup = {
  'extend': 'com',
}
ky = {
  'extend': 'com',
}
kyoto = {
  'extend': 'com',
}
kz = {
  'extend': 'com',
}
lacaixa = {
  'extend': 'com',
}
ladbrokes = {
  'extend': 'com',
}
la = {
  'extend': 'com',
}
lamborghini = {
  'extend': 'com',
}
lamer = {
  'extend': 'com',
}
lancaster = {
  'extend': 'com',
}
lancia = {
  'extend': 'com',
}
lancome = {
  'extend': 'com',
}
land = {
  'extend': 'com',
}
landrover = {
  'extend': 'com',
}
lasalle = {
  'extend': 'com',
}
lat = {
  'extend': 'com',
}
latino = {
  'extend': 'com',
}
latrobe = {
  'extend': 'com',
}
law = {
  'extend': 'com',
}
lawyer = {
  'extend': 'com',
}
lds = {
  'extend': 'com',
}
lease = {
  'extend': 'com',
}
leclerc = {
  'extend': 'com',
}
lefrak = {
  'extend': 'com',
}
legal = {
  'extend': 'com',
}
lego = {
  'extend': 'com',
}
lexus = {
  'extend': 'com',
}
lgbt = {
  'extend': 'com',
}
liaison = {
  'extend': 'com',
}
lidl = {
  'extend': 'com',
}
life = {
  'extend': 'com',
}
lifestyle = {
  'extend': 'com',
}
lighting = {
  'extend': 'com',
}
limited = {
  'extend': 'com',
}
limo = {
  'extend': 'com',
}
linde = {
  'extend': 'com',
}
link = {
  'extend': 'com',
}
lipsy = {
  'extend': 'com',
}
live = {
  'extend': 'com',
}
lixil = {
  'extend': 'com',
}
loan = {
  'extend': 'com',
}
loans = {
  'extend': 'com',
}
locker = {
  'extend': 'com',
}
locus = {
  'extend': 'com',
}
lol = {
  'extend': 'com',
}
london = {
  'extend': 'com',
}
lotte = {
  'extend': 'com',
}
lotto = {
  'extend': 'com',
}
love = {
  'extend': 'com',
}
lplfinancial = {
  'extend': 'com',
}
lpl = {
  'extend': 'com',
}
ltda = {
  'extend': 'com',
}
ltd = {
  'extend': 'com',
}
lt = {
  'extend': 'com',
}
lu = {
  'extend': 'com',
}
lundbeck = {
  'extend': 'com',
}
luxe = {
  'extend': 'com',
}
luxury = {
  'extend': 'com',
}
ly = {
  'extend': 'com',
}
macys = {
  'extend': 'com',
}
madrid = {
  'extend': 'com',
}
ma = {
  'extend': 'com',
}
maison = {
  'extend': 'com',
}
makeup = {
  'extend': 'com',
}
management = {
  'extend': 'com',
}
mango = {
  'extend': 'com',
}
man = {
  'extend': 'com',
}
market = {
  'extend': 'com',
}
marketing = {
  'extend': 'com',
}
markets = {
  'extend': 'com',
}
marriott = {
  'extend': 'com',
}
maserati = {
  'extend': 'com',
}
mba = {
  'extend': 'com',
}
mckinsey = {
  'extend': 'com',
}
med = {
  'extend': 'com',
}
media = {
  'extend': 'com',
}
meet = {
  'extend': 'com',
}
melbourne = {
  'extend': 'com',
}
meme = {
  'extend': 'com',
}
memorial = {
  'extend': 'com',
}
men = {
  'extend': 'com',
}
menu = {
  'extend': 'com',
}
metlife = {
  'extend': 'com',
}
mg = {
  'extend': 'com',
}
miami = {
  'extend': 'com',
}
mini = {
  'extend': 'com',
}
mit = {
  'extend': 'com',
}
mitsubishi = {
  'extend': 'com',
}
mk = {
  'extend': 'com',
}
ml = {
  'extend': 'com',
}
mls = {
  'extend': 'com',
}
mma = {
  'extend': 'com',
}
mn = {
  'extend': 'com',
}
mobi = {
  'extend': 'com',
}
mobile = {
  'extend': 'com',
}
moda = {
  'extend': 'com',
}
moe = {
  'extend': 'com',
}
mo = {
  'extend': 'com',
}
mom = {
  'extend': 'com',
}
monash = {
  'extend': 'com',
}
money = {
  'extend': 'com',
}
monster = {
  'extend': 'com',
}
mopar = {
  'extend': 'com',
}
mormon = {
  'extend': 'com',
}
mortgage = {
  'extend': 'com',
}
moscow = {
  'extend': 'com',
}
motorcycles = {
  'extend': 'com',
}
mov = {
  'extend': 'com',
}
movie = {
  'extend': 'com',
}
movistar = {
  'extend': 'com',
}
mp = {
  'extend': 'com',
}
mq = {
  'extend': 'com',
}
ms = {
  'extend': 'com',
}
mtn = {
  'extend': 'com',
}
mtpc = {
  'extend': 'com',
}
mtr = {
  'extend': 'com',
}
mu = {
  'extend': 'com',
}
museum = {
  'extend': 'com',
}
mutuelle = {
  'extend': 'com',
}
mx = {
  'extend': 'com',
}
my = {
  'extend': 'com',
}
mz = {
  'extend': 'com',
}
nab = {
  'extend': 'com',
}
nadex = {
  'extend': 'com',
}
nagoya = {
  'extend': 'com',
}
nationwide = {
  'extend': 'com',
}
natura = {
  'extend': 'com',
}
navy = {
  'extend': 'com',
}
nc = {
  'extend': 'com',
}
nec = {
  'extend': 'com',
}
netbank = {
  'extend': 'com',
}
network = {
  'extend': 'com',
}
newholland = {
  'extend': 'com',
}
new = {
  'extend': 'com',
}
news = {
  'extend': 'com',
}
nextdirect = {
  'extend': 'com',
}
next = {
  'extend': 'com',
}
nexus = {
  'extend': 'com',
}
ng = {
  'extend': 'com',
}
ngo = {
  'extend': 'com',
}
nico = {
  'extend': 'com',
}
nikon = {
  'extend': 'com',
}
ninja = {
  'extend': 'com',
}
nissan = {
  'extend': 'com',
}
nissay = {
  'extend': 'com',
}
no = {
  'extend': 'com',
}
nokia = {
  'extend': 'com',
}
norton = {
  'extend': 'com',
}
nowruz = {
  'extend': 'com',
}
nowtv = {
  'extend': 'com',
}
nra = {
  'extend': 'com',
}
nrw = {
  'extend': 'com',
}
nu = {
  'extend': 'com',
}
nyc = {
  'extend': 'com',
}
obi = {
  'extend': 'com',
}
observer = {
  'extend': 'com',
}
off = {
  'extend': 'com',
}
okinawa = {
  'extend': 'com',
}
olayangroup = {
  'extend': 'com',
}
olayan = {
  'extend': 'com',
}
ollo = {
  'extend': 'com',
}
omega = {
  'extend': 'com',
}
one = {
  'extend': 'com',
}
ong = {
  'extend': 'com',
}
onyourside = {
  'extend': 'com',
}
ooo = {
  'extend': 'com',
}
oracle = {
  'extend': 'com',
}
orange = {
  'extend': 'com',
}
organic = {
  'extend': 'com',
}
orientexpress = {
  'extend': 'com',
}
origins = {
  'extend': 'com',
}
osaka = {
  'extend': 'com',
}
ott = {
  'extend': 'com',
}
ovh = {
  'extend': 'com',
}
page = {
  'extend': 'com',
}
panasonic = {
  'extend': 'com',
}
paris = {
  'extend': 'com',
}
pars = {
  'extend': 'com',
}
partners = {
  'extend': 'com',
}
parts = {
  'extend': 'com',
}
party = {
  'extend': 'com',
}
pccw = {
  'extend': 'com',
}
pe = {
  'extend': 'com',
}
pet = {
  'extend': 'com',
}
pf = {
  'extend': 'com',
}
philips = {
  'extend': 'com',
}
phone = {
  'extend': 'com',
}
photography = {
  'extend': 'com',
}
photo = {
  'extend': 'com',
}
photos = {
  'extend': 'com',
}
physio = {
  'extend': 'com',
}
pics = {
  'extend': 'com',
}
pictures = {
  'extend': 'com',
}
pid = {
  'extend': 'com',
}
pink = {
  'extend': 'com',
}
pioneer = {
  'extend': 'com',
}
pizza = {
  'extend': 'com',
}
place = {
  'extend': 'com',
}
play = {
  'extend': 'com',
}
playstation = {
  'extend': 'com',
}
plumbing = {
  'extend': 'com',
}
plus = {
  'extend': 'com',
}
pm = {
  'extend': 'com',
}
pnc = {
  'extend': 'com',
}
pohl = {
  'extend': 'com',
}
poker = {
  'extend': 'com',
}
politie = {
  'extend': 'com',
}
porn = {
  'extend': 'com',
}
post = {
  'extend': 'com',
}
press = {
  'extend': 'com',
}
pr = {
  'extend': 'com',
}
prod = {
  'extend': 'com',
}
productions = {
  'extend': 'com',
}
prof = {
  'extend': 'com',
}
progressive = {
  'extend': 'com',
}
pro = {
  'extend': 'com',
}
promo = {
  'extend': 'com',
}
properties = {
  'extend': 'com',
}
property = {
  'extend': 'com',
}
protection = {
  'extend': 'com',
}
pt = {
  'extend': 'com',
}
pub = {
  'extend': 'com',
}
pwc = {
  'extend': 'com',
}
pw = {
  'extend': 'com',
}
qa = {
  'extend': 'com',
}
qpon = {
  'extend': 'com',
}
quebec = {
  'extend': 'com',
}
quest = {
  'extend': 'com',
}
racing = {
  'extend': 'com',
}
radio = {
  'extend': 'com',
}
raid = {
  'extend': 'com',
}
realestate = {
  'extend': 'com',
}
realty = {
  'extend': 'com',
}
recipes = {
  'extend': 'com',
}
red = {
  'extend': 'com',
}
redstone = {
  'extend': 'com',
}
redumbrella = {
  'extend': 'com',
}
rehab = {
  'extend': 'com',
}
re = {
  'extend': 'com',
}
reise = {
  'extend': 'com',
}
reisen = {
  'extend': 'com',
}
reit = {
  'extend': 'com',
}
reliance = {
  'extend': 'com',
}
rentals = {
  'extend': 'com',
}
rent = {
  'extend': 'com',
}
repair = {
  'extend': 'com',
}
report = {
  'extend': 'com',
}
republican = {
  'extend': 'com',
}
restaurant = {
  'extend': 'com',
}
rest = {
  'extend': 'com',
}
review = {
  'extend': 'com',
}
reviews = {
  'extend': 'com',
}
rexroth = {
  'extend': 'com',
}
richardli = {
  'extend': 'com',
}
rich = {
  'extend': 'com',
}
ricoh = {
  'extend': 'com',
}
rightathome = {
  'extend': 'com',
}
ril = {
  'extend': 'com',
}
rio = {
  'extend': 'com',
}
rip = {
  'extend': 'com',
}
rmit = {
  'extend': 'com',
}
rocks = {
  'extend': 'com',
}
rodeo = {
  'extend': 'com',
}
rogers = {
  'extend': 'com',
}
ro = {
  'extend': 'com',
}
rs = {
  'extend': 'com',
}
rsvp = {
  'extend': 'com',
}
ruhr = {
  'extend': 'com',
}
run = {
  'extend': 'com',
}
rwe = {
  'extend': 'com',
}
saarland = {
  'extend': 'com',
}
sa = {
  'extend': 'com',
}
sale = {
  'extend': 'com',
}
salon = {
  'extend': 'com',
}
samsclub = {
  'extend': 'com',
}
samsung = {
  'extend': 'com',
}
sandvikcoromant = {
  'extend': 'com',
}
sandvik = {
  'extend': 'com',
}
sanofi = {
  'extend': 'com',
}
sap = {
  'extend': 'com',
}
sarl = {
  'extend': 'com',
}
saxo = {
  'extend': 'com',
}
sb = {
  'extend': 'com',
}
sbi = {
  'extend': 'com',
}
sbs = {
  'extend': 'com',
}
sca = {
  'extend': 'com',
}
scb = {
  'extend': 'com',
}
schaeffler = {
  'extend': 'com',
}
schmidt = {
  'extend': 'com',
}
scholarships = {
  'extend': 'com',
}
school = {
  'extend': 'com',
}
sc = {
  'extend': 'com',
}
schule = {
  'extend': 'com',
}
schwarz = {
  'extend': 'com',
}
science = {
  'extend': 'com',
}
scjohnson = {
  'extend': 'com',
}
scor = {
  'extend': 'com',
}
scot = {
  'extend': 'com',
}
seat = {
  'extend': 'com',
}
security = {
  'extend': 'com',
}
seek = {
  'extend': 'com',
}
se = {
  'extend': 'com',
}
select = {
  'extend': 'com',
}
services = {
  'extend': 'com',
}
ses = {
  'extend': 'com',
}
seven = {
  'extend': 'com',
}
sew = {
  'extend': 'com',
}
sex = {
  'extend': 'com',
}
sexy = {
  'extend': 'com',
}
sfr = {
  'extend': 'com',
}
sg = {
  'extend': 'com',
}
shangrila = {
  'extend': 'com',
}
sharp = {
  'extend': 'com',
}
shaw = {
  'extend': 'com',
}
shell = {
  'extend': 'com',
}
sh = {
  'extend': 'com',
}
shia = {
  'extend': 'com',
}
shiksha = {
  'extend': 'com',
}
shoes = {
  'extend': 'com',
}
shopping = {
  'extend': 'com',
}
shouji = {
  'extend': 'com',
}
show = {
  'extend': 'com',
}
showtime = {
  'extend': 'com',
}
shriram = {
  'extend': 'com',
}
si = {
  'extend': 'com',
}
sina = {
  'extend': 'com',
}
singles = {
  'extend': 'com',
}
site = {
  'extend': 'com',
}
sk = {
  'extend': 'com',
}
ski = {
  'extend': 'com',
}
skin = {
  'extend': 'com',
}
sky = {
  'extend': 'com',
}
sling = {
  'extend': 'com',
}
smart = {
  'extend': 'com',
}
sm = {
  'extend': 'com',
}
sncf = {
  'extend': 'com',
}
sn = {
  'extend': 'com',
}
soccer = {
  'extend': 'com',
}
social = {
  'extend': 'com',
}
softbank = {
  'extend': 'com',
}
software = {
  'extend': 'com',
}
sohu = {
  'extend': 'com',
}
so = {
  'extend': 'com',
}
solar = {
  'extend': 'com',
}
solutions = {
  'extend': 'com',
}
sony = {
  'extend': 'com',
}
soy = {
  'extend': 'com',
}
space = {
  'extend': 'com',
}
spiegel = {
  'extend': 'com',
}
spreadbetting = {
  'extend': 'com',
}
srl = {
  'extend': 'com',
}
srt = {
  'extend': 'com',
}
stada = {
  'extend': 'com',
}
star = {
  'extend': 'com',
}
starhub = {
  'extend': 'com',
}
statebank = {
  'extend': 'com',
}
statoil = {
  'extend': 'com',
}
stcgroup = {
  'extend': 'com',
}
stc = {
  'extend': 'com',
}
stockholm = {
  'extend': 'com',
}
storage = {
  'extend': 'com',
}
store = {
  'extend': 'com',
}
studio = {
  'extend': 'com',
}
study = {
  'extend': 'com',
}
style = {
  'extend': 'com',
}
sucks = {
  'extend': 'com',
}
supplies = {
  'extend': 'com',
}
supply = {
  'extend': 'com',
}
support = {
  'extend': 'com',
}
surf = {
  'extend': 'com',
}
surgery = {
  'extend': 'com',
}
swatch = {
  'extend': 'com',
}
swiss = {
  'extend': 'com',
}
sx = {
  'extend': 'com',
}
sydney = {
  'extend': 'com',
}
sy = {
  'extend': 'com',
}
symantec = {
  'extend': 'com',
}
systems = {
  'extend': 'com',
}
tab = {
  'extend': 'com',
}
taipei = {
  'extend': 'com',
}
tatamotors = {
  'extend': 'com',
}
tatar = {
  'extend': 'com',
}
tattoo = {
  'extend': 'com',
}
tax = {
  'extend': 'com',
}
taxi = {
  'extend': 'com',
}
tc = {
  'extend': 'com',
}
tci = {
  'extend': 'com',
}
tdk = {
  'extend': 'com',
}
team = {
  'extend': 'com',
}
tech = {
  'extend': 'com',
}
technology = {
  'extend': 'com',
}
telecity = {
  'extend': 'com',
}
telefonica = {
  'extend': 'com',
}
tel = {
  'extend': 'com',
}
temasek = {
  'extend': 'com',
}
tennis = {
  'extend': 'com',
}
teva = {
  'extend': 'com',
}
tf = {
  'extend': 'com',
}
tg = {
  'extend': 'com',
}
thd = {
  'extend': 'com',
}
theater = {
  'extend': 'com',
}
theatre = {
  'extend': 'com',
}
th = {
  'extend': 'com',
}
tiaa = {
  'extend': 'com',
}
tickets = {
  'extend': 'com',
}
tienda = {
  'extend': 'com',
}
tiffany = {
  'extend': 'com',
}
tips = {
  'extend': 'com',
}
tires = {
  'extend': 'com',
}
tirol = {
  'extend': 'com',
}
tk = {
  'extend': 'com',
}
tl = {
  'extend': 'com',
}
tm = {
  'extend': 'com',
}
tn = {
  'extend': 'com',
}
today = {
  'extend': 'com',
}
to = {
  'extend': 'com',
}
tokyo = {
  'extend': 'com',
}
tools = {
  'extend': 'com',
}
top = {
  'extend': 'com',
}
toray = {
  'extend': 'com',
}
toshiba = {
  'extend': 'com',
}
total = {
  'extend': 'com',
}
tours = {
  'extend': 'com',
}
town = {
  'extend': 'com',
}
toyota = {
  'extend': 'com',
}
toys = {
  'extend': 'com',
}
trade = {
  'extend': 'com',
}
trading = {
  'extend': 'com',
}
training = {
  'extend': 'com',
}
travelchannel = {
  'extend': 'com',
}
travelers = {
  'extend': 'com',
}
travelersinsurance = {
  'extend': 'com',
}
travel = {
  'extend': 'com',
}
tr = {
  'extend': 'com',
}
trust = {
  'extend': 'com',
}
trv = {
  'extend': 'com',
}
tui = {
  'extend': 'com',
}
tvs = {
  'extend': 'com',
}
tw = {
  'extend': 'com',
}
tz = {
  'extend': 'com',
}
ua = {
  'extend': 'com',
}
ubank = {
  'extend': 'com',
}
ubs = {
  'extend': 'com',
}
uconnect = {
  'extend': 'com',
}
ug = {
  'extend': 'com',
}
university = {
  'extend': 'com',
}
uol = {
  'extend': 'com',
}
ups = {
  'extend': 'com',
}
uy = {
  'extend': 'com',
}
uz = {
  'extend': 'com',
}
vacations = {
  'extend': 'com',
}
vana = {
  'extend': 'com',
}
vanguard = {
  'extend': 'com',
}
vegas = {
  'extend': 'com',
}
ve = {
  'extend': 'com',
}
ventures = {
  'extend': 'com',
}
verisign = {
  'extend': 'com',
}
versicherung = {
  'extend': 'com',
}
vet = {
  'extend': 'com',
}
vg = {
  'extend': 'com',
}
viajes = {
  'extend': 'com',
}
video = {
  'extend': 'com',
}
vig = {
  'extend': 'com',
}
viking = {
  'extend': 'com',
}
villas = {
  'extend': 'com',
}
vin = {
  'extend': 'com',
}
vip = {
  'extend': 'com',
}
virgin = {
  'extend': 'com',
}
visa = {
  'extend': 'com',
}
vision = {
  'extend': 'com',
}
vista = {
  'extend': 'com',
}
vistaprint = {
  'extend': 'com',
}
viva = {
  'extend': 'com',
}
vlaanderen = {
  'extend': 'com',
}
vodka = {
  'extend': 'com',
}
volkswagen = {
  'extend': 'com',
}
volvo = {
  'extend': 'com',
}
vote = {
  'extend': 'com',
}
voting = {
  'extend': 'com',
}
voto = {
  'extend': 'com',
}
voyage = {
  'extend': 'com',
}
vu = {
  'extend': 'com',
}
wales = {
  'extend': 'com',
}
walmart = {
  'extend': 'com',
}
walter = {
  'extend': 'com',
}
wang = {
  'extend': 'com',
}
warman = {
  'extend': 'com',
}
watch = {
  'extend': 'com',
}
webcam = {
  'extend': 'com',
}
weber = {
  'extend': 'com',
}
website = {
  'extend': 'com',
}
wedding = {
  'extend': 'com',
}
wed = {
  'extend': 'com',
}
weibo = {
  'extend': 'com',
}
wf = {
  'extend': 'com',
}
whoswho = {
  'extend': 'com',
}
wien = {
  'extend': 'com',
}
wiki = {
  'extend': 'com',
}
wine = {
  'extend': 'com',
}
win = {
  'extend': 'com',
}
wme = {
  'extend': 'com',
}
wolterskluwer = {
  'extend': 'com',
}
woodside = {
  'extend': 'com',
}
work = {
  'extend': 'com',
}
works = {
  'extend': 'com',
}
world = {
  'extend': 'com',
}
ws = {
  'extend': 'com',
}
wtc = {
  'extend': 'com',
}
wtf = {
  'extend': 'com',
}
xerox = {
  'extend': 'com',
}
xfinity = {
  'extend': 'com',
}
xihuan = {
  'extend': 'com',
}
xin = {
  'extend': 'com',
}
# Invalid dict name
#xn--11b4c3d = {
#  'extend': 'com',
#}
#xn--1qqw23a = {
#  'extend': 'com',
#}
#xn--30rr7y = {
#  'extend': 'com',
#}
#xn--3bst00m = {
#  'extend': 'com',
#}
#xn--3ds443g = {
#  'extend': 'com',
#}
#xn--3e0b707e = {
#  'extend': 'com',
#}
#xn--3oq18vl8pn36a = {
#  'extend': 'com',
#}
#xn--3pxu8k = {
#  'extend': 'com',
#}
#xn--42c2d9a = {
#  'extend': 'com',
#}
#xn--45q11c = {
#  'extend': 'com',
#}
#xn--4gbrim = {
#  'extend': 'com',
#}
#xn--55qw42g = {
#  'extend': 'com',
#}
#xn--55qx5d = {
#  'extend': 'com',
#}
#xn--5su34j936bgsg = {
#  'extend': 'com',
#}
#xn--5tzm5g = {
#  'extend': 'com',
#}
#xn--6frz82g = {
#  'extend': 'com',
#}
#xn--6qq986b3xl = {
#  'extend': 'com',
#}
#xn--80adxhks = {
#  'extend': 'com',
#}
#xn--80ao21a = {
#  'extend': 'com',
#}
#xn--80aqecdr1a = {
#  'extend': 'com',
#}
#xn--80asehdb = {
#  'extend': 'com',
#}
#xn--80aswg = {
#  'extend': 'com',
#}
#xn--90a3ac = {
#  'extend': 'com',
#}
#xn--90ae = {
#  'extend': 'com',
#}
#xn--90ais = {
#  'extend': 'com',
#}
#xn--9dbq2a = {
#  'extend': 'com',
#}
#xn--9et52u = {
#  'extend': 'com',
#}
#xn--9krt00a = {
#  'extend': 'com',
#}
#xn--b4w605ferd = {
#  'extend': 'com',
#}
#xn--c1avg = {
#  'extend': 'com',
#}
#xn--c2br7g = {
#  'extend': 'com',
#}
#xn--cg4bki = {
#  'extend': 'com',
#}
#xn--clchc0ea0b2g2a9gcd = {
#  'extend': 'com',
#}
#xn--czrs0t = {
#  'extend': 'com',
#}
#xn--czru2d = {
#  'extend': 'com',
#}
#xn--d1acj3b = {
#  'extend': 'com',
#}
#xn--d1alf = {
#  'extend': 'com',
#}
#xn--e1a4c = {
#  'extend': 'com',
#}
#xn--efvy88h = {
#  'extend': 'com',
#}
#xn--estv75g = {
#  'extend': 'com',
#}
#xn--fhbei = {
#  'extend': 'com',
#}
#xn--fiq228c5hs = {
#  'extend': 'com',
#}
#xn--fiq64b = {
#  'extend': 'com',
#}
#xn--fiqs8s = {
#  'extend': 'com',
#}
#xn--fiqz9s = {
#  'extend': 'com',
#}
#xn--fjq720a = {
#  'extend': 'com',
#}
#xn--flw351e = {
#  'extend': 'com',
#}
#xn--fzys8d69uvgm = {
#  'extend': 'com',
#}
#xn--hxt814e = {
#  'extend': 'com',
#}
#xn--i1b6b1a6a2e = {
#  'extend': 'com',
#}
#xn--io0a7i = {
#  'extend': 'com',
#}
#xn--j1aef = {
#  'extend': 'com',
#}
#xn--j1amh = {
#  'extend': 'com',
#}
#xn--j6w193g = {
#  'extend': 'com',
#}
#xn--jlq61u9w7b = {
#  'extend': 'com',
#}
#xn--kcrx77d1x4a = {
#  'extend': 'com',
#}
#xn--kprw13d = {
#  'extend': 'com',
#}
#xn--kpry57d = {
#  'extend': 'com',
#}
#xn--kput3i = {
#  'extend': 'com',
#}
#xn--lgbbat1ad8j = {
#  'extend': 'com',
#}
#xn--mgb9awbf = {
#  'extend': 'com',
#}
#xn--mgba3a4f16a = {
#  'extend': 'com',
#}
#xn--mgba7c0bbn0a = {
#  'extend': 'com',
#}
#xn--mgbaam7a8h = {
#  'extend': 'com',
#}
#xn--mgbab2bd = {
#  'extend': 'com',
#}
#xn--mgbca7dzdo = {
#  'extend': 'com',
#}
#xn--mgberp4a5d4ar = {
#  'extend': 'com',
#}
#xn--mgbi4ecexp = {
#  'extend': 'com',
#}
#xn--mgbt3dhd = {
#  'extend': 'com',
#}
#xn--mgbtx2b = {
#  'extend': 'com',
#}
#xn--mgbx4cd0ab = {
#  'extend': 'com',
#}
#xn--mix891f = {
#  'extend': 'com',
#}
#xn--mk1bu44c = {
#  'extend': 'com',
#}
#xn--mxtq1m = {
#  'extend': 'com',
#}
#xn--ngbc5azd = {
#  'extend': 'com',
#}
#xn--ngbe9e0a = {
#  'extend': 'com',
#}
#xn--node = {
#  'extend': 'com',
#}
#xn--nqv7f = {
#  'extend': 'com',
#}
#xn--nqv7fs00ema = {
#  'extend': 'com',
#}
#xn--o3cw4h = {
#  'extend': 'com',
#}
#xn--ogbpf8fl = {
#  'extend': 'com',
#}
#xn--p1acf = {
#  'extend': 'com',
#}
#xn--p1ai = {
#  'extend': 'com',
#}
#xn--pssy2u = {
#  'extend': 'com',
#}
#xn--q9jyb4c = {
#  'extend': 'com',
#}
#xn--qcka1pmc = {
#  'extend': 'com',
#}
#xn--rhqv96g = {
#  'extend': 'com',
#}
#xn--ses554g = {
#  'extend': 'com',
#}
#xn--t60b56a = {
#  'extend': 'com',
#}
#xn--tckwe = {
#  'extend': 'com',
#}
#xn--tiq49xqyj = {
#  'extend': 'com',
#}
#xn--unup4y = {
#  'extend': 'com',
#}
#xn--vermgensberater-ctb = {
#  'extend': 'com',
#}
#xn--vermgensberatung-pwb = {
#  'extend': 'com',
#}
#xn--vhquv = {
#  'extend': 'com',
#}
#xn--vuq861b = {
#  'extend': 'com',
#}
#xn--w4r85el8fhu5dnra = {
#  'extend': 'com',
#}
#xn--w4rs40l = {
#  'extend': 'com',
#}
#xn--wgbl6a = {
#  'extend': 'com',
#}
#xn--xhq521b = {
#  'extend': 'com',
#}
#xn--y9a3aq = {
#  'extend': 'com',
#}
#xn--yfro4i67o = {
#  'extend': 'com',
#}
#xn--ygbi2ammx = {
#  'extend': 'com',
#}
#xn--zfr164b = {
#  'extend': 'com',
#}
xperia = {
  'extend': 'com',
}
xxx = {
  'extend': 'com',
}
xyz = {
  'extend': 'com',
}
yachts = {
  'extend': 'com',
}
yodobashi = {
  'extend': 'com',
}
yoga = {
  'extend': 'com',
}
youtube = {
  'extend': 'com',
}
yt = {
  'extend': 'com',
}
yun = {
  'extend': 'com',
}
zara = {
  'extend': 'com',
}
zip = {
  'extend': 'com',
}
zm = {
  'extend': 'com',
}
zone = {
  'extend': 'com',
}
zuerich = {
  'extend': 'com',
}
