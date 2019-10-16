package actions

import (
	"net"
	"regexp"
	"strings"

	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/extractit/connection"
)

// Validate will validate the input is properly setup with whatever rules you put in
// You can also use this to pre-set any values before they are run by the Run method.
// Note that for Actions, the  Input message is inspected every time time, just before it
// is handed to the Run method. Keep this in mind when setting any properties on the Input i
// You can return a set of errors for any reason to fail the step.
// Otherwise, return nil for success
func (i *IPExtractorInput) Validate(log plog.Logger) []error {
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
func (o *IPExtractorOutput) Validate(log plog.Logger) []error {
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
func (a *IPExtractorAction) Run(conn *connection.Connection, input *IPExtractorInput, log plog.Logger) (*IPExtractorOutput, error) {
	output := &IPExtractorOutput{}
	badData := regexp.MustCompile(`(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{1,4})(\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{1,2})){4,7}`)
	ip4 := regexp.MustCompile(`(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{1,2})(\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{1,2})){3}`)
	ip6 := regexp.MustCompile("(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))")

	if input.File != nil {
		prune := badData.FindAllString(input.Str, -1)
		for _, element := range prune {
			input.Str = strings.Replace(input.Str, element, "", -1)
		}
		ips := ip4.FindAllString(string(input.File), -1)
		// Check for valid IPv4 and adds to output
		output.IPAddrs = ipChecker(output.IPAddrs, ips)

		s := ip6.FindAllString(string(input.File), -1)
		output.IPAddrs = append(s, output.IPAddrs...)
	}
	if input.Str != "" {
		// Clean data
		prune := badData.FindAllString(input.Str, -1)
		for _, element := range prune {
			input.Str = strings.Replace(input.Str, element, "", -1)
		}
		st := ip6.FindAllString(input.Str, -1)
		s := ip4.FindAllString(input.Str, -1)
		output.IPAddrs = ipChecker(output.IPAddrs, s)
		output.IPAddrs = append(st, output.IPAddrs...)
	}
	output.IPAddrs = uniqueStrings(output.IPAddrs)

	// Use the `log` object passed into the Connect method and any logging information
	// will be returned with the message in the log field. Otherwise, it will be discarded.

	// return output and no error for success
	// return nil and error for failure

	return output, nil
}

// Test will test the action with the given input over the given connection.
// For this, you should design the output result to be used with the tests in the test/ directory.
// You do not need to / should not need to invoke the actual API, this is just for testing.
func (a *IPExtractorAction) Test(conn *connection.Connection, input *IPExtractorInput, log plog.Logger) (*IPExtractorOutput, error) {
	output := &IPExtractorOutput{}
	// Your code here
	// NOTE: The input you receive in the test method cannot be gauranteed to contain "good" value.
	// You should not assume the input is something you can trust in this context.

	// Use the `log` object passed into the Connect method and any logging information
	// will be returned with the message in the log field. Otherwise, it will be discarded.

	// return output and no error for success
	// return nil and error for failure

	return output, nil
}

func ipChecker(IPAddrs, ips []string) []string {
	for _, ip := range ips {
		trial := net.ParseIP(ip)
		if trial.To4() != nil {
			IPAddrs = append(IPAddrs, trial.String())
		}
	}
	return IPAddrs
}