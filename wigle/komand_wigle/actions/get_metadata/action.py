import komand
from .schema import GetMetadataInput, GetMetadataOutput
# Custom imports below
from komand_wigle.util.utils import clear_empty_values


class GetMetadata(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_metadata',
                description='Get metadata for cell networks',
                input=GetMetadataInput(),
                output=GetMetadataOutput())

    def run(self, params={}):
        self.logger.info(
            'GetMetadata: Getting cell network metadata from server ...'
        )
        p = clear_empty_values(params)
        api_params = {
            'mcc': p.get('mcc', None),
            'mnc': p.get('mnc', None)
        }
        response = self.connection.call_api(
            'get', 'cell/mccMnc', params=api_params
        )
        cell_network_metadata = []
        for mcc, mncs in response.items():
            cell_mcc = {'mcc': mcc}
            cell_mcc['cell_mncs'] = []
            for mnc, metadata in mncs.items():
                cell_mnc = {'mnc': mnc}
                cell_mnc['metadata'] = metadata
                cell_mcc['cell_mncs'].append(cell_mnc)
            cell_network_metadata.append(cell_mcc)
        return {'cell_network_metadata': cell_network_metadata}

    def test(self):
        return {
          "cell_network_metadata": [
            {
              "mcc": "288",
              "cell_mncs": [
                {
                  "mnc": "01",
                  "metadata": {
                    "type": "National",
                    "countryName": "Faroe Islands (Kingdom of Denmark)",
                    "countryCode": "FO",
                    "mcc": "288",
                    "mnc": "01",
                    "brand": "Faroese Telecom",
                    "operator": "Faroese Telecom",
                    "status": "Operational",
                    "bands": "GSM 900 / UMTS 900 / UMTS 2100 / LTE 800 / LTE 1800"
                  }
                },
                {
                  "mnc": "02",
                  "metadata": {
                    "type": "National",
                    "countryName": "Faroe Islands (Kingdom of Denmark)",
                    "countryCode": "FO",
                    "mcc": "288",
                    "mnc": "02",
                    "brand": "Hey",
                    "operator": "Vodafone Faroe Islands",
                    "status": "Operational",
                    "bands": "GSM 900 / UMTS 2100 / LTE 1800",
                    "notes": "Former Kall, also uses MCC 274 MNC 02 (Iceland)"
                  }
                },
                {
                  "mnc": "03",
                  "metadata": {
                    "type": "National",
                    "countryName": "Faroe Islands (Kingdom of Denmark)",
                    "countryCode": "FO",
                    "mcc": "288",
                    "mnc": "03",
                    "operator": "Edge Mobile Sp/F",
                    "status": "Not operational",
                    "bands": "GSM 1800",
                    "notes": "Planned"
                  }
                }
              ]
            }
          ]
        }
