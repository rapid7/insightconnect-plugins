import requests
import json
import komand


def query_api(request_url, token):
    try:
        if token == "" or token == None:
            results = requests.get(request_url)
        else:
            headers = {"Authorization": token}
            results = requests.get(request_url, headers=headers)
        body = json.loads(results.text)
        cleaned_body = clean_dict_recursive(body)
        return {'response': cleaned_body}
    except:
        return {'response': {'Errors': [{'Error': 'Unknown Error'}]}}


def test_api(request_url, token):
    try:
        if token == "" or token == None:
            results = requests.get(request_url)
        else:
            headers = {"Authorization": token}
            results = requests.get(request_url, headers=headers)
        results = requests.get(request_url, headers=headers)
        if results.status_code == 200:
            return {'response': {'CommandArgument': 'API Up, Auth Successful'}}
        else:
           return { 'response': {'Errors': [{'Error': 'API Returned Failing Status Code'}]}}
    except:
        return { 'response': {'Errors': [{'Error': 'Connection Error'}]}}


def clean_dict_recursive(dic):
    dictionary = dict(dic)
    for k,v in dic.items():
        if type(v) == dict:
            v = clean_dict_recursive(v)
        if type(v) == list:
            v = handle_missing_strings(v)
        if v == None:
            del dictionary[k]
    return dictionary


def handle_missing_strings(array):
    for i in array:
        if type(i) == dict:
            for k,v in i.items():
                if v == None:
                    i[k] = ""
    return array
