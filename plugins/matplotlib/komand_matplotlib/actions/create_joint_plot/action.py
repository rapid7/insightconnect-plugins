import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import CreateJointPlotInput, CreateJointPlotOutput

# Custom imports below
import base64
import pandas as pd
import seaborn as sns
from io import BytesIO


class CreateJointPlot(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_joint_plot",
            description="Create a joint plot that illustrates the distribution between two data series",
            input=CreateJointPlotInput(),
            output=CreateJointPlotOutput(),
        )

    def run(self, params={}):
        # Set styles
        sns.set_palette(params.get("color_palette"))
        sns.set(style=params.get("margin_style"))

        # Process the data and create the plot
        try:
            decoded_data = base64.b64decode(params.get("csv_data"))
        except Exception as error:
            self.logger.error(f"Failed to decode base64 encoded CSV data with error: {error}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        df = pd.read_csv(BytesIO(decoded_data))
        x = params.get("x_value")
        y = params.get("y_value")
        kind = params.get("kind")

        args = {"data": df, "x": x, "y": y, "kind": kind}

        if not x or (x not in df):
            error = f"Column for X value({x}) not in data set, cannot create plot..."
            self.logger.error(error)
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
        elif not y or (y not in df):
            error = f"Column for Y value ({y}) not in data set, cannot create plot..."
            self.logger.error(error)
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        # JointPlots have the savefig method, call it directly
        self.logger.info("Creating plot...")
        plot = sns.jointplot(**args)

        # bbox_inches is required to ensure that labels are cut off
        plot.savefig("plot.png", bbox_inches="tight")
        with open(
            "plot.png",
            "rb",
        ) as f:
            plot = base64.b64encode(f.read())

        return {"csv": params.get("csv_data"), "plot": plot.decode("utf-8")}

    def test(self):
        self.logger.info("No connection required, success!")
        return {"csv": "", "plot": ""}
