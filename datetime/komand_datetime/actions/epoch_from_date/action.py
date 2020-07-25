import insightconnect_plugin_runtime
from .schema import EpochFromDateInput, EpochFromDateOutput, Input, Output
# Custom imports below
import maya


class EpochFromDate(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='epoch_from_date',
                description='Convert a datetime to an Epoch',
                input=EpochFromDateInput(),
                output=EpochFromDateOutput())

    def run(self, params={}):
        inp_date = params.get(Input.DATETIME)
        try:
            mayadt = maya.MayaDT.from_rfc3339(inp_date)
        except TypeError:
            self.logger.error("Non-RFC3339 date provided, input datetime must be RFC3339")
            raise
        except Exception as e:
            self.logger.error("Error occurred: {}".format(e))
        else:
            return {Output.EPOCH: int(mayadt.epoch)}
