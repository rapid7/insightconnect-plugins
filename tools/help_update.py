#!/usr/bin/env python3
import re
import os


class HelpUpdate:
    @staticmethod
    def convert():
        help_file = "./help.md"
        try:
            with open(help_file) as h:
                contents = h.read()
        except FileNotFoundError:
            return None
        description = HelpUpdate.get_description(contents)
        key_features = HelpUpdate.get_key_features()
        requirements = HelpUpdate.get_requirements()
        documentation = HelpUpdate.get_documentation(contents)
        versions = HelpUpdate.get_versions(contents)
        links = HelpUpdate.get_links(contents)

        output = description + key_features + requirements + documentation + versions + links
        return output

    @staticmethod
    def get_description(contents: str) -> str:
        pattern = "## About([\s\S]*?)##"
        match: str = re.findall(pattern, contents)[0]
        return "# Description\n\n" + match.strip() + "\n\n"

    @staticmethod
    def get_key_features() -> str:
        key_features = """# Key Features\n
* Feature 1
* Feature 2
* Feature 3
"""
        return key_features + "\n"

    @staticmethod
    def get_requirements() -> str:
        requirements = """# Requirements\n
* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product
"""
        return requirements + "\n"

    @staticmethod
    def get_documentation(contents: str) -> str:
        output = "# Documentation\n\n"

        # grab connection info
        pattern = "## Connection([\s\S]*?)## "
        match: str = re.findall(pattern, contents)[0]
        setup = "## Setup\n\n" + match.strip() + "\n\n"

        # grab details
        pattern = "## Actions([\s\S]*?)## Triggers"
        match = re.findall(pattern, contents)[0]
        match = re.sub("# ", "## ", match)
        details = "## Technical Details\n\n" + "### Actions\n\n" + match.strip() + "\n\n"

        # grab triggers
        pattern = "## Triggers([\s\S]*?)## Connection"
        match = re.findall(pattern, contents)[0]
        match = re.sub("# ", "## ", match)
        details += "### Triggers\n\n" + match.strip() + "\n\n"

        # grab troubleshooting
        pattern = "## Troubleshooting([\s\S]*?)## "
        match = re.findall(pattern, contents)[0]
        troubleshooting = "## Troubleshooting\n\n" + match.strip() + "\n\n"

        # grab custom types
        pattern = "## Custom Output Types([\s\S]*)## Workflows"
        try:
            match = re.findall(pattern, contents)[0]
            match = re.sub("# ", "## ", match)
        except IndexError:
            match = "_This plugin does not contain any custom output types._"
        types = "### Custom Output Types\n\n" + match.strip() + "\n\n"

        output += setup + details + types + troubleshooting
        return output

    @staticmethod
    def get_versions(contents: str) -> str:
        pattern = "## Versions([\s\S]*?)## "
        match = re.findall(pattern, contents)[0].strip()
        lines: list[str] = match.split("*")
        lines.reverse()
        lines.remove("")
        if not lines[0].endswith("\n"):
            lines[0] += "\n"
        output = "".join(["*" + line for line in lines])
        return "# Version History\n\n" + output + "\n"

    @staticmethod
    def get_links(contents: str) -> str:
        output = "# Links\n\n"

        try:
            pattern = "## References([\s\S]*?)## "
            match = re.findall(pattern, contents)[0]
        except IndexError:
            pattern = "## References([\s\S]*)"
            match = re.findall(pattern, contents)[0]
        references = "## References\n\n" + match.strip() + "\n\n"

        output += references
        return output
