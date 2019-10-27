package qualys

import "encoding/xml"

const (
	// Version of the Client
	Version = "v0.0.2"
	// UserAgent of the Client
	UserAgent = "goqualys/" + Version
)

// Platform specific API Base URLs
const (
	USPlatform1    = "https://qualysapi.qualys.com/"
	USPlatform2    = "https://qualysapi.qg2.apps.qualys.com/"
	USPlatform3    = "https://qualysapi.qg3.apps.qualys.com/"
	EUPlatform1    = "https://qualysapi.qualys.eu/"
	EUPatform2     = "https://qualysapi.qg2.apps.qualys.eu/"
	IndiaPlatform1 = "https://qualysapi.qg1.apps.qualys.in/"
)

// SimpleReturn ...
type SimpleReturn struct {
	XMLName  xml.Name `xml:"SIMPLE_RETURN"`
	Response Response
}

// Response ...
type Response struct {
	XMLName  xml.Name `xml:"RESPONSE,omitempty"`
	Datetime string   `xml:"DATETIME,omitempty"`
	Text     string   `xml:"TEXT,omitempty"`
	ItemList []*Item  `xml:"ITEM_LIST>ITEM,omitempty"`
}

// Item ...
type Item struct {
	XMLName xml.Name `xml:"ITEM,omitempty"`
	Key     string   `xml:"KEY,omitempty"`
	Value   string   `xml:"VALUE,omitempty"`
}
