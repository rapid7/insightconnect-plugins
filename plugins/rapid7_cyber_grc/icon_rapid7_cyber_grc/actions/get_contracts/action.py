import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetContractsInput, GetContractsOutput, Input, Output, Component

# Custom imports below
from ...util.dates import date_window_clauses, now, odata_datetime


class GetContracts(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_contracts",
            description=Component.DESCRIPTION,
            input=GetContractsInput(),
            output=GetContractsOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        filter_ = params.get(Input.FILTER)
        include_expired = params.get(Input.INCLUDE_EXPIRED)
        order_by = params.get(Input.ORDER_BY)
        renewing_within_days = params.get(Input.RENEWING_WITHIN_DAYS)
        select = params.get(Input.SELECT)
        skip = params.get(Input.SKIP)
        top = params.get(Input.TOP)
        # END INPUT BINDING - DO NOT REMOVE

        # endDate is a plain date field on a contract, so the renewal window narrows the
        # query at the API. Every clause is parenthesised when there is more than one,
        # because an unparenthesised or in the caller's filter would bind looser than the
        # and and widen the result instead. A filter on its own is passed through
        # untouched.
        clauses = [clause for clause in [filter_] + self._window(renewing_within_days, include_expired) if clause]
        if len(clauses) > 1:
            combined = " and ".join(f"({clause})" for clause in clauses)
        else:
            combined = clauses[0] if clauses else None

        records = self.connection.client.list_records(
            "Contracts", filter_=combined, select=select, order_by=order_by, top=top, skip=skip
        )
        return {Output.CONTRACTS: records, Output.COUNT: len(records)}

    @staticmethod
    def _window(renewing_within_days, include_expired):
        """Clauses for the renewal window, empty when no window was asked for.

        A contract that ended last year is not renewing, so the window has a lower bound
        of now as well as an upper bound, unless the caller asks to see the expired ones
        too, which is how a workflow catches a renewal that was already missed.
        """
        clauses = date_window_clauses("endDate", renewing_within_days, False)
        if clauses and not include_expired:
            clauses.append(f"endDate ge {odata_datetime(now())}")
        return clauses
