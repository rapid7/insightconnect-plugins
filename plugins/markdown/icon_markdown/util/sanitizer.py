import logging
from typing import Set
from html import escape
from bs4 import BeautifulSoup, NavigableString

logger = logging.getLogger(__name__)

# HTML tags to be encoded
DENIED_TAGS: Set[str] = {
    "script",
    "iframe",
    "object",
    "embed",
    "link",
    "style",
}

# HTML Attributes to be encoded (event handlers)
DENIED_ATTRIBUTES: Set[str] = {
    "onload",
    "onerror",
    "onabort",
    "onunload",
    "onbeforeunload",
}


def _encode_tag(tag) -> NavigableString:
    """Convert a tag to an escaped NavigableString."""
    return NavigableString(escape(str(tag), quote=False))


def sanitize_html(html_content: str) -> str:
    """
    Sanitize HTML content by encoding potentially dangerous elements.

    This function uses an explicit denylist approach:
    1. Encodes tags: script, iframe, object, embed, link, style
    2. Encodes tags with event handler attributes

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
        elif any(attr.lower() in DENIED_ATTRIBUTES for attr in tag.attrs):
            event_handlers = [
                attr for attr in tag.attrs if attr.lower() in DENIED_ATTRIBUTES
            ]
            logger.warning(
                "Sanitizing HTML: encoded <%s> tag with attributes %s", tag.name, event_handlers
            )
            tag.replace_with(_encode_tag(tag))

    return soup.decode(formatter=None)
