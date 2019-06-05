#!/usr/bin/env python3
import yaml
from yaml.error import YAMLError
import os
import sys
from typing import Any, Optional
from enum import Enum


class ComponentType(Enum):
    """
    Enum to allow for identifying the type of a plugin component (Connection, Action, Trigger)
    """
    connection = "connection"
    action = "action"
    trigger = "trigger"


class IO(object):
    """
    An Input or Output on a Connection, Action, Trigger
    """

    def __init__(self,
                 identifier: str,
                 title: Optional[str],
                 description: Optional[str],
                 type_: str,
                 required: bool,
                 default: Optional[Any],
                 enum: Optional[list] = None,
                 raw_parameters: set = {}
                 ):
        """
        Initializer for an input or output belonging to a component
        :param identifier: Identifier for an IO (optional)
        :param title: Title of an IO (optional)
        :param description: Description of an IO (optional)
        :param type_: Type of an IO (eg. string, integer, number, boolean, etc)
        :param required: Boolean indicator of requiredness
        :param default: Default value for the IO (optional)
        :param enum: Enum values (optional)
        :param raw_parameters: All properties belonging to the IO as a set of strings

        """
        self.identifier = identifier
        self.title = title
        self.description = description
        self.type_ = type_
        self.required = False if not required else True
        self.default = default
        self.enum = enum
        self.raw_parameters = raw_parameters

    def __lt__(self, other):
        return self.identifier < other.identifier

    @property
    def is_custom(self):
        """
        Returns whether or not the IO is of a custom/non-standard type.
        Standard types defined at https://komand.github.io/python/spec.html#base-types
        :return: Boolean indicating if a type is custom
        """
        # Strip off possible list indicator and compare against standard types
        return self.type_.lstrip("[]") not in {"boolean",
                                               "integer",
                                               "int",
                                               "number",
                                               "float",
                                               "string",
                                               "date",
                                               "bytes",
                                               "object",
                                               "password",
                                               "python",
                                               "file",
                                               "credential_username_password",
                                               "credential_asymmetric_key",
                                               "credential_secret_key",
                                               "credential_token"}

    @classmethod
    def from_dict(cls, raw: {str: Any}):
        # Get the first and only key from the dict anonymously and assign that to an identifier
        identifier = list(raw.keys())[0]

        return cls(identifier=identifier,
                   title=raw[identifier].get("title"),
                   description=raw[identifier].get("description"),
                   type_=raw[identifier].get("type"),
                   required=raw[identifier].get("required"),
                   default=raw[identifier].get("default"),
                   enum=raw[identifier].get("enum"),
                   raw_parameters=set(raw[identifier].keys()))


class CustomType(object):
    """
    A CustomType object, comprised of a single identifier and multiple IO components
    """

    def __init__(self, identifier: str, properties: [IO]):
        self.identifier = identifier
        self.properties = properties


class PluginComponent(object):
    """
    A Connection, Action, or Trigger
    """

    def __init__(self,
                 component_type: ComponentType,
                 identifier: str = None,
                 title: Optional[str] = None,
                 description: Optional[str] = None,
                 inputs: [IO] = None,
                 outputs: [IO] = None,
                 raw_parameters: set = {}):
        """
        Initializer for a PluginComponent
        :param component_type: Type of the component
        :param title: Title of the component. Not present on a Connection component
        :param description: Description of the component. Not present on a Connection component
        :param inputs: List of component inputs (optional)
        :param outputs: List of component outputs (never present on a Connection component) (optional)
        :param raw_parameters: All top-level properties (input/output/etc) belonging to the component as a set of strings
        """
        self.component_type = component_type
        self.identifier = identifier
        self.title = title
        self.description = description
        self.inputs = inputs
        self.outputs = outputs
        self.raw_parameters = raw_parameters

    def __lt__(self, other):
        return self.identifier < other.identifier

    @classmethod
    def new_action(cls, raw: dict):
        # Get the first and only key from the dict anonymously and assign that to an identifier
        identifier: str = list(raw.keys())[0]
        raw_parameters: {str} = set(raw[identifier].keys())

        input_, output = raw[identifier].get("input"), raw[identifier].get("output")

        inputs: [IO] = [IO.from_dict(raw={k: v}) for k, v in input_.items()] if input_ else []
        outputs: [IO] = [IO.from_dict(raw={k: v}) for k, v in output.items()] if output else []

        return cls(component_type=ComponentType.action,
                   identifier=identifier,
                   title=raw[identifier].get("title"),
                   description=raw[identifier].get("description"),
                   inputs=inputs,
                   outputs=outputs,
                   raw_parameters=raw_parameters)

    @classmethod
    def new_trigger(cls, raw: dict):
        # Get the first and only key from the dict anonymously and assign that to an identifier
        identifier: str = list(raw.keys())[0]
        raw_parameters: {str} = set(raw[identifier].keys())

        input_, output = raw[identifier].get("input"), raw[identifier].get("output")

        inputs: [IO] = [IO.from_dict(raw={k: v}) for k, v in input_.items()] if input_ else []
        outputs: [IO] = [IO.from_dict(raw={k: v}) for k, v in output.items()] if output else []

        return cls(component_type=ComponentType.trigger,
                   identifier=identifier,
                   title=raw[identifier].get("title"),
                   description=raw[identifier].get("description"),
                   inputs=inputs,
                   outputs=outputs,
                   raw_parameters=raw_parameters)

    @classmethod
    def new_connection(cls, raw: dict):
        # Create a list of IO objects from the raw inputs dict
        inputs: [IO] = [IO.from_dict(raw={k: v}) for k, v in raw.items()] if raw else []
        return cls(component_type=ComponentType.connection,
                   identifier="connection",
                   inputs=inputs)


class PluginSpec(object):
    """
    A plugin specification file
    """

    def __init__(self,
                 spec_version: str,
                 name: str,
                 title: str,
                 description: str,
                 version: str,
                 vendor: str,
                 tags: [str],
                 types: [CustomType],
                 connection: PluginComponent = None,
                 actions: [PluginComponent] = [],
                 triggers: [PluginComponent] = []):
        self.spec_version = spec_version
        self.name = name
        self.title = title
        self.description = description
        self.version = version
        self.vendor = vendor
        self.tags = tags
        self.types = types
        self.connection = connection
        self.actions = actions
        self.triggers = triggers

    @classmethod
    def load_from_file(cls, path_):
        if not os.path.isfile(path_):
            return None

        f = open(path_, "r")
        try:
            spec = yaml.safe_load(f)
        except YAMLError as e:
            raise Exception("Error: Provided spec file was not valid YAML!") from e
        f.close()

        custom_types: [CustomType] = []
        for identifier, properties in spec.get("types", {}).items():
            io = [IO.from_dict(raw={k: v}) for k, v in properties.items()]
            custom_types.append(CustomType(identifier=identifier, properties=io))

        connection = PluginComponent.new_connection(raw=spec.get("connection")) if spec.get("connection") else None
        actions = [PluginComponent.new_action(raw={k: v}) for k, v in spec.get("actions").items()] if spec.get(
            "actions") else []
        triggers = [PluginComponent.new_action(raw={k: v}) for k, v in spec.get("triggers").items()] if spec.get(
            "triggers") else []

        return cls(spec_version=spec.get("plugin_spec_version"),
                   name=spec.get("name"),
                   title=spec.get("title"),
                   description=spec.get("description"),
                   version=spec.get("version"),
                   vendor=spec.get("vendor"),
                   tags=spec.get("tags"),
                   types=custom_types,
                   connection=connection,
                   actions=actions,
                   triggers=triggers)


class Help(object):
    """
    Class for providing yaml-to-markdown (spec to help file) functionality
    """

    # Represents a linebreak in Markdown
    MD_BREAK = "\n\n"

    def __init__(self, spec: PluginSpec):
        """
        Initialize a Help object
        :param spec: PluginSpec object to load
        """
        self.spec = spec

        self.actions: [str] = []
        self.triggers: [str] = []
        self.connection: str = None

    @classmethod
    def load_from_file(cls, path_: str):
        """
        Convenience initializer for a Help object
        :param path_: Path to a plugin.spec.yaml
        :return: New Help object
        """
        spec = PluginSpec.load_from_file(path_=path_)
        return cls(spec=spec)

    @staticmethod
    def _generate_input_table(inputs: [IO]) -> str:
        """
        Generates a markdown table for component inputs
        :param inputs: List of IO objects for a component
        :return: Markdown table as a string
        """
        table = (
            "|Name|Type|Default|Required|Description|Enum|\n"
            "|----|----|-------|--------|-----------|----|\n")

        for counter, io in enumerate(sorted(inputs), 1):
            # if io.is_custom:
            #     # Custom type, so link to the custom type table.
            #     # Link could be for an array of custom types, so strip the array symbol off otherwise a broken link
            #     # will be generated.
            #     type_text = f"[{io.type_}](#{io.type_.lstrip('[]')})"
            # else:
            #     type_text = io.type_

            table += f"|{io.identifier}|{io.type_}|{io.default}|{io.required}|{io.description}|{io.enum}|"
            table += "\n" if counter < len(inputs) else ""

        return table

    @staticmethod
    def _generate_output_table(outputs: [IO]) -> str:
        """
        Generates a markdown table for component outputs
        :param outputs: List of IO objects for a component
        :return: Markdown table as a string
        """
        table = (
            "|Name|Type|Required|Description|\n"
            "|----|----|--------|-----------|\n")

        for counter, io in enumerate(sorted(outputs), 1):
            # if io.is_custom:
            #     # Custom type, so link to the custom type table.
            #     # Link could be for an array of custom types, so strip the array symbol off otherwise a broken link
            #     # will be generated.
            #     type_text = f"[{io.type_}](#{io.type_.lstrip('[]')})"
            # else:
            #     type_text = io.type_

            table += (f"|{io.identifier}|"
                      f"{io.type_}|"
                      f"{io.required}|"
                      f"{io.description}|")
            table += "\n" if counter < len(outputs) else ""

        return table

    def _generate_component_section(self, section_type: ComponentType) -> str:
        """
        Generates a markdown help section for a class of components (actions or triggers)
        :param section_type: ComponentType enum value representing the section type to generate
        :return: Markdown section as a string
        """
        assert (section_type != ComponentType.connection), "generate_component_section does not support connections!"

        # Both actions and triggers are of type PluginComponent - so they can be swapped in/out in the code below
        components = self.spec.actions if section_type == ComponentType.action else self.spec.triggers
        singular = "action" if section_type == ComponentType.action else "trigger"

        markdown = f"## {singular.capitalize()}s{self.MD_BREAK}"
        if not components:
            markdown += f"_This plugin does not contain any {singular}s._{self.MD_BREAK}"
            return markdown

        for component in sorted(components):
            # Base: Based on the first word of the description, determine the help description base sentence
            # Description: Lowercase the first letter of the first word so it flows w/ the base sentence
            has_s = component.description.split(" ")[0].endswith("s")
            base = f"This {singular}" if has_s else f"This {singular} is used to"
            description = component.description[0].lower() + component.description[1:]

            markdown += (f"### {component.title}{self.MD_BREAK}"
                         f"{base} {description}.{self.MD_BREAK}")
            if component.inputs:
                markdown += (f"#### Input{self.MD_BREAK}"
                             f"{self._generate_input_table(inputs=component.inputs)}{self.MD_BREAK}")
            if component.outputs:
                markdown += (f"#### Output{self.MD_BREAK}"
                             f"{self._generate_output_table(outputs=component.outputs)}{self.MD_BREAK}"
                             f"Example output:{self.MD_BREAK}"
                             f"```\n"
                             f"```{self.MD_BREAK}")

        return markdown

    def _generate_about_section(self) -> str:
        """
        Generates a markdown About section
        :return: Markdown string as section
        """

        try:
            leads_with_title = self.spec.description.index(self.spec.title) == 0
        except ValueError:  # Title not found at all in the description
            leads_with_title = False

        description = self.spec.description.replace(self.spec.title, "", 1 if leads_with_title else 0)
        markdown = (f"## About{self.MD_BREAK}"
                    f"[{self.spec.title}](LINK TO PRODUCT/VENDOR WEBSITE) {description}."
                    f"{self.MD_BREAK}")

        return markdown


    def generate_full_markdown(self) -> str:
        """
        Generates a formatted plugin help file as a markdown string
        :return: Markdown help file string
        """
        markdown = ""

        # Title
        markdown += f"# {self.spec.title}{self.MD_BREAK}"

        # About section
        markdown += self._generate_about_section()

        # Actions
        markdown += self._generate_component_section(section_type=ComponentType.action)

        # Triggers
        markdown += self._generate_component_section(section_type=ComponentType.trigger)

        # Connection
        markdown += f"## Connection{self.MD_BREAK}"
        if self.spec.connection:
            markdown += (f"The connection configuration accepts the following parameters:{self.MD_BREAK}"
                         f"{self._generate_input_table(inputs=self.spec.connection.inputs)}{self.MD_BREAK}")
        else:
            markdown += f"_This plugin does not contain a connection._{self.MD_BREAK}"

        # Troubleshooting
        markdown += (f"## Troubleshooting{self.MD_BREAK}"
                     f"_This plugin does not contain any troubleshooting information._{self.MD_BREAK}")

        # Workflows
        markdown += (f"## Workflows{self.MD_BREAK}"
                     f"Examples:{self.MD_BREAK}"
                     f"* EXAMPLE HERE {self.MD_BREAK}")

        # Versions
        markdown += (f"## Versions{self.MD_BREAK}"
                     f"* 1.0.0 - Initial plugin{self.MD_BREAK}")

        # References
        markdown += (f"## References{self.MD_BREAK}"
                     f"* [{self.spec.title}](LINK TO PRODUCT/VENDOR WEBSITE){self.MD_BREAK}")

        # Custom Types
        markdown += f"## Custom Output Types{self.MD_BREAK}"
        if self.spec.types:
            for type_ in self.spec.types:
                markdown += (f"### {type_.identifier}{self.MD_BREAK}"
                             f"{self._generate_output_table(outputs=type_.properties)}{self.MD_BREAK}")
        else:
            markdown += f"_This plugin does not contain any custom output types._"

        return markdown


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("./help.py <path/plugin.spec.yaml>")
        sys.exit(0)

    path = sys.argv[1]

    help_ = Help.load_from_file(path_=path)
    help_markdown = help_.generate_full_markdown()
    print(help_markdown)
