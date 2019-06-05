import re

def tsv_syntax_good(tsv):
    parsed = parse_tsv_string(tsv) 
    size = len(parsed[0])
    for row in parsed:
        if len(row) != size:
            return False
    return True

def fields_syntax_good(fields):
    re_single = '\s*f[0-9]+\s*'
    re_range = '' + re_single + '(-' + re_single + ')?'
    re_multi = '' + re_range + '(,' + re_range + ')*'
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
            field_list.extend(range(start, end+1))
        else:
            n = field_to_number(f)
            if n not in safe_range:
                return None
            field_list.append(field_to_number(f))
    field_list.sort()
    return field_list

##
# Converts TSV string to two-dimensional list
#
# @param tsv The string to parse
# @return Two-dimensional list consisting of items on each line of TSV string
##
def parse_tsv_string(tsv):
    tsv_list = tsv.split('\n')
    parsed = []
    for line in tsv_list:
        if line != '':
            parsed.append(line.split('\t'))
    return parsed

##
# Converts the two-dimensional TSV array back to string form
#
# @param tsv The two-dimensional array of the original TSV string
# @return The string of the TSV
##
def convert_tsv_array(tsv):
    item_delim = '\t'
    line_delim = '\n'
    lines = []

    for line in tsv:
        lines.append(item_delim.join(line))
    tsv_string = line_delim.join(lines)
    return tsv_string

##
# Keeps specified positions in the list (1-indexed) of the line from TSV string
#
# @param line The list representing all of the items on the line of the TSV
# @param fields The list containing the indexes of the fields to keep
# @return The list of the line with only the specified remaining fields
##
def keep_fields(line, fields):
    result = []
    for field in fields:
        result.append(line[field - 1])
    return result
