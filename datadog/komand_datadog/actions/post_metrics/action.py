import komand
from .schema import PostMetricsInput, PostMetricsOutput, Input, Output, Component
# Custom imports below
from komand_datadog.util.endpoints import Metrics
from komand_datadog.util.resource_helper import ResourceHelper


class PostMetrics(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='post_metrics',
                description=Component.DESCRIPTION,
                input=PostMetricsInput(),
                output=PostMetricsOutput())

    def run(self, params={}):
        request = ResourceHelper(self.connection.session, self.logger)
        series = params.get(Input.SERIES)

        if not isinstance(series, list):
            raise Exception('Error: Series input was not an array of objects')
        
        payload = { "series": series }

        self.logger.info(payload)

        url = Metrics.post_metrics(self.connection.url)
        response = request.resource_request(url, 'post', params=self.connection.auth, payload=payload)
        result = response.get('resource')
        if result.get('errors'):
            error = result['errors']
            raise Exception(f'An error occurred with Datadog. Datadog responded with {error}')

        return response
