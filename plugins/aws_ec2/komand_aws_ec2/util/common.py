import botocore.exceptions
import botocore.response
import json
import base64
import datetime
import re
import requests

from komand.action import Action


class AWSAction(Action):
    """
    Abstract class for handling any aws-cli request.
    """

    def __init__(self, name, description, input, output, aws_service, aws_command, pagination_helper=None):
        """

        Initializes a new AwsAction object.

        :param name: The name of the action. Should be snake case.
        :param description: The description fo the action.
        :param input: The input schema object
        :param output: The output schema object
        :param aws_service: The AWS service. Should be snake case.
        :param aws_command: The type of request to invoke. Should be snake case.
        """
        super().__init__(name=name, description=description, input=input, output=output)
        self.aws_service = aws_service
        self.aws_command = aws_command
        self.pagination_helper = pagination_helper

    def handle_rest_call(self, client_function, params):

        helper = self.connection.helper

        # Format the input parameters for the botocall call
        try:
            params = helper.format_input(params)
        except Exception as e:
            self.logger.error("Unable to format input parameters")
            raise e

        # Execute the botocore function
        try:
            response = client_function(**params)
        except botocore.exceptions.EndpointConnectionError as e:
            self.logger.error(
                "Error occurred when invoking the aws-cli: Unable to reach the url endpoint."
                + " Check the connection region is correct."
            )
            raise e
        except botocore.exceptions.ParamValidationError as e:
            self.logger.error("Error occurred when invoking the aws-cli. Input parameters were missing or incorrect")
            raise e
        except botocore.exceptions.ClientError as e:
            self.logger.error(
                "Error occurred when invoking the aws-cli. Check client connection keys and input arguments."
            )
            raise e
        except Exception as e:
            self.logger.error("Error occurred when invoking the aws-cli.")
            raise e

        # Format the output parameters for the komand action output schema
        try:
            if "properties" in self.output.schema:
                response = helper.format_output(self.output.schema, response)
            else:
                response = helper.format_output(None, response)
        except Exception as e:
            self.logger.error("Unable to format output parameters")
            raise e

        return response

    def run(self, params={}):
        """
        Executes the aws-cli command with the given input parameters.

        Exceptions are raised if:
        * The command cannot be found inside botocore.
        * The input parameters are invalid.
        * The output parameters cannot be formatted.
        * The call to AWS fails

        :param self: The action object.
        :param params: The input parameters, which adhere to the input schema
        :return: the output parameters, which adhere to the output schema
        """
        client = self.connection.client

        # There exists a function for each command in the service client
        # object.
        try:
            client_function = getattr(client, self.aws_command)
        except AttributeError as e:
            self.logger.error('Unable to find the command "' + self.aws_service + " " + self.aws_command + '"')
            raise e

        response = self.handle_rest_call(client_function, params)

        # Handle possible paginatin if this action supports pagination.
        if self.pagination_helper:
            while self.pagination_helper.handle_pagination(params, response):
                self.logger.info("Response was paginated. Performing another call.")
                response, max_hit = self.pagination_helper.merge_responses(
                    params, self.handle_rest_call(client_function, params), response
                )
                if max_hit:
                    break
            self.pagination_helper.remove_keys(response)

        return response

    def test(self, params={}):
        """
        Tests that the aws-cli command is executable with the given connection.

        This tests simply curls the url endpoint to check for internet connectivity.

        :param self: The action object.
        :param params: The input parameters.
        :return: None on success, exception on failure.
        """

        client = self.connection.client
        helper = self.connection.helper

        endpoint = client._endpoint.host
        r = requests.get(endpoint)

        assert r.ok  # noqa: B101

        if "properties" in self.output.schema:
            response = helper.format_output(self.output.schema, {})
        else:
            response = helper.format_output(None, {})

        return response


class ActionHelper:
    """
    Helper class for invoking AWS.
    """

    @staticmethod
    def to_upper_camel_case(snake_str):
        components = snake_str.split("_")
        # We capitalize the first letter of each component except the first one
        # with the 'title' method and join them together.
        return "".join(x.title() for x in components)

    @staticmethod
    def format_input(params):
        """
        Formats the input parameters to be consumable by botocore.

        Keys are formatted to upper camel case.

        Input parameters should be left out of the botocore request if the variable is:
        * an empty list
        * an empty dict
        * a zero-length string

        :param params: The input parameters.
        :return: The formatted input parameters as a new dictionary.
        """
        formatted_params = {}

        # Drop invalid empty parameters
        for k, v in params.items():
            if isinstance(v, list) and (len(v) == 0):
                continue
            elif isinstance(v, dict) and (len(v.keys()) == 0):
                continue
            elif isinstance(v, str) and (v == ""):
                continue
            else:
                formatted_params[k.replace("$", "")] = v

        formatted_params = ActionHelper.convert_all_to_upper_camel_case(formatted_params)

        return formatted_params

    @staticmethod
    def get_empty_output(output_schema):
        """
        Returns a dictionary which maps output parameters to default values.

        To adhere to an action's output schema, empty lists and dictionaries must exist.

        :param output_schema: The output schema.
        :return: A dictionary which maps properties to empty values.
        """
        empty_output = {}
        if "properties" in output_schema:
            output_properties = output_schema["properties"]
            for prop_key in output_properties:
                prop = output_properties[prop_key]
                if "type" in prop:
                    if prop["type"] == "array":
                        empty_output[prop_key] = []
                    elif prop["type"] == "object":
                        empty_output[prop_key] = {}
                elif "$ref" in prop:
                    prop = output_schema["definitions"][prop_key]
                    if "type" in prop:
                        if prop["type"] == "array":
                            empty_output[prop_key] = []
                        elif prop["type"] == "object":
                            empty_output[prop_key] = {}

        empty_output["response_metadata"] = {"request_id": "", "http_status_code": 0}
        return empty_output

    def fix_output_types(self, output):
        """
        Formats the output of a botocore call to be correct types.

        The botocore response dictionary contains types which are not supported by Komand.

        * Dictionary values are recursively formatted
        * List values are recursively formatted
        * Primitive types are matched as best as possible

        :param output: the output dictionary.
        :return: A formatted output dictionary.
        """

        if isinstance(output, dict):
            new_dict = {}
            for key in output:
                new_dict[key] = self.fix_output_types(output[key])
            return new_dict
        elif isinstance(output, list):
            new_list = []
            for item in output:
                new_list.append(self.fix_output_types(item))
            return new_list
        elif isinstance(output, str):
            return output
        elif isinstance(output, botocore.response.StreamingBody):
            return base64.b64encode(output.read()).decode("utf-8")
        elif isinstance(output, bytes):
            return base64.b64encode(output).decode("utf-8")
        elif isinstance(output, int):
            return output
        elif isinstance(output, bool):
            return output
        elif isinstance(output, float):
            return str(output)
        elif isinstance(output, datetime.datetime):
            return output.isoformat()
        else:
            return json.dumps(output)

    first_cap_re = re.compile("(.)([A-Z][a-z]+)")
    all_cap_re = re.compile("([a-z0-9])([A-Z])")

    @staticmethod
    def to_snake_case(camel_case):
        """
        Converts an upper camel case string to snake case.

        :param camel_case: The upper camel case string.
        :return: The same string in snake_case
        """

        s1 = ActionHelper.first_cap_re.sub(r"\1_\2", camel_case)
        return ActionHelper.all_cap_re.sub(r"\1_\2", s1).lower()

    @staticmethod
    def convert_all_to_upper_camel_case(obj):
        """
        Recursively converts dictionary keys to from upper camel case to snake case.
        :param obj: The object.
        :return: The object with snake case keys.
        """

        if isinstance(obj, dict):
            new_obj = {}
            for k, v in obj.items():
                new_v = ActionHelper.convert_all_to_upper_camel_case(v)
                new_obj[ActionHelper.to_upper_camel_case(k)] = new_v
            return new_obj
        elif isinstance(obj, list):
            new_obj = []
            for l in obj:
                new_l = ActionHelper.convert_all_to_upper_camel_case(l)
                new_obj.append(new_l)
            return new_obj
        else:
            return obj

    @staticmethod
    def convert_all_to_snake_case(obj):
        """
        Recursively converts dictionary keys to from upper camel case to snake case.
        :param obj: The object.
        :return: The object with snake case keys.
        """

        if isinstance(obj, dict):
            new_obj = {}
            for k, v in obj.items():
                new_v = ActionHelper.convert_all_to_snake_case(v)
                new_obj[ActionHelper.to_snake_case(k)] = new_v
            return new_obj
        elif isinstance(obj, list):
            new_obj = []
            for l in obj:
                new_l = ActionHelper.convert_all_to_snake_case(l)
                new_obj.append(new_l)
            return new_obj
        else:
            return obj

    def format_output(self, output_schema, output):
        """
        Formats a botocore response into a correct Komand response.

        Keys are formatted to snake case.

        :param output_schema: The output json schema
        :param output: The response from the botocore call
        :return: Correctly formatted botocall response
        """

        # Fix types
        output = self.fix_output_types(output)

        output = ActionHelper.convert_all_to_snake_case(output)

        # Add empty lists/dicts if values are missing
        if output_schema:
            empty = self.get_empty_output(output_schema)
            for key in empty:
                if key not in output:
                    output[key] = empty[key]

        return output


class PaginationHelper:
    """
    A helper class for dealing with paginated requests.
    """

    def __init__(
        self, input_token, output_token, result_key, limit_key=None, more_results=None, non_aggregate_keys=None
    ):
        self.input_token = input_token
        self.output_token = output_token
        self.result_key = result_key
        self.limit_key = limit_key
        self.more_results = more_results
        self.non_aggregate_keys = non_aggregate_keys
        self.keys_to_remove = []
        self.keys_to_remove.extend(input_token)
        self.keys_to_remove.extend(output_token)
        if more_results:
            self.keys_to_remove.append(self.more_results)

    def remove_keys(self, params):
        """
        Remove pagination related keys from output parameters.
        :param params: params.
        :return: None
        """
        for k in self.keys_to_remove:
            params.pop(k, None)

    def handle_pagination(self, input, output):
        """
        Looks at the output of a rest call and determines if the call was paginated.

        :param input: The input variables
        :param output: The output variables
        :return: True if more results are available, False otherwise
        """

        is_paginated = False

        if self.more_results and self.more_results in output.keys() and output[self.more_results]:
            is_paginated = True

        for idx, val in enumerate(self.input_token):

            if self.output_token[idx] in output.keys():
                input[self.input_token[idx]] = output[self.output_token[idx]]
                is_paginated = True

        return is_paginated

    def merge_responses(self, input, a, b):
        """
        Merges two output dictionaries together.
        :param input:
        :param a:
        :param b:
        :return:
        """

        max_hit = False

        for r in self.result_key:

            c = a[r]
            a[r] = b[r]
            a[r].extend(c)

            if self.limit_key and self.limit_key in input.keys():
                if len(a[r]) >= input[self.limit_key]:
                    max_hit = True
                    a[r] = a[r][: input[self.limit_key]]

        return a, max_hit
