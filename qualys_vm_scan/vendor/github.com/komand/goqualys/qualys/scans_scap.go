package qualys

import (
	"context"
	"net/http"
	"strconv"
	"time"
)

// SCAPScanService ...
type SCAPScanService service

// SCAPScanListOptions ...
type SCAPScanListOptions struct {
	Action         string    `url:"action,omitempty"`
	Reference      string    `url:"scan_ref,omitempty"`
	State          string    `url:"state,omitempty"`
	Processed      int       `url:"processed,omitempty"`
	Type           string    `url:"type,omitempty"`
	Target         string    `url:"target,omitempty"`
	UserLogin      string    `url:"user_login,omitempty"`
	LaunchedAfter  time.Time `url:"launched_after_datetime,omitempty"`
	LaunchedBefore time.Time `url:"launched_before_datetime,omitempty"`
}

// List ...
func (s *SCAPScanService) List(ctx context.Context, opt SCAPScanListOptions) ([]*Scan, *http.Response, error) {
	opt.Action = "list"
	u, err := addOptions("api/2.0/fo/scan/scap", opt)
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

	scanListOutput := ScanListOutput{}
	var scans []*Scan
	resp, err := s.client.Do(ctx, req, &scanListOutput)
	if err != nil {
		return nil, resp, err
	}

	scans = scanListOutput.ScanListResponse.Scans

	return scans, resp, nil
}

// SCAPScanLaunchOptions ...
type SCAPScanLaunchOptions struct {
	Action      string `url:"action,omitempty"`
	Title       string `url:"scan_title,omitempty"`
	OptionTitle string `url:"option_title,omitempty"`
	Priority    int    `url:"priority,omitempty"`
	IP          string `url:"ip,omitempty"`
}

// Launch ...
func (s *SCAPScanService) Launch(ctx context.Context, opt SCAPScanLaunchOptions) (*Scan, *http.Response, error) {
	opt.Action = "launch"
	u, err := addOptions("api/2.0/fo/scan/scap", opt)
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

	scan := &Scan{}
	for _, item := range sr.Response.ItemList {
		switch item.Key {
		case "ID":
			id, err := strconv.Atoi(item.Value)
			if err != nil {
				return nil, nil, err
			}
			scan.ID = id
		case "REFERENCE":
			scan.Reference = item.Value
		}
	}

	return scan, resp, nil
}

// SCAPScanPauseOptions ...
type SCAPScanPauseOptions struct {
	Reference string `url:"scan_ref,omitempty"`
}

// Pause ...
func (s *SCAPScanService) Pause(ctx context.Context, opt SCAPScanPauseOptions) (*Scan, *http.Response, error) {
	u := "api/2.0/fo/scan/scap?action=pause&scan_ref=" + opt.Reference
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

	scan := &Scan{}
	for _, item := range sr.Response.ItemList {
		switch item.Key {
		case "ID":
			id, err := strconv.Atoi(item.Value)
			if err != nil {
				return nil, nil, err
			}
			scan.ID = id
		case "REFERENCE":
			scan.Reference = item.Value
		}
	}

	return scan, resp, nil
}

// SCAPScanResumeOptions ...
type SCAPScanResumeOptions struct {
	Reference string `url:"scan_ref,omitempty"`
}

// Resume ...
func (s *SCAPScanService) Resume(ctx context.Context, opt SCAPScanResumeOptions) (*Scan, *http.Response, error) {
	u := "api/2.0/fo/scan/scap?action=resume&scan_ref=" + opt.Reference
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

	scan := &Scan{}
	for _, item := range sr.Response.ItemList {
		switch item.Key {
		case "ID":
			id, err := strconv.Atoi(item.Value)
			if err != nil {
				return nil, nil, err
			}
			scan.ID = id
		case "REFERENCE":
			scan.Reference = item.Value
		}
	}

	return scan, resp, nil
}

// SCAPScanCancelOptions ...
type SCAPScanCancelOptions struct {
	Reference string `url:"scan_ref,omitempty"`
}

// Cancel ...
func (s *SCAPScanService) Cancel(ctx context.Context, opt SCAPScanCancelOptions) (*Scan, *http.Response, error) {
	u := "api/2.0/fo/scan/scap?action=cancel&scan_ref=" + opt.Reference
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

	scan := &Scan{}
	for _, item := range sr.Response.ItemList {
		switch item.Key {
		case "ID":
			id, err := strconv.Atoi(item.Value)
			if err != nil {
				return nil, nil, err
			}
			scan.ID = id
		case "REFERENCE":
			scan.Reference = item.Value
		}
	}

	return scan, resp, nil
}

// SCAPScanDeleteOptions ...
type SCAPScanDeleteOptions struct {
	Reference string `url:"scan_ref,omitempty"`
}

// Delete ...
func (s *SCAPScanService) Delete(ctx context.Context, opt SCAPScanDeleteOptions) (*Scan, *http.Response, error) {
	u := "api/2.0/fo/scan/scap?action=delete&scan_ref=" + opt.Reference
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

	scan := &Scan{}
	for _, item := range sr.Response.ItemList {
		switch item.Key {
		case "ID":
			id, err := strconv.Atoi(item.Value)
			if err != nil {
				return nil, nil, err
			}
			scan.ID = id
		case "REFERENCE":
			scan.Reference = item.Value
		}
	}

	return scan, resp, nil
}
