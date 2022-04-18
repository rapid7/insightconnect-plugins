import csv
import json
import re
from io import StringIO

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException


def csv_syntax_good(csv_string: str) -> bool:
    if not csv_string:
        raise PluginException(cause="CSV input is empty.", assistance="Please provide a valid CSV input.")

    parsed = parse_csv_string(csv_string)
    size = len(parsed[0])
    for row in parsed:
        if len(row) != size:
            return False
    return True


def fields_syntax_good(fields: str) -> bool:
    if not fields:
        raise PluginException(cause="Empty fields input.", assistance="Please provide valid fields.")

    re_single = r"\s*f[0-9]+\s*"
    re_range = r"" + re_single + "(-" + re_single + ")?"
    re_multi = r"" + re_range + "(," + re_range + ")*"
    pattern = re.compile("^" + re_multi + "$")
    if pattern.match(fields):
        return True
    return False


##
# Converts field to integer
# Ex. 'f2' -> 2
#
# @param field String of field
# @return integer representation of fiele
##
def field_to_number(field):
    if field.startswith("f"):
        field = field[1:]
    return int(field)


##
# Converts fields string to list of integers corresponding to position of field
#
# @param fields String of fields to keep
# @return List containing integers to reference position of each field
##
def get_field_list(fields, num_fields):
    field_split = fields.split(",")
    field_list = []
    safe_range = range(1, num_fields + 1)

    for f in field_split:
        f = f.strip()
        if "-" in f:
            start, end = f.split("-")
            start = field_to_number(start.strip())
            end = field_to_number(end.strip())
            if start < 1 or start not in safe_range or end not in safe_range:
                return None
            field_list.extend(range(start, end + 1))
        else:
            n = field_to_number(f)
            if n not in safe_range:
                return None
            field_list.append(field_to_number(f))
    field_list.sort()
    return field_list


def parse_csv_string(csv_string: str) -> list:
    csv_list = csv_string.split("\n")
    parsed = []
    for line in csv.reader(csv_list, quotechar='"', delimiter=",", quoting=csv.QUOTE_ALL, skipinitialspace=True):
        if line:
            parsed.append(line)
    return parsed


##
# Converts the two-dimensional CSV array back to string form
#
# @param csv The two-dimensional array of the original CSV string
# @return The string of the CSV
##
def convert_csv_array(csv_array):
    item_delim = ","
    line_delim = "\n"
    lines = []

    for line in csv_array:
        lines.append(item_delim.join(line))
    csv_string = line_delim.join(lines)
    return csv_string


##
# Keeps specified positions in the list (1-indexed) of the line from CSV string
#
# @param line The list representing all of the items on the line of the CSV
# @param fields The list containing the indexes of the fields to keep
# @return The list of the line with only the specified remaining fields
##
def keep_fields(line, fields):
    result = []
    for field in fields:
        result.append(line[field - 1])
    return result


def csv_to_dict(string_csv: str, action: insightconnect_plugin_runtime.Action) -> list:
    csv_list = string_csv.split("\n")

    if len(csv_list) > 0:
        try:
            header = [csv_list[0]]
            action.logger.info(f"Header: {header}, Length: {len(header)}")
        except Exception:
            raise PluginException(
                cause="CSV string seems to be invalid - cannot extract header row.",
                assistance="Please provide a valid CSV input.",
            )
        try:
            first_row = [csv_list[1]]
            action.logger.info(f"Sample Data: {first_row}, Length: {len(first_row)}")
        except Exception:
            raise PluginException(
                cause="CSV string seems to be invalid - cannot extract first value row.",
                assistance="Please provide a valid CSV input.",
            )

    csv_data = csv.DictReader(csv_list, quotechar='"', delimiter=",", quoting=csv.QUOTE_ALL, skipinitialspace=True)

    return [json.loads(json.dumps(row)) for row in csv_data]


def json_to_csv(input_json: dict) -> str:
    output = StringIO()
    csv_writer = csv.writer(output)
    keys = []

    # get all keys from json
    for entry in input_json:
        keys.extend(list(entry.keys()))

    # remove duplicated keys
    keys = list(dict.fromkeys(keys))

    if keys:
        csv_writer.writerow(keys)
        for entry in input_json:
            for index, _ in enumerate(keys):
                entry[keys[index]] = entry.get(keys[index], "")
            csv_writer.writerow(entry.values())

    return output.getvalue()
