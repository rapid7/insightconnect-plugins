#!/usr/bin/env python

import os
import subprocess
from datetime import datetime
import json
import hashlib
import sys
from os import stat
from pwd import getpwuid

file_paths = []
json_output = {"malicious_files": []}
sha1 = hashlib.sha1()

# Get output from scan result.
def open_file(s):
       with open(s,'r') as f:
               f.next()
               f.next()
               f.next()
               for line in f:
                       if "FOUND" in line:
                               x = line.split(':')
                               file_paths.append(x[0])
       if len(file_paths) == 0:
               print {}
               return
       for p in file_paths:
               filename = p
               get_time = os.path.getctime(p)
               format_time = datetime.fromtimestamp(get_time).strftime('%Y-%m-%d %H:%M:%S')
               hashvalue = hashlib.sha1(filename).hexdigest()
               owner_name = getpwuid(stat(filename).st_uid).pw_name
               json_output["malicious_files"].append({"file":p, "owner":owner_name, "hash_value":hashvalue, "time_created":format_time})

       print json.dumps(json_output)

# Scan the directory
def get_scan():
       if (len(sys.argv))!= 2:
               print "Usage: python clam_av.py <Directory Path>"
       else:
               _now = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
               _file= "Result" + _now + ".txt"
               s = sys.argv[1]
               d = '/tmp'
               try:
                       subprocess.check_call(["clamscan","--quiet", "-r", s, "-l", d +"/"+ _file])
               except OSError as e :
                       # Error 0 - Clamscan is not installed on host
                       print("0")
                       return
               except :
                       pass
               open_file(d + "/" + _file)

get_scan()
