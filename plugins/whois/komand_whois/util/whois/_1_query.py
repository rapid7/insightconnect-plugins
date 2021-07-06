#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import time
import sys
import os


PYTHON_VERSION = sys.version_info[0]
CACHE = {}
CACHE_MAX_AGE = 60 * 60 * 48  # 48h

try:
    import json
except ImportError:
    import simplejson as json


def cache_load(cf):
    if not os.path.isfile(cf): return
    global CACHE
    f = open(cf, 'r')
    try:
        CACHE = json.load(f)
    except:
        pass
    f.close()


def cache_save(cf):
    global CACHE
    f = open(cf, 'w')
    json.dump(CACHE, f)
    f.close()


def do_query(dl, host=None, force=0, cache_file=None, slow_down=0, ignore_returncode=0):
    k = '.'.join(dl)
    if cache_file: cache_load(cache_file)
    if force or k not in CACHE or CACHE[k][0] < time.time() - CACHE_MAX_AGE:
        CACHE[k] = (
        int(time.time()),
        _do_whois_query(dl, host, ignore_returncode),
        )
        if cache_file: cache_save(cache_file)
        if slow_down: time.sleep(slow_down)

    return CACHE[k][1]


def _do_whois_query(dl, host, ignore_returncode):
    """
    Linux 'whois' command wrapper
    """
    if host == None:
        p = subprocess.Popen(['whois', '.'.join(dl)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    else:
        p = subprocess.Popen(['whois', '-h', host, '.'.join(dl)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    r = p.communicate()[0]
    if PYTHON_VERSION == 3:
        try:
            r = r.decode()
        except UnicodeDecodeError:
            r = r.decode('ISO-8859-1')

    if not ignore_returncode and p.returncode != 0: raise Exception(r)
    return r
