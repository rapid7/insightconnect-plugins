package plugin

// Actionable must be implemented by Actions to work with Plugins
type Actionable interface {
	Act() error          // Act will run the action.
	Name() string        // Name is the name of the action
	Description() string // Description describes the action
}

// Action defines a struct that should be embedded within any
// implemented Action.
type Action struct{}
