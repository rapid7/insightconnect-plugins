import komand
from .schema import CreatePairPlotInput, CreatePairPlotOutput
# Custom imports below
import base64
import pandas as pd
import seaborn as sns
from io import BytesIO


class CreatePairPlot(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_pair_plot',
                description='Create a pair plot that illustrates the distribution between all numerical columns in a data set',
                input=CreatePairPlotInput(),
                output=CreatePairPlotOutput())

    def run(self, params={}):
        # Set styles
        sns.set_palette(params.get('color_palette'))
        sns.set(style=params.get('margin_style'))

        # Process the data and create the plot
        try:
            decoded_data = base64.b64decode(params.get('csv_data'))
        except Exception as e:
            error = f"Failed to decode base64 encoded CSV data with error: {e}"
            self.logger.error(error)
            raise e

        df = pd.read_csv(BytesIO(decoded_data))
        kind = params.get('kind')
        hue = params.get('hue')

        args = {
            "kind": kind
        }

        if hue and (len(hue) > 0):
            args['hue'] = hue

            if hue not in df:
                error = f"Column for hue ({hue}) not in data set, cannot create plot..."
                self.logger.error(error)
                return Exception(error)

        # Pairgrids have the savefig method, call it directly
        self.logger.info("Creating plot...")
        plot = sns.pairplot(df, **args)

        # bbox_inches is required to ensure that labels are cut off
        plot.savefig('plot.png', bbox_inches="tight")
        with open('plot.png', 'rb') as f:
            plot = base64.b64encode(f.read())

        return {
            "csv": params.get('csv_data'),
            "plot": plot.decode('utf-8')
        }

    def test(self):
        self.logger.info('No connection required, success!')
        return {
            "csv": "",
            "plot": ""
        }
