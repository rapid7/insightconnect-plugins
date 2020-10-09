#!/usr/bin/env python
import json
from past.builtins import basestring
from future.utils import iteritems
import sys
from collections import OrderedDict
from jinja2 import Template
import os


# set to true if you don't want to try to generate nested types
OBJECTS_ONLY = False

filename = sys.argv[1]

this_dir = os.path.dirname(__file__)
rel_path = "templates/template.json_to_spec.j2"
abs_path_template = os.path.join(this_dir,rel_path)

with open(filename) as data_file:    
    data = json.load(data_file)

with open(abs_path_template) as f:
    spec_template = Template(f.read())



type_refs = {}
types = OrderedDict()
output = OrderedDict()

def type_name_unused(name):
    if not name in types:
        return name
    i = 0 
    while True:
        name = '%s_%d' % (name, i)
        if not name in types:
            return name
        i += 1
    
def detect_type(name, value, level=0):
   if isinstance(value, basestring):
       return 'string'
   if isinstance(value, bool):
       return 'boolean'
   if isinstance(value, int):
       return 'integer'
   if isinstance(value, float):
       return 'float'
   if isinstance(value, list):
       if value:
           return '"[]{}"'.format(detect_type(name, value[0], level + 1))
       else:
           return '[]object'

   if isinstance(value, dict):
       keys = sorted(value.keys())
       if len(keys) == 0 or OBJECTS_ONLY: 
           return 'object'
       list_key = str(keys)
       if list_key in type_refs:
           return type_refs[list_key]

       type_name = type_name_unused(name)
       typ = {}
       for k in keys:
           typ[str(k)] = {
                        'title': str(k).replace("_", " ").title(),
                        'type': detect_type(k, value[k]),
                        'description': str(k).replace("_", " ").capitalize(),
                        }
       type_refs[list_key] = type_name
       types[str(type_name)] = typ
       return str(type_name)


def dump_to_spec(sections):
    return spec_template.render(sections=sections)


def build_spec(item):
    if not isinstance(item, dict):
        raise "Not a object. You must start with a JSON object, not an array or any other type: %s" % item
    for key, value in iteritems(item):
        output[str(key)] = {
                'title': str(key).replace("_", " ").title(),
                'type': detect_type(key, value),
                'description': str(key).replace("_", " ").capitalize(),
                }
    typesection = { 'types': types }
    outputsection = { 'output': output }
    sections = {}
    sections.update(typesection)
    sections.update(outputsection)

    print(dump_to_spec(sections))


build_spec(data)
