package actions

func getPriority(priority string) int {
	p := 0
	switch priority {
	case "1 - Emergency":
		p = 1
	case "2 - Ultimate":
		p = 2
	case "3 - Critical":
		p = 3
	case "4 - Major":
		p = 4
	case "5 - High":
		p = 5
	case "6 - Standard":
		p = 6
	case "7 - Medium":
		p = 7
	case "8 - Minor":
		p = 8
	case "9 - Low":
		p = 9
	}
	return p
}
