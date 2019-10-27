import komand
from .schema import (
    GetSampleAnalysisInput,
    GetSampleAnalysisOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
from icon_cisco_threatgrid.util.api import ThreatGrid


class GetSampleAnalysis(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_sample_analysis",
            description=Component.DESCRIPTION,
            input=GetSampleAnalysisInput(),
            output=GetSampleAnalysisOutput(),
        )

    def run(self, params={}):
        sample_id = params.get(Input.SAMPLE_ID)

        api: ThreatGrid = self.connection.api

        artifacts = clean_artifact(api.get_artifact_analysis(sample_id=sample_id))
        iocs = clean_data(api.get_ioc_analysis(sample_id=sample_id))
        network_streams = clean_data(
            api.get_network_streams_analysis(sample_id=sample_id)
        )
        processes = clean_data(api.get_processes_analysis(sample_id=sample_id))
        annotations = clean_annotations(
            api.get_annotations_analysis(sample_id=sample_id)
        )
        metadata = clean_data(api.get_metadata_analysis(sample_id=sample_id))

        # self.logger.info(artifacts)

        report = {
            Output.ARTIFACT_REPORT: artifacts,
            Output.IOCS_REPORT: iocs,
            Output.NETWORK_STREAMS_REPORT: network_streams,
            Output.PROCESSES_REPORT: processes,
            Output.ANNOTATIONS_REPORT: annotations,
            Output.METADATA_REPORT: metadata,
        }

        return komand.helper.clean(report)


def clean_data(analysis_data):
    """
    Normilizes items from data for custom types
    :param analysis_data API get analysis request
    :return:
    """
    data = {}

    if analysis_data.get("data"):
        data = analysis_data.get("data")

    if data.get("items"):
        data_items = data.get("items")
        if isinstance(data_items, dict):
            items = [v for k, v in data.get("items").items()]
            if len(items) == 0:
                items = []
            data["items"] = items
            analysis_data["data"] = data
            return analysis_data
    elif type(data.get("items")) == dict:
        # if items are blank set as list for type
        if len(data.get("items")) == 0:
            analysis_data["data"]["items"] = []

    return analysis_data


def clean_artifact(artifact_data):
    items = []
    data = {}

    if artifact_data.get("data"):
        data = artifact_data.get("data")

    if data.get("items"):
        data_items = data.get("items")
        if isinstance(data_items, dict):
            for k, v in data.get("items").items():
                # Fix imports list containing a string and an int
                if v.get("forensics", False):
                    imports = []
                    # Clean imports
                    if v.get("forensics").get("imports", False):
                        imports = clean_imports(v.get("forensics").get("imports"))
                    v["forensics"]["imports"] = imports
                    # Clean sections
                    if v.get("forensics").get("sections", False):
                        if isinstance(v.get("forensics").get("sections"), dict):
                            v["forensics"]["sections"] = [
                                v.get("forensics").get("sections")
                            ]
                    # Clean exports
                    exports = []
                    if v.get("forensics").get("exports", False):
                        exports = clean_exports(v.get("forensics").get("exports"))
                    v["forensics"]["exports"] = exports
                # Attach new value to items
                items.append(v)
            data["items"] = items
            artifact_data["data"] = data
            return artifact_data
    # No item return
    return artifact_data


def clean_annotations(annotation_data):
    data = {}

    if annotation_data.get("data"):
        data = annotation_data.get("data")

    if data.get("items"):
        data_items = data.get("items")
        if isinstance(data_items, dict):
            networks = []
            if data_items.get("network"):
                for k, v in data_items.get("network").items():
                    # format network key
                    v["ip"] = k
                    networks.append(v)
            data["items"]["network"] = networks
            annotation_data["data"] = data
        return annotation_data
    return annotation_data


def clean_imports(imports):
    clean = []
    for item in imports:
        # Check for entries and format to string
        if item.get("entries"):
            entries = []
            for entry in item.get("entries"):
                entries.append([str(i) for i in entry])
            item["entries"] = entries
        # add corrected import to import list
        clean.append(item)
    return clean


def clean_exports(exports):
    clean = []
    for item in exports:
        export = []
        for i in item:
            export.append(str(i))
        clean.append(export)
    return clean
