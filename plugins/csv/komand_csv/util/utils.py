import csv
import json
import re
from io import StringIO
from typing import Any, Dict, List, Union

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
# @return integer representation of field
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


Scalar = Union[str, int, float, bool, None]
JSONVal = Union[Scalar, Dict[str, Any], List[Any]]
TAG_RE = re.compile(r"<[^>]+>")


def strip_html(text: str) -> str:
    """Remove HTML tags and return plain text."""
    if text is None:
        return ""
    return TAG_RE.sub("", str(text))


def join_scalars(values: List[Scalar], joiner: str) -> str:
    """Join a list of scalar values into a string using the provided delimiter."""
    return joiner.join("" if value is None else str(value) for value in values)


def emit_scalar(items_dict: Dict[str, str], key: str, value: Scalar) -> None:
    """Emit a single scalar cell value with HTML stripping always enabled."""
    as_string = "" if value is None else str(value)
    items_dict[key] = strip_html(as_string)


def flatten_mapping(
    mapping: Dict[str, Any],
    *,
    items_dict: Dict[str, str],
    base_key: str,
    key_separator: str,
    list_joiner: str,
    list_expand_limit: int,
    list_overflow_suffix: str,
) -> None:
    """Flatten a nested mapping into items_dict using dot-notation for keys."""
    if not mapping:
        if base_key:
            items_dict[base_key] = ""
        return

    for sub_key, sub_value in mapping.items():
        new_key = f"{base_key}{key_separator}{sub_key}" if base_key else str(sub_key)
        flatten_value(
            sub_value,
            key=new_key,
            items_dict=items_dict,
            key_separator=key_separator,
            list_joiner=list_joiner,
            list_expand_limit=list_expand_limit,
            list_overflow_suffix=list_overflow_suffix,
        )


def flatten_sequence(
    sequence: List[Any],
    *,
    items_dict: Dict[str, str],
    key: str,
    key_separator: str,
    list_joiner: str,
    list_expand_limit: int,
    list_overflow_suffix: str,
) -> None:
    """Flatten a list: join scalars, expand dicts up to limit, overflow as compact JSON."""
    if not sequence:
        items_dict[key] = ""
        return

    contains_no_dicts = all(not isinstance(element, dict) for element in sequence)
    contains_only_dicts = all(isinstance(element, dict) for element in sequence)

    if contains_no_dicts:
        items_dict[key] = strip_html(join_scalars(sequence, list_joiner))
        return

    if contains_only_dicts:
        limit = max(0, int(list_expand_limit))
        elements_to_expand = sequence[:limit]
        for element_index, element in enumerate(elements_to_expand):
            flatten_mapping(
                element,
                items_dict=items_dict,
                base_key=f"{key}[{element_index}]",
                key_separator=key_separator,
                list_joiner=list_joiner,
                list_expand_limit=list_expand_limit,
                list_overflow_suffix=list_overflow_suffix,
            )
        if len(sequence) > limit:
            items_dict[f"{key}{list_overflow_suffix}"] = json.dumps(sequence[limit:], separators=(",", ":"))
        return

    # Mixed list: keep intact in *_rest as compact JSON
    items_dict[f"{key}{list_overflow_suffix}"] = json.dumps(sequence, separators=(",", ":"))


def flatten_value(
    value: Any,
    *,
    key: str,
    items_dict: Dict[str, str],
    key_separator: str,
    list_joiner: str,
    list_expand_limit: int,
    list_overflow_suffix: str,
) -> None:
    """Dispatch flatten logic based on value type."""
    if isinstance(value, dict):
        flatten_mapping(
            value,
            items_dict=items_dict,
            base_key=key,
            key_separator=key_separator,
            list_joiner=list_joiner,
            list_expand_limit=list_expand_limit,
            list_overflow_suffix=list_overflow_suffix,
        )
    elif isinstance(value, list):
        flatten_sequence(
            value,
            items_dict=items_dict,
            key=key,
            key_separator=key_separator,
            list_joiner=list_joiner,
            list_expand_limit=list_expand_limit,
            list_overflow_suffix=list_overflow_suffix,
        )
    else:
        emit_scalar(items_dict, key, value)


def flatten_dict(
    data: Dict[str, JSONVal],
    *,
    parent_key: str = "",
    key_separator: str = ".",
    list_joiner: str = "|",
    list_expand_limit: int = 3,
    list_overflow_suffix: str = "_rest",
) -> Dict[str, str]:
    """
    Flatten a nested dict into a single-level dict for CSV:
      - objects: dot keys
      - list of scalars: joined with delimiter (HTML stripped)
      - list of objects: expand key[i].subkey up to limit; remainder in key_rest
      - mixed lists: key_rest as compact JSON
      - all leaf values are HTML stripped
    """
    items_dict: Dict[str, str] = {}
    for sub_key, sub_value in (data or {}).items():
        full_key = f"{parent_key}{key_separator}{sub_key}" if parent_key else str(sub_key)
        flatten_value(
            sub_value,
            key=full_key,
            items_dict=items_dict,
            key_separator=key_separator,
            list_joiner=list_joiner,
            list_expand_limit=list_expand_limit,
            list_overflow_suffix=list_overflow_suffix,
        )
    return items_dict


def json_to_csv(
    input_json: Union[Dict[str, Any], List[Dict[str, Any]]],
    *,
    key_sep: str = ".",
    list_joiner: str = "|",
    list_expand_limit: int = 3,
) -> str:
    """
    Convert JSON (object or list of objects) into a flattened CSV string.
    HTML is always stripped from all leaf values.
    """
    if isinstance(input_json, dict):
        records = [input_json]
    elif isinstance(input_json, list):
        records = input_json
    else:
        raise PluginException(
            cause="Invalid JSON input.", assistance="Provide a JSON object or a JSON array of objects."
        )

    output_buffer = StringIO()
    csv_writer = csv.writer(output_buffer)

    flat_rows: List[Dict[str, str]] = []
    header_keys: List[str] = []

    for record in records or []:
        if not isinstance(record, dict):
            flat_row = {"value": strip_html("" if record is None else str(record))}
        else:
            flat_row = flatten_dict(
                record,
                key_separator=key_sep,
                list_joiner=list_joiner,
                list_expand_limit=list_expand_limit,
            )
        flat_rows.append(flat_row)
        header_keys.extend(flat_row.keys())

    seen = set()
    ordered_keys: List[str] = []
    for key in header_keys:
        if key not in seen:
            seen.add(key)
            ordered_keys.append(key)

    if ordered_keys:
        csv_writer.writerow(ordered_keys)
        for row in flat_rows:
            csv_writer.writerow([row.get(key, "") for key in ordered_keys])

    return output_buffer.getvalue()
