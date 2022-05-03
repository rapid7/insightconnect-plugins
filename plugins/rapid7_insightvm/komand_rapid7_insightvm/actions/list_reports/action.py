import insightconnect_plugin_runtime
from .schema import ListReportsInput, ListReportsOutput, Input, Output, Component

# Custom imports below
import requests
import json
from komand_rapid7_insightvm.util import endpoints
from insightconnect_plugin_runtime.exceptions import PluginException


class ListReports(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_reports",
            description=Component.DESCRIPTION,
            input=ListReportsInput(),
            output=ListReportsOutput(),
        )

    def run(self, params={}):  # noqa: MC0001
        page = 0
        size = 10
        sort = params.get(Input.SORT)
        name = params.get(Input.NAME)

        try:
            page_response = self.connection.session.get(
                url=endpoints.Report.list_reports(self.connection.console_url, page, size, sort), verify=False
            ).json()
            total_pages = page_response.get("page", {}).get("totalPages", 0)
        except json.decoder.JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)
        except requests.RequestException as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        reports = []

        if name:
            self.logger.info(f"Searching for report matching name {name}")

        for page in range(total_pages):  # pylint: disable=too-many-nested-blocks
            endpoint = endpoints.Report.list_reports(self.connection.console_url, page, size, sort)
            try:
                self.logger.info(f"Trying {endpoint}")
                current_page = self.connection.session.get(url=endpoint, verify=False)
                if current_page.status_code in [200, 201]:  # 200 is documented, 201 is undocumented
                    obtained_reports = current_page.json().get("resources", [])
                    if obtained_reports and isinstance(obtained_reports, list):
                        for report in obtained_reports:
                            if name and report.get("name") == name:
                                self.logger.info(f"Found entry matching {name}")
                                return {
                                    Output.FOUND: True,
                                    Output.LIST: [{"name": report.get("name"), "id": report.get("id")}],
                                }
                            if not name:
                                reports.append(
                                    {
                                        "name": report.get("name", "None"),
                                        "id": report.get("id", "None"),
                                    }
                                )
                    else:
                        self.logger.error(f"Resource is not a key in object returned by InsightVM for {endpoint}")
                        self.logger.debug(current_page)
            except requests.RequestException as error:
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
            except json.decoder.JSONDecodeError:
                self.logger.error(f"InsightVM is returning malformed JSON for {endpoint}")
                continue

        if reports:
            return {Output.FOUND: True, Output.LIST: reports}

        return {Output.FOUND: False, Output.LIST: reports}
