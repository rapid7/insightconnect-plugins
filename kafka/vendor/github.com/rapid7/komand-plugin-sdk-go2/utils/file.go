// Package utils is a random package of helper functions used either by other packages in the SDK
// or simply provided to help developers perform common tasks.
package utils

import (
	"os"
	"path/filepath"
)

// OpenFile is a low level call to safely open a file, with the provided flags and permissions
// if the path underwhich the file is found does not exist, OpenFile will create that path
// using os.ModePerm. However the behavior of whether or not it creates the file when not found
// is up to the caller of OpenFile to determine via the flags/perms arguments. You can combine several
// flags together, by passing them in a bitwise OR, ie: OpenFile("blah",os.O_RDWR|os.O_CREATE|os.O_EXCL,0600)
func OpenFile(name string, flags int, perms os.FileMode) (*os.File, error) {
	if _, err := os.Stat(name); err != nil {
		// If it didn't exist
		var ok bool
		if ok, err = DoesFileExist(name); err != nil {
			// Create the file and all directories leading up to it, if it didn't exist
			return nil, err
		}
		if !ok { // if the file doesn't exist, do a best-effort attempt to make any missing parts of the directory first
			if err = os.MkdirAll(filepath.Dir(name), os.ModePerm); err != nil {
				return nil, err
			}
		}
	}
	// Create the file if it doesn't exist, otherwise open the file if it's already on disk, based on flags
	return os.OpenFile(name, flags, perms)
}

// DoesFileExist returns an error because there is a slight chance something goes wrong
// when checking the file system, and so the caller may need to bubble the error up to it's caller
// I'm not 100% sure how or why this might happen, but it's better to not ignore it, even at the cost
// of a slightly dumber API
func DoesFileExist(name string) (bool, error) {
	if _, err := os.Stat(name); err != nil {
		if os.IsNotExist(err) {
			return false, nil
		}
		return false, err
	}
	return true, nil
}
