import komand
from .schema import ParseInput, ParseOutput
# Custom imports below
import base64
import email
from komand_eml.util import utils
from bs4 import UnicodeDammit


class Parse(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='parse',
                description='Extract headers and file attachments',
                input=ParseInput(),
                output=ParseOutput())

    def run(self, params={}):
        result = {}
        try:
            eml_file = base64.b64decode(params.get('eml_file')).decode('utf-8')
        except Exception as ex:
            self.logger.debug(ex)
            self.logger.debug("Failed to parse message as UTF-8, attempting to detwingle first before retrying parse")
            eml_file = UnicodeDammit.detwingle(base64.b64decode(params.get('eml_file'))).decode('utf-8', errors='ignore')
        msg = email.message_from_string(eml_file)

        result['date'] = msg['Date']
        result['from'] = msg['From']
        result['to'] = msg['To'] or msg['Delivered-To'] or ''
        if result['to'] == None:
            result['to'] == ''
        if result['to'] == '':
            self.logger.debug("No To address.")
        result['subject'] = msg['Subject']
        bdy = utils.body(msg, self.logger)
        result['body'] = bdy
        atchs = utils.attachments(msg, self.logger)
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
        self.logger.info("*"*10)
        self.logger.info({ 'result': result })
        return { 'result': result }

    def test(self, params={}):
        return {}
