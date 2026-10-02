import base64
import binascii
import os
import unicodedata
from urllib.parse import quote
from email.mime.base import MIMEBase
from smtplib import SMTP, SMTPException, SMTPRecipientsRefused, SMTPSenderRefused

from insightconnect_plugin_runtime.exceptions import PluginException

DEFAULT_ATTACHMENT_FILENAME = "attachment"
MAX_FILENAME_LENGTH = 255
# Non-ASCII names are percent-encoded (RFC 2231) on a single header line, which must stay under 998 characters
MAX_ENCODED_FILENAME_LENGTH = 900
MAX_EXTENSION_LENGTH = 20


def close_client(client: SMTP) -> None:
    """Close the SMTP session, falling back to dropping the socket if the server is already gone."""
    try:
        client.quit()
    except (SMTPException, OSError):
        client.close()


def clean_addresses(addresses: list[str]) -> list[str]:
    """Drop blank entries and surrounding whitespace from a list of addresses."""
    return [address.strip() for address in addresses or [] if address and address.strip()]


def describe_refused_recipients(refused: dict[str, tuple[int, bytes]]) -> str:
    """Summarize refused recipients by count and SMTP codes, without their addresses."""
    codes = sorted({code for code, _ in refused.values()})
    return f"The server refused {len(refused)} recipient(s) (SMTP codes: {', '.join(map(str, codes))})"


def describe_smtp_error(error: Exception) -> str:
    """Describe an SMTP error without the recipient/sender addresses that smtplib embeds in some of them."""
    if isinstance(error, SMTPRecipientsRefused):
        return describe_refused_recipients(error.recipients)
    if isinstance(error, SMTPSenderRefused):
        return f"The server refused the sender (SMTP code: {error.smtp_code})"
    return str(error)


def sanitize_filename(filename: str) -> str:
    """Drop control, format and line/paragraph separator characters so a filename can never inject extra headers."""
    sanitized = "".join(
        character
        for character in filename
        if unicodedata.category(character)[0] != "C" and unicodedata.category(character) not in ("Zl", "Zp")
    ).strip()
    return sanitized or DEFAULT_ATTACHMENT_FILENAME


def truncate_filename(filename: str) -> str:
    """Shorten an overly long filename, keeping its extension, so the Content-Disposition line stays valid."""

    def is_too_long(name: str) -> bool:
        encoded_length = len(name) if name.isascii() else len(quote(name, safe=""))
        return len(name) > MAX_FILENAME_LENGTH or encoded_length > MAX_ENCODED_FILENAME_LENGTH

    if not is_too_long(filename):
        return filename

    stem, extension = os.path.splitext(filename)
    if len(extension) > MAX_EXTENSION_LENGTH:
        stem, extension = filename, ""
    while stem and is_too_long(stem + extension):
        stem = stem[:-1]
    return (stem.rstrip() + extension) if stem.strip() else DEFAULT_ATTACHMENT_FILENAME + extension


def create_attachment_part(attachment: dict[str, str], label: str) -> MIMEBase:
    """Build a MIME part from a `file` object ({"filename": ..., "content": <base64>}); `label` names the input entry in errors."""
    filename = truncate_filename(sanitize_filename(attachment.get("filename") or ""))
    # Base64 produced by other tools may be line-wrapped; whitespace is not part of the data
    content = "".join((attachment.get("content") or "").split())

    try:
        decoded = base64.b64decode(content, validate=True)
    except (binascii.Error, ValueError) as error:
        raise PluginException(
            cause=f"Content of {label} is not valid Base64.",
            assistance="Ensure the content of every attachment is Base64-encoded.",
            data=str(error),
        ) from error

    part = MIMEBase("application", "octet-stream")
    # Re-encode so the payload is wrapped at 76 characters, as required for email line lengths
    part.set_payload(base64.encodebytes(decoded).decode("ascii"))
    part["Content-Transfer-Encoding"] = "base64"
    # add_header quotes the filename, so names containing spaces are handled; non-ASCII uses RFC 2231
    part.add_header(
        "Content-Disposition",
        "attachment",
        filename=filename if filename.isascii() else ("utf-8", "", filename),
    )
    return part
