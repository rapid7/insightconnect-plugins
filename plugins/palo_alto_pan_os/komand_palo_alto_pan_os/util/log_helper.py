from insightconnect_plugin_runtime.action import Action


class LogHelper(Action):
    def __init__(self) -> None:
        super(self.__class__, self).__init__(name="loghelper", description="Log Helper", input=None, output=None)

    def run(self, params={}) -> None:
        pass

    def test(self, params={}) -> None:
        pass
