import os
import sys
from unittest import TestCase
from unittest.mock import Mock

import botocore
import botocore.exceptions
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_dynamodb.util.api import AWSCommunicationAPI
from parameterized.parameterized import param, parameterized

sys.path.append(os.path.abspath("../"))


class StubApiClient(AWSCommunicationAPI):
    def __init__(self, *args, **kwargs):
        self.client = Mock()
        ResourceNotFoundException = type(
            "ResourceNotFoundException", (BaseException,), {"response": "some freaking response"}
        )
        self.client.configure_mock(**{"exceptions.ResourceNotFoundException": ResourceNotFoundException})

    def raises_resource_not_found(self):
        raise self.client.exceptions.ResourceNotFoundException()

    def raises_endpoint_connection_error(self):
        raise botocore.exceptions.EndpointConnectionError

    def raises_param_validation_error(self):
        raise botocore.exceptions.ParamValidationError

    def raises_client_error(self):
        raise botocore.exceptions.ClientError("error", "scan")

    def raises_attribute_error(self):
        raise AttributeError()

    def raises_exception(self):
        raise Exception()


class TestApiClient(TestCase):
    def test__handle_api_call_ok(self):
        client = StubApiClient()
        client._handle_rest_call(lambda: {}, {})

    @parameterized.expand(
        [
            param("raises_endpoint_connection_error"),
            param("raises_resource_not_found"),
            param("raises_param_validation_error"),
            param("raises_client_error"),
            param("raises_attribute_error"),
            param("raises_exception"),
        ]
    )
    def test__handle_api_call_raises(self, attr_name):
        with self.assertRaises(PluginException) as ctx:
            client = StubApiClient()
            client._handle_rest_call(client.__getattribute__(attr_name), {})
