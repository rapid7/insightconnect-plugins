import komand
from .schema import MetricsRenderInput, MetricsRenderOutput
# Custom imports below
import base64


class MetricsRender(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='metrics_render',
                description='Render metrics data as a graph',
                input=MetricsRenderInput(),
                output=MetricsRenderOutput())

    def run(self, params={}):
        query = komand.helper.clean_dict(params)
        for (tvar, tsub) in query.pop('templates', {}).items():
            query['template[%s]' % tvar] = tsub

        graph_params = query.pop('graph_params', {})

        # unset literal value
        if graph_params.get('hideLegend', '') == 'unset':
            graph_params.pop('hideLegend')

        # convert list values to comma-separated strings
        color_list = graph_params.pop('colorList', [])
        if color_list:
            graph_params['colorList'] = ','.join(color_list)
        y_divisors = graph_params.pop('yDivisors', [])
        if y_divisors:
            graph_params['yDivisors'] = ','.join(y_divisors)

        # remove params without known defaults
        # to avoid overriding graphite_api's inbuilt defaults
        for gkey in ('leftWidth', 'logBase', 'rightWidth', 'valueLabelsMin',
                     'yMax', 'yMaxLeft', 'yMaxRight',
                     'yStep', 'yStepLeft', 'yStepRight',
                     'yMin', 'yMinLeft', 'yMinRight'):
            if graph_params.get(gkey, -1) == 0:
                graph_params.pop(gkey)

        query.update(komand.helper.clean_dict(graph_params))

        response = self.connection.request(
            'GET', ('render',),
            params=query
        )
        if response.ok:
            return {'graph': base64.b64encode(response.content).decode('utf-8')}
        else:
            self.logger.error('Graphite API: ' + response.json().get('message', ''))
            response.raise_for_status()

    def test(self):
        return self.connection.test()
