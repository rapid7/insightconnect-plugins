import json
import os
from typing import Callable
from unittest import mock

import requests
from icon_azure_compute.connection.schema import Input

from utils import STUB_CONNECTION

BASE_URL = "https://management.azure.com"
OAUTH_2_URL = "https://login.microsoftonline.com"

TENANT_ID = STUB_CONNECTION.get(Input.TENANT_ID)
CLIENT_ID = STUB_CONNECTION.get(Input.CLIENT_ID)
CLIENT_SECRET = STUB_CONNECTION.get(Input.CLIENT_SECRET)
API_VERSION = STUB_CONNECTION.get(Input.API_VERSION)

STUB_SUBSCRIPTION_ID = "ExampleSubscriptionID"
STUB_RESOURCE_GROUP_NAME = "ExampleResourceGroupName"

STUB_AVAILABILITY_SET_NAME = "ExampleAvailabilitySetName"
STUB_LOCATION_NAME = "ExampleLocationName"
STUB_VM_NAME = "ExampleVmName"


class MockResponse:
    def __init__(self, filename: str, status_code: int, text: str = "") -> None:
        self.filename = filename
        self.status_code = status_code
        self.text = text

    def json(self):
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file:
            return json.load(file)


def mocked_request(side_effect: Callable, method: str) -> None:
    mock_function = requests
    setattr(mock_function, method, mock.Mock(side_effect=side_effect))


def mock_conditions(url: str, status_code: int) -> MockResponse:
    if url == f"{OAUTH_2_URL}/{TENANT_ID}/oauth2/token/":
        return MockResponse("oauth2-token", status_code)
    elif (
        url == f"{BASE_URL}/subscriptions/{STUB_SUBSCRIPTION_ID}/resourceGroups/{STUB_RESOURCE_GROUP_NAME}/providers/"
        f"Microsoft.Compute/availabilitySets/{STUB_AVAILABILITY_SET_NAME}/vmSizes?api-version={API_VERSION}"
    ):
        return MockResponse("availability_set_vm", status_code)
    elif (
        url == f"{BASE_URL}/subscriptions/{STUB_SUBSCRIPTION_ID}/resourceGroups/"
        f"{STUB_RESOURCE_GROUP_NAME}/providers/Microsoft.Compute/virtualMachines/"
        f"{STUB_VM_NAME}?api-version={API_VERSION}"
    ):
        return MockResponse("info_vm", status_code)
    elif (
        url
        == f"{BASE_URL}/subscriptions/{STUB_SUBSCRIPTION_ID}/resourceGroups/{STUB_RESOURCE_GROUP_NAME}/providers/Microsoft.Compute/virtualmachines?api-version={API_VERSION}"
    ):
        return MockResponse("list_vm", status_code)
    elif (
        url
        == f"{BASE_URL}/subscriptions/{STUB_SUBSCRIPTION_ID}/providers/Microsoft.Compute/virtualmachines?api-version={API_VERSION}"
    ):
        return MockResponse("vm_in_subscription", status_code)
    elif (
        url
        == f"{BASE_URL}/subscriptions/{STUB_SUBSCRIPTION_ID}/resourceGroups/{STUB_RESOURCE_GROUP_NAME}/providers/Microsoft.Compute/virtualMachines/{STUB_VM_NAME}/vmSizes?api-version={API_VERSION}"
    ):
        return MockResponse("sizes_vm", status_code)
    elif (
        url
        == f"{BASE_URL}/subscriptions/{STUB_SUBSCRIPTION_ID}/providers/Microsoft.Compute/locations/{STUB_LOCATION_NAME}/vmSizes?api-version={API_VERSION}"
    ):
        return MockResponse("sizes_vm_subscription", status_code)
    elif any(
        (
            url
            == f"{BASE_URL}/subscriptions/{STUB_SUBSCRIPTION_ID}/resourceGroups/{STUB_RESOURCE_GROUP_NAME}/providers/Microsoft"
            f".Compute/virtualMachines/{STUB_VM_NAME}?api-version={API_VERSION}",
            url
            == (
                f"{BASE_URL}/subscriptions/{STUB_SUBSCRIPTION_ID}/resourceGroups/{STUB_RESOURCE_GROUP_NAME}/providers/Microsoft"
                f".Compute/virtualMachines/{STUB_VM_NAME}/generalize?api-version={API_VERSION}"
            ),
            url
            == f"{BASE_URL}/subscriptions/{STUB_SUBSCRIPTION_ID}/resourceGroups/{STUB_RESOURCE_GROUP_NAME}/providers/Microsoft.Compute/virtualMachines/{STUB_VM_NAME}/restart?api-version={API_VERSION}",
            url
            == f"{BASE_URL}/subscriptions/{STUB_SUBSCRIPTION_ID}/resourceGroups/{STUB_RESOURCE_GROUP_NAME}/providers/Microsoft"
            f".Compute/virtualMachines/{STUB_VM_NAME}/capture?api-version={API_VERSION}",
            url
            == f"{BASE_URL}/subscriptions/{STUB_SUBSCRIPTION_ID}/resourceGroups/{STUB_RESOURCE_GROUP_NAME}/providers/Microsoft.Compute/virtualMachines/{STUB_VM_NAME}/start?api-version={API_VERSION}",
            url
            == f"{BASE_URL}/subscriptions/{STUB_SUBSCRIPTION_ID}/resourceGroups/{STUB_RESOURCE_GROUP_NAME}/providers/Microsoft.Compute/virtualMachines/{STUB_VM_NAME}/deallocate?api-version={API_VERSION}",
            url
            == f"{BASE_URL}/subscriptions/{STUB_SUBSCRIPTION_ID}/resourceGroups/{STUB_RESOURCE_GROUP_NAME}/providers/Microsoft.Compute/virtualMachines/{STUB_VM_NAME}/powerOff?api-version={API_VERSION}",
        )
    ):
        return MockResponse("", status_code)
    elif "InvalidJSON" in url:
        return MockResponse("invalid_json", status_code)
    elif "Exception" in url:
        raise Exception("Exception")
    raise Exception("Response has been not implemented")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], 200)


def mock_request_202(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], 202)


def mock_request_500(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], 500)
