package parameter

import (
	"encoding/json"
	"fmt"
	"io"
)

// much of this code is taken from the Drone (drone.io) project

// Stdin is the parameter set taken in from the command line
var Stdin *ParamSet

// ParamSet holds a list of parameters passed in on the composed io.Reader
type ParamSet struct {
	reader io.Reader
	params map[string]interface{}
}

// NewParamSet creates a new ParamSet for the given io.Reader
func NewParamSet(reader io.Reader) *ParamSet {
	var p = new(ParamSet)
	p.reader = reader
	p.params = map[string]interface{}{}
	return p
}

// Param defines a parameter with the specified name.
func (p ParamSet) Param(name string, value interface{}) {
	p.params[name] = value
}

// Parse parses parameter definitions from the map.
func (p ParamSet) Parse() error {
	raw := map[string]json.RawMessage{}
	err := json.NewDecoder(p.reader).Decode(&raw)
	if err != nil {
		return err
	}

	for key, val := range p.params {
		data, ok := raw[key]
		if !ok {
			continue
		}
		err := json.Unmarshal(data, val)
		if err != nil {
			return fmt.Errorf("Unable to unmarshal %s. %s", key, err)
		}
	}

	return nil
}

// Unmarshal parses the JSON payload from the command
// arguments and unmarshal into a value pointed to by v.
func (p ParamSet) Unmarshal(v interface{}) error {
	return json.NewDecoder(p.reader).Decode(v)
}

// Param defines a parameter with the specified name.
func Param(name string, value interface{}) {
	Stdin.Param(name, value)
}

// Parse parses parameter definitions from the map.
func Parse() error {
	return Stdin.Parse()
}

// Unmarshal parses the JSON payload from the command
// arguments and unmarshal into a value pointed to by v.
func Unmarshal(v interface{}) error {
	return Stdin.Unmarshal(v)
}

// MustUnmarshal parses the JSON payload from the command
// arguments and unmarshal into a value pointed to by v.
// If there is an error, it will panic instead of returning
// the error.
func MustUnmarshal(v interface{}) {
	err := Stdin.Unmarshal(v)
	if err != nil {
		panic(err)
	}
}

// MustParse parses parameter definitions from the map
// and panics if there is a parsing error.
func MustParse() {
	err := Parse()
	if err != nil {
	}
	panic(err)
}
