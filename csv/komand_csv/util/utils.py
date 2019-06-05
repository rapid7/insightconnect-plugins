import csv
import json
import re


def csv_syntax_good(csv):
    parsed = parse_csv_string(csv)
    size = len(parsed[0])
    for row in parsed:
        if len(row) != size:
            return False
    return True


def fields_syntax_good(fields):
    re_single = r'\s*f[0-9]+\s*'
    re_range = r'' + re_single + '(-' + re_single + ')?'
    re_multi = r'' + re_range + '(,' + re_range + ')*'
    pattern = re.compile('^' + re_multi + '$')
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
    if field.startswith('f'):
        field = field[1:]
    return int(field)


##
# Converts fields string to list of integers corresponding to position of field
#
# @param fields String of fields to keep
# @return List containing integers to reference position of each field
##
def get_field_list(fields, num_fields):
    field_split = fields.split(',')
    field_list = []
    safe_range = range(1, num_fields + 1)

    for f in field_split:
        f = f.strip()
        if '-' in f:
            start, end = f.split('-')
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


##
# Converts CSV string to two-dimensional list
#
# @param csv The string to parse
# @return Two-dimensional list consisting of items on each line of CSV string
##
def parse_csv_string(csv):
    csv_list = csv.split('\n')
    parsed = []
    for line in csv_list:
        if line != '':
            parsed.append(line.split(','))
    return parsed


##
# Converts the two-dimensional CSV array back to string form
#
# @param csv The two-dimensional array of the original CSV string
# @return The string of the CSV
##
def convert_csv_array(csv):
    item_delim = ','
    line_delim = '\n'
    lines = []

    for line in csv:
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


##
# Converts a CSV string to a list of dictionariea
#
# @param csv The string of the CSV
# @return List of dictionaries
##
def csv_to_dict(s, action):
    ret_list = []

    # Create array of CSV rows
    csv_list = s.split('\n')

    # Create list from CSV header (first line)
    try:
        if len(csv_list) > 0:
            header = [csv_list[0]]
            action.logger.info('Header: %s, Length: %s', header, len(header))
    except Exception as e:
        action.logger.error("Element 0 doesn't exist in array")
        action.logger.error("Exception: " + str(e))
        raise

    # Skip first line to get data
    try:
        if len(csv_list) > 0:
            first_row = [csv_list[1]]
            action.logger.info('Sample Data: %s, Length: %s', first_row, len(first_row))
    except Exception as e:
        action.logger.error("Element 1 doesn't exist in array")
        action.logger.error("Exception: " + str(e))
        raise

    csv_data = csv.DictReader(csv_list)
    for row in csv_data:
        ret_list.append(json.loads(json.dumps(row)))

    return ret_list
