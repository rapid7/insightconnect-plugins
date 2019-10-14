package actions

// Code generated by the Komand Go SDK Generator. DO NOT EDIT

// LaunchCompliancePolicyReportInputOutputFormatPdf is an enumerated value
const LaunchCompliancePolicyReportInputOutputFormatPdf = "pdf"

// LaunchCompliancePolicyReportInputOutputFormatHTML is an enumerated value
const LaunchCompliancePolicyReportInputOutputFormatHTML = "html"

// LaunchCompliancePolicyReportInputOutputFormatMht is an enumerated value
const LaunchCompliancePolicyReportInputOutputFormatMht = "mht"

// LaunchCompliancePolicyReportInputOutputFormatXML is an enumerated value
const LaunchCompliancePolicyReportInputOutputFormatXML = "xml"

// LaunchCompliancePolicyReportInputOutputFormatCsv is an enumerated value
const LaunchCompliancePolicyReportInputOutputFormatCsv = "csv"

// LaunchCompliancePolicyReportInput is the input for LaunchCompliancePolicyReport
type LaunchCompliancePolicyReportInput struct {
	AssetGroupIds string `json:"asset_group_ids"`
	HostID        int    `json:"host_id"`
	Instance      string `json:"instance"`
	Ips           string `json:"ips"`
	OutputFormat  string `json:"output_format"`
	PolicyID      int    `json:"policy_id"`
	ReportRefs    string `json:"report_refs"`
	TemplateID    int    `json:"template_id"`
	Title         string `json:"title"`
}

// LaunchCompliancePolicyReportOutput is the output for LaunchCompliancePolicyReport
type LaunchCompliancePolicyReportOutput struct {
	ID int `json:"id"`
}

// LaunchCompliancePolicyReportAction is an action the plugin can take
type LaunchCompliancePolicyReportAction struct{}
