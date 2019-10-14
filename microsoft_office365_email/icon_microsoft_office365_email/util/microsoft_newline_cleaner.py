import quopri


def remove_microsoft_newlines(s: str) -> str:
    # Removes Microsoft specific newlines when raw emails are returned

    # I say we nuke it from orbit
    s = s.replace("=\r\n\r\n", "")
    s = s.replace("=\r\n", "")
    s = s.replace("=\n\n", "")
    s = s.replace("=\n", "")  # This is dangerous, but I'd rather preserve links and give ill formatted output
    try:
        s = quopri.decodestring(s).decode("UTF-8")
    except Exception:
        pass  # quopri will only work on ASCII characters, it barfs if it hits unicode...in that case just return the string

    return s
