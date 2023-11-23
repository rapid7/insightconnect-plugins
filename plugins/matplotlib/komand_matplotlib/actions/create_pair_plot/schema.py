# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create a pair plot that illustrates the distribution between all numerical columns in a data set"


class Input:
    COLOR_PALETTE = "color_palette"
    CSV_DATA = "csv_data"
    HUE = "hue"
    KIND = "kind"
    MARGIN_STYLE = "margin_style"


class Output:
    CSV = "csv"
    PLOT = "plot"


class CreatePairPlotInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "color_palette": {
      "type": "string",
      "title": "Color Palette",
      "description": "Color palette of the plot",
      "default": "dark",
      "enum": [
        "deep",
        "muted",
        "bright",
        "pastel",
        "dark",
        "colorblind"
      ],
      "order": 4
    },
    "csv_data": {
      "type": "string",
      "format": "bytes",
      "displayType": "bytes",
      "title": "CSV Data",
      "description": "Base64 encoded CSV data from which to create the plot",
      "order": 1
    },
    "hue": {
      "type": "string",
      "title": "Hue",
      "description": "Column by which to provide data segmentation (labels)",
      "order": 3
    },
    "kind": {
      "type": "string",
      "title": "Kind",
      "description": "Kind of data representation to use in the created plot",
      "default": "scatter",
      "enum": [
        "scatter",
        "reg",
        "resid",
        "kde",
        "hex"
      ],
      "order": 2
    },
    "margin_style": {
      "type": "string",
      "title": "Margin Style",
      "description": "Style of the margin of the plot",
      "default": "dark",
      "enum": [
        "darkgrid",
        "whitegrid",
        "dark",
        "white",
        "ticks"
      ],
      "order": 5
    }
  },
  "required": [
    "color_palette",
    "csv_data",
    "kind",
    "margin_style"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreatePairPlotOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "csv": {
      "type": "string",
      "format": "bytes",
      "displayType": "bytes",
      "title": "CSV",
      "description": "Base64 encoded CSV data used to generate the plot",
      "order": 1
    },
    "plot": {
      "type": "string",
      "format": "bytes",
      "displayType": "bytes",
      "title": "Plot",
      "description": "Base64 encoded PNG plot data (can be attached to an email)",
      "order": 2
    }
  },
  "required": [
    "csv",
    "plot"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
