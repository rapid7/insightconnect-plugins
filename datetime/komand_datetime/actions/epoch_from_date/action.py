import komand
from .schema import EpochFromDateInput, EpochFromDateOutput
# Custom imports below
import maya


class EpochFromDate(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='epoch_from_date',
                description='Convert a datetime to an Epoch',
                input=EpochFromDateInput(),
                output=EpochFromDateOutput())

    def run(self, params={}):
        inp_date = params.get("datetime")
        try:
            mayadt = maya.MayaDT.from_rfc3339(inp_date)
        except TypeError:
            self.logger.error("Non-RFC3339 date provided, input datetime must be RFC3339")
            raise
        except Exception as e:
            self.logger.error("Error occurred: %s" % e)
        else:
            return {"epoch": int(mayadt.epoch)}
