import komand
from .schema import SpreadListToSheetInput, SpreadListToSheetOutput, Input, Output
# Custom imports below
import gspread


class SpreadListToSheet(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='spread_list_to_sheet',
            description='Given a starting cell, this action will take a list of data and push it to either rows or columns in a Google Sheet',
            input=SpreadListToSheetInput(),
            output=SpreadListToSheetOutput())

    def run(self, params={}):
        sheet = params.get(Input.SHEET_ID)
        start_cell = params.get(Input.CELL)
        update_list = params.get(Input.UPDATE_LIST)
        worksheet = params.get(Input.WORKSHEET)
        direction = params.get(Input.DIRECTION)

        active_work_sheet = self.get_active_work_sheet(sheet, worksheet)
        cell_range = self.create_target_cell_range(direction, start_cell, update_list)
        cell_list = self.update_cells(active_work_sheet, cell_range, update_list)
        info = self.push_cells(active_work_sheet, cell_list)

        return {Output.UPDATE_INFORMATION: info}

    def update_cells(self, active_work_sheet, cell_range, update_list):
        self.logger.info("Getting cell range")
        cell_list = active_work_sheet.range(cell_range)
        for i, cell in enumerate(cell_list):
            cell.value = update_list[i]
        return cell_list

    def get_active_work_sheet(self, sheet, worksheet):
        try:
            active_sheet = self.connection.google_client.open_by_key(sheet)
        except gspread.exceptions.APIError as e:
            self.logger.error(e)
            raise Exception(e['error']['message'])
        self.logger.info("Getting sheet " + worksheet + " from active sheet " + sheet)
        try:
            active_work_sheet = active_sheet.worksheet(worksheet)
        except gspread.exceptions.WorksheetNotFound as e:
            raise Exception(e)
        return active_work_sheet

    def push_cells(self, active_work_sheet, cell_list):
        self.logger.info(str("Updated cells, pushing to sheet"))
        try:
            info = active_work_sheet.update_cells(cell_list)
        except gspread.exceptions.IncorrectCellLabel as e:
            raise Exception(e)
        return info

    def create_target_cell_range(self, direction, start_cell, update_list):
        start_cell_cord = gspread.utils.a1_to_rowcol(start_cell)
        list_size = len(update_list) - 1

        self.logger.info("Direction: " + direction)
        if direction == "column":
            end_cell_cord = (start_cell_cord[0] + list_size, start_cell_cord[1])
        else:
            end_cell_cord = (start_cell_cord[0], start_cell_cord[1] + list_size)

        end_cell = gspread.utils.rowcol_to_a1(end_cell_cord[0], end_cell_cord[1])
        cell_range = start_cell + ":" + end_cell
        self.logger.info("Target range: " + str(cell_range))

        return cell_range
