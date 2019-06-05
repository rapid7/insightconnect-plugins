import komand
import requests


def get_domain(rec):
    return clean_dict_recursive({
            'primary_domain': rec.get('primaryDomain'),
            'ever_compromised': rec.get('everCompromised'),
            'dynamic_dns': rec.get('dynamicDns'),
            'subdomains': rec.get('subdomains'),
            'tld': rec.get('tld'),
            'tags': rec.get('tags'),
            })


def get_address(rec):
    return clean_dict_recursive({
            'autonomous_system_name': rec.get('autonomousSystemName'),
            'autonomous_system_number': rec.get('autonomousSystemNumber'),
            'country': rec.get('country'),
            'ever_compromised': rec.get('everCompromised'),
            'latitude': rec.get('latitude'),
            'longitude': rec.get('longitude'),
            'network': rec.get('network'),
            'sinkhole': rec.get('sinkhole'),
            'tags': rec.get('tags'),
            })


def clean_dict_recursive(obj):
    obj = komand.helper.clean_dict(obj)
    for k, v in obj.items():
        if isinstance(v, dict):
            obj[k] = clean_dict_recursive(v)

    return obj


def get_project_by_name(proj_name, auth):
    r = requests.get('https://api.passivetotal.org/v2/project', auth=auth).json()
    for project in r[u'results']:
        if project[u'name'] == proj_name:
            return project[u'guid']
    raise Exception('Project not found')
