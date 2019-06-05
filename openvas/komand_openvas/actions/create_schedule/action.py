import komand
from .schema import CreateScheduleInput, CreateScheduleOutput
# Custom imports below
import sys


class CreateSchedule(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_schedule',
                description='Create a schedule to run a scan on.',
                input=CreateScheduleInput(),
                output=CreateScheduleOutput())

    def isLeapYear(self, year):
        if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
            return True
        return False

    def validateDateTime(self, hour, minute, month, day, year):
        if hour > 23 or hour < 0:
            raise ValueError('Hour is invalid, should be between 0 and 23')
        if minute > 59 or minute < 0:
            raise ValueError('Minute is invalid, should be between 0 and 59')
        if month > 12 or month < 0:
            raise ValueError('Month is invalid, should be between 0 and 12')
        month31s = [1,3,5,7,8,10,12]
        month30s = [4,6,9,11]
        if month in month31s:
            if day > 31 or day < 0:
                raise ValueError('Day is invalid, should be between 0 and 31 for month ' + str(month))
        elif month in month30s:
            if day > 30 or day < 0:
                raise ValueError('Day is invalid, should be between 0 and 30 for month ' + str(month))
        else:
            if self.isLeapYear(year):
                if day > 29 or day < 0:
                    raise ValueError('Day is invalid, should be between 0 and 29 for month ' + str(month) + ' and year ' + year)
            else:
                if day > 28 or day < 0:
                    raise ValueError('Day is invalid, should be between 0 and 28 for month ' + str(month))
        if year < 0:
            raise ValueError('Year is invalid, sorry, we dont deal with BC')
        return

    def run(self, params={}):
        name = str(params.get('name'))
        duration = params.get('duration') # can return None, if nothing there
        if duration:
            duration = int(duration)
        period = params.get('period')
        if period:
            period = int(period)
        first_time_dict = dict(params.get('first_time'))

        if duration is not None:
            if duration < 0:
                self.logger.error('Error trying to parse duration, cannot be negative')
                return {'schedule_id': '', 'success': False,
                        'message': 'Error trying to parse duration, cannot be negative'}
        if period is not None:
            if period < 0:
                self.logger.error('Error trying to parse period, cannot be negative')
                return {'schedule_id': '', 'success': False,
                        'message': 'Error trying to parse period, cannot be negative'}

        first_time_hour = int(first_time_dict['hour'])
        first_time_minute = int(first_time_dict['minute'])
        first_time_month = int(first_time_dict['month'])
        first_time_day = int(first_time_dict['day'])
        first_time_year = int(first_time_dict['year'])
        try:
            self.validateDateTime(first_time_hour, first_time_minute, first_time_month, first_time_day, first_time_year)
        except ValueError as err:
            self.logger.error('Error trying to parse First Time datetime object: ' + str(err))
            return {'schedule_id': '', 'success': False, 'message': 'Error trying to parse First Time datetime object: '
                                                                    + str(err)}

        try:
            if duration and period:
                schedule_id = self.connection.scanner.create_schedule(name=name, hour=first_time_hour,
                                                                      minute=first_time_minute,month=first_time_month,
                                                                      day=first_time_day,year=first_time_year,
                                                                      period=period, duration=duration)
            elif duration and not period:
                schedule_id = self.connection.scanner.create_schedule(name=name, hour=first_time_hour,
                                                                      minute=first_time_minute,month=first_time_month,
                                                                      day=first_time_day, year=first_time_year,
                                                                      duration=duration)
            elif not duration and period:
                schedule_id = self.connection.scanner.create_schedule(name=name, hour=first_time_hour,
                                                                      minute=first_time_minute, month=first_time_month,
                                                                      day=first_time_day, year=first_time_year,
                                                                      period=period)
            else:
                schedule_id = self.connection.scanner.create_schedule(name=name, hour=first_time_hour,
                                                                      minute=first_time_minute, month=first_time_month,
                                                                      day=first_time_day, year=first_time_year)
        except:
            self.logger.error('Error creating schedule: ' + ' | '.join([str(sys.exc_info()[0]),str(sys.exc_info()[1])]))
            return{'schedule_id': '', 'success': False, 'message': 'Error creating schedule: ' +
                                                                   ' | '.join([str(sys.exc_info()[0]),
                                                                               str(sys.exc_info()[1])])}

        return {'schedule_id': schedule_id, 'success': True, 'message': 'Successfully created new schedule.'}

    def test(self):
        """TODO: Test action"""
        return {}
