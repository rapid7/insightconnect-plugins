import logging
from typing import Set
from html import escape
from urllib.parse import urlparse
from bs4 import BeautifulSoup, NavigableString

logger = logging.getLogger(__name__)

# HTML tags to be encoded (resource-loading, redirect, and script vectors)
DENIED_TAGS: Set[str] = {
    "script",
    "iframe",
    "object",
    "embed",
    "link",
    "style",
    "meta",
    "base",
    "svg",
    "math",
    "video",
    "audio",
    "source",
    "track",
    "picture",
    "form",
    "input",
}

# HTML Attributes to be encoded (event handlers + inline CSS)
DENIED_ATTRIBUTES: Set[str] = {
    "onload",
    "onerror",
    "onabort",
    "onunload",
    "onbeforeunload",
    "onclick",
    "onmouseover",
    "onmouseout",
    "onmousedown",
    "onmouseup",
    "onfocus",
    "onblur",
    "onchange",
    "onsubmit",
    "onreset",
    "onkeydown",
    "onkeyup",
    "onkeypress",
    "oninput",
    "onanimationstart",
    "onanimationend",
    "ontransitionend",
    "style",
}

# Attributes dereferenced by wkhtmltopdf/QtWebKit at render time (real SSRF sinks).
# Only inline data: URIs and relative URLs are safe here.
RESOURCE_URL_ATTRS: Set[str] = {
    "src",
    "poster",
    "background",
    "srcset",
    "xlink:href",
    "ping",
}
RESOURCE_URL_ALLOWED_SCHEMES: Set[str] = {"data"}

# Attributes that produce a clickable hyperlink or form target in the final PDF;
# they are not fetched at render time, so ordinary web schemes are safe.
LINK_URL_ATTRS: Set[str] = {"href", "action", "formaction"}
LINK_URL_ALLOWED_SCHEMES: Set[str] = {"http", "https", "mailto"}


def _encode_tag(tag) -> NavigableString:
    """Convert a tag to an escaped NavigableString."""
    return NavigableString(escape(str(tag), quote=False))


def _url_scheme(value: str) -> str:
    if not value:
        return ""
    return urlparse(value.strip()).scheme.lower()


def _is_disallowed(value: str, allowed_schemes: Set[str]) -> bool:
    """A URL is disallowed when it has an explicit scheme outside the allowlist.

    Relative URLs (no scheme) are considered safe because wkhtmltopdf without a
    base URL cannot dereference them.
    """
    scheme = _url_scheme(value)
    if not scheme:
        return False
    return scheme not in allowed_schemes


def _has_unsafe_url_attribute(tag) -> bool:
    for attr_name, attr_value in tag.attrs.items():
        name = attr_name.lower()
        if name in RESOURCE_URL_ATTRS:
            allowed = RESOURCE_URL_ALLOWED_SCHEMES
        elif name in LINK_URL_ATTRS:
            allowed = LINK_URL_ALLOWED_SCHEMES
        else:
            continue
        values = attr_value if isinstance(attr_value, list) else [attr_value]
        for value in values:
            if isinstance(value, str) and _is_disallowed(value, allowed):
                return True
    return False


def sanitize_html(html_content: str) -> str:
    """
    Sanitize HTML content by encoding potentially dangerous elements.

    Denylist-based sanitization:
    1. Encodes tags known to execute scripts, load remote resources, or redirect.
    2. Encodes tags carrying denied attributes (event handlers, inline style).
    3. Encodes tags whose URL-bearing attributes point to a disallowed scheme
       (e.g. file:, javascript:, gopher:); relative URLs are preserved.

    Args:
        html_content: The HTML content to sanitize

    Returns:
        Sanitized HTML content safe for rendering or conversion to PDF
    """
    if not html_content:
        return html_content

    soup = BeautifulSoup(html_content, "html.parser")

    for tag in reversed(soup.find_all(True)):
        if tag.name in DENIED_TAGS:
            logger.warning("Sanitizing HTML: encoded <%s> tag", tag.name)
            tag.replace_with(_encode_tag(tag))
            continue
        denied_attrs = [attr for attr in tag.attrs if attr.lower() in DENIED_ATTRIBUTES]
        if denied_attrs:
            logger.warning("Sanitizing HTML: encoded <%s> tag with attributes %s", tag.name, denied_attrs)
            tag.replace_with(_encode_tag(tag))
            continue
        if _has_unsafe_url_attribute(tag):
            logger.warning("Sanitizing HTML: encoded <%s> tag with disallowed URL scheme", tag.name)
            tag.replace_with(_encode_tag(tag))

    return soup.decode(formatter=None)
