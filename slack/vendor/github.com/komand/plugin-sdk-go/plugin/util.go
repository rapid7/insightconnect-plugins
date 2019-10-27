package plugin

import (
	"errors"
	"strings"
)

func joinErrors(errs []error) error {
	mega := make([]string, 1)
	for _, e := range errs {
		if e != nil {
			mega = append(mega, e.Error())
		}
	}
	return errors.New(strings.Join(mega, "\n"))
}

func clean(errs []error) []error {

	if errs == nil {
		return nil
	}
	r := make([]error, 0)
	for _, e := range errs {
		if e != nil {
			r = append(r, e)
		}
	}

	if len(r) > 0 {
		return r
	}
	return nil
}
