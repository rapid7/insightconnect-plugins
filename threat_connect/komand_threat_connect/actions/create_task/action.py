import komand
from .schema import CreateTaskInput, CreateTaskOutput
# Custom imports below


class CreateTask(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_task',
                description='Create a Task Resource in the ThreatConnect platform',
                input=CreateTaskInput(),
                output=CreateTaskOutput())

    def run(self, params={}):
        tasks = self.connection.threat_connect.tasks()

        # name, owner required
        task = tasks.add(params.get('name'), params.get('owner'))

        if params.get('attributes'):
            a_vals = [list(v.values())[0] for v in params.get('attributes')]
            a_keys = [list(k.keys())[0] for k in params.get('attributes')]
            for i in range(len(a_keys)):
                task.add_attribute(a_keys[i], a_vals[i])

        if params.get('tags'):
            result_tags = [tag.strip() for tag in params.get('tags').split(',')]
            for r_tag in result_tags:
                task.add_tag(r_tag)

        if params.get('security_label'):
            task.set_security_label(params.get('security_label'))

        if params.get('due_date'):
            # date
            task.set_due_date(params.get('due_date'))
        if params.get('escalation_date'):
            # date
            task.set_escalation_date(params.get('escalation_date'))
        if params.get('reminder_date'):
            # date
            task.set_reminder_date(params.get('reminder_date'))
        if params.get('escalated'):
            # boolean
            task.set_escalated(params.get('escalated'))
        if params.get('overdue'):
            # boolean
            task.set_overdue(params.get('overdue'))
        if params.get('reminded'):
            # boolean
            task.set_reminded(params.get('reminded'))
        if params.get('status'):
            # In Progress, Completed, Waiting on Someone, Deferred
            task.set_status(params.get('status'))
        if params.get('assignee'):
            # email
            task.add_assignee(params.get('assignee'))
        if params.get('escalatee'):
            # email
            task.add_escalatee(params.get('escalatee'))

        try:
            a = task.commit()
            return {'id': a.id}
        except RuntimeError as e:
            self.logger.error('Error: {0}'.format(e))
            raise e

    def test(self):
        owners = self.connection.threat_connect.owners()
        owner = ""
        try:
            owners.retrieve()
        except RuntimeError as e:
            raise e

        for owner in owners:
            owner = owner.name
        return {'Owner Name': owner}