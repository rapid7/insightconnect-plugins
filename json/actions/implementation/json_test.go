package implementation

import "testing"

//debug
//func TestStdIoHack (t *testing.T) { t.Errorf("fake fail to see stdio") }

func TestTransform(t *testing.T) {
	for _, c := range TestTransformCases {
		got := Transform(c.sourceData, c.sourceTemplate, c.transTemplate)
		if !Same(got, c.want) {
			t.Errorf("Transform got %v but wanted %v", got, c.want)
		}
	}
}

var TestTransformCases = []struct {
	sourceData     JSON
	sourceTemplate JSON
	transTemplate  JSON
	want           JSON
}{
	{ // 1 of 5
		JSONMap{
			"author":      "Neil Stephenson",
			"title":       "Snow Crash",
			"age":         20,
			"description": "villain activates bicameral mind",
			"characters":  JSONArray{"Hiro Protagonist", "Skateboarder"},
		},
		JSONMap{
			"title":      "$0",
			"author":     "$1",
			"characters": JSONArray{"$2"},
			"age":        "$3",
		},
		JSONMap{
			"bug name":    "$0",
			"owner":       "$2",
			"reported by": "$1",
			"age in eons": "$3",
		},
		JSONMap{
			"bug name":    "Snow Crash",
			"owner":       "Hiro Protagonist",
			"reported by": "Neil Stephenson",
			"age in eons": 20,
		},
	},
	{ // 2 of 5
		JSONMap{
			"OK": "GO",
			"Now": JSONArray{1, 2, 3,
				JSONMap{
					"is": JSONArray{1, 2, 3,
						JSONMap{
							"the": JSONArray{1, 2, 3,
								JSONMap{
									"time": "to come to the aid of the party",
								}}}}}}},
		JSONMap{
			"OK": "GO",
			"Now": JSONArray{"$1", 2, 3,
				JSONMap{
					"is": JSONArray{1, "$2", 3,
						JSONMap{
							"the": JSONArray{1, 2, "$3",
								JSONMap{
									"time": "$4",
								}}}}}}},
		JSONMap{
			"numbers": JSONArray{"$1", "$2", "$3"},
			"advice":  "$4",
		},
		JSONMap{
			"numbers": JSONArray{1, 2, 3},
			"advice":  "to come to the aid of the party",
		},
	},
	{ // 3 of 5
		JSONMap{
			"OK": "GO",
			"Now": JSONArray{1, 2, 3,
				JSONMap{
					"is": JSONArray{1, 2, 3,
						JSONMap{
							"the": JSONArray{1, 2, 3,
								JSONMap{
									"time": "to come to the aid of the party",
								}}}}}}},
		JSONMap{
			"OK": "GO",
			"Now": JSONArray{"$1",
				JSONMap{
					"is": JSONArray{1, "$2",
						JSONMap{
							"the": JSONArray{1, 2, "$3",
								JSONMap{
									"time": "$4",
								}}}}}}},
		JSONMap{
			"numbers": JSONArray{"$1", "$2", "$3"},
			"advice":  "$4",
		},
		JSONMap{
			"numbers": JSONArray{1, "", ""},
			"advice":  "",
		},
	},
	{ // 4 of 5 - regexp filter on array element
		JSONMap{
			"Reviews": JSONArray{"so-so", "banal", "special!", "puzzling", "quite good!"},
		},
		JSONMap{
			"Reviews": "$1:.*special.*|.*good.*|.*great.*",
		},
		JSONMap{
			"Critics Raved!": "$1",
		},
		JSONMap{
			"Critics Raved!": JSONArray{"special!", "quite good!"},
		},
	},
	{ // 5 of 5 - regexp filter on array element is case-insensitive
		JSONMap{
			"Reviews": JSONArray{"So-so...", "Banal", "Special!", "Puzzling", "Good to see"},
		},
		JSONMap{
			"Reviews": "$1:.*special.*|.*good.*|.*great.*",
		},
		JSONMap{
			"Critics Raved!": "$1",
		},
		JSONMap{
			"Critics Raved!": JSONArray{"Special!", "Good to see"},
		},
	},
}

func TestGetExtractionMap(t *testing.T) {
	cases := []struct {
		varName    VarName
		inTemplate JSONMap
		query      Query
	}{
		{"$0", JSONMap{"Hootie": "$0"}, Query{NewMA("Hootie", 0)}},
		{
			"$Embedded",
			JSONMap{"Blowfish": JSONArray{123, "$Embedded", "leaf"}},
			Query{NewMA("Blowfish", 1), NewAA(1, 2)},
		},
		{
			"$Gnarly",
			JSONMap{
				"OK": "GO",
				"Now": JSONArray{1, 2, 3,
					JSONMap{
						"is": JSONArray{1, 2,
							JSONMap{
								"the": JSONArray{1,
									JSONMap{
										"time": "$Gnarly",
									}}}}}},
			},
			Query{NewMA("Now", 1), NewAA(3, 2), NewMA("is", 3), NewAA(2, 4), NewMA("the", 5), NewAA(1, 6), NewMA("time", 7)},
		},
	}
	for _, c := range cases {
		got := GetExtractionMap(c.inTemplate)
		if !IsSameQuery(got[c.varName], c.query) {
			t.Errorf("GetExtractionMap got query %v, wanted query %v", got[c.varName], c.query)
		}
	}
}

func TestGetViaQuery(t *testing.T) {
	cases := []struct {
		source JSON
		query  Query
		want   string
	}{
		{
			JSONMap{
				"OK": "GO",
				"Now": JSONArray{1, 2, 3,
					JSONMap{
						"is": JSONArray{1, 2,
							JSONMap{
								"the": JSONArray{1,
									JSONMap{
										"time": "to come to the party",
									}}}}}},
			},
			Query{NewMA("Now", 1), NewAA(3, 2), NewMA("is", 3), NewAA(2, 4), NewMA("the", 5), NewAA(1, 6), NewMA("time", 7)},
			"to come to the party",
		},
	}
	for _, c := range cases {
		got := GetViaQuery(c.source, c.query)
		if got != c.want {
			t.Errorf("GetViaQuery got %v, wanted %v", got, c.want)
		}
	}
}

func TestGetSubstitutionEnv(t *testing.T) {
	cases := []struct {
		source   JSON
		xtractor ExtractionMap
		want     SubstitutionEnv
	}{
		{
			JSONMap{
				"Top":    JSONArray{1, "of the town", 2},
				"Bottom": "Quark",
			},
			ExtractionMap{
				"$0": Query{NewMA("Top", 1), NewAA(1, 2)},
				"$1": Query{NewMA("Bottom", 1)},
			},
			SubstitutionEnv{
				"$0": "of the town",
				"$1": "Quark",
			},
		},
	}
	for _, c := range cases {
		got := GetSubstitutionEnv(c.source, c.xtractor)
		for k, v := range got {
			if !Same(v, c.want[k]) {
				t.Errorf("GetSubstitutionEnv got %v, wanted %v", got, c.want)
			}
		}
	}
}

func TestSubstitute(t *testing.T) {
	cases := []struct {
		transTemplate JSON
		env           SubstitutionEnv
		want          JSON
	}{
		{
			JSONMap{
				"age_of_bug_in_eons": "$111",
				"author":             "$222",
				"climate":            "$333",
			},
			SubstitutionEnv{
				"$111": 42,
				"$222": JSONArray{"Neil", "Stevenson"},
				"$333": "the rain in Spain",
			},
			JSONMap{
				"age_of_bug_in_eons": 42,
				"author":             JSONArray{"Neil", "Stevenson"},
				"climate":            "the rain in Spain",
			},
		},
	}
	for _, c := range cases {
		got := Substitute(c.transTemplate, c.env)
		if !Same(got, c.want) {
			t.Errorf("Substitute got %v, wanted %v", got, c.want)
		}
	}
}

func TestSame(t *testing.T) {
	cases := []struct {
		thing1 interface{}
		thing2 interface{}
		same   bool
	}{
		// nil branches
		{nil, nil, true},
		{nil, 1, false},
		{nil, "yo!", false},
		// int branches
		{1, 1, true},
		{1, 2, false},
		{1, "yo!", false},
		{1, nil, false},
		// float branches
		{1.0, 1.0, true},
		{1, 2.0, false},
		{1.0, "yo!", false},
		{1.0, nil, false},
		// string branches
		{"yo", "yo", true},
		{"yo", "yeah", false},
		{"yo", 1, false},
		{"yo", nil, false},
		// array branches
		{JSONArray{true, 1, "two", JSONMap{"k": "v"}},
			JSONArray{true, 1, "two", JSONMap{"k": "v"}}, true},
		{JSONArray{true, 1, "two", JSONMap{"k": "v"}},
			JSONArray{true, "one", 2, JSONMap{"k": "v"}}, false},

		// JSON branches

		// empty map
		{JSONMap{}, JSONMap{}, true},
		{JSONMap{}, JSONMap{"k": "v"}, false},
		{JSONMap{"k": "v"}, JSONMap{}, false},

		// vanilla
		{JSONMap{"k1": "v1", "k2": 2}, JSONMap{"k1": "v1", "k2": 2}, true},
		{JSONMap{"k1": "v1", "k2": 2}, JSONMap{"k1": "v1", "k2": "2"}, false},

		// order doesn't matter
		{JSONMap{"k1": "v1", "k2": "v2"}, JSONMap{"k2": "v2", "k1": "v1"}, true},

		// nested
		{JSONMap{"k1": "v1", "k2": "v2", "k3": JSONMap{"k11": "v11"}},
			JSONMap{"k1": "v1", "k2": "v2", "k3": JSONMap{"k11": "v11"}}, true},
		{JSONMap{"k1": "v1", "k2": "v2", "k3": JSONMap{"k11": "v11"}, "k4": 4},
			JSONMap{"k1": "v1", "k2": "v2", "k3": JSONMap{"k11": "v11"}, "k4": 4}, true},
		{JSONMap{"k1": "v1", "k2": "v2", "k3": JSONMap{"k11": "v11"}},
			JSONMap{"k1": "v1", "k2": "v2", "k3": JSONMap{"k11": 11}}, false},
		{JSONMap{"k1": "v1", "k2": "v2", "k3": JSONMap{"k11": "v11"}, "k4": 4},
			JSONMap{"k1": "v1", "k2": "v2", "k3": JSONMap{"k11": "v11"}, "k4": "v4"}, false},
	}
	for _, c := range cases {
		got := Same(c.thing1, c.thing2)
		if got != c.same {
			t.Errorf("Same(%v, %v) == %v, want %v", c.thing1, c.thing2, got, c.same)
		}
	}
}
