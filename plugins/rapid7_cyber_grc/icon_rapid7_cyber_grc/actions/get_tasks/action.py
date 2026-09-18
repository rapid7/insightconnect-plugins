import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetTasksInput, GetTasksOutput, Input, Output, Component

# Custom imports below
from ...util.dates import date_window_clauses

# The field holding the assignee on a task, and the two fields inside it a caller is
# likely to know the owner by.
ASSIGNEE_FIELD = "assignedTo"
ASSIGNEE_EMAIL = "userEmail"
ASSIGNEE_ID = "usersID"


class GetTasks(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_tasks", description=Component.DESCRIPTION, input=GetTasksInput(), output=GetTasksOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        due_within_days = params.get(Input.DUE_WITHIN_DAYS)
        filter = params.get(Input.FILTER)
        order_by = params.get(Input.ORDER_BY)
        overdue_only = params.get(Input.OVERDUE_ONLY)
        owner = params.get(Input.OWNER)
        select = params.get(Input.SELECT)
        skip = params.get(Input.SKIP)
        status_id = params.get(Input.STATUS_ID)
        top = params.get(Input.TOP)
        # END INPUT BINDING - DO NOT REMOVE

        # statusID and dueDate are plain scalar fields on a task, so a status and a due
        # date window both narrow the query at the API rather than here. When they join a
        # filter the caller wrote, every clause is parenthesised, because an
        # unparenthesised or in that filter would bind looser than the and and widen the
        # result instead. A filter on its own is passed through untouched.
        clauses = [
            clause
            for clause in [filter, f"statusID eq {status_id}" if status_id else None]
            + date_window_clauses("dueDate", due_within_days, overdue_only)
            if clause
        ]
        if len(clauses) > 1:
            combined = " and ".join(f"({clause})" for clause in clauses)
        else:
            combined = clauses[0] if clauses else None

        if not (owner or "").strip():
            records = self.connection.client.list_records(
                "Tasks", filter_=combined, select=select, order_by=order_by, top=top, skip=skip
            )
            return {Output.TASKS: records, Output.COUNT: len(records)}

        # The assignee is a nested object with no filterable scalar ID beside it, so an
        # owner cannot be given to $filter. Read the tasks the rest of the query matches
        # and apply the owner here, then window the result so Top and Skip count the
        # owner's tasks rather than every task the API returned.
        records = self.connection.client.list_records(
            "Tasks", filter_=combined, select=self._with_assignee(select), order_by=order_by
        )
        matching = [record for record in records if self._assigned_to(record, owner)]
        self.logger.info(f"{len(matching)} of {len(records)} task(s) are assigned to {owner}")

        windowed = matching[skip:] if skip else matching
        if top:
            windowed = windowed[:top]
        return {Output.TASKS: windowed, Output.COUNT: len(windowed)}

    @staticmethod
    def _with_assignee(select):
        """A Select that leaves the assignee out would filter every task away."""
        if not select:
            return select
        fields = [field.strip() for field in select.split(",") if field.strip()]
        if ASSIGNEE_FIELD not in fields:
            fields.append(ASSIGNEE_FIELD)
        return ",".join(fields)

    @staticmethod
    def _assigned_to(record, owner):
        """Match the owner against the assignee's email address or numeric user ID."""
        assignee = record.get(ASSIGNEE_FIELD) or {}
        wanted = owner.strip().casefold()
        email = str(assignee.get(ASSIGNEE_EMAIL) or "").strip().casefold()
        return wanted in (email, str(assignee.get(ASSIGNEE_ID) or ""))
