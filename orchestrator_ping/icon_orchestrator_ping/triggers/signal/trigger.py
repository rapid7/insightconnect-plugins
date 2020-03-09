import komand
from .schema import SignalInput, SignalOutput, Input, Output, Component
# Custom imports below
import atexit


class Signal(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='signal',
                description=Component.DESCRIPTION,
                input=SignalInput(),
                output=SignalOutput())

    def run(self, params={}):
        input_message = params[Input.STARTUP_MESSAGE]
        output_message = params[Input.SHUTDOWN_MESSAGE]

        def exit_handler(delegate: Signal) -> None:
            self.logger.info("Trigger is exiting, sending output message!")
            delegate.send({Output.MESSAGE: output_message})

        atexit.register(exit_handler, **{"delegate": self})

        # Send the startup message first
        self.send({Output.MESSAGE: input_message})

        while True:
            continue
