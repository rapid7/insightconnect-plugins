package types

// Code generated by the Komand Go SDK Generator. DO NOT EDIT

// Files is a custom type generated off of the spec
type Files struct {
	Exes    []string `json:"exes"`
	Flashes []string `json:"flashes"`
	Images  []string `json:"images"`
	Macs    []string `json:"macs"`
	Webs    []string `json:"webs"`
	Zips    []string `json:"zips"`
	Docs    []string `json:"docs"`
}
