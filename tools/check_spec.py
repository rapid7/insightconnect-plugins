#!/usr/bin/env python

import subprocess
import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

RED = '\033[31m'
YELLOW = '\033[33m'
BOLD = '\033[1m'
CEND = '\033[0m'

def check_args(args):
    """ check_args ensures we are running the script with the right number of arguments"""
    if len(args) != 2:
        print('./check_spec.py <path/plugin.spec.yaml>')
        sys.exit(0)

def must_exec(cmd):
    """ must_exec ensures the executed commands are successful """
    print('')
    print('[' + YELLOW + '*' + CEND + ']' + ' ' + BOLD + "Validating spec with js-yaml" + CEND)
    exit_code = 0
    try:
        subprocess.check_output(cmd)
        exit_code = 0
        print('[' + YELLOW + 'SUCCESS' + CEND + ']' + " Passes js-yaml spec check" + "\n")
    except OSError:
        print('[' + RED + 'FAIL' + CEND + ']' + " js-yaml is not installed, try: node install npm")
    except subprocess.CalledProcessError as ex:
        exit_code = ex.returncode
        print('[' + RED + 'FAIL' + CEND + ']' + " Failed js-yaml spec check")
        sys.exit(1)

def validate(spec_path):
    """ validate validates a yaml file at the spec_path """
    cmd = ["js-yaml", spec_path]
    must_exec(cmd)

if __name__ == '__main__':
    check_args(sys.argv)
    validate(sys.argv[1])
