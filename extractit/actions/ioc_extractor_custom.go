package actions

import (
	"regexp"

	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/extractit/connection"
	"mvdan.cc/xurls"
)

// Validate will validate the input is properly setup with whatever rules you put in
// You can also use this to pre-set any values before they are run by the Run method.
// Note that for Actions, the  Input message is inspected every time time, just before it
// is handed to the Run method. Keep this in mind when setting any properties on the Input i
// You can return a set of errors for any reason to fail the step.
// Otherwise, return nil for success
func (i *IocExtractorInput) Validate(log plog.Logger) []error {
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
func (o *IocExtractorOutput) Validate(log plog.Logger) []error {
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
func (a *IocExtractorAction) Run(conn *connection.Connection, input *IocExtractorInput, log plog.Logger) (*IocExtractorOutput, error) {
	output := &IocExtractorOutput{}
	ip4 := regexp.MustCompile("(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\[?\\.\\]?){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)")
	ip6 := regexp.MustCompile("(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))")
	dom := regexp.MustCompile(`[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~]*)`)
	em := regexp.MustCompile("[A-Za-z0-9_.]+@[0-9a-z.-]+")
	mc := regexp.MustCompile(`([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})`)
	fp := regexp.MustCompile(`/\S+`)
	dt := regexp.MustCompile(`\d{1,2}/\d{1,2}/\d{4}`)
	md := regexp.MustCompile("[A-Fa-f0-9]{32}")
	sha1 := regexp.MustCompile("[A-Fa-f0-9]{40}")
	sha25 := regexp.MustCompile("[A-Fa-f0-9]{64}")
	sha51 := regexp.MustCompile("[A-Fa-f0-9]{128}")

	if input.File != nil {
		output.Iocs = dedup(xurls.Relaxed.FindAllString(string(input.File), -1))
		IP := ip4.FindAllString(string(input.File), -1)
		s := ip6.FindAllString(string(input.File), -1)
		domain := dom.FindAllString(string(input.File), -1)
		em := em.FindStringSubmatch(string(input.File))
		mac := mc.FindAllString(string(input.File), -1)
		f := fp.FindAllString(string(input.File), -1)
		d := dt.FindAllString(string(input.File), -1)
		Md5 := md.FindAllString(string(input.File), -1)
		Sha1 := sha1.FindAllString(string(input.File), -1)
		Sha2 := sha25.FindAllString(string(input.File), -1)
		Sha5 := sha51.FindAllString(string(input.File), -1)

		output.Iocs = append(output.Iocs, s...)
		output.Iocs = append(output.Iocs, d...)
		output.Iocs = append(output.Iocs, IP...)
		output.Iocs = append(output.Iocs, domain...)
		output.Iocs = append(output.Iocs, mac...)
		output.Iocs = append(output.Iocs, f...)
		output.Iocs = append(output.Iocs, Md5...)
		output.Iocs = append(output.Iocs, Sha1...)
		output.Iocs = append(output.Iocs, Sha2...)
		output.Iocs = append(output.Iocs, em...)
		output.Iocs = append(output.Iocs, Sha5...)
	}
	if input.Str != "" {
		Iocs := dedup(xurls.Relaxed.FindAllString(input.Str, -1))
		IP := ip6.FindAllString(input.Str, -1)
		s := ip4.FindAllString(input.Str, -1)
		domain := dom.FindAllString(input.Str, -1)
		em := em.FindStringSubmatch(input.Str)
		mac := mc.FindAllString(input.Str, -1)
		f := fp.FindAllString(input.Str, -1)
		d := dt.FindAllString(input.Str, -1)
		Md5 := md.FindAllString(input.Str, -1)
		Sha1 := sha1.FindAllString(input.Str, -1)
		Sha2 := sha25.FindAllString(input.Str, -1)
		Sha5 := sha51.FindAllString(input.Str, -1)

		output.Iocs = append(output.Iocs, Iocs...)
		output.Iocs = append(output.Iocs, s...)
		output.Iocs = append(output.Iocs, d...)
		output.Iocs = append(output.Iocs, IP...)
		output.Iocs = append(output.Iocs, domain...)
		output.Iocs = append(output.Iocs, mac...)
		output.Iocs = append(output.Iocs, f...)
		output.Iocs = append(output.Iocs, Md5...)
		output.Iocs = append(output.Iocs, Sha1...)
		output.Iocs = append(output.Iocs, Sha2...)
		output.Iocs = append(output.Iocs, em...)
		output.Iocs = append(output.Iocs, Sha5...)
	}

	output.Iocs = uniqueStrings(output.Iocs)

	// Use the `log` object passed into the Connect method and any logging information
	// will be returned with the message in the log field. Otherwise, it will be discarded.

	// return output and no error for success
	// return nil and error for failure

	return output, nil
}

// Test will test the action with the given input over the given connection.
// For this, you should design the output result to be used with the tests in the test/ directory.
// You do not need to / should not need to invoke the actual API, this is just for testing.
func (a *IocExtractorAction) Test(conn *connection.Connection, input *IocExtractorInput, log plog.Logger) (*IocExtractorOutput, error) {
	output := &IocExtractorOutput{}
	// Your code here
	// NOTE: The input you receive in the test method cannot be gauranteed to contain "good" value.
	// You should not assume the input is something you can trust in this context.

	// Use the `log` object passed into the Connect method and any logging information
	// will be returned with the message in the log field. Otherwise, it will be discarded.

	// return output and no error for success
	// return nil and error for failure

	return output, nil
}
