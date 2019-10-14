package implementation

// BoolBranch detects a golang bool
func BoolBranch(thing1 JSON) bool {
	_, b := thing1.(bool)
	return b
}

// IntBranch detects a golang int
func IntBranch(thing1 JSON) bool {
	_, b := thing1.(int)
	return b
}

// Float64Branch detects a golang float64
func Float64Branch(thing1 JSON) bool {
	_, b := thing1.(float64)
	return b
}

// StringBranch detects a golang string
func StringBranch(thing1 JSON) bool {
	_, b := thing1.(string)
	return b
}

// MapBranch returns true if it argument is a JSONMap
func MapBranch(thing1 JSON) bool {
	_, b := thing1.(JSONMap)
	return b
}

// ArrayBranch returns true if it argument is a JSONArray
func ArrayBranch(thing1 JSON) bool {
	_, b := thing1.(JSONArray)
	return b
}

// RawMapBranch returns true if it argument is a raw JSON map
// (i.e. map[string]interface{})
func RawMapBranch(thing1 interface{}) bool {
	_, b := thing1.(map[string]interface{})
	return b
}

// RawArrayBranch returns true if it argument is a raw JSON array
// (i.e. []interface{})
func RawArrayBranch(thing1 interface{}) bool {
	_, b := thing1.([]interface{})
	return b
}
