package actions

// Code generated by the Komand Go SDK Generator. DO NOT EDIT

// FilepathExtractorInput is the input for FilepathExtractor
type FilepathExtractorInput struct {
	File []byte `json:"file"`
	Str  string `json:"str"`
}

// FilepathExtractorOutput is the output for FilepathExtractor
type FilepathExtractorOutput struct {
	Filepaths []string `json:"filepaths"`
}

// FilepathExtractorAction is an action the plugin can take
type FilepathExtractorAction struct{}
