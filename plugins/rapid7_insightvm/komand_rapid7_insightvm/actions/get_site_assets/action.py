import komand
from .schema import GetSiteAssetsInput, GetSiteAssetsOutput

# Custom imports below
import requests
from komand_rapid7_insightvm.util import endpoints
from collections import namedtuple
import json
from komand.exceptions import PluginException


class GetSiteAssets(komand.Action):
    _ERRORS = {
        400: "Bad Request",
        401: "Unauthorized",
        500: "Internal Server Error",
        503: "Service Unavailable",
        000: "Unknown Status Code",
    }

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_site_assets",
            description="Gets assets for a site",
            input=GetSiteAssetsInput(),
            output=GetSiteAssetsOutput(),
        )

    def run(self, params={}):
        site_id = params.get("site_id")
        endpoint = endpoints.Site.get_site_assets(self.connection.console_url, site_id)
        self.logger.info("Using %s ..." % endpoint)

        resources = []
        current_page = 0
        while True:
            self.logger.info("Fetching results from page %d" % current_page)
            response = self.get_assets(endpoint=endpoint, endpoint_page=current_page)

            resources += response.resources  # Grab resources and append to total
            self.logger.info(
                "Got %d assets from page %d / %d" % (len(response.resources), response.page_num, response.total_pages)
            )

            if (response.total_pages == 0) or ((response.total_pages - 1) == response.page_num):
                self.logger.info("All pages consumed, returning results...")
                break  # exit the loop
            else:
                self.logger.info("More pages exist, fetching...")
                current_page += 1

        return {"assets": resources}

    def get_assets(self, endpoint, endpoint_page, size=500):
        self.logger.info("Fetching up to %d assets from endpoint page %d ..." % (size, endpoint_page))
        try:
            response = self.connection.session.get(
                url=endpoint, verify=False, params={"size": size, "page": endpoint_page}
            )
        except requests.RequestException as e:
            self.logger.error(e)
            raise

        else:
            if response.status_code in [200, 201]:  # 200 is documented, 201 is undocumented
                response_json = response.json()

                Result = namedtuple("Result", "page_num total_pages resources")
                r = Result(
                    page_num=response_json["page"]["number"],
                    total_pages=response_json["page"]["totalPages"],
                    resources=response_json["resources"],
                )

                return r

            else:
                try:
                    reason = response.json()["message"]
                except KeyError:
                    reason = "Unknown error occurred. Please contact support or try again later."
                except json.decoder.JSONDecodeError:
                    raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=reason.text)

                status_code_message = self._ERRORS.get(response.status_code, self._ERRORS[000])
                self.logger.error(
                    "{status} ({code}): {reason}".format(
                        status=status_code_message, code=response.status_code, reason=reason
                    )
                )
                raise PluginException(preset=PluginException.Preset.UNKNOWN)
