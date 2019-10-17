package implementation

import "strings"

/*
To exercise:
bash-3.2$ go clean json/actions/implementation
bash-3.2$ go build json/actions/implementation
bash-3.2$ go test json/actions/implementation
ok  	json/actions/implementation	0.041s
*/

// *** top-level types

// JSON lets us call out the specific use case for interface{} (useful
// for testing, etc.)
type JSON interface{}

// JSONMap lets us call out the specific use case for interface{} (useful
// for testing, etc.)
type JSONMap map[string]JSON

// JSONArray lets us call out the specific use case for interface{} (useful
// for testing, etc.)
type JSONArray []JSON

// VarName lets this package call out that certain strings represent
// variables sites in JSON data or templates
type VarName string

// IsVar lets this package detect a variable site in JSON data or
// templates
func IsVar(maybeVarName JSON) bool {
	name, ok := maybeVarName.(string)
	return ok && strings.HasPrefix(name, "$")
}

// ExtractionMap is a type name used throughout this package (see
// design.txt)
type ExtractionMap map[VarName]Query

// SubstitutionEnv is a type name used throughout this package (see
// design.txt)
type SubstitutionEnv map[VarName]JSON

// *** the raw and the cooked

// IsRaw and the RawXXX machinery throughout this package are due to
// the fact that the external encoding/json uses implicit interface{}
// types while this code uses explicit JSONxxx types.  This in turn is
// due to the fact that this package needs the named types to build test
// data conveniently
func IsRaw(source JSON) bool {
	isRaw := false
	_, isRaw = source.(map[string]interface{})
	if !isRaw {
		_, isRaw = source.([]interface{})
	}
	return isRaw
}

// *** top-level workhorse

// input:
// - source JSON data
// - source JSON template
// - target JSON template

// output:
// - target JSON: contains source data and looks like target template

// Transform is the top-level workhorse func in this package
func Transform(
	sourceData JSON, sourceTemplate JSON, targetTemplate JSON) (targetData JSON) {
	xtractor := GetExtractionMap(sourceTemplate)
	env := GetSubstitutionEnv(sourceData, xtractor)
	return Substitute(targetTemplate, env)
}

// *** extraction map

// GetExtractionMap - given a piece of JSON as source template, determines
// how to access its variables (i.e. strings beginning with "$")
func GetExtractionMap(sourceTemplate JSON) ExtractionMap {
	xtractor := make(ExtractionMap)
	populateExtractionMap(sourceTemplate, NoMoreAccessors(), xtractor)
	return xtractor
}

func populateExtractionMap(
	thing JSON, acc Accessor, xtractor ExtractionMap) {
	switch {
	case IsVar(thing): // reached from within a JSONArray
		nameMaybeFilter := strings.Split(thing.(string), ":")
		if len(nameMaybeFilter) > 1 {
			acc.Filter = nameMaybeFilter[1]
		}
		xtractor[VarName(nameMaybeFilter[0])] = accessorList2Query(acc)
	case MapBranch(thing):
		for k, v := range thing.(JSONMap) {
			extractMapShared(k, v.(interface{}), acc, xtractor)
		}
	case RawMapBranch(thing):
		for k, v := range thing.(map[string]interface{}) {
			extractMapShared(k, v, acc, xtractor)
		}
	case ArrayBranch(thing):
		array := thing.(JSONArray)
		for i := 0; i < len(array); i++ {
			populateExtractionMap(array[i], NewArrayAccessor(i, acc), xtractor)
		}
	case RawArrayBranch(thing):
		array := thing.([]interface{})
		for i := 0; i < len(array); i++ {
			populateExtractionMap(array[i], NewArrayAccessor(i, acc), xtractor)
		}
	}
}

func extractMapShared(
	k string, v interface{}, acc Accessor, xtractor ExtractionMap) {
	newacc := NewMapAccessor(k, acc)
	if IsVar(v) {
		nameMaybeFilter := strings.Split(v.(string), ":")
		if len(nameMaybeFilter) > 1 {
			newacc.Filter = nameMaybeFilter[1]
		}
		xtractor[VarName(nameMaybeFilter[0])] = accessorList2Query(newacc)
	} else {
		populateExtractionMap(v, newacc, xtractor)
	}
}

func accessorList2Query(acc Accessor) Query {
	array := make([]Accessor, acc.Depth)
	for accPtr := &acc; accPtr.Depth > 0; accPtr = accPtr.Prev {
		array[accPtr.Depth-1] = *accPtr
	}
	return array
}

// *** substitution environment

// GetSubstitutionEnv - given a piece of JSON that adheres to the
// source template, finds the values in the same places that the source
// template specified variables
func GetSubstitutionEnv(
	source JSON, xtractor ExtractionMap) SubstitutionEnv {
	env := make(SubstitutionEnv)
	for k, v := range xtractor {
		env[k] = GetViaQuery(source, v)
	}
	return env
}

// *** deep substitute

// Substitute - given an piece of JSON as target template, produce a
// copy containing the values obtained from the source JSON, as specified
// by variables in the source template (i.e. as specified by the
// substitution environment)
func Substitute(
	targetTemplate JSON, env SubstitutionEnv) (output JSON) {
	return deepSubstitute(targetTemplate, env)
}

func deepSubstitute(thing JSON, env SubstitutionEnv) JSON {
	switch {
	case (thing == nil) || BoolBranch(thing) || IntBranch(thing) || Float64Branch(thing):
		return thing
	case IsVar(thing): // reached from within a JSONArray
		return env[VarName(thing.(string))]
	case StringBranch(thing):
		return thing.(string) + "" // i.e. new string
	case MapBranch(thing):
		newmap := make(JSONMap)
		for k, v := range thing.(JSONMap) {
			substituteMapShared(newmap, k, v, env, IsVar(v), false)
		}
		return newmap
	case RawMapBranch(thing):
		newmap := make(map[string]interface{})
		for k, v := range thing.(map[string]interface{}) {
			substituteMapShared(newmap, k, v, env, IsVar(v), true)
		}
		return newmap
	case ArrayBranch(thing):
		array := thing.(JSONArray)
		newarray := make(JSONArray, len(array))
		for i := 0; i < len(array); i++ {
			newarray[i] = deepSubstitute(array[i], env)
		}
		return newarray
	case RawArrayBranch(thing):
		array := thing.([]interface{})
		newarray := make([]interface{}, len(array))
		for i := 0; i < len(array); i++ {
			newarray[i] = deepSubstitute(array[i], env)
		}
		return newarray
	default:
		return nil
	}
}

func substituteMapShared(
	m interface{},
	k string, v interface{}, env SubstitutionEnv,
	isVar bool, isRaw bool) {
	if isRaw {
		newmap := m.(map[string]interface{})
		if isVar {
			newmap[k] = env[VarName(v.(string))]
		} else {
			newmap[k] = deepSubstitute(v, env)
		}
	} else {
		newmap := m.(JSONMap)
		if isVar {
			newmap[k] = env[VarName(v.(string))]
		} else {
			newmap[k] = deepSubstitute(v, env)
		}
	}
}
