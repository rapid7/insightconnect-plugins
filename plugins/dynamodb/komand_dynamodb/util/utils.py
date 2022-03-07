import base64
import datetime
import json

import botocore.response

from insightconnect_plugin_runtime.exceptions import PluginException


class Utils:
    @staticmethod
    def prepare_input_for_aws_call(params: dict, schema: dict) -> dict:
        try:
            params = Utils.format_input(params, schema)
        except Exception:
            raise PluginException(
                cause="Unable to format input parameters.",
                assistance="Please check the inputs and try again.",
            )
        return params

    @staticmethod
    def format_input(params: dict, schema: dict):
        formatted_params = {}
        # Drop invalid empty parameters
        for k, v in params.items():
            if v:
                formatted_params[k.replace("$", "")] = v
        return Utils.convert_all_dict_keys_to_upper_camel_case(formatted_params, schema, schema)

    @staticmethod
    def convert_all_dict_keys_to_upper_camel_case(
        dict_to_convert: any, root_schema: dict, schema: dict, has_lower_level=False
    ):
        """
        Recursively converts dictionary keys to upper camel case.
        :param dict_to_convert: Dict in which all keys will be converted to upper camel case.
        :param root_schema: The root schema from plugin spec.
        :param schema: The scheme that will be used to iterate through the  defined data types.
        :param has_lower_level: Param defines if property have lower level object.
        :return: The object with snake case keys.
        """

        if schema and "$ref" in schema:
            return Utils.convert_all_dict_keys_to_upper_camel_case(
                dict_to_convert,
                root_schema,
                Utils.get_schema_from_ref(root_schema, schema["$ref"]),
                has_lower_level,
            )

        if isinstance(dict_to_convert, dict):
            if has_lower_level:
                new_obj = {}
                for key, value in dict_to_convert.items():
                    new_v = Utils.convert_all_dict_keys_to_upper_camel_case(value, root_schema, None, has_lower_level)
                    new_obj[Utils.to_upper_camel_case(key)] = new_v
                return new_obj
            elif Utils.does_schema_contain_object(schema):
                new_obj = {}
                for key, value in dict_to_convert.items():
                    if "properties" in schema and key in schema["properties"]:
                        new_v = Utils.convert_all_dict_keys_to_upper_camel_case(
                            value,
                            root_schema,
                            schema["properties"][key],
                            key == "response_metadata",
                        )
                        new_obj[Utils.to_upper_camel_case(key)] = new_v
                return new_obj
            else:
                return dict_to_convert
        elif Utils.is_json_schema(dict_to_convert, schema):
            new_obj = []
            for key in dict_to_convert:
                new_l = Utils.convert_all_dict_keys_to_upper_camel_case(key, root_schema, schema["items"])
                new_obj.append(new_l)
            return new_obj
        else:
            return dict_to_convert

    @staticmethod
    def is_json_schema(obj: object, schema: dict) -> bool:
        if isinstance(obj, list) and schema:
            if "type" in schema:
                if schema.get("type") == "array" and "items" in schema:
                    return True
        return False

    @staticmethod
    def does_schema_contain_object(schema: dict) -> bool:
        if schema and "type" in schema:
            if schema.get("type") == "object" and "properties" in schema:
                return True
        return False

    @staticmethod
    def get_schema_from_ref(schema: dict, ref: str) -> any:
        """
        Return object which describe of custom type definition.
        For example if ref is equals "#/definitions/custom_definition_object" function will return object
        from schema which define structure of custom_definition_object.
        :param schema: The schema, which is generated from plugin spec.
        :param ref: The ref string which tell which definitions need to pull from schema
        :return: The object which define type of ref
        """
        ref = ref[1:]

        while "/" in ref:
            index = ref.find("/", 1)
            if index == -1:
                schema = schema[ref[1:]]
                ref = ""
            else:
                schema = schema[ref[1:index]]
                ref = ref[index:]
        return schema

    @staticmethod
    def to_upper_camel_case(snake_str: str) -> str:
        components = snake_str.split("_")
        return "".join(component.title() for component in components).replace("Aws", "AWS")

    @staticmethod
    def get_empty_output(schema: dict) -> dict:
        """
        Returns a dictionary where schema parameters mapped to default values.
        :param schema: The output schema.
        :return: A dictionary which maps properties to empty values.
        """
        empty_output = {}
        if "properties" in schema:
            output_properties = schema["properties"]
            for key in output_properties:
                prop = output_properties[key]
                if "type" in prop:
                    Utils.generate_empty_list_or_dict(key, prop, empty_output)
                elif "$ref" in prop:
                    prop = schema["definitions"][key]
                    if "type" in prop:
                        Utils.generate_empty_list_or_dict(key, prop, empty_output)

        empty_output["response_metadata"] = {"request_id": "", "http_status_code": 0}
        return empty_output

    @staticmethod
    def generate_empty_list_or_dict(key: str, value_for_key: any, empty_output: dict) -> dict:
        if value_for_key["type"] == "array":
            empty_output[key] = []
        elif value_for_key["type"] == "object":
            empty_output[key] = {}
        return empty_output

    @staticmethod
    def fix_output_types(output):
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
                new_dict[key] = Utils.fix_output_types(output[key])
            return new_dict
        elif isinstance(output, list):
            new_list = []
            for item in output:
                new_list.append(Utils.fix_output_types(item))
            return new_list
        elif isinstance(output, str):
            return output.replace('"', "")
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

    @staticmethod
    def map_return_item_collection_metrics(user_input: bool) -> str:
        return "SIZE" if user_input else "NONE"

    @staticmethod
    def map_return_values(user_input: bool) -> str:
        return "ALL_OLD" if user_input else "NONE"
