from abc import ABC, abstractmethod

import pypandoc
from icon_html.util.helpers import read_file_content, convert_with_temporary_file


class HTMLConverterStrategy(ABC):
    """General abstraction layer for HTMLConverter strategy"""

    @abstractmethod
    def convert(self, input_html_string: str) -> str:
        pass


class ConvertToDocx(HTMLConverterStrategy):
    def convert(self, input_html_string: str) -> str:
        return convert_with_temporary_file(input_html_string, "docx", "html", "temp_html_2_docx.docx")


class ConvertToEpub(HTMLConverterStrategy):
    def convert(self, input_html_string: str) -> str:
        return convert_with_temporary_file(input_html_string, "epub", "html", "temp_html_3_epub.epub")


class ConvertToHTML(HTMLConverterStrategy):
    def convert(self, input_html_string: str) -> str:
        return pypandoc.convert_text(input_html_string, "html", "md")


class ConvertToHTML5(HTMLConverterStrategy):
    def convert(self, input_html_string: str) -> str:
        return pypandoc.convert_text(input_html_string, "html5", "md")


class ConvertToMarkdown(HTMLConverterStrategy):
    def convert(self, input_html_string: str) -> str:
        return pypandoc.convert_text(input_html_string, "rst", "html")


class ConvertToPDF(HTMLConverterStrategy):
    def convert(self, input_html_string: str) -> str:
        return convert_with_temporary_file(input_html_string, "pdf", "html", "temp_html_2_pdf.pdf")
