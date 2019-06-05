#!/usr/bin/env python
import os
import sys

import logging
import yaml


PLUGINS = 0
TRIGGERS = 0
ACTIONS = 0
# Example or incomplete plugins
SKIP_PLUGINS = ['dbdemo', 'example', 'example_types']
DEFAULT_TYPES = [ 'bool', 'boolean', 'bytes', 'credential_username_password', 'credential_secret_key', 'credential_asymmetric_key',
                  'date', 'file', 'float', 'int', 'integer', 'number', 'object', 'password', 'python', 'string', '[]boolean', '[]bytes', '[]date', '[]file', '[]string', '[]integer', '[]object',
                ]

def read_plugin_spec(path):
    if not os.path.isfile(path):
        return None
    f = open(path, 'r')
    return yaml.safe_load(f)

def check_args(args):
    if len(args) != 2:
        print('./stats.py [<path/plugin.spec.yaml>|total|go|python|custom_inputs]')
        sys.exit(0)
    return args[1]

def is_yaml(data):
    if type(data) is None:
        logging.error('Error: %s is not a file!', PATH)
        sys.exit(1)

def get_specs(lang='total'):
    spec_list=[]
    for f in os.listdir('.'):
        if f in SKIP_PLUGINS:
            continue
        if os.path.isdir(f):
            spec = f + '/plugin.spec.yaml'
            if os.path.isfile(spec):
                if lang == 'go':
                    if os.path.isdir(f + '/cmd') or \
                        os.path.isdir(f + '/connection') or \
                        os.path.isdir(f + '/actions') or \
                        os.path.isdir(f + '/triggers'):
                        spec_list.append(spec)
                if lang == 'python':
                    if os.path.isdir(f + '/bin') or os.path.isdir(f + '/setup.py'):
                        spec_list.append(spec)
                if lang == 'total':
                    spec_list.append(spec)
    return spec_list

def count_components(plugin, component=None):
    if component not in plugin:
        return 0
    if plugin[component] is None:
        return 0
    return len(plugin[component])

def list_components(plugin, component=None, behavior=None):
    components=[]
    if component not in plugin:
        return components
    if plugin[component] is None:
        return components
    for name in plugin[component]:
        if behavior == 'custom_inputs':
            if 'input' not in plugin[component][name]:
                continue
            if plugin[component][name]['input'] is None:
                continue
            for var in plugin[component][name]['input']:
                tipe = plugin[component][name]['input'][var]['type']
                if tipe in DEFAULT_TYPES:
                    continue
                print('  Found non-builtin input type: {}'.format(tipe))
                components.append(name)
        else:
            components.append(name)
    return components

def gen_stats(plugin, behavior=None):

    triggers = list_components(plugin, component='triggers', behavior=behavior)
    actions = list_components(plugin, component='actions', behavior=behavior)

    if behavior == 'custom_inputs':
        result = len(triggers) + len(actions)
        if result == 0:
            return

    print('Name: %s' % plugin.get('name'))
    print('  Title: %s' % plugin.get('title'))
    print('  Description: %s' % plugin.get('description'))
    print('  Vendor: %s' % plugin.get('vendor'))
    print('  Version: %s' % plugin.get('version'))
    trigger_count = count_components(plugin, component='triggers')
    action_count  = count_components(plugin, component='actions')
    print('  Triggers: %d' % trigger_count)
    print('  Actions: %d' % action_count)

    if trigger_count > 0:
        print('  Trigger List: %s' % ' '.join(map(str, triggers)))
    if action_count > 0:
        print('  Action List: %s' % ' '.join(map(str, actions)))

def gen_total_stats(lang):
    global PLUGINS
    global TRIGGERS
    global ACTIONS
    spec_list = get_specs(lang)
    for path in spec_list:
        data = read_plugin_spec(path)
        is_yaml(data)
        PLUGINS += 1
        TRIGGERS += count_components(data, component='triggers')
        ACTIONS += count_components(data, component='actions')
        gen_stats(data)

    print('''
Total:
  Plugins: %d
  Triggers: %d
  Actions: %d
  ''' % (PLUGINS, TRIGGERS, ACTIONS))

def gen_custom_input_stats():
    spec_list = get_specs()
    for path in spec_list:
        data = read_plugin_spec(path)
        is_yaml(data)
        gen_stats(data, behavior='custom_inputs')

ARG = check_args(sys.argv)

if ARG == 'total':
    gen_total_stats(ARG)
    sys.exit(0)

if ARG == 'go':
    gen_total_stats(ARG)
    sys.exit(0)

if ARG == 'python':
    gen_total_stats(ARG)
    sys.exit(0)

if ARG == 'custom_inputs':
    gen_custom_input_stats()
    sys.exit(0)

# Stats for single plugin
PATH = ARG
DATA = read_plugin_spec(PATH)
is_yaml(DATA)
gen_stats(DATA)
sys.exit(0)
