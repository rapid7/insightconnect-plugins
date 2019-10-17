package qualys

import (
	"context"
	"net/http"
	"strconv"
	"time"
)

// PCScanService ...
type PCScanService service

// PCScanListOptions ...
type PCScanListOptions struct {
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
func (s *PCScanService) List(ctx context.Context, opt PCScanListOptions) ([]*Scan, *http.Response, error) {
	opt.Action = "list"
	u, err := addOptions("api/2.0/fo/scan/compliance", opt)
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

// PCScanLaunchOptions ...
type PCScanLaunchOptions struct {
	Action      string `url:"action,omitempty"`
	Title       string `url:"scan_title,omitempty"`
	OptionTitle string `url:"option_title,omitempty"`
	Priority    int    `url:"priority,omitempty"`
	IP          string `url:"ip,omitempty"`
}

// Launch ...
func (s *PCScanService) Launch(ctx context.Context, opt PCScanLaunchOptions) (*Scan, *http.Response, error) {
	opt.Action = "launch"
	u, err := addOptions("api/2.0/fo/scan/compliance", opt)
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

// PCScanPauseOptions ...
type PCScanPauseOptions struct {
	Reference string `url:"scan_ref,omitempty"`
}

// Pause ...
func (s *PCScanService) Pause(ctx context.Context, opt PCScanPauseOptions) (*Scan, *http.Response, error) {
	u := "api/2.0/fo/scan/compliance?action=pause&scan_ref=" + opt.Reference
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

// PCScanResumeOptions ...
type PCScanResumeOptions struct {
	Reference string `url:"scan_ref,omitempty"`
}

// Resume ...
func (s *PCScanService) Resume(ctx context.Context, opt PCScanResumeOptions) (*Scan, *http.Response, error) {
	u := "api/2.0/fo/scan/compliance?action=resume&scan_ref=" + opt.Reference
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

// PCScanCancelOptions ...
type PCScanCancelOptions struct {
	Reference string `url:"scan_ref,omitempty"`
}

// Cancel ...
func (s *PCScanService) Cancel(ctx context.Context, opt PCScanCancelOptions) (*Scan, *http.Response, error) {
	u := "api/2.0/fo/scan/compliance?action=cancel&scan_ref=" + opt.Reference
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

// PCScanDeleteOptions ...
type PCScanDeleteOptions struct {
	Reference string `url:"scan_ref,omitempty"`
}

// Delete ...
func (s *PCScanService) Delete(ctx context.Context, opt PCScanDeleteOptions) (*Scan, *http.Response, error) {
	u := "api/2.0/fo/scan/compliance?action=delete&scan_ref=" + opt.Reference
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
