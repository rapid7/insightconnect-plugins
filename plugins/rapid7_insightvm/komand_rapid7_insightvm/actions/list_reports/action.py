import insightconnect_plugin_runtime
from .schema import ListReportsInput, ListReportsOutput

# Custom imports below
import requests
import json
from komand_rapid7_insightvm.util import endpoints


class ListReports(insightconnect_plugin_runtime.Action):
    _ERRORS = {
        401: "Unauthorized",
        404: "Not Found",
        500: "Internal Server Error",
        503: "Service Unavailable",
        000: "Unknown Status Code",
    }

    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_reports",
            description="List reports and return their identifiers",
            input=ListReportsInput(),
            output=ListReportsOutput(),
        )

    def run(self, params={}):  # noqa: MC0001
        page = 0
        size = 1
        sort = params.get("sort")

        name_search = False
        if params.get("name"):
            name = params.get("name")
            name_search = True

        # Get pages
        try:
            # Build API URL
            page_endpoint = endpoints.Report.list_reports(self.connection.console_url, page, size, sort)
            page_resp = self.connection.session.get(url=page_endpoint, verify=False)
            self.logger.info(page_resp.json())
            page_dict = page_resp.json()["page"]
        except json.decoder.JSONDecodeError:
            self.logger.error("InsightVM is returning malformed JSON")
            raise
        except KeyError:
            self.logger.info(page_resp.json())
            reason = "Unknown error occurred. Please contact support or try again later."
            self.logger.error(reason)
            raise

        # Get total pages
        try:
            tp = page_dict["totalPages"]
            self.logger.info(f"Total pages of results: {tp}")
        except KeyError:
            self.logger.error("Unable to obtain totalPages from InsightVM")
            if isinstance(page_dict, dict):
                self.logger.info(page_dict)
            raise

        reports = []

        if name_search is True:
            self.logger.info(f"Searching for report matching name {name}")

        for _ in range(tp):  # pylint: disable=too-many-nested-blocks
            page = page + 1
            # Build API URL
            endpoint = endpoints.Report.list_reports(self.connection.console_url, page, size, sort)
            try:
                self.logger.info(f"Trying {endpoint}")
                item = self.connection.session.get(url=endpoint, verify=False)
                r = item.json()

                if item.status_code in [200, 201]:  # 200 is documented, 201 is undocumented

                    if isinstance(r, dict):
                        if "resources" in r:
                            resources = r["resources"]
                            if isinstance(resources, list):
                                for report in resources:
                                    if name_search is True:
                                        if report["name"] == name:
                                            self.logger.info(f"Found entry matching {name}")
                                            return {
                                                "found": True,
                                                "list": [{"name": report["name"], "id": report["id"]}],
                                            }

                                    reports.append(
                                        {
                                            "name": report.get("name", "None"),
                                            "id": report.get("id", "None"),
                                        }
                                    )
                        else:
                            self.logger.error(f"Resource is not a key in object returned by InsightVM for {endpoint}")
                            self.logger.debug(r)

            except requests.RequestException as e:
                self.logger.error(e)
                raise
            except json.decoder.JSONDecodeError:
                self.logger.error(f"InsightVM is returning malformed JSON for {endpoint}")
                continue

            # Did not find user supplied name
            if name_search is True:
                self.logger.info("Matching report name not found")

        return {"found": False, "list": reports}
