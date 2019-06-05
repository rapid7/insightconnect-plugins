# Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009
# Python Software Foundation.
# All rights reserved.
#
# Copyright (c) 2000 BeOpen.com.
# All rights reserved.
#
# Copyright (c) 1995-2001 Corporation for National Research Initiatives.
# All rights reserved.
#
# Copyright (c) 1991-1995 Stichting Mathematisch Centrum.
# All rights reserved.
#
# Copyright (C) 2010 McAfee, Inc.  All Rights Reserved.
#
# This version of quote() is intended to replace urllib.quote() and contains a fix for
# http://bugs.python.org/issue1712522 which will allow unicode strings.
# 
always_safe = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'
               'abcdefghijklmnopqrstuvwxyz'
               '0123456789' '_.-')
_safemaps = {}

def quote(s, safe = '/', encoding=None, errors=None):
    """quote('abc def') -> 'abc%20def'

    Each part of a URL, e.g. the path info, the query, etc., has a
    different set of reserved characters that must be quoted.

    RFC 2396 Uniform Resource Identifiers (URI): Generic Syntax lists
    the following reserved characters.

    reserved    = ";" | "/" | "?" | ":" | "@" | "&" | "=" | "+" |
                  "$" | ","

    Each of these characters is reserved in some component of a URL,
    but not necessarily in all of them.

    By default, the quote function is intended for quoting the path
    section of a URL.  Thus, it will not encode '/'.  This character
    is reserved, but in typical usage the quote function is being
    called on a path where the existing slash characters are used as
    reserved characters.
    
    string and safe may be either str or unicode objects.

    The optional encoding and errors parameters specify how to deal with
    non-ASCII characters, as accepted by the unicode.encode method.
    By default, encoding='utf-8' (characters are encoded with UTF-8), and
    errors='strict' (unsupported characters raise a UnicodeEncodeError).
    """
    if encoding is not None or isinstance(s, unicode):
        if encoding is None:
            encoding = 'utf-8'
        if errors is None:
            errors = 'strict'
        s = s.encode(encoding, errors)
    if isinstance(safe, unicode):
        # Normalize 'safe' by converting to str and removing non-ASCII chars
        safe = safe.encode('ascii', 'ignore')
        print safe
    # (Note that if 'safe' is already a str, non-ASCII bytes are allowed,
    # keeping with historical Python behaviour)
    cachekey = safe
    
    try:
        safe_map = _safemaps[cachekey]
    except KeyError:
        safe += always_safe
        safe_map = {}
        for i in range(256):
            c = chr(i)
            safe_map[c] = (c in safe) and c or ('%%%02X' % i)
        _safemaps[cachekey] = safe_map
    res = map(safe_map.__getitem__, s)
    return ''.join(res)    
