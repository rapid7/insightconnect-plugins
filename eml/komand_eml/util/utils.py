# Custom imports below
import re
import email
from bs4 import UnicodeDammit


def body(b, log):
    if b.is_multipart():
        for part in b.walk():
            ctype = part.get_content_type()
            cdispo = str(part.get('Content-Disposition'))

            # skip any text/plain (txt) attachments
            if ctype == 'text/plain' and 'attachment' not in cdispo:
                try:
                    body = part.get_payload(decode=True).decode('utf-8')  # decode
                except Exception as ex:
                    log.debug(ex)
                    log.debug("Failed to parse message as UTF-8, attempting to detwingle first before retrying parse")
                    body = UnicodeDammit.detwingle(part.get_payload(decode=True)).decode('utf-8', errors='ignore')
            elif ctype == 'text/html' and 'attachment' not in cdispo:
                try:
                    body = part.get_payload(decode=True).decode('utf-8').replace('\n','')  # decode
                except Exception as ex:
                    log.debug(ex)
                    log.debug("Failed to parse message as UTF-8, attempting to detwingle first before retrying parse")

                    body = UnicodeDammit.detwingle(part.get_payload(decode=True)).decode('utf-8', errors='ignore').replace('\n','')


        return body
    else:
        try:
            return b.get_payload(decode=True).decode('utf-8')
        except:
            log.debug(u"\uE05A".encode('unicode-escape'))
            return UnicodeDammit.detwingle(b.get_payload(decode=True)).decode('utf-8', errors='ignore').replace('\n','')

def attachments(mail, log):
    attachments = []

    filename_pattern = re.compile('name=".*"')

    count = 0
    for part in mail.walk():
        count += 1
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

        filename = part.get_filename()

        if filename is None:
            # Attempt to get filename from Content-Type header
            content_line = filename_pattern.findall(part.get('Content-Type'))
            # Test if array has contents
            if content_line:
               # Attempt parsing filename, it *might* be here
               filename = content_line[0].lstrip('name=').strip('"')

               log.debug('Content-Type filename: %s', filename)
        # Fall back to a dynamic file name chosen by us
        if not filename:
            filename = 'Attachment-{}'.format(count)
            log.debug('Dynamic filename: %s', filename)


        content = part.get_payload(decode=False)
        if type(content) != type(''):
            #attached email
            content = part.as_string()
            log.debug('Content not string')
        content = content.replace("\r\n","")
        attachments.append({
            'filename': filename,
            'content': content,
            'content_type': part.get_content_type(),
            })

    if count == 0:
        log.debug("No attachment")
        attachments.append({
            'filename': '',
            'content': '',
            'content_type': '',
            })
    return attachments
