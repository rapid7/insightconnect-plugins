package actions

import (
	"time"

	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/cacador/connection"
	"github.com/rapid7/komand-plugins/cacador/types"
	"github.com/sroberts/cacador/aux"
)

// Validate will validate the input is properly setup with whatever rules you put in
// You can also use this to pre-set any values before they are run by the Run method.
// Note that for Actions, the  Input message is inspected every time time, just before it
// is handed to the Run method. Keep this in mind when setting any properties on the Input i
// You can return a set of errors for any reason to fail the step.
// Otherwise, return nil for success
func (i *ExtractInput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)

	// Custom validation code here
	// Append errors as needed

	// return
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Validate will validate the output is properly setup with whatever rules you put in
// You can leave this blank if you want to, but if you need to enforce restrictions
// here is where you can return a number of errors. Otherwise, return nil for success
func (o *ExtractOutput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)

	// Custom validation code here
	// Append errors as needed

	// return
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Run will run the action with the given input over the given connection
func (a *ExtractAction) Run(conn *connection.Connection, input *ExtractInput, log plog.Logger) (*ExtractOutput, error) {
	output := &ExtractOutput{}
	// Your code here

	// Use the `log` object passed into the Connect method and any logging information
	// will be returned with the message in the log field. Otherwise, it will be discarded.

	// return output and no error for success
	// return nil and error for failure

	output.Hashes = GetHashStrings(input.Text)
	output.Networks = GetNetworkstrings(input.Text)
	output.Files = GetFilenameStrings(input.Text)
	output.Utilities = GetUtilityStrings(input.Text)
	output.Time = time.Now().String()

	return output, nil
}

// Test will test the action with the given input over the given connection.
// For this, you should design the output result to be used with the tests in the test/ directory.
// You do not need to / should not need to invoke the actual API, this is just for testing.
func (a *ExtractAction) Test(conn *connection.Connection, input *ExtractInput, log plog.Logger) (*ExtractOutput, error) {
	output := &ExtractOutput{}
	// Your code here
	// NOTE: The input you receive in the test method cannot be gauranteed to contain "good" value.
	// You should not assume the input is something you can trust in this context.

	// Use the `log` object passed into the Connect method and any logging information
	// will be returned with the message in the log field. Otherwise, it will be discarded.

	// return output and no error for success
	// return nil and error for failure
	data := "http://www.foo.com and word.exe but nothing else 192.5.5.5"
	output.Hashes = GetHashStrings(data)
	output.Networks = GetNetworkstrings(data)
	output.Files = GetFilenameStrings(data)
	output.Utilities = GetUtilityStrings(data)
	output.Time = time.Now().String()
	return output, nil
}

// GetHashStrings takes a string and returns a struct of hashes
func GetHashStrings(data string) types.Hashes {
	empty := make([]string, 0)
	h := types.Hashes{}

	h.Md5s = aux.Dedup(aux.HashRegexs["md5"].FindAllString(data, -1))
	h.Sha1s = aux.Dedup(aux.HashRegexs["sha1"].FindAllString(data, -1))
	h.Sha256s = aux.Dedup(aux.HashRegexs["sha256"].FindAllString(data, -1))
	h.Sha512s = aux.Dedup(aux.HashRegexs["sha512"].FindAllString(data, -1))
	h.Ssdeeps = aux.Dedup(aux.HashRegexs["ssdeep"].FindAllString(data, -1))

	if h.Md5s == nil {
		h.Md5s = empty
	}

	if h.Sha1s == nil {
		h.Sha1s = empty
	}

	if h.Sha256s == nil {
		h.Sha256s = empty
	}

	if h.Sha512s == nil {
		h.Sha512s = empty
	}

	if h.Ssdeeps == nil {
		h.Ssdeeps = empty
	}

	return h
}

// GetNetworkstrings takes a string and returns network based IOCs
func GetNetworkstrings(data string) types.Networks {
	empty := make([]string, 0)

	n := types.Networks{}

	n.Domains = aux.Dedup(aux.CleanDomains(aux.NetworkRegexs["domain"].FindAllString(data, -1)))
	n.Emails = aux.Dedup(aux.NetworkRegexs["email"].FindAllString(data, -1))
	n.Ipv4s = aux.Dedup(aux.CleanIpv4(aux.NetworkRegexs["ipv4"].FindAllString(data, -1)))
	n.Ipv6s = aux.Dedup(aux.NetworkRegexs["ipv6"].FindAllString(data, -1))
	n.Urls = aux.Dedup(aux.CleanUrls(aux.NetworkRegexs["url"].FindAllString(data, -1)))

	if n.Domains == nil {
		n.Domains = empty
	}

	if n.Emails == nil {
		n.Emails = empty
	}

	if n.Ipv4s == nil {
		n.Ipv4s = empty
	}

	if n.Ipv6s == nil {
		n.Ipv6s = empty
	}

	if n.Urls == nil {
		n.Urls = empty
	}

	return n
}

// GetFilenameStrings takes a string and returns a struct of file IOCs
func GetFilenameStrings(data string) types.Files {

	f := types.Files{}
	empty := make([]string, 0)

	f.Docs = aux.Dedup(aux.FileRegexs["doc"].FindAllString(data, -1))
	f.Exes = aux.Dedup(aux.FileRegexs["exe"].FindAllString(data, -1))
	f.Flashes = aux.Dedup(aux.FileRegexs["flash"].FindAllString(data, -1))
	f.Images = aux.Dedup(aux.FileRegexs["img"].FindAllString(data, -1))
	f.Macs = aux.Dedup(aux.FileRegexs["mac"].FindAllString(data, -1))
	f.Webs = aux.Dedup(aux.FileRegexs["web"].FindAllString(data, -1))
	f.Zips = aux.Dedup(aux.FileRegexs["zip"].FindAllString(data, -1))

	if f.Docs == nil {
		f.Docs = empty
	}

	if f.Exes == nil {
		f.Exes = empty
	}

	if f.Flashes == nil {
		f.Flashes = empty
	}
	if f.Images == nil {
		f.Images = empty
	}
	if f.Macs == nil {
		f.Macs = empty
	}
	if f.Webs == nil {
		f.Webs = empty
	}
	if f.Zips == nil {
		f.Zips = empty
	}

	return f
}

// GetUtilityStrings takes a string and returns utility strings
func GetUtilityStrings(data string) types.Utilities {
	u := types.Utilities{}
	empty := make([]string, 0)

	u.Cves = aux.Dedup(aux.UtilityRegexs["cve"].FindAllString(data, -1))
	if u.Cves == nil {
		u.Cves = empty
	}
	return u
}
