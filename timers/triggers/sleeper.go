package triggers

import (
	"fmt"
	"os"
	"time"
)

// TimePeriod represents the repeat time period
type TimePeriod string

const (
	hourlyPeriod = TimePeriod("hourly")
	dailyPeriod  = TimePeriod("daily")
	weeklyPeriod = TimePeriod("weekly")
)

// futureTime is the time since Jan 1, year 0.
// It's timezone is assumed to be the current local time
func durationUntilFutureTime(now time.Time, futureTime time.Time, period TimePeriod) time.Duration {
	day := now.Day()
	hour := now.Hour()
	var increment time.Duration

	switch period {
	case hourlyPeriod:
		increment = time.Hour
	case dailyPeriod:
		increment = 24 * time.Hour
		hour = futureTime.Hour()
	case weeklyPeriod:
		increment = 7 * 24 * time.Hour
		hour = futureTime.Hour()
		// Note that for futureTime, we encode weekday in the day of the month (e.g., 1 = Sunday)
		dayDiff := (futureTime.Day() - 1) - int(now.Weekday())
		if dayDiff > 0 {
			day = day + dayDiff
		} else {
			day = day + 7 + dayDiff
		}
	default:
		// never happens but force a long time if it does
		day = day + 30
	}

	futureTime = time.Date(now.Year(), now.Month(), day, hour,
		futureTime.Minute(), futureTime.Second(), futureTime.Nanosecond(),
		now.Location())
	if futureTime.Before(now) {
		futureTime = futureTime.Add(increment)
	}

	return futureTime.Sub(now)
}

func sleepUntilNextTime(times []time.Time, period TimePeriod) {
	now := time.Now().UTC()

	var duration time.Duration
	var noDuration time.Duration
	for _, t := range times {
		d := durationUntilFutureTime(now, t, period)
		if duration == noDuration || d < duration {
			duration = d
		}
	}
	if duration == noDuration {
		// No duration is an error
		fmt.Fprintln(os.Stderr, "No valid sleep times")
		os.Exit(1)
	}
	time.Sleep(duration + 200*time.Millisecond) // the extra sleep is to prevent the same event from being triggered again because time.Now hasn't advanced
}
