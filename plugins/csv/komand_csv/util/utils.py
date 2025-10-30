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
_TAG_RE = re.compile(r"<[^>]+>")


def _strip_html(s: str) -> str:
    if s is None:
        return ""
    # Remove tags; leave text content
    return _TAG_RE.sub("", str(s))


def _join_scalars(values: List[Scalar], joiner: str) -> str:
    return joiner.join("" if v is None else str(v) for v in values)


def _emit_scalar(items: Dict[str, str], key: str, val: Scalar) -> None:
    # ALWAYS strip HTML per requested behavior
    s = "" if val is None else str(val)
    items[key] = _strip_html(s)


def _flatten_mapping(
    m: Dict[str, Any],
    *,
    items: Dict[str, str],
    base: str,
    sep: str,
    list_joiner: str,
    list_expand_limit: int,
    list_overflow_suffix: str,
) -> None:
    if not m:
        if base:
            items[base] = ""
        return
    for k, v in m.items():
        new_key = f"{base}{sep}{k}" if base else str(k)
        _flatten_value(
            v,
            key=new_key,
            items=items,
            sep=sep,
            list_joiner=list_joiner,
            list_expand_limit=list_expand_limit,
            list_overflow_suffix=list_overflow_suffix,
        )


def _flatten_sequence(
    seq: List[Any],
    *,
    items: Dict[str, str],
    key: str,
    sep: str,
    list_joiner: str,
    list_expand_limit: int,
    list_overflow_suffix: str,
) -> None:
    if not seq:
        items[key] = ""
        return

    none_are_dicts = all(not isinstance(v, dict) for v in seq)
    all_are_dicts = all(isinstance(v, dict) for v in seq)

    if none_are_dicts:
        # list of scalars → join
        items[key] = _strip_html(_join_scalars(seq, list_joiner))
        return

    if all_are_dicts:
        # list of objects → expand up to limit; remainder → *_rest
        limit = max(0, int(list_expand_limit))
        to_expand = seq[:limit]
        for i, element in enumerate(to_expand):
            _flatten_mapping(
                element,
                items=items,
                base=f"{key}[{i}]",
                sep=sep,
                list_joiner=list_joiner,
                list_expand_limit=list_expand_limit,
                list_overflow_suffix=list_overflow_suffix,
            )
        if len(seq) > limit:
            items[f"{key}{list_overflow_suffix}"] = json.dumps(seq[limit:], separators=(",", ":"))
        return

    # mixed list (dicts + scalars) → keep intact in *_rest compact JSON
    items[f"{key}{list_overflow_suffix}"] = json.dumps(seq, separators=(",", ":"))


def _flatten_value(
    value: Any,
    *,
    key: str,
    items: Dict[str, str],
    sep: str,
    list_joiner: str,
    list_expand_limit: int,
    list_overflow_suffix: str,
) -> None:
    if isinstance(value, dict):
        _flatten_mapping(
            value,
            items=items,
            base=key,
            sep=sep,
            list_joiner=list_joiner,
            list_expand_limit=list_expand_limit,
            list_overflow_suffix=list_overflow_suffix,
        )
    elif isinstance(value, list):
        _flatten_sequence(
            value,
            items=items,
            key=key,
            sep=sep,
            list_joiner=list_joiner,
            list_expand_limit=list_expand_limit,
            list_overflow_suffix=list_overflow_suffix,
        )
    else:
        _emit_scalar(items, key, value)


def _flatten_dict(
    data: Dict[str, JSONVal],
    *,
    parent_key: str = "",
    sep: str = ".",
    list_joiner: str = "|",
    list_expand_limit: int = 3,
    list_overflow_suffix: str = "_rest",
) -> Dict[str, str]:
    """
    Flattens a nested dict into a flat dict of strings (CSV-friendly).

    - Objects: dot.notation
    - Lists of scalars: joined with list_joiner (ALWAYS HTML-stripped)
    - Lists of objects: expanded as key[i].subkey up to list_expand_limit; remainder compacted as JSON in key{list_overflow_suffix}
    - Mixed lists: compact JSON in key{list_overflow_suffix}
    - All leaf values are converted to strings and HTML tags are ALWAYS stripped.
    """
    items: Dict[str, str] = {}
    for k, v in (data or {}).items():
        full_key = f"{parent_key}{sep}{k}" if parent_key else str(k)
        _flatten_value(
            v,
            key=full_key,
            items=items,
            sep=sep,
            list_joiner=list_joiner,
            list_expand_limit=list_expand_limit,
            list_overflow_suffix=list_overflow_suffix,
        )
    return items


def json_to_csv(
    input_json: Union[Dict[str, Any], List[Dict[str, Any]]],
    *,
    key_sep: str = ".",
    list_joiner: str = "|",
    list_expand_limit: int = 3,
    strip_html: bool = True,  # kept for backward compatibility; ignored (HTML stripping is always ON)
) -> str:
    """
    Convert JSON (object or list of objects) into a flattened CSV string.

    Parameters:
      - key_sep:            separator for nested object keys (default ".")
      - list_joiner:        delimiter for lists of scalars (default "|")
      - list_expand_limit:  max expanded elements for lists of objects (default 3)
      - strip_html:         (ignored) HTML is ALWAYS stripped from all leaf values
    """
    # Normalize to list of dicts
    if isinstance(input_json, dict):
        records = [input_json]
    elif isinstance(input_json, list):
        records = input_json
    else:
        raise PluginException(
            cause="Invalid JSON input.", assistance="Provide a JSON object or a JSON array of objects."
        )

    output = StringIO()
    csv_writer = csv.writer(output)

    # 1) Flatten each record and collect all keys (preserve order)
    flat_rows: List[Dict[str, str]] = []
    header_keys: List[str] = []

    for entry in records or []:
        if not isinstance(entry, dict):
            # Defensive: non-dict entries become a scalar column "value"
            flat = {"value": _strip_html("" if entry is None else str(entry))}
        else:
            flat = _flatten_dict(
                entry,
                sep=key_sep,
                list_joiner=list_joiner,
                list_expand_limit=list_expand_limit,
            )
        flat_rows.append(flat)
        header_keys.extend(flat.keys())

    # 2) De-duplicate keys while preserving order
    seen = set()
    ordered_keys: List[str] = []
    for k in header_keys:
        if k not in seen:
            seen.add(k)
            ordered_keys.append(k)

    # 3) Write CSV with empty string for missing values
    if ordered_keys:
        csv_writer.writerow(ordered_keys)
        for row in flat_rows:
            csv_writer.writerow([row.get(k, "") for k in ordered_keys])

    return output.getvalue()
