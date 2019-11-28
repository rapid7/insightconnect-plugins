import komand
from .schema import GetAssetVulnerabilitiesInput, GetAssetVulnerabilitiesOutput
# Custom imports below
import requests
from komand_rapid7_insightvm.util import endpoints
from collections import namedtuple
import json
from komand.exceptions import PluginException


class GetAssetVulnerabilities(komand.Action):

    _ERRORS = {
        401: "Unauthorized",
        404: "Not Found",
        500: "Internal Server Error",
        503: "Service Unavailable",
        000: "Unknown Status Code"
    }

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_asset_vulnerabilities',
                description='Get vulnerabilities found on an asset. Can only be used if the asset has first been scanned (via Komand or other means)',
                input=GetAssetVulnerabilitiesInput(),
                output=GetAssetVulnerabilitiesOutput())

    def run(self, params={}):
        asset_id = params.get("asset_id")
        endpoint = endpoints.VulnerabilityResult.vulnerabilities_for_asset(self.connection.console_url, asset_id)
        self.logger.info("Using %s ..." % endpoint)

        vulnerabilities = []
        current_page = 0
        while True:
            self.logger.info("Fetching results from page %d" % current_page)
            response = self.get_vulnerabilities(endpoint=endpoint, endpoint_page=current_page)

            vulnerabilities += response.resources  # Grab resources and append to total
            self.logger.info("Got %d vulnerabilities from page %d / %d" % (len(response.resources),
                                                                           response.page_num,
                                                                           response.total_pages))

            if (response.total_pages == 0) or ((response.total_pages - 1) == response.page_num):
                self.logger.info("All pages consumed, returning results...")
                break  # exit the loop
            else:
                self.logger.info("More pages exist, fetching...")
                current_page += 1

        return {"vulnerabilities": vulnerabilities}

    def get_vulnerabilities(self, endpoint, endpoint_page, size=500):
        """
        Retrieves vulnerabilities for an asset
        :param endpoint: Endpoint to reach
        :param endpoint_page: The page to retrieve results for (due to pagination)
        :param size: How many results to retrieve per call, default to 500
        :return: Namedtuple object containing current page number, total pages, and results
        """
        self.logger.info("Fetching up to %d vulnerabilities from endpoint page %d ..." % (size, endpoint_page))
        try:
            response = self.connection.session.get(url=endpoint,
                                                   verify=False,
                                                   params={"size": size,
                                                           "page": endpoint_page}
                                                   )
        except requests.RequestException as e:
            self.logger.error(e)
            raise

        else:
            if response.status_code in [200, 201]:  # 200 is documented, 201 is undocumented
                response_json = response.json()

                Result = namedtuple("Result", "page_num total_pages resources")
                r = Result(page_num=response_json["page"]["number"],
                           total_pages=response_json["page"]["totalPages"],
                           resources=response_json["resources"])

                return r

            else:
                try:
                    reason = response.json()["message"]
                except KeyError:
                    reason = "Unknown error occurred. Please contact support or try again later."
                except json.decoder.JSONDecodeError:
                    raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=reason.text)

                status_code_message = self._ERRORS.get(response.status_code, self._ERRORS[000])
                self.logger.error("{status} ({code}): {reason}".format(status=status_code_message,
                                                                       code=response.status_code,
                                                                       reason=reason))
                raise PluginException(preset=PluginException.Preset.UNKNOWN)
