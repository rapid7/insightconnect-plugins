import komand
from .schema import TextInput, TextOutput, Input, Output, Component
# Custom imports below
from bs4 import BeautifulSoup

class Text(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='text',
                description=Component.DESCRIPTION,
                input=TextInput(),
                output=TextOutput())

    def run(self, params={}):
        in_text = params.get(Input.DOC)
        remove_scripts = params.get(Input.REMOVE_SCRIPTS, False)
        if in_text: # BeautifulSoup will bomb on null text
            soup = BeautifulSoup(in_text, features='html.parser')
            if remove_scripts:
                for script in soup(["script", "style"]):  # remove all javascript and stylesheet code
                    script.extract()
            output = soup.get_text()
            return {Output.TEXT: output}
        else:
            return {Output.TEXT: ""}
