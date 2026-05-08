# Description

Leverage Anthropic's Claude AI models to assist with security analysis, incident summarization, IOC analysis, and natural language processing tasks in SOC workflows

# Key Features

* Send prompts to Claude for security analysis and investigation assistance
* Analyze indicators of compromise with AI-powered context
* Summarize lengthy security alerts, logs, and reports
* Count tokens to manage API usage and costs

# Requirements

* Anthropic API key from https://console.anthropic.com

# Supported Product Versions

* 2025-05-07 Claude API v1

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|Anthropic API key|None|sk-ant-api03-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|None|None|
|model|string|claude-sonnet-4-6|True|Claude model to use for requests. If the specified model is unavailable or invalid, the plugin will fall back to the latest available Sonnet model|None|claude-sonnet-4-6|claude-sonnet-4-6|Enter any valid Claude model ID from https://docs.anthropic.com/en/docs/about-claude/models. The plugin will fall back to claude-sonnet-4-6 if the specified model is unavailable.|

Example input:

```
{
  "api_key": "sk-ant-api03-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "model": "claude-sonnet-4-6"
}
```

## Technical Details

### Actions


#### Analyze IOCs

This action is used to submit indicators of compromise to Claude for AI-powered analysis including context, risk 
assessment, and recommended actions

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|context|string|None|False|Additional context about where these IOCs were observed|None|Found in email attachment from unknown sender targeting finance department|Describe where these IOCs were found...|Providing context helps Claude give more relevant analysis|
|indicators|[]string|None|True|List of indicators of compromise to analyze (IPs, domains, hashes, URLs, email addresses)|None|["192.168.1.100", "evil-domain.com", "44d88612fea8a8f36de82e1278abb02f"]|None|None|
|max_tokens|integer|4096|False|Maximum number of tokens to generate in the response|None|4096|None|None|
  
Example input:

```
{
  "context": "Found in email attachment from unknown sender targeting finance department",
  "indicators": [
    "192.168.1.100",
    "evil-domain.com",
    "44d88612fea8a8f36de82e1278abb02f"
  ],
  "max_tokens": 4096
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|analysis|string|True|Claude's analysis of the provided IOCs|IOC Analysis: 192.168.1.100 is a private IP address. evil-domain.com is suspicious.|
|model|string|True|The model used for the analysis|claude-sonnet-4-6|
|usage|object|False|Token usage information|{'input_tokens': 156, 'output_tokens': 203}|
  
Example output:

```
{
  "analysis": "IOC Analysis: 192.168.1.100 is a private IP address. evil-domain.com is suspicious.",
  "model": "claude-sonnet-4-6",
  "usage": {
    "input_tokens": 156,
    "output_tokens": 203
  }
}
```

#### Count Tokens

This action is used to count the number of tokens in a message before sending it to Claude. Useful for managing API 
costs and ensuring messages fit within model limits

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|prompt|string|None|True|The message content to count tokens for|None|Analyze this log file for suspicious activity...|Enter the text to count tokens for...|None|
|system_prompt|string|None|False|Optional system prompt to include in the token count|None|You are a security analyst|None|None|
  
Example input:

```
{
  "prompt": "Analyze this log file for suspicious activity...",
  "system_prompt": "You are a security analyst"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|input_tokens|integer|True|The number of input tokens in the message|18|
  
Example output:

```
{
  "input_tokens": 18
}
```

#### Send Prompt

This action is used to send a message to Claude and receive a response. Use this for freeform security analysis, 
investigation assistance, or any natural language task

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|max_tokens|integer|4096|False|Maximum number of tokens to generate in the response|None|4096|None|None|
|prompt|string|None|True|The message to send to Claude|None|Analyze this suspicious email header and identify potential indicators of phishing|Enter your prompt for Claude...|None|
|system_prompt|string|None|False|Optional system prompt to set context for Claude's response|None|You are a senior SOC analyst specializing in phishing detection|You are a security analyst...|Sets the persona and context for Claude. Use this to focus responses on security analysis|
  
Example input:

```
{
  "max_tokens": 4096,
  "prompt": "Analyze this suspicious email header and identify potential indicators of phishing",
  "system_prompt": "You are a senior SOC analyst specializing in phishing detection"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|model|string|True|The model used for the response|claude-sonnet-4-6|
|response|string|True|Claude's response text|Based on the email headers provided, I've identified several indicators of phishing.|
|usage|object|False|Token usage information|{'input_tokens': 42, 'output_tokens': 87}|
  
Example output:

```
{
  "model": "claude-sonnet-4-6",
  "response": "Based on the email headers provided, I've identified several indicators of phishing.",
  "usage": {
    "input_tokens": 42,
    "output_tokens": 87
  }
}
```

#### Summarize Text

This action is used to summarize lengthy security content such as alerts, incident reports, threat intelligence, or log
 data into concise actionable summaries

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|focus|string|None|False|What aspect to focus the summary on|["key findings and recommended actions", "timeline of events", "affected systems and users", "indicators of compromise", "executive summary", ""]|key findings and recommended actions|e.g., key findings, timeline, affected systems...|Guides Claude to emphasize specific aspects in the summary|
|max_tokens|integer|2048|False|Maximum number of tokens to generate in the response|None|2048|None|None|
|text|string|None|True|The text content to summarize|None|Multiple failed login attempts detected from IP 10.0.0.5 targeting user accounts...|Paste the text to summarize...|None|
  
Example input:

```
{
  "focus": "key findings and recommended actions",
  "max_tokens": 2048,
  "text": "Multiple failed login attempts detected from IP 10.0.0.5 targeting user accounts..."
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|model|string|True|The model used for the summary|claude-sonnet-4-6|
|summary|string|True|The summarized text|Key Findings: Multiple failed login attempts from IP 10.0.0.5 targeting 15 user accounts.|
|usage|object|False|Token usage information|{'input_tokens': 89, 'output_tokens': 112}|
  
Example output:

```
{
  "model": "claude-sonnet-4-6",
  "summary": "Key Findings: Multiple failed login attempts from IP 10.0.0.5 targeting 15 user accounts.",
  "usage": {
    "input_tokens": 89,
    "output_tokens": 112
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 1.0.0 - Initial plugin release

# Links

* [Anthropic](https://www.anthropic.com)

## References

* [Claude API Docs](https://platform.claude.com/docs/en/home)