package qualys

import (
	"context"
	"encoding/xml"
	"net/http"
	"time"
)

// KnowledgeBaseService ...
type KnowledgeBaseService service

// KnowledgeBaseVulnerability holds a subset of the total available fields
// If more fields are needed add them to this
type KnowledgeBaseVulnerability struct {
	XMLName       xml.Name `xml:"VULN,omitempty"`
	QID           string   `xml:"QID,omitempty"`
	Type          string   `xml:"VULN_TYPE,omitempty"`
	Severity      string   `xml:"SEVERITY_LEVEL,omitempty"`
	Title         string   `xml:"TITLE,omitempty"`
	Category      string   `xml:"CATEGORY,omitempty"`
	DetectionInfo string   `xml:"DETECTION_INFO,omitempty"`
}

// KnowledgeBaseListResponse ...
type KnowledgeBaseListResponse struct {
	XMLName           xml.Name                      `xml:"RESPONSE,omitempty"`
	Datetime          time.Time                     `xml:"DATETIME,omitempty"`
	VulnerabilityList []*KnowledgeBaseVulnerability `xml:"VULN_LIST>VULN,omitempty"`
}

// KnowledgeBaseListOutput ...
type KnowledgeBaseListOutput struct {
	XMLName                   xml.Name `xml:"KNOWLEDGE_BASE_VULN_LIST_OUTPUT,omitempty"`
	KnowledgeBaseListResponse KnowledgeBaseListResponse
}

// KnowledgeBaseListOptions ...
type KnowledgeBaseListOptions struct {
	Action                      string    `url:"action,omitempty"`
	IDs                         string    `url:"ids,omitempty"`
	MinID                       string    `url:"id_min,omitempty"`
	MaxID                       string    `url:"id_max,omitempty"`
	IsPatchable                 bool      `url:"is_patchable,omitempty"`
	LastModifiedAfter           time.Time `url:"last_modified_after,omitempty"`
	LastModifiedBefore          time.Time `url:"last_modified_before,omitempty"`
	LastModifiedByUserAfter     time.Time `url:"last_modified_by_user_after,omitempty"`
	LastModifiedByUserBefore    time.Time `url:"last_modified_by_user_before,omitempty"`
	LastModifiedByServiceAfter  time.Time `url:"last_modified_by_service_after,omitempty"`
	LastModifiedByServiceBefore time.Time `url:"last_modified_by_user_before,omitempty"`
	PublishedAfter              time.Time `url:"published_after,omitempty"`
	PublishedBefore             time.Time `url:"published_before,omitempty"`
	DiscoveryMethod             string    `url:"discovery_method,omitempty"`
	DiscoveryAuthTypes          string    `url:"discovery_auth_types,omitempty"`
	ShowPCIReasons              int       `url:"show_pci_reasons,omitempty"`
}

// List ...
func (s *KnowledgeBaseService) List(ctx context.Context, opt KnowledgeBaseListOptions) ([]*KnowledgeBaseVulnerability, *http.Response, error) {
	opt.Action = "list"
	u, err := addOptions("api/2.0/fo/knowledge_base/vuln/", opt)
	if err != nil {
		return nil, nil, err
	}

	ro := RequestOptions{
		Method: "POST",
		URL:    u,
		Accept: "application/xml",
	}

	req, err := s.client.NewRequest(ro)
	if err != nil {
		return nil, nil, err
	}

	kblo := KnowledgeBaseListOutput{}
	var vulns []*KnowledgeBaseVulnerability
	resp, err := s.client.Do(ctx, req, &kblo)
	if err != nil {
		return nil, resp, err
	}

	vulns = kblo.KnowledgeBaseListResponse.VulnerabilityList

	return vulns, resp, nil
}
