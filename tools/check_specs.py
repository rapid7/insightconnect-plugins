#!/usr/bin/env python

import logging
import os
import sys

from check_spec import validate

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

BASE_DIR = os.path.dirname(os.path.realpath(__file__)) + '/..'

def get_plugin_spec(spec_dir):
    """ get_plugin_spec checks if there is a spec file in the dir and returns the path """
    if not os.path.isdir(spec_dir):
        return None

    spec_path = os.path.join(BASE_DIR, spec_dir, 'plugin.spec.yaml')
    if not os.path.exists(spec_path):
        return None

    return os.path.abspath(spec_path)

if __name__ == '__main__':
    for directory in os.listdir(BASE_DIR):
        spec = get_plugin_spec(directory)
        if spec:
            validate(spec)
