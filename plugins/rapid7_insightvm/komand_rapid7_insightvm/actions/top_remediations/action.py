import insightconnect_plugin_runtime
from .schema import TopRemediationsInput, TopRemediationsOutput, Input, Output, Component

# Custom imports below
import csv
import io
import uuid
from komand_rapid7_insightvm.util import util
from insightconnect_plugin_runtime.exceptions import PluginException


class TopRemediations(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="top_remediations",
            description=Component.DESCRIPTION,
            input=TopRemediationsInput(),
            output=TopRemediationsOutput(),
        )

    def run(self, params={}):
        remediations_limit = params.get(Input.LIMIT)
        # Generate unique identifier for report names
        identifier = uuid.uuid4()

        # Report: Top Remediations
        report_payload = {
            "name": f"Rapid7-InsightConnect-TopRemediation-{identifier}",
            "format": "sql-query",
            "query": TopRemediations.remediations_query(remediations_limit),
            "version": "2.3.0",
        }
        # Add scope if set in action
        if (params.get(Input.SCOPE) != "none") and (len(params.get(Input.SCOPE_IDS)) > 0):
            report_payload["scope"] = {params.get(Input.SCOPE): params.get(Input.SCOPE_IDS)}

        self.logger.info("Generating top remediations for InsightVM and scope")
        report_contents = util.adhoc_sql_report(self.connection, self.logger, report_payload)

        # Structure returned remediations
        remediations = {}
        try:
            csv_report = csv.DictReader(io.StringIO(report_contents["raw"]))
        except Exception as e:
            raise PluginException(
                cause="Error: Failed to process query response for top remediations.",
                assistance=f"Exception returned was {e}",
            )
        for row in csv_report:
            remediation = {
                "solutionId": int(row["solution_id"]),
                "nexposeId": row["nexpose_id"],
                "summary": row["summary"],
                "fix": row["fix"],
                "assetCount": int(row["assets"]),
                "vulnerabilityCount": int(row["vulnerabilities"]),
                "riskScore": int(float(row["riskscore"])),
                "assets": [],
                "vulnerabilities": [],
            }
            remediations[row["solution_id"]] = remediation

        # Report: Gather Asset Details
        asset_report_payload = {
            "name": f"Rapid7-InsightConnect-TopRemediation-Asset-{identifier}",
            "format": "sql-query",
            "query": TopRemediations.assets_query(remediations_limit),
            "version": "2.3.0",
        }
        # Add scope if set in action
        if (params.get(Input.SCOPE) != "none") and (len(params.get(Input.SCOPE_IDS)) > 0):
            asset_report_payload["scope"] = {params.get(Input.SCOPE): params.get(Input.SCOPE_IDS)}

        # Structure and add remediation assets to remediations
        self.logger.info("Processing assets of top remediations")
        asset_report_contents = util.adhoc_sql_report(self.connection, self.logger, asset_report_payload)
        try:
            csv_report = csv.DictReader(io.StringIO(asset_report_contents["raw"]))
        except Exception as e:
            raise PluginException(
                cause="Error: Failed to process query response for remediation assets.",
                assistance=f"Exception returned was {e}",
            )
        for row in csv_report:
            # Only track assets up to the asset limit
            asset_limit = params.get(Input.ASSET_LIMIT)
            if (asset_limit == 0) or (len(remediations[row["solution_id"]]["assets"]) < asset_limit):
                asset = {
                    "id": int(row["asset_id"]),
                    "hostName": row["host_name"],
                    "ip": row["ip_address"],
                    "mac": row["mac_address"],
                    "os": row["name"],
                    "riskScore": int(float(row["riskscore"])),
                    "criticalityTag": TopRemediations.highest_criticality(row["criticality_tag"].split(",")),
                }
                remediations[row["solution_id"]]["assets"].append(asset)

        # Report: Gather Vulnerabilitiy Details
        vulnerability_report_payload = {
            "name": f"Rapid7-InsightConnect-TopRemediation-Vulnerability-{identifier}",
            "format": "sql-query",
            "query": TopRemediations.vulnerabilities_query(remediations_limit),
            "version": "2.3.0",
        }
        # Add scope if set in action
        if (params.get(Input.SCOPE) != "none") and (len(params.get(Input.SCOPE_IDS)) > 0):
            vulnerability_report_payload["scope"] = {params.get(Input.SCOPE): params.get(Input.SCOPE_IDS)}

        # Structure and add remediation vulnerabilities to remediations
        self.logger.info("Processing vulnerabilities of top remediations")
        vulnerability_report_contents = util.adhoc_sql_report(
            self.connection, self.logger, vulnerability_report_payload
        )
        try:
            csv_report = csv.DictReader(io.StringIO(vulnerability_report_contents["raw"]))
        except Exception as e:
            raise PluginException(
                cause="Error: Failed to process query response for remediation vulnerabilities.",
                assistance=f"Exception returned was {e}",
            )
        for row in csv_report:
            # Only track vulnerabilities up to the vulnerability limit
            vuln_limit = params.get(Input.VULNERABILITY_LIMIT)
            if (vuln_limit == 0) or (len(remediations[row["solution_id"]]["vulnerabilities"]) < vuln_limit):
                vulnerability = {
                    "id": int(row["vulnerability_id"]),
                    "title": row["title"],
                    "description": row["description"],
                    "cvssScore": row["cvss_score"],
                    "severity": int(row["severity_score"]),
                    "riskScore": int(float(row["riskscore"])),
                }
                remediations[row["solution_id"]]["vulnerabilities"].append(vulnerability)

        self.logger.info(f"Top remediations processed, generated {len(remediations)} remediations")

        return {Output.REMEDIATIONS: list(remediations.values())}

    @staticmethod
    def remediations_query(limit):
        return (
            f"SELECT fr.solution_id, fr.assets, fr.vulnerabilities, fr.riskscore, ds.nexpose_id, "  # noqa: B608
            f'ds.summary AS "summary", htmlToText(ds.fix) AS "fix", '
            f"array_to_string(array_agg(DISTINCT da.ip_address), ', ') AS \"ip_addresses\", "
            f"array_to_string(array_agg(DISTINCT da.host_name),', ') AS \"host_names\" "
            f"FROM fact_remediation({limit}, 'riskscore DESC') AS fr "
            f"JOIN dim_solution AS ds ON fr.solution_id = ds.solution_id "
            f"JOIN dim_asset_vulnerability_solution davs ON fr.solution_id = davs.solution_id "
            f"JOIN dim_asset AS da ON davs.asset_id = da.asset_id "
            f"GROUP BY fr.solution_id, fr.assets, fr.vulnerabilities, fr.riskscore, "
            f"ds.nexpose_id, ds.summary, ds.fix"
        )

    @staticmethod
    def assets_query(limit):
        return (
            f"WITH criticality_tags AS ( "  # noqa: B608
            f"SELECT asset_id, array_to_string(array_agg(distinct tag_name),',') AS criticality_tag "
            f"FROM dim_tag "
            f"JOIN dim_tag_asset USING (tag_id) "
            f"WHERE tag_type = 'CRITICALITY' "
            f"GROUP BY asset_id "
            f"), "
            f"remediation_assets AS ( "
            f"SELECT DISTINCT solution_id, asset_id "
            f"FROM dim_asset_vulnerability_solution "
            f") "
            f"SELECT DISTINCT fr.solution_id, da.asset_id, da.mac_address, da.ip_address, da.host_name, dos.name, "
            f"fa.riskscore, ct.criticality_tag "
            f"FROM fact_remediation({limit}, 'riskscore DESC') AS fr "
            f"JOIN remediation_assets ra ON fr.solution_id = ra.solution_id "
            f"JOIN dim_asset AS da ON ra.asset_id = da.asset_id "
            f"JOIN fact_asset AS fa ON ra.asset_id = fa.asset_id "
            f"LEFT JOIN criticality_tags AS ct ON ra.asset_id = ct.asset_id "
            f"JOIN dim_operating_system AS dos ON da.operating_system_id = dos.operating_system_id"
        )

    @staticmethod
    def vulnerabilities_query(limit):
        return (
            f"WITH remediation_vulnerabilities AS ( "  # noqa: B608
            f"SELECT DISTINCT solution_id, vulnerability_id "
            f"FROM dim_asset_vulnerability_solution "
            f")"
            f"SELECT DISTINCT fr.solution_id, dv.vulnerability_id, dv.title, dv.description, "
            f"dv.severity_score, dv.riskscore, dv.cvss_score "
            f"FROM fact_remediation({limit}, 'riskscore DESC') AS fr "
            f"JOIN remediation_vulnerabilities rv ON fr.solution_id = rv.solution_id "
            f"JOIN dim_vulnerability AS dv ON rv.vulnerability_id = dv.vulnerability_id"
        )

    @staticmethod
    def highest_criticality(criticalities):
        criticality_tag = ""
        criticalities = list(filter(None, criticalities))

        tag_weight = {
            "Very High": 5,
            "High": 4,
            "Medium": 3,
            "Low": 2,
            "Very Low": 1,
            "": 0,
        }

        # Out of list of tags for device from reporting data model, pick the tag of the highest criticality
        for tag in criticalities:
            if tag_weight[tag] > tag_weight[criticality_tag]:
                criticality_tag = tag

        return criticality_tag
