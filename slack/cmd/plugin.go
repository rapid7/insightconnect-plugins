package main

import (
	"os"

	"github.com/komand/plugin-sdk-go/plugin"

	"slack/triggers"

	"slack/actions"
)

var (
	// Name plugin name
	Name = "Slack"
	// Vendor plugin vendor
	Vendor = "komand"
	// Version plugin version
	Version = "0.2.0"
	// Description plugin description
	Description = "Slack integrations"
)

// Slack is the Slack Plugin type
type Slack struct {
	plugin.Plugin
}

// New creates a new Slack plugin
func New() *Slack {
	i := &Slack{}
	i.Init(plugin.Meta{
		Name:        Name,
		Vendor:      Vendor,
		Version:     Version,
		Description: Description,
	})

	// triggers

	i.AddTrigger(&triggers.SlackEventTrigger{})

	i.AddTrigger(&triggers.SlackMessageTrigger{})

	i.AddTrigger(&triggers.SlackMessageWithFileTrigger{})

	// actions

	i.AddAction(&actions.SlackDisableAction{})

	i.AddAction(&actions.SlackEnableAction{})

	i.AddAction(&actions.SlackPostMessageAction{})

	i.AddAction(&actions.SlackSearchAction{})

	i.AddAction(&actions.SlackUploadFileAction{})
	i.AddAction(&actions.SlackUploadSnippetAction{})
	return i
}

func main() {
	cli := plugin.CLI(New(), os.Args[1:])
	cli.Run()
}
