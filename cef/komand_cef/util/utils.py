'''
Utils for parsing CEF
Source: https://github.com/hpsec/cefp/blob/master/contrib/python/cefp.py
Notes: Modified to work with python 3
'''

import re
from komand.exceptions import PluginException

cef_key_re = re.compile(r' ([\w.-]+?)=')
cef_first_key_re = re.compile(r'([\w.-]+?)=')
cef_pipe_re = re.compile(r'\\*?\|')


def parse_cef(s):
    d = dict()
    fields = []
    field_start = 0
    for match in cef_pipe_re.finditer(s):
        start, end = match.span()
        if (end - start) % 2 == 0:
            # There are an odd number of backslashes, so the pipe is escaped.
            # A negative lookbehind may be a better way to do this.
            continue
        field = s[field_start:end - 1]
        fields.append(field.replace('\\|', '|').replace('\\\\', '\\'))
        field_start = end
        if len(fields) == 7:
            break
    else:
        raise PluginException(cause='Wrong value', assistance='CEF string does not have enough pipe characters')

    if 'CEF:0' not in fields[0]:
        raise PluginException(cause='Wrong value', assistance='CEF string is missing CEF:0 header')

    d['device_vendor'] = fields[1]
    d['device_product'] = fields[2]
    d['device_version'] = fields[3]
    d['signature_id'] = fields[4]
    d['name'] = fields[5]
    d['severity'] = fields[6]

    parse_cef_extension(d, s[field_start:])
    if '_cefVer' not in d:
        raise PluginException(cause='Wrong value', assistance='CEF string is missing _cefVer')

    # swap _cefVer to version
    d['version'] = d['_cefVer']
    d.pop('_cefVer', None)
    return d


def parse_cef_extension(d, s):
    last_start = len(s)
    matches = cef_key_re.finditer(s)
    # Look at the key value pairs from the end to the beginning because the
    # only way to find the end of a value is to find the start of the next key.
    for match in reversed(list(matches)):
        start, end = match.span()
        d[match.group(1)] = unescape_cef_value(s[end:last_start])
        last_start = start

    # The first key-value pair may be preceded by a space. If it is not, add
    # it to d .
    leftover = s[:last_start]
    match = cef_first_key_re.match(leftover)
    if match:
        d[match.group(1)] = unescape_cef_value(s[match.end():last_start])
    return d


def unescape_cef_value(s):
    s = s.replace('\\r', '\r').replace('\\n', '\n')
    return s.replace('\\=', '=').replace('\\\\', '\\')


def obj_to_cef(item):
    HEADER_KEYS = [
        'device_vendor',
        'device_product',
        'device_version',
        'signature_id',
        'name',
        'severity'
    ]
    header = ['' for _ in HEADER_KEYS]
    extension = {}
    for key, value in item.items():
        if key in HEADER_KEYS:
            esc = value.replace('\\', '\\\\').replace('|', '\\|')
            header[HEADER_KEYS.index(key)] = esc.encode('utf-8')
        elif key in ['_cefVer', 'version']:
            continue
        else:
            basestring = (str, bytes)

        if isinstance(value, basestring):
            value = value.replace('\\', '\\\\').replace('=', '\\=')
            value = value.replace('\r', '\\r').replace('\n', '\\n')
            extension[key] = value.encode('utf-8')
        else:
            extension[key] = str(value)

    header_str = '|'.join(map(bytes.decode, header))
    extension_str = ' '.join(
        f'{key}={bytes.decode(value)}'
        for key, value in extension.items()
    )
    return f'CEF:0|{header_str}|{extension_str} _cefVer=0.1\n'
