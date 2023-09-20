import insightconnect_plugin_runtime
from .schema import GetManagedAppsInput, GetManagedAppsOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.helper import clean
import validators


class GetManagedApps(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_managed_apps",
            description=Component.DESCRIPTION,
            input=GetManagedAppsInput(),
            output=GetManagedAppsOutput(),
        )

    def run(self, params={}):
        app = params.get(Input.APP)
        if validators.uuid(app):
            return {Output.MANAGEDAPPS: clean(self.connection.api.get_managed_app(app))}
        return {Output.MANAGEDAPPS: clean(self.connection.api.get_managed_apps_all_pages(app))}
