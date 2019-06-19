import komand
from .schema import GetKmlInput, GetKmlOutput
# Custom imports below


class GetKml(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_kml',
                description='Get a KML summary approximation for a successfully processed file uploaded by the current user',
                input=GetKmlInput(),
                output=GetKmlOutput())

    def run(self, params={}):
        self.logger.info('GetKml: Downloading summary from server ...')
        transid = params.get('transid')
        response = self.connection.call_api(
            'get', 'file/kml/{}'.format(transid)
        )
        if response.status_code == 204:
            message = 'No KML file available for {}'.format(transid)
            self.logger.error('GetKml: ' + message)
            raise ValueError(message)
        return {'kml': str(response.content)}

    def test(self):
        return {
            'kml': """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
            <kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:xal="urn:oasis:names:tc:ciq:xsdschema:xAL:2.0" xmlns:atom="http://www.w3.org/2005/Atom">
                <Document>
                    <name>MyMarkers</name>
                    <Style id="highConfidence">
                        <IconStyle id="highConfidenceStyle">
                            <scale>1.0</scale>
                            <heading>0.0</heading>
                            <Icon>
                                <href>http://maps.google.com/mapfiles/kml/pushpin/grn-pushpin.png</href>
                                <refreshInterval>0.0</refreshInterval>
                                <viewRefreshTime>0.0</viewRefreshTime>
                                <viewBoundScale>0.0</viewBoundScale>
                            </Icon>
                        </IconStyle>
                    </Style>
                    <Style id="mediumConfidence">
                        <IconStyle id="medConfidenceStyle">
                            <scale>1.0</scale>
                            <heading>0.0</heading>
                            <Icon>
                                <href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
                                <refreshInterval>0.0</refreshInterval>
                                <viewRefreshTime>0.0</viewRefreshTime>
                                <viewBoundScale>0.0</viewBoundScale>
                            </Icon>
                        </IconStyle>
                    </Style>
                    <Style id="lowConfidence">
                        <IconStyle id="lowConfidenceStyle">
                            <scale>1.0</scale>
                            <heading>0.0</heading>
                            <Icon>
                                <href>http://maps.google.com/mapfiles/kml/pushpin/red-pushpin.png</href>
                                <refreshInterval>0.0</refreshInterval>
                                <viewRefreshTime>0.0</viewRefreshTime>
                                <viewBoundScale>0.0</viewBoundScale>
                            </Icon>
                        </IconStyle>
                    </Style>
                    <Style id="zeroConfidence">
                        <IconStyle id="zeroConfidenceStyle">
                            <scale>1.0</scale>
                            <heading>0.0</heading>
                            <Icon>
                                <href>http://maps.google.com/mapfiles/kml/pushpin/wht-pushpin.png</href>
                                <refreshInterval>0.0</refreshInterval>
                                <viewRefreshTime>0.0</viewRefreshTime>
                                <viewBoundScale>0.0</viewBoundScale>
                            </Icon>
                        </IconStyle>
                    </Style>
                    <Placemark>
                        <name>COMPLETELYNEWSSID123456</name>
                        <open>1</open>
                        <description>Network ID: AA:29:CC:BB:BB:BB
            Encryption: WPA2
            Time: 2018-07-16T17:18:00.000-07:00
            Signal: -87.0
            Accuracy: 1071.0
            </description>
                        <styleUrl>#zeroConfidence</styleUrl>
                        <Point>
                            <coordinates>11.5,50.11000061</coordinates>
                        </Point>
                    </Placemark>
                </Document>
            </kml>
            """
        }
