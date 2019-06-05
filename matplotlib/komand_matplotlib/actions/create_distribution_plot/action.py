import komand
from .schema import CreateDistributionPlotInput, CreateDistributionPlotOutput
# Custom imports below
import base64
import pandas as pd
import seaborn as sns
from io import BytesIO


class CreateDistributionPlot(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_distribution_plot',
                description='Create a distribution plot that illustrates the distribution between two data series',
                input=CreateDistributionPlotInput(),
                output=CreateDistributionPlotOutput())

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

        column = params.get('column')
        df = pd.read_csv(BytesIO(decoded_data))

        if not column or (column not in df):
            error = f"Column ({column}) not found in data set, cannot create plot..."
            self.logger.error(error)
            return Exception(error)

        # AxesSubplots (the plot object returned) don't have the savefig method, get the figure, then save it
        self.logger.info("Creating plot...")
        plot = sns.distplot(df[column], kde=params.get('kde'))
        fig = plot.get_figure()

        # bbox_inches is required to ensure that labels are cut off
        fig.savefig('plot.png', bbox_inches="tight")
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
