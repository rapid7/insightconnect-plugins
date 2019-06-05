import komand
from .schema import SchedReportInput, SchedReportOutput
# Custom imports below


class SchedReport(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='sched_report',
                description='Check if an indexation has been launched within threshold (by default 12 days, can be changed in Hippocampe/core/conf/hippo/hippo.conf)',
                input=SchedReportInput(),
                output=SchedReportOutput())

    def run(self, params={}):
        launched_indexations = self.connection.api.sched_report()
        return {'launched_indexations': launched_indexations}
