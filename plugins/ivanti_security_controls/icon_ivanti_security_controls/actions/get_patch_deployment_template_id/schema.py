# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get a Patch Deployment Template ID by searching for the Patch Deployment Template Name"


class Input:
    PATCH_DEPLOYMENT_TEMPLATE_NAME = "patch_deployment_template_name"


class Output:
    PATCH_DEPLOYMENT_TEMPLATE_ID = "patch_deployment_template_id"


class GetPatchDeploymentTemplateIdInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "patch_deployment_template_name": {
      "type": "string",
      "title": "Patch Deployment Template Name",
      "description": "The name of the patch deployment template",
      "order": 1
    }
  },
  "required": [
    "patch_deployment_template_name"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetPatchDeploymentTemplateIdOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "patch_deployment_template_id": {
      "type": "string",
      "title": "Patch Deployment Template ID",
      "description": "The ID of the patch deployment template",
      "order": 1
    }
  },
  "required": [
    "patch_deployment_template_id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
