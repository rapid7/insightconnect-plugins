package actions

func uniqueStrings(input []string) []string {
	u := make([]string, 0)
	m := make(map[string]bool)

	for _, val := range input {
		if _, ok := m[val]; !ok {
			m[val] = true
			u = append(u, val)
		}
	}

	return u
}
