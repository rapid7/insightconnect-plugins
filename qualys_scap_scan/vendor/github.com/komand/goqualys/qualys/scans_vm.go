package qualys

import (
	"context"
	"net/http"
	"strconv"
	"time"
)

// VMScanService ...
type VMScanService service

// VMScanListOptions ...
type VMScanListOptions struct {
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
func (s *VMScanService) List(ctx context.Context, opt VMScanListOptions) ([]*Scan, *http.Response, error) {
	opt.Action = "list"
	u, err := addOptions("api/2.0/fo/scan/", opt)
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

// VMScanLaunchOptions ...
type VMScanLaunchOptions struct {
	Action      string `url:"action,omitempty"`
	Title       string `url:"scan_title,omitempty"`
	OptionTitle string `url:"option_title,omitempty"`
	Priority    int    `url:"priority,omitempty"`
	IP          string `url:"ip,omitempty"`
}

// Launch ...
func (s *VMScanService) Launch(ctx context.Context, opt VMScanLaunchOptions) (*Scan, *http.Response, error) {
	opt.Action = "launch"
	u, err := addOptions("api/2.0/fo/scan/", opt)
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

// VMScanPauseOptions ...
type VMScanPauseOptions struct {
	Reference string `url:"scan_ref,omitempty"`
}

// Pause ...
func (s *VMScanService) Pause(ctx context.Context, opt VMScanPauseOptions) (*Scan, *http.Response, error) {
	u := "api/2.0/fo/scan/?action=pause&scan_ref=" + opt.Reference
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

// VMScanResumeOptions ...
type VMScanResumeOptions struct {
	Reference string `url:"scan_ref,omitempty"`
}

// Resume ...
func (s *VMScanService) Resume(ctx context.Context, opt VMScanResumeOptions) (*Scan, *http.Response, error) {
	u := "api/2.0/fo/scan/?action=resume&scan_ref=" + opt.Reference
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

// VMScanCancelOptions ...
type VMScanCancelOptions struct {
	Reference string `url:"scan_ref,omitempty"`
}

// Cancel ...
func (s *VMScanService) Cancel(ctx context.Context, opt VMScanCancelOptions) (*Scan, *http.Response, error) {
	u := "api/2.0/fo/scan/?action=cancel&scan_ref=" + opt.Reference
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

// VMScanDeleteOptions ...
type VMScanDeleteOptions struct {
	Reference string `url:"scan_ref,omitempty"`
}

// Delete ...
func (s *VMScanService) Delete(ctx context.Context, opt VMScanDeleteOptions) (*Scan, *http.Response, error) {
	u := "api/2.0/fo/scan/?action=delete&scan_ref=" + opt.Reference
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
