#!/usr/bin/python
import json
import os


SPECS_DIR = "_json_specs"

os.chdir("..")
plugins_root = os.getcwd()
plugin_directories = os.listdir()  # Essentially a list of plugin names
os.mkdir(SPECS_DIR)

for plugin_directory in plugin_directories:
    print("Parsing %s" % plugin_directory)
    spec = os.path.join(plugins_root, plugin_directory, 'plugin.spec.yaml')
    if os.path.isfile(spec):
        with open(spec, 'r') as spec_file:
            spec_contents = spec_file.read()
            output = {'spec':  spec_contents}

            os.chdir(os.path.join(plugins_root, SPECS_DIR))
            with open(plugin_directory + '.json', 'w') as outfile:
                json.dump(output, outfile)
