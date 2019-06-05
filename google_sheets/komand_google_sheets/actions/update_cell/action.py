import komand
from .schema import UpdateCellInput, UpdateCellOutput
# Custom imports below
import gspread


class UpdateCell(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_cell',
                description='Updates a specified cell in Google Sheets with new data',
                input=UpdateCellInput(),
                output=UpdateCellOutput())

    def run(self, params={}):
        sheet = params.get('sheet_id')
        cell = params.get('cell')
        update = params.get('update')
        worksheet = params.get('worksheet')

        try:
            active_sheet = self.connection.google_client.open_by_key(sheet)
        except gspread.exceptions.APIError as e:
            self.logger.error(e)
            raise Exception(e['error']['message'])
        try:
            active_work_sheet = active_sheet.worksheet(worksheet)
        except gspread.exceptions.WorksheetNotFound as e:
            raise Exception(e)
        try:
            info = active_work_sheet.update_acell(cell, update)
        except gspread.exceptions.IncorrectCellLabel as e:
            raise Exception(e)
        value = active_work_sheet.acell(cell).value

        return {'value': value, 'update_information': info}

    def test(self):
        if self.connection.test():
            return {'value': 'sample', 'update_information': {}}
