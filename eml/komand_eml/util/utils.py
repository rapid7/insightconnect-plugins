# Custom imports below
import re
from bs4 import UnicodeDammit


def body(b, log):
    if b.is_multipart():
        payload = None
        for part in b.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get('Content-Disposition'))

            if content_type == 'text/plain' and 'attachment' not in content_disposition:
                try:
                    payload = part.get_payload(decode=True).decode('utf-8')
                except Exception as ex:
                    log.debug(ex)
                    log.debug("Failed to parse message as UTF-8, attempting to detwingle first before retrying parse")
                    payload = UnicodeDammit.detwingle(part.get_payload(decode=True)).decode('utf-8', errors='ignore')
            elif content_type == 'text/html' and 'attachment' not in content_disposition:
                try:
                    payload = part.get_payload(decode=True).decode('utf-8').replace('\n', '')  # decode
                except Exception as ex:
                    log.debug(ex)
                    log.debug("Failed to parse message as UTF-8, attempting to detwingle first before retrying parse")
                    payload = UnicodeDammit.detwingle(part.get_payload(decode=True)).decode('utf-8', errors='ignore').replace('\n', '')

        return payload
    else:
        try:
            return b.get_payload(decode=True).decode('utf-8')
        except Exception as e:
            log.worning(e)
            log.debug(u"\uE05A".encode('unicode-escape'))
            return UnicodeDammit.detwingle(b.get_payload(decode=True)).decode('utf-8', errors='ignore').replace('\n', '')


def attachments(mail, log):
    attachments_list = []
    filename_pattern = re.compile('name=".*"')

    count = 0
    for part in mail.walk():
        count += 1
        if part.get_content_maintype() == 'multipart' or part.get('Content-Disposition') is None:
            continue

        filename = part.get_filename()
        if filename is None:
            content_line = filename_pattern.findall(part.get('Content-Type'))
            if content_line:
                filename = content_line[0].lstrip('name=').strip('"')
                log.debug('Content-Type filename: %s', filename)
        if not filename:
            filename = f'Attachment-{count}'
            log.debug('Dynamic filename: %s', filename)

        content = part.get_payload(decode=False)
        if isinstance(content, str):
            content = part.as_string()
            log.debug('Content not string')
        content = content.replace("\r\n", "")
        attachments_list.append({
            'filename': filename,
            'content': content,
            'content_type': part.get_content_type(),
        })

    if count == 0:
        log.debug("No attachment")
        attachments_list.append({
            'filename': '',
            'content': '',
            'content_type': '',
        })
    return attachments_list
