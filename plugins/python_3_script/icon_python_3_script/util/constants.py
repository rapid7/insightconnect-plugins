DEFAULT_ENCODING = "utf-8"
DEFAULT_PROCESS_TIMEOUT = 30
DEFAULT_CONNECTION_TIMEOUT = 60
ENVIRONMENT_BASE_DIRECTORY = "/workspace/cache/python_dependencies/environments"

RUN_FUNCTION_TEMPLATE = """import os
import sys
import json

username = os.environ.get("SCRIPT_USERNAME")
password = os.environ.get("SCRIPT_PASSWORD")
secret_key = os.environ.get("SCRIPT_SECRET_KEY")
secret_credential_1 = os.environ.get("SCRIPT_SECRET_CREDENTIAL_1")
secret_credential_2 = os.environ.get("SCRIPT_SECRET_CREDENTIAL_2")
secret_credential_3 = os.environ.get("SCRIPT_SECRET_CREDENTIAL_3")

{function_}
sys.stdout.write("{execution_id}" + json.dumps({function_name}({parameters})))
"""
