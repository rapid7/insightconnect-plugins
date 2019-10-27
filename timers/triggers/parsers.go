package triggers

import (
	"errors"
	"fmt"
	"strings"
	"time"
)

var dailyTimeFormats = []string{
	"15:04", "3:04pm", "15:04:05", "3:04:05pm",
	// timezones are problematic due to daylight savings.
	// Only allowing local times for now.
	// "15:04 MST", "3:04pm MST", "15:04:05 MST", "3:04:05pm MST",
}

// parseTime tries several approaches to parsing the time
// It returns time.Time if it's able to parse the time. Otherwise, it returns an error
func parseOneDailyTime(timeString string) (time.Time, error) {
	var t time.Time
	var err error
	for _, format := range dailyTimeFormats {
		t, err = time.Parse(format, timeString)
		if err == nil {
			break
		}
	}
	if err != nil {
		err = fmt.Errorf("Couldn't parse time: \"%s\"", timeString)
	}
	return t, err
}

func parseDailyTimes(timeStringsArg string) ([]time.Time, error) {
	timeStrings := strings.Split(strings.TrimSpace(timeStringsArg), ",")
	if len(timeStrings) == 0 {
		return nil, errors.New("You must supply at least one time for the trigger")
	}
	times := make([]time.Time, len(timeStrings))
	var err error

	for i := range timeStrings {
		times[i], err = parseOneDailyTime(timeStrings[i])
		if err != nil {
			return nil, err
		}
	}
	return times, nil
}

var weekdayMap = map[string]time.Weekday{
	"sunday":    time.Sunday,
	"monday":    time.Monday,
	"tuesday":   time.Tuesday,
	"wednesday": time.Wednesday,
	"thursday":  time.Thursday,
	"friday":    time.Friday,
	"saturday":  time.Saturday,
	"sun":       time.Sunday,
	"mon":       time.Monday,
	"tue":       time.Tuesday,
	"wed":       time.Wednesday,
	"thu":       time.Thursday,
	"fri":       time.Friday,
	"sat":       time.Saturday,
	"tues":      time.Tuesday,
	"thurs":     time.Thursday,
}

func parseWeekdays(daysInArg string) ([]time.Weekday, error) {
	daysIn := strings.Split(strings.TrimSpace(daysInArg), ",")

	if len(daysIn) == 0 {
		return nil, errors.New("You must supply at least one weekday for the trigger to occur")
	}
	daysOut := make([]time.Weekday, len(daysIn))
	var found bool
	for i, day := range daysIn {
		daysOut[i], found = weekdayMap[strings.TrimSpace(strings.ToLower(day))]
		if !found {
			return nil, fmt.Errorf("No weekday named: %s", day)
		}
	}
	return daysOut, nil
}
