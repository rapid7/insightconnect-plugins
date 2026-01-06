import logging
import os
import json
from types import SimpleNamespace
from zenpy.lib.api_objects import Comment, Ticket
import zenpy

from icon_zendesk.connection import Connection
from icon_zendesk.connection.schema import Input

from insightconnect_plugin_runtime.exceptions import PluginException


class Util:
    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                Input.TOKEN: {"secretKey": "TOKEN"},
                Input.SUBDOMAIN: "testdomain",
                Input.EMAIL: "test@test.com",
            }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename):
                self.filename = filename

            def read(self):
                if self.filename == "error":
                    raise PluginException(preset=PluginException.Preset.SERVER_ERROR)
                if self.filename == "empty":
                    return {}
                file_path = os.path.join(
                    os.path.dirname(os.path.realpath(__file__)), "example_api_responses", f"{self.filename}.json.resp"
                )
                file_text = Util.read_file_to_string(file_path)
                returned_obj = json.loads(file_text, object_hook=lambda d: SimpleNamespace(**d))
                return returned_obj

            @property
            def ticket(self):
                return self.read()

        if len(args) > 0:
            if isinstance(args[0], Ticket):
                if "CreateTicket" in args[0].description:
                    return MockResponse("create_ticket_response")
                elif "Exception" in args[0].description:
                    raise zenpy.lib.exception.RatelimitBudgetExceeded
                # put Update ticket case here
                if "closed" in args[0].status:
                    return MockResponse("update_ticket_response")
            else:
                if hasattr(args[0], "id"):
                    if args[0].id == 5:
                        return MockResponse("user_suspended_response").read()
                    elif args[0].id == 6:
                        return MockResponse("user_suspended_fails").read()
        if "id" in kwargs:
            if kwargs["id"] == 0:
                return MockResponse("create_ticket_response")
            elif kwargs["id"] == -1:
                # this exception is raised upon a bad response from server
                raise zenpy.lib.exception.APIException("Bad ID Input")
            elif kwargs["id"] == 1:
                # update ticket happy path
                return MockResponse("create_ticket_response").read()
            elif kwargs["id"] == 1902872923584:
                # show user happy path
                return MockResponse("show_user_response").read()
            elif kwargs["id"] == 5:
                return MockResponse("user_suspended_response").read()
            elif kwargs["id"] == 6:
                return MockResponse("user_suspended_fails").read()
            elif kwargs["id"] == 7:
                # show memberships happy path
                return MockResponse("show_memberships_response").read()
        if "type" in kwargs:
            if kwargs["type"] == "organization":
                return MockResponse("search_response_organization").read()
            elif kwargs["type"] == "ticket":
                return MockResponse("search_response_ticket").read()
            elif kwargs["type"] == "user":
                return MockResponse("search_response_user").read()
            elif kwargs["type"] == "error":
                raise zenpy.lib.exception.TooManyValuesException
            elif kwargs["type"] == "error 2":
                raise zenpy.lib.exception.SearchResponseLimitExceeded
            elif kwargs["type"] == "empty":
                return []
        if "user" in kwargs:
            if kwargs["user"] == 1:
                return MockResponse("show_memberships_response").read()
            elif kwargs["user"] == -1:
                raise PluginException
            elif kwargs["user"] == -2:
                raise zenpy.lib.exception.TooManyValuesException
            elif kwargs["user"] == -3:
                raise zenpy.lib.exception.SearchResponseLimitExceeded
            elif kwargs["user"] == -4:
                raise zenpy.lib.exception.RecordNotFoundException
            elif kwargs["user"] == -5:
                raise zenpy.lib.exception.ZenpyCacheException
            elif kwargs["user"] == -6:
                raise zenpy.lib.exception.RatelimitBudgetExceeded

    @staticmethod
    def read_file_to_string(filename):
        with open(filename, "rt") as my_file:
            return my_file.read()
