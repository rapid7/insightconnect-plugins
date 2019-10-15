// Package log is a simple logger abstraction that buffers internally, and writes out at a user-defined period
// this enables us to log inside of an action, but delay where and when the log is written to an external source
// so that the http server and the "one and done" old school action invocations can use the same log, but present
// data back to the user in a simple manner.
package log

import (
	"bytes"
	"fmt"
	"io"
	"log"
)

// Level defines logging levels
type Level int

// This const block defines logging level constants for other packages to use
const (
	Info  Level = 0
	Warn  Level = 1
	Error Level = 2
)

// Logger is a very lightweight interface around 2 simple log calls
type Logger interface {
	Error(string)
	Warn(string)
	Info(string)
	Errorf(string, ...interface{})
	Warnf(string, ...interface{})
	Infof(string, ...interface{})
	SetLevel(Level)
}

// BufferedLogger is a wrapper around a []string buffer. It is threadsafe questionmarks?
type BufferedLogger struct {
	buf   bytes.Buffer
	level Level
}

// NewBufferedLogger will return a new instance of Logger
func NewBufferedLogger(level Level) *BufferedLogger {
	return &BufferedLogger{
		level: level,
	}
}

// Error logs at the error level
func (l *BufferedLogger) Error(line string) {
	if l.level >= Error {
		l.buf.WriteString(line + "\n")
	}
}

// Warn logs at the warn level
func (l *BufferedLogger) Warn(line string) {
	if l.level >= Warn {
		l.buf.WriteString(line + "\n")
	}
}

// Info logs at the info level
func (l *BufferedLogger) Info(line string) {
	if l.level >= Info {
		l.buf.WriteString(line + "\n")
	}
}

// Errorf logs at the error level
func (l *BufferedLogger) Errorf(line string, vals ...interface{}) {
	if l.level >= Error {
		l.buf.WriteString(fmt.Sprintf(line, vals...))
	}
}

// Warnf logs at the warn level
func (l *BufferedLogger) Warnf(line string, vals ...interface{}) {
	if l.level >= Warn {
		l.buf.WriteString(fmt.Sprintf(line, vals...))
	}
}

// Infof logs at the info level
func (l *BufferedLogger) Infof(line string, vals ...interface{}) {
	if l.level >= Info {
		l.buf.WriteString(fmt.Sprintf(line, vals...))
	}
}

// Flush will flush the logger to the provided io.Writer. This could be stdout, stderr, a string builder, etc.
func (l *BufferedLogger) Flush(w io.Writer) (int64, error) {
	return l.buf.WriteTo(w)
}

// String will implement the Stringer interface and also return a copy of the log data as a string
func (l *BufferedLogger) String() string {
	return l.buf.String()
}

// SetLevel will change the level of the logger. This call is not threadsafe - by design it is never called in a location
// where multiple threads would touch it.
func (l *BufferedLogger) SetLevel(level Level) {
	l.level = level
}

// NormalLogger is just a passthrough to calling log.X
// The reason this exists instead of just using the builtin logger as an interface
// is that the Println signature takes a variadic of interfaces{} which i can't easily
// turn into strings for the buffer in the buffered logger. So, it's a little bit of
// fuffery to make things easier for the real purpose of the logger, which is buffering.
type NormalLogger struct {
	level Level
}

// NewNormalLogger returns a new normal logger
func NewNormalLogger(level Level) *NormalLogger {
	return &NormalLogger{
		level: level,
	}
}

// Error logs at the error level
func (l *NormalLogger) Error(line string) {
	if l.level >= Error {
		log.Println(line)
	}
}

// Warn logs at the warn level
func (l *NormalLogger) Warn(line string) {
	if l.level >= Warn {
		log.Println(line)
	}
}

// Info logs at the info level
func (l *NormalLogger) Info(line string) {
	if l.level >= Info {
		log.Println(line)
	}
}

// Errorf logs at the error level
func (l *NormalLogger) Errorf(line string, vals ...interface{}) {
	if l.level >= Error {
		log.Printf(line, vals...)
	}
}

// Warnf logs at the warn level
func (l *NormalLogger) Warnf(line string, vals ...interface{}) {
	if l.level >= Warn {
		log.Printf(line, vals...)
	}
}

// Infof logs at the info level
func (l *NormalLogger) Infof(line string, vals ...interface{}) {
	if l.level >= Info {
		log.Printf(line, vals...)
	}
}

// SetLevel will change the level of the logger. This call is not threadsafe - by design it is never called in a location
// where multiple threads would touch it.
func (l *NormalLogger) SetLevel(level Level) {
	l.level = level
}
