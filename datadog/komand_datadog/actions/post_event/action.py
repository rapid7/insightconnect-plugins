import komand
from .schema import PostEventInput, PostEventOutput, Input, Output, Component
# Custom imports below
from komand_datadog.util.endpoints import Events
from komand_datadog.util.resource_helper import ResourceHelper


class PostEvent(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='post_event',
                description=Component.DESCRIPTION,
                input=PostEventInput(),
                output=PostEventOutput())

    def run(self, params={}):
        request = ResourceHelper(self.connection.session, self.logger)
        tags = params.get(Input.TAGS)
        # Create tags list
        tags = tags.split(',')
        temp = {'title': params.get(Input.EVENT_TITLE),
                'text': params.get(Input.TEXT),
                'date_happened': params.get(Input.DATE_HAPPENED),
                'priority': params.get(Input.PRIORITY),
                'host': params.get(Input.HOST),
                'tags': tags,
                'alert_type': params.get(Input.ALERT_TYPE)}
        # If tags list is [''] remove tags
        if not temp['tags'][0]:
            del temp['tags']

        payload = dict()
        # create payload values only if they exist
        for item in temp:
            if temp[item]:
                payload[item] = temp[item]

        url = Events.events(self.connection.url)
        response = request.resource_request(url, 'post', params=self.connection.auth, payload=payload)
        result = response.get('resource')
        if result.get('errors'):
            error = result['errors']
            raise Exception(f'An error occurred with Datadog. Datadog responded with {error}')

        try:
            for item in result['event']:
                if result['event'][item] is None:
                    result['event'][item] = ''
        except KeyError:
            self.logger.error(result)
            raise Exception('Data returned from Datadog was in an unexpected format. Contact support for help.')

        if result['event'].get('tags') == '':
            result['event']['tags'] = []
        if result['event'].get('related_event_id') == '':
            result['event']['related_event_id'] = []
        return {Output.EVENT: result['event']}
