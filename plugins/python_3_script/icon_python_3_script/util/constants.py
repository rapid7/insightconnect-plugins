INDENTATION_CHARACTER = " " * 4
DEFAULT_ENCODING = "utf-8"
DEFAULT_PROCESS_TIMEOUT = 5 * 60

RUN_FUNCTION_TEMPLATE = """import sys
from argparse import ArgumentParser

sys.path.append("/var/cache/python_dependencies/lib/python3.9/site-packages")

parser = ArgumentParser()
parser.add_argument("--username")
parser.add_argument("--password")
parser.add_argument("--secret_key")

arguments = parser.parse_args()
username = arguments.username
password = arguments.password
secret_key = arguments.secret_key

{function_}
sys.stdout.write("{execution_id}" + str({function_name}({parameters})))
"""
