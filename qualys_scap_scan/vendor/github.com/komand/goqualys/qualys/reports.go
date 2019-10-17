package qualys

import (
	"bytes"
	"context"
	"encoding/xml"
	"fmt"
	"net/http"
	"strconv"
	"time"
)

// ReportStatus ...
type ReportStatus struct {
	XMLName xml.Name `xml:"STATUS,omitempty"`
	State   string   `xml:"STATE,omitempty"`
}

// Report ...
type Report struct {
	XMLName            xml.Name  `xml:"REPORT,omitempty"`
	ID                 int       `xml:"ID,omitempty"`
	Title              string    `xml:"TITLE,omitempty"`
	Type               string    `xml:"type,omitempty"`
	UserLogin          string    `xml:"USER_LOGIN,omitempty"`
	LaunchDatetime     time.Time `xml:"LAUNCH_DATETIME,omitempty"`
	OutputFormat       string    `xml:"OUTPUT_FORMAT,omitempty"`
	Size               string    `xml:"SIZE,omitempty"`
	Status             ReportStatus
	ExpirationDatetime time.Time `xml:"EXPIRATION_DATETIME,omitempty"`
}

// ReportService ...
type ReportService service

// ReportListResponse ...
type ReportListResponse struct {
	XMLName  xml.Name  `xml:"RESPONSE,omitempty"`
	Datetime time.Time `xml:"DATETIME,omtempty"`
	Reports  []*Report `xml:"REPORT_LIST>REPORT,omitempty"`
}

// ReportListOutput ..
type ReportListOutput struct {
	XMLName            xml.Name `xml:"REPORT_LIST_OUTPUT,omitempty"`
	ReportListResponse ReportListResponse
}

// ReportListOptions ...
type ReportListOptions struct {
	Action        string    `url:"action,omitempty"`
	ID            int       `url:"id,omitempty"`
	State         string    `url:"state,omitempty"`
	UserLogin     string    `url:"user_login,omitempty"`
	ExpiresBefore time.Time `url:"expires_before_datetime,omitempty"`
}

// List ...
func (s *ReportService) List(ctx context.Context, opt ReportListOptions) ([]*Report, *http.Response, error) {
	opt.Action = "list"
	u, err := addOptions("api/2.0/fo/report/", opt)
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

	rlo := ReportListOutput{}
	var reports []*Report
	resp, err := s.client.Do(ctx, req, &rlo)
	if err != nil {
		return nil, resp, err
	}

	reports = rlo.ReportListResponse.Reports

	return reports, resp, nil
}

// ReportLaunchOptions ...
type ReportLaunchOptions struct {
	Action       string `url:"action,omitempty"`
	Type         string `url:"report_type,omitempty"`
	TemplateID   string `url:"template_id"`
	Title        string `url:"report_title,omitempty"`
	OutputFormat string `url:"output_format"`
}

// MapReportLaunchOptions ...
type MapReportLaunchOptions struct {
	ReportLaunchOptions
	Domain        string `url:"domain,omitempty"`
	IPRestriction string `url:"ip_restriction,omitempty"`
	ReportRefs    string `url:"report_refs"`
}

// LaunchMapReport ...
func (s *ReportService) LaunchMapReport(ctx context.Context, opt MapReportLaunchOptions) (*Report, *http.Response, error) {
	opt.Action = "launch"
	opt.Type = "Map"
	u, err := addOptions("api/2.0/fo/report/", opt)
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

	var sr SimpleReturn
	resp, err := s.client.Do(ctx, req, &sr)
	if err != nil {
		return nil, resp, err
	}

	report := &Report{}
	for _, item := range sr.Response.ItemList {
		switch item.Key {
		case "ID":
			id, err := strconv.Atoi(item.Value)
			if err != nil {
				return nil, nil, err
			}
			report.ID = id
		}
	}

	return report, resp, nil
}

// ScanReportLaunchOptions ...
// TODO: split this into Scan Based Findings and Host Based Findings
type ScanReportLaunchOptions struct {
	ReportLaunchOptions
	IPRestriction string `url:"ip_restriction,omitempty"`
	ReportRefs    string `url:"report_refs"`
}

// LaunchScanReport ...
func (s *ReportService) LaunchScanReport(ctx context.Context, opt ScanReportLaunchOptions) (*Report, *http.Response, error) {
	opt.Action = "launch"
	opt.Type = "Scan"
	u, err := addOptions("api/2.0/fo/report/", opt)
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

	var sr SimpleReturn
	resp, err := s.client.Do(ctx, req, &sr)
	if err != nil {
		return nil, resp, err
	}

	report := &Report{}
	for _, item := range sr.Response.ItemList {
		switch item.Key {
		case "ID":
			id, err := strconv.Atoi(item.Value)
			if err != nil {
				return nil, nil, err
			}
			report.ID = id
		}
	}

	return report, resp, nil
}

// PatchReportLaunchOptions ...
type PatchReportLaunchOptions struct {
	ReportLaunchOptions
	IPs           string `url:"ips,omitempty"`
	AssetGroupIDs string `url:"asset_group_ids,omitempty"`
}

// LaunchPatchReport ...
func (s *ReportService) LaunchPatchReport(ctx context.Context, opt PatchReportLaunchOptions) (*Report, *http.Response, error) {
	opt.Action = "launch"
	opt.Type = "Patch"
	u, err := addOptions("api/2.0/fo/report/", opt)
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

	var sr SimpleReturn
	resp, err := s.client.Do(ctx, req, &sr)
	if err != nil {
		return nil, resp, err
	}

	report := &Report{}
	for _, item := range sr.Response.ItemList {
		switch item.Key {
		case "ID":
			id, err := strconv.Atoi(item.Value)
			if err != nil {
				return nil, nil, err
			}
			report.ID = id
		}
	}

	return report, resp, nil
}

// RemediationReportLaunchOptions ...
type RemediationReportLaunchOptions struct {
	ReportLaunchOptions
	IPs           string `url:"ips,omitempty"`
	AssetGroupIDs string `url:"asset_group_ids,omitempty"`
	AssigneeType  string `url:"assignee_type,omitempty"`
}

// LaunchRemediationReport ...
func (s *ReportService) LaunchRemediationReport(ctx context.Context, opt RemediationReportLaunchOptions) (*Report, *http.Response, error) {
	opt.Action = "launch"
	opt.Type = "Remediation"
	u, err := addOptions("api/2.0/fo/report/", opt)
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

	var sr SimpleReturn
	resp, err := s.client.Do(ctx, req, &sr)
	if err != nil {
		return nil, resp, err
	}

	report := &Report{}
	for _, item := range sr.Response.ItemList {
		switch item.Key {
		case "ID":
			id, err := strconv.Atoi(item.Value)
			if err != nil {
				return nil, nil, err
			}
			report.ID = id
		}
	}

	return report, resp, nil
}

// ComplianceReportLaunchOptions ...
type ComplianceReportLaunchOptions struct {
	ReportLaunchOptions
	IPs           string `url:"ips,omitempty"`
	AssetGroupIDs string `url:"asset_group_ids,omitempty"`
	ReportRefs    string `url:"report_refs"`
}

// LaunchComplianceReport ...
func (s *ReportService) LaunchComplianceReport(ctx context.Context, opt ComplianceReportLaunchOptions) (*Report, *http.Response, error) {
	opt.Action = "launch"
	opt.Type = "Compliance"
	u, err := addOptions("api/2.0/fo/report/", opt)
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

	var sr SimpleReturn
	resp, err := s.client.Do(ctx, req, &sr)
	if err != nil {
		return nil, resp, err
	}

	report := &Report{}
	for _, item := range sr.Response.ItemList {
		switch item.Key {
		case "ID":
			id, err := strconv.Atoi(item.Value)
			if err != nil {
				return nil, nil, err
			}
			report.ID = id
		}
	}

	return report, resp, nil
}

// CompliancePolicyReportLaunchOptions ...
type CompliancePolicyReportLaunchOptions struct {
	ReportLaunchOptions
	PolicyID      int    `url:"policy_id,omitempty"`
	AssetGroupIDs string `url:"asset_group_ids,omitempty"`
	IPs           string `url:"ips,omitempty"`
	HostID        int    `url:"host_id,omitempty"`
	Instance      string `url:"instance_string,omitempty"`
	ReportRefs    string `url:"report_refs"`
}

// LaunchCompliancePolicyReport ...
func (s *ReportService) LaunchCompliancePolicyReport(ctx context.Context, opt CompliancePolicyReportLaunchOptions) (*Report, *http.Response, error) {
	opt.Action = "launch"
	opt.Type = "Policy"
	u, err := addOptions("api/2.0/fo/report/", opt)
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

	var sr SimpleReturn
	resp, err := s.client.Do(ctx, req, &sr)
	if err != nil {
		return nil, resp, err
	}

	report := &Report{}
	for _, item := range sr.Response.ItemList {
		switch item.Key {
		case "ID":
			id, err := strconv.Atoi(item.Value)
			if err != nil {
				return nil, nil, err
			}
			report.ID = id
		}
	}

	return report, resp, nil
}

// ReportCancelOptions ...
type ReportCancelOptions struct {
	ID int `url:"id,omitempty"`
}

// Cancel ...
func (s *ReportService) Cancel(ctx context.Context, opt ReportCancelOptions) (*Report, *http.Response, error) {
	u := fmt.Sprintf("api/2.0/fo/report/?action=cancel&id=%d", opt.ID)
	ro := RequestOptions{
		Method: "POST",
		URL:    u,
		Accept: "application/xml",
	}

	req, err := s.client.NewRequest(ro)
	if err != nil {
		return nil, nil, err
	}

	var sr SimpleReturn
	resp, err := s.client.Do(ctx, req, &sr)
	if err != nil {
		return nil, resp, err
	}

	scan := &Report{}
	for _, item := range sr.Response.ItemList {
		switch item.Key {
		case "ID":
			id, err := strconv.Atoi(item.Value)
			if err != nil {
				return nil, nil, err
			}
			scan.ID = id
		}
	}

	return scan, resp, nil
}

// ReportDeleteOptions ...
type ReportDeleteOptions struct {
	ID int `url:"id,omitempty"`
}

// Delete ...
func (s *ReportService) Delete(ctx context.Context, opt ReportDeleteOptions) (*Report, *http.Response, error) {
	u := fmt.Sprintf("api/2.0/fo/report/?action=delete&id=%d", opt.ID)
	ro := RequestOptions{
		Method: "POST",
		URL:    u,
		Accept: "application/xml",
	}

	req, err := s.client.NewRequest(ro)
	if err != nil {
		return nil, nil, err
	}

	var sr SimpleReturn
	resp, err := s.client.Do(ctx, req, &sr)
	if err != nil {
		return nil, resp, err
	}

	report := &Report{}
	for _, item := range sr.Response.ItemList {
		switch item.Key {
		case "ID":
			id, err := strconv.Atoi(item.Value)
			if err != nil {
				return nil, nil, err
			}
			report.ID = id
		}
	}

	return report, resp, nil
}

// ReportFetchOptions ...
type ReportFetchOptions struct {
	Action string `url:"action,omitempty"`
	ID     int    `url:"id,omitempty"`
}

// Fetch ...
func (s *ReportService) Fetch(ctx context.Context, opt ReportFetchOptions) (*bytes.Buffer, *http.Response, error) {
	u := fmt.Sprintf("api/2.0/fo/report/?action=fetch&id=%d", opt.ID)

	ro := RequestOptions{
		Method: "POST",
		URL:    u,
		Accept: "application/xml",
	}

	req, err := s.client.NewRequest(ro)
	if err != nil {
		return nil, nil, err
	}

	var b bytes.Buffer
	resp, err := s.client.Do(ctx, req, &b)
	if err != nil {
		return nil, resp, err
	}

	return &b, resp, nil
}
