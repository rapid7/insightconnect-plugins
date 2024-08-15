import insightconnect_plugin_runtime
from .schema import ParseTapAlertInput, ParseTapAlertOutput, Input, Output

# Custom imports below
from bs4 import BeautifulSoup
from komand_proofpoint_tap.util.tap_formatter import TAP
from urlextract import URLExtract
from komand_proofpoint_tap.util.helpers import clean
from insightconnect_plugin_runtime.helper import convert_dict_to_camel_case


def parse_html_table(table):
    data = {}
    rows = table.find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        if len(cells) == 2:
            key = cells[0].get_text(strip=True).lower().replace(" ", "_")
            value = cells[1].get_text(strip=True)
            data[key] = value
    return data


class ParseTapAlert(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="parse_tap_alert",
            description="Parses a TAP alert",
            input=ParseTapAlertInput(),
            output=ParseTapAlertOutput(),
        )

    def run(self, params={}):
        tap_alert = params.get(Input.TAPALERT)
        soup = BeautifulSoup(tap_alert, "html.parser")
        tables = soup.find_all("table")

        parsed_tables = []

        for table in tables:
            rows = []
            for row in table.find_all("tr"):
                cols = row.find_all(["td", "th"])
                cols = [ele.text.strip() for ele in cols]
                rows.append(cols)
            parsed_tables.append(rows)

        clean_data = TAP(parsed_tables).data

        # Get the Threat details URL which is NOT an HTML table element, but instead the <a> link of the
        #    table element
        extractor = URLExtract()
        cleaned_input_for_extractor = tap_alert.replace("\n", "")
        urls_from_input = extractor.find_urls(cleaned_input_for_extractor)
        threat_details_urls = list(
            filter(
                lambda u: r"threat/email" in u and r"threatinsight.proofpoint.com" in u[:40],
                urls_from_input,
            )
        )
        if threat_details_urls:
            clean_data["threat"]["threatDetailsUrl"] = threat_details_urls[0]
        clean_data["browser"] = clean(clean_data.get("browser", {}))
        clean_data["message"] = clean(clean_data.get("message", {}))
        clean_data["threat"] = clean(clean_data.get("threat", {}))
        return {Output.RESULTS: convert_dict_to_camel_case(clean_data)}
