import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import SendSmsInput, SendSmsOutput, Input, Output, Component
from twilio.base.exceptions import TwilioRestException
from komand_twilio.util.utils import handle_exception_status_code


class SendSms(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="send_sms",
            description=Component.DESCRIPTION,
            input=SendSmsInput(),
            output=SendSmsOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        message = params.get(Input.MESSAGE, "")
        send_to_number = params.get(Input.TO_NUMBER, "").strip()
        # END INPUT BINDING - DO NOT REMOVE

        try:
            message = self.connection.client.messages.create(
                body=message,
                to=send_to_number,
                from_=self.connection.twilio_phone_number,
            )
            return {Output.MESSAGE_SID: message.sid}
        except TwilioRestException as error:
            handle_exception_status_code(error)
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
