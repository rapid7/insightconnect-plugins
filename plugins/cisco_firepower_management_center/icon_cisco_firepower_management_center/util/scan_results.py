from icon_cisco_firepower_management_center.util.commands import (
    generate_set_os_command,
    generate_add_host_command,
    generate_add_result_command,
    generate_set_source_command,
)


class ScanResults(object):

    FOOTER = "ScanUpdate\n"

    def __init__(self, max_page_size):
        self.max_page_size = max_page_size
        self.commands = [""]
        self.added_hosts = {}

    def add_scan_result(self, address, scan_result, operation):
        new_host = False
        command = ""
        if not self.added_hosts.get(address):
            new_host = True
            host = scan_result.get("host", {})
            command += generate_add_host_command(address)
            command += generate_set_os_command(host, address)
            self.added_hosts[address] = True

        details = scan_result.get("scan_result_details", {})
        source_id = details.get("source_id", "")
        command += generate_set_source_command(source_id)
        command += generate_add_result_command(details, address)
        if new_host:
            command += operation
            command += "\n"
        else:
            command += self.FOOTER
        self.__add_command(command)

    def __add_command(self, command):
        current_index = len(self.commands) - 1
        current_size = len(self.commands[current_index])
        footer_size = len(self.FOOTER)

        # If the command and the footer can fit to the current page
        if current_size + len(command) + footer_size < self.max_page_size:
            self.commands[current_index] += command
            return

        # Command can't fit on current page, so add the footer to the
        # current page and add the command to a new page.
        self.commands[current_index] += self.FOOTER
        self.commands.append(command)
