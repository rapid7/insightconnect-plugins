INDENTATION_CHARACTER = " " * 4
DEFAULT_ENCODING = "utf-8"
DEFAULT_PROCESS_TIMEOUT = 30

RUN_FUNCTION_TEMPLATE = """import sys
import json
from argparse import ArgumentParser

sys.path.append("/var/cache/python_dependencies/lib/python3.9/site-packages")

parser = ArgumentParser()
parser.add_argument("--username")
parser.add_argument("--password")
parser.add_argument("--secret_key")
parser.add_argument("--secret_credential_1")
parser.add_argument("--secret_credential_2")
parser.add_argument("--secret_credential_3")

arguments = parser.parse_args()
username = arguments.username
password = arguments.password
secret_key = arguments.secret_key
secret_credential_1 = arguments.secret_credential_1
secret_credential_2 = arguments.secret_credential_2
secret_credential_3 = arguments.secret_credential_3

{function_}
sys.stdout.write("{execution_id}" + json.dumps({function_name}({parameters})))
"""
