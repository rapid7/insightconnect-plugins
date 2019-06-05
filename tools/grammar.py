#!/usr/bin/env python3
import yaml
import os, sys
import logging
import requests

HEADERS = { 'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json' }
URL = 'https://languagetool.org/api/v2/check'
RED = '\033[31m'
YELLOW = '\033[33m'
BOLD = '\033[1m'
CEND = '\033[0m'

def read_plugin_spec(path):
    if not os.path.isfile(path):
        return None
    f = open(path, 'r')
    return yaml.safe_load(f)

def check_args(args):
    argc = len(args)
    if argc != 3:
      print('./grammar.py <path/plugin.spec.yaml> [print|check]')
      sys.exit(0)

def is_yaml(data):
    if type(data) is None:
      logging.error('Error: %s is not a file!', path)
      sys.exit(1)

def get_text(data: dict) -> list:
    # YAML sections to check
    sections = [ 'actions', 'triggers', 'connection' ]
    # List of checked results
    sentences = []
    
    # Iterate over descriptions
    for section in sections:
        if section in data:
            for top_level in data[section]:
                for description in data[section][top_level]:
                    if isinstance(data[section][top_level][description], str):
                        sentences.append(data[section][top_level][description])
                    if isinstance(data[section][top_level][description], dict):
                        for bottom_level in data[section][top_level][description]:
                            sentences.append(data[section][top_level][description][bottom_level]['description'])

    # Get plugin's description
    if 'description' in data:
        sentences.append(data['description'])

    return sentences

check_args(sys.argv)
path = sys.argv[1]
arg = sys.argv[2]
plugin = path.split('/')[0]
data = read_plugin_spec(path)
is_yaml(data)
sentences = get_text(data)

if arg == 'print':
    for line in sentences:
        print(line)

if arg == 'check':

    for sentence in sentences:
    
        try:
            data = { 'text': sentence, 'language': 'en-US', 'enabledOnly': 'false' }
            response = requests.post(URL, data=data, headers=HEADERS)
            data = response.json()
            response.raise_for_status()
        except:
            logging.error("Request failed for sentence '{}'".format(sentence))
            continue
        
        if 'matches' in data:
            # Number of issues
            count = len(data['matches'])
            for match in data['matches']:
                # {'message': 'Possible spelling mistake found', 'shortMessage': 'Spelling mistake', 'replacements': [{'value': 'Woman'}, {'value': 'Roman'}, {'value': 'Domain'}, {'value': 'Oman'}]
                if 'message' in match:
                    suggestions = list(map(lambda x: x.popitem()[1], match['replacements']))
                    print(f"[{RED}FAIL{CEND}] {match['message']} in sentence '{sentence}'. Possible suggestions: {suggestions}")
    print(f"[{YELLOW}SUCCESS{CEND}] Grammar and spelling check complete")
