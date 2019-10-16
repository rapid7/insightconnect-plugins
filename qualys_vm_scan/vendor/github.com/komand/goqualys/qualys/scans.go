package qualys

import (
	"encoding/xml"
	"time"
)

// ScanListOutput ...
type ScanListOutput struct {
	XMLName          xml.Name `xml:"SCAN_LIST_OUTPUT"`
	ScanListResponse ScanListResponse
}

// ScanListResponse ..
type ScanListResponse struct {
	XMLName  xml.Name `xml:"RESPONSE,omitempty"`
	Datetime string   `xml:"DATETIME,omitempty"`
	Scans    []*Scan  `xml:"SCAN_LIST>SCAN,omitempty"`
}

// Scan ...
type Scan struct {
	XMLName    xml.Name      `xml:"SCAN,omitempty"`
	ID         int           `xml:"ID,omitempty"`
	Reference  string        `xml:"REF,omitempty"`
	Type       string        `xml:"TYPE,omitempty"`
	UserLogin  string        `xml:"USER_LOGIN,omitempty"`
	LaunchedAt time.Time     `xml:"LAUNCH_DATETIME,omitempty"`
	Duration   time.Duration `xml:"DURATION,omitempty"`
	Priority   string        `xml:"PROCESSING_PRIORITY,omitempty"`
	Processed  int           `xml:"PROCESSED,omitempty"`
	State      string        `xml:"STATUS>STATE,omitempty"`
	Target     string        `xml:"TARGET,omitempty"`
}
