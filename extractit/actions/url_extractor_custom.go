package actions

import (
	"net"
	"net/url"
	"strings"

	"github.com/goware/urlx"
	"github.com/mvdan/xurls"
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/extractit/connection"
)

// Validate will validate the input is properly setup with whatever rules you put in
// You can also use this to pre-set any values before they are run by the Run method.
// Note that for Actions, the  Input message is inspected every time time, just before it
// is handed to the Run method. Keep this in mind when setting any properties on the Input i
// You can return a set of errors for any reason to fail the step.
// Otherwise, return nil for success
func (i *URLExtractorInput) Validate(log plog.Logger) []error {
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
func (o *URLExtractorOutput) Validate(log plog.Logger) []error {
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
func (a *URLExtractorAction) Run(conn *connection.Connection, input *URLExtractorInput, log plog.Logger) (*URLExtractorOutput, error) {
	output := &URLExtractorOutput{}
	if input.File != nil {
		urls := parseForURLs(input.File, " ", log)
		output.Urls = dedup(urls)
	}

	if input.Str != "" {
		urls := parseForURLs([]byte(input.Str), " ", log)
		urls = dedup(urls)
		output.Urls = append(output.Urls, urls...)
	}

	// Use the `log` object passed into the Connect method and any logging information
	// will be returned with the message in the log field. Otherwise, it will be discarded.

	// return output and no error for success
	// return nil and error for failure

	return output, nil
}

// Test will test the action with the given input over the given connection.
// For this, you should design the output result to be used with the tests in the test/ directory.
// You do not need to / should not need to invoke the actual API, this is just for testing.
func (a *URLExtractorAction) Test(conn *connection.Connection, input *URLExtractorInput, log plog.Logger) (*URLExtractorOutput, error) {
	output := &URLExtractorOutput{}
	test := "The sun sets on the sahara in https://www.mali.empire"
	output.Urls = parseForURLs([]byte(test), " ", log)
	output.Urls = uniqueStrings(output.Urls)
	// NOTE: The input you receive in the test method cannot be gauranteed to contain "good" value.
	// You should not assume the input is something you can trust in this context.

	// Use the `log` object passed into the Connect method and any logging information
	// will be returned with the message in the log field. Otherwise, it will be discarded.

	// return output and no error for success
	// return nil and error for failure

	return output, nil
}

// parseStringForURLs takes a byte slice and returns a slice or strings
func parseForURLs(b []byte, sep string, log plog.Logger) []string {
	strReplace := strings.Replace(string(b), "\n", " ", -1)
	splitString := strings.Split(strReplace, sep)
	var urls []string
	for _, nurl := range splitString {
		extractedURL := xurls.Relaxed().FindString(nurl)
		parsedURL, err := urlx.Parse(extractedURL)
		if err == nil {
			isIP := checkIP(parsedURL.Host)
			if !isIP {
				encodedURL, err := url.QueryUnescape(extractedURL)
				if err != nil {
					urls = append(urls, encodedURL)
				} else { // Something bombed while escaping, return the original URL.
					urls = append(urls, extractedURL)
				}
			}
		} else {
			log.Error(err.Error())
		}
	}
	return urls
}

func checkIP(ip string) bool {
	trial := net.ParseIP(ip)
	if trial.To4() == nil {
		return false
	}
	return true
}

func dedup(items []string) []string {
	uniques := make(map[string]interface{})
	for _, key := range items {
		uniques[key] = true
	}

	result := make([]string, 0)
	for key := range uniques {
		result = append(result, key)
	}

	return result
}
