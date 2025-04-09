from abc import ABC, abstractmethod

import pypandoc
from insightconnect_plugin_runtime.plugin import is_running_in_cloud

from icon_html.util.helpers import convert_with_temporary_file


class HTMLConverterStrategy(ABC):
    """General abstraction layer for HTMLConverter strategy"""

    @abstractmethod
    def convert(self, input_html_string: str) -> str:
        pass


class ConvertToDocx(HTMLConverterStrategy):
    def convert(self, input_html_string: str) -> str:
        return convert_with_temporary_file(
            input_html_string,
            "docx",
            "html",
            "temp_html_2_docx.docx",
            sandbox=is_running_in_cloud(),
        )


class ConvertToEpub(HTMLConverterStrategy):
    def convert(self, input_html_string: str) -> str:
        return convert_with_temporary_file(
            input_html_string,
            "epub",
            "html",
            "temp_html_3_epub.epub",
            sandbox=is_running_in_cloud(),
        )


class ConvertToHTML(HTMLConverterStrategy):
    def convert(self, input_html_string: str) -> str:
        return pypandoc.convert_text(input_html_string, "html", "md", sandbox=is_running_in_cloud())


class ConvertToHTML5(HTMLConverterStrategy):
    def convert(self, input_html_string: str) -> str:
        return pypandoc.convert_text(input_html_string, "html5", "md", sandbox=is_running_in_cloud())


class ConvertToMarkdown(HTMLConverterStrategy):
    def convert(self, input_html_string: str) -> str:
        return pypandoc.convert_text(input_html_string, "rst", "html", sandbox=is_running_in_cloud())


class ConvertToPDF(HTMLConverterStrategy):
    def convert(self, input_html_string: str) -> str:
        return convert_with_temporary_file(
            input_html_string,
            "pdf",
            "html",
            "temp_html_2_pdf.pdf",
            sandbox=is_running_in_cloud(),
        )
