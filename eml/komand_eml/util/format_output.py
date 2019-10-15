import komand_eml.util.utils as utils
import email


def format_result(logger, msg):
    result = {}
    result['date'] = msg['Date']
    result['from'] = msg['From']
    result['to'] = msg['To'] or msg['Delivered-To'] or ''
    if result['to'] == None:
        result['to'] == ''
    if result['to'] == '':
        logger.debug("No To address.")
    result['subject'] = msg['Subject']
    bdy = utils.body(msg, logger)
    result['body'] = bdy
    atchs = utils.attachments(msg, logger)
    result['attachments'] = []
    for a in atchs:
        result['attachments'].append(a)
    parser = email.parser.HeaderParser()
    headers = parser.parsestr(msg.as_string())
    header_list = []
    for h in headers.items():
        header_list.append({
            'key': h[0],
            'value': h[1]
        })
    result['headers'] = header_list
    logger.info("*" * 10)
    logger.info({'result': result})
    return result
