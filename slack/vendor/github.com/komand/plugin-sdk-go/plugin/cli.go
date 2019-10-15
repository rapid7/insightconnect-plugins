package plugin

import (
	"fmt"
	"log"
	"strings"

	ansi "github.com/mgutz/ansi"

	kingpin "gopkg.in/alecthomas/kingpin.v2"
)

var (
	lime  = ansi.ColorCode("green+h:black")
	red   = ansi.ColorCode("red")
	green = ansi.ColorCode("green")
	reset = ansi.ColorCode("reset")
)

type debuggable interface {
	SetDebugLog(string) error
	SetDebug()
}

type sampleable interface {
	SampleStartMessage(string) (string, error)
}

type cli struct {
	Args   []string
	Plugin Pluginable
}

// CLI for plugins.
func CLI(plugin Pluginable, args []string) *cli {
	return &cli{Args: args, Plugin: plugin}
}

func (c *cli) info() {
	fmt.Println(c.description())
}

func (c *cli) description() string {
	result := "\n"
	result += fmt.Sprintf("Name:        %s%s%s\n", green, c.Plugin.Name(), reset)
	result += fmt.Sprintf("Vendor:      %s%s%s\n", green, c.Plugin.Vendor(), reset)
	result += fmt.Sprintf("Version:     %s%s%s\n", green, c.Plugin.Version(), reset)
	result += fmt.Sprintf("Description: %s%s%s\n", green, c.Plugin.Description(), reset)

	if len(c.Plugin.Triggers()) > 0 {
		result += fmt.Sprintf("\n")
		result += fmt.Sprintf("Triggers (%s%d%s): \n", green, len(c.Plugin.Triggers()), reset)
		for name, item := range c.Plugin.Triggers() {
			result += fmt.Sprintf("└── %s%s%s (%s%s)\n", green, name, reset, item.Description(), reset)
		}
	}

	if len(c.Plugin.Actions()) > 0 {

		result += fmt.Sprintf("\n")
		result += fmt.Sprintf("Actions (%s%d%s): \n", green, len(c.Plugin.Actions()), reset)
		for name, item := range c.Plugin.Actions() {
			result += fmt.Sprintf("└── %s%s%s (%s%s)\n", green, name, reset, item.Description(), reset)
		}
	}
	return result
}

func (c *cli) sample(name string) {
	if sampler, ok := c.Plugin.(sampleable); ok {
		msg, err := sampler.SampleStartMessage(name)
		if err != nil {
			log.Fatalf("Unable to generate a sample: %s", err)
		} else {
			fmt.Println(msg)
		}
	}
}

// Run the CLI
func (c *cli) Run() {

	plugin := c.Plugin
	app := kingpin.New(c.Plugin.Name(), c.Plugin.Description())
	app.Version(c.Plugin.Version())

	debug := app.Flag("debug", "Log events to stdout").Bool()

	test := app.Command("test", "Run a test using the start message on stdin.")
	info := app.Command("info", "Display plugin info (triggers and actions).")
	sample := app.Command("sample", "Show a sample start message for the provided trigger or action.")
	sampleOpt := sample.Arg("trigger or action", "Trigger or action name to generate sample message for.").Required().String()
	run := app.Command("run", "Run the plugin (default command). You must supply the start message on stdin.")

	for i, argv := range c.Args {
		if argv == "--" {
			c.Args = c.Args[0:(i)]
			break
		}
	}

	if len(c.Args) < 1 || (len(c.Args) == 1 && strings.HasSuffix(c.Args[0], "debug")) {
		c.Args = append(c.Args, "run")
	}

	args, err := app.Parse(c.Args)

	if *debug {
		if dbgable, ok := plugin.(debuggable); ok {
			dbgable.SetDebug()
		}
	}

	switch kingpin.MustParse(args, err) {

	case sample.FullCommand():
		c.sample(*sampleOpt)
	case info.FullCommand():
		c.info()
	case run.FullCommand():
		if err := plugin.Run(); err != nil {
			log.Fatalf("Run failed: %v", err)
		}
	case test.FullCommand():
		if err := plugin.Test(); err != nil {
			log.Fatalf("Test failed: %v", err)
		}
	default:
		if err := plugin.Run(); err != nil {
			log.Fatalf("Unable to execute: %s", err)
		}

	}
}
