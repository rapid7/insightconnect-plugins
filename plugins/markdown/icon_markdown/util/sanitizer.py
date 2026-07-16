import logging
import re
from typing import Dict, Set
from urllib.parse import urlparse
from bs4 import BeautifulSoup, NavigableString

logger = logging.getLogger(__name__)

# Allowlist-based sanitization: only the tags/attributes/URL schemes below survive; everything
# else is HTML-encoded (kept as visible text) before the HTML is handed to wkhtmltopdf. An
# allowlist is used deliberately instead of a denylist so that new resource-loading vectors are
# blocked by default rather than requiring the denylist to be patched for each one.

# Tags produced by pandoc for standard Markdown (headings, emphasis, links, images, lists, task
# lists, tables incl. grid/alignment/caption/colgroup, definition lists, footnotes, blockquotes,
# code blocks/spans, sub/sup/del, hr). Any tag outside this set is encoded.
ALLOWED_TAGS: Set[str] = {
    "a",
    "p",
    "br",
    "hr",
    "div",
    "span",
    "pre",
    "code",
    "blockquote",
    "figure",
    "figcaption",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "strong",
    "em",
    "b",
    "i",
    "del",
    "sub",
    "sup",
    "ul",
    "ol",
    "li",
    "dl",
    "dt",
    "dd",
    "label",
    "input",
    "section",
    "table",
    "thead",
    "tbody",
    "tfoot",
    "tr",
    "th",
    "td",
    "caption",
    "colgroup",
    "col",
    "img",
}

# Attributes allowed on any allowed tag. These carry no resource-loading or scripting behavior.
GLOBAL_ATTRS: Set[str] = {
    "class",
    "id",
    "title",
    "role",
    "tabindex",
    "aria-hidden",
    "dir",
    "lang",
    "align",
}

# Additional attributes allowed only on specific tags. URL-bearing (href/src) and style attributes
# are validated further below.
TAG_ATTRS: Dict[str, Set[str]] = {
    "a": {"href"},
    "img": {"src", "alt"},
    "ol": {"type"},
    "li": {"value"},
    "input": {"type", "checked", "disabled"},
    "th": {"style", "colspan", "rowspan", "scope"},
    "td": {"style", "colspan", "rowspan"},
    "col": {"style", "span"},
    "colgroup": {"style", "span"},
    "table": {"style"},
    "pre": {"class"},
    "code": {"class"},
}

# Hyperlink attributes: not fetched at render time, so ordinary web schemes (and relative
# URLs / pure fragments) are safe. javascript:, data:, file:, etc. are rejected.
LINK_ATTRS: Set[str] = {"href"}
LINK_ALLOWED_SCHEMES: Set[str] = {"http", "https", "mailto"}

# Resource attributes dereferenced by wkhtmltopdf/QtWebKit during layout (real SSRF sinks).
# Only inline data: URIs and genuinely relative paths are safe; protocol-relative (//host) is
# rejected because the document is rendered from a file:// base and could still resolve to a host.
RESOURCE_ATTRS: Set[str] = {"src"}
RESOURCE_ALLOWED_SCHEMES: Set[str] = {"data"}

# The style attribute is only needed for table column alignment/width that pandoc emits. Permit it
# solely on table-layout tags and only when the whole value is text-align / width / height
# declarations — anything containing url(), expression(), behavior:, etc. is rejected.
STYLE_ALLOWED_TAGS: Set[str] = {"th", "td", "col", "colgroup", "table"}
SAFE_STYLE = re.compile(
    r"^\s*(?:(?:text-align\s*:\s*(?:left|right|center|justify)"
    r"|(?:width|height)\s*:\s*\d+(?:\.\d+)?\s*(?:%|px|em|rem)?)\s*;?\s*)+$",
    re.IGNORECASE,
)


def _encode_tag(tag) -> NavigableString:
    """Replace a tag with its raw string form.

    The returned NavigableString is *not* pre-escaped; escaping happens exactly once when the
    document is serialized with ``formatter="minimal"``. Pre-escaping here would double-encode.
    """
    return NavigableString(str(tag))


def _url_scheme(value: str) -> str:
    if not value:
        return ""
    return urlparse(value.strip()).scheme.lower()


def _is_safe_link(value: str) -> bool:
    """A hyperlink URL is safe when it is relative/a fragment or uses an allowed web scheme."""
    if not isinstance(value, str):
        return False
    scheme = _url_scheme(value)
    if not scheme:
        return True
    return scheme in LINK_ALLOWED_SCHEMES


def _is_safe_resource(value: str) -> bool:
    """A resource URL is safe only if it is a data: URI or a genuinely relative path.

    Protocol-relative references (//host/...) are rejected: with a file:// base URL they would not
    be a network fetch, but they are never legitimate output from Markdown and only ever appear as
    an attempt to reach a remote host, so they are treated as unsafe.
    """
    if not isinstance(value, str):
        return False
    stripped = value.strip()
    scheme = _url_scheme(stripped)
    if scheme:
        return scheme in RESOURCE_ALLOWED_SCHEMES
    return not stripped.startswith("//")


def _iter_values(attr_value):
    """bs4 exposes some attributes (e.g. class) as a list; normalize to an iterable of strings."""
    if isinstance(attr_value, list):
        return attr_value
    return [attr_value]


def _is_detached(tag, soup) -> bool:
    """True if the tag is no longer attached to the document root.

    When an outer tag is encoded it is replaced by escaped text, detaching the whole subtree. Its
    descendants are still present in the pre-computed find_all() snapshot, so they must be skipped:
    they are already represented (escaped once) inside the encoded ancestor, and re-encoding them
    would double-escape.
    """
    node = tag
    while node is not None:
        if node is soup:
            return False
        node = node.parent
    return True


def _is_safe_style(tag_name: str, attr_value) -> bool:
    """Style is only allowed on table-layout tags and only for alignment/width declarations."""
    if tag_name not in STYLE_ALLOWED_TAGS:
        return False
    style_value = " ".join(str(value) for value in _iter_values(attr_value))
    return bool(SAFE_STYLE.match(style_value))


def _is_allowed_attribute(tag_name: str, attr: str, attr_value) -> bool:
    """Return True if a single attribute (and its value) is allowed on the given tag."""
    if attr not in (GLOBAL_ATTRS | TAG_ATTRS.get(tag_name, set())):
        return False
    if attr in LINK_ATTRS:
        return all(_is_safe_link(value) for value in _iter_values(attr_value))
    if attr in RESOURCE_ATTRS:
        return all(_is_safe_resource(value) for value in _iter_values(attr_value))
    if attr == "style":
        return _is_safe_style(tag_name, attr_value)
    return True


def _is_allowed_tag(tag) -> bool:
    """Return True if the tag and every one of its attributes/values passes the allowlist."""
    name = tag.name.lower()
    if name not in ALLOWED_TAGS:
        return False
    return all(
        _is_allowed_attribute(name, attr_name.lower(), attr_value) for attr_name, attr_value in tag.attrs.items()
    )


def sanitize_html(html_content: str) -> str:
    """
    Sanitize HTML content by encoding anything outside the allowlist.

    Allowlist-based sanitization:
    1. Encodes any tag whose name is not in ALLOWED_TAGS.
    2. Encodes any allowed tag that carries an attribute outside its allowlist (this removes event
       handlers and unrecognized resource attributes such as srcset/ping/background by omission).
    3. Encodes any allowed tag whose href/src points to a disallowed scheme, or whose style value
       is not a safe alignment/width declaration.

    The result is serialized with ``formatter="minimal"`` so every text node is HTML-escaped
    exactly once (only &, <, > are escaped; non-ASCII text is left as-is). This prevents
    entity-escaped markup (e.g. from a Markdown code span) from being resurrected into live tags on
    output, while keeping the serialized HTML as close as possible to what pandoc emitted.

    Args:
        html_content: The HTML content to sanitize

    Returns:
        Sanitized HTML content safe for rendering or conversion to PDF
    """
    if not html_content:
        return html_content

    soup = BeautifulSoup(html_content, "html.parser")

    # Walk in document order so the outermost disallowed tag is encoded first, absorbing its whole
    # subtree into a single escaped-once text node. Descendants of an already-encoded tag are
    # detached from the document and skipped to avoid double-escaping.
    for tag in soup.find_all(True):
        if _is_detached(tag, soup):
            continue
        if not _is_allowed_tag(tag):
            logger.warning("Sanitizing HTML: encoded <%s> tag", tag.name)
            tag.replace_with(_encode_tag(tag))

    return soup.decode(formatter="minimal")
