## 🧩 Type of Change
<!-- Choose the type of change -->
- [ ] Feature
- [ ] Bug fix
- [ ] Other

## 🧠 Background & Motivation
<!-- Why is this change needed? What problem or context led to this PR? -->
<!-- Provide a short explanation of the motivation and the problem being solved. -->
<!-- Examples: 
- "Users reported X error when doing Y"
- "New feature X was requested"
-->

## ✨ What Changed
<!-- What was done? Summarize the key changes in this PR. -->
<!-- Describe the core implementation and high-level impact. -->
<!-- Examples:
- "Added new action 'X' to plugin Y"
- "Refactored X to improve performance"
-->

## 🧪 Testing
<!-- Describe how you verified the changes work as intended -->
<!-- Include details of your testing process, such as:
- Unit tests
- Manual testing steps
- Any relevant screenshots or logs
-->

### ✅ Checklist
- [ ] Unit tests added/updated ([generation guide](https://docs.rapid7.com/insightconnect/unit-test-generation) | [writing guide](https://docs.rapid7.com/insightconnect/unit-test-primer))
- [ ] Manually tested in InsightConnect (if applicable)

### 🔍 Plugin Validation

Please run the following commands and provide the output. **For action/trigger tests and runs, include outputs for all actions/triggers that were created or modified in this PR.**

<details>
<summary>Plugin Validation Output (<code>insight-plugin validate</code>)</summary>

```
# Paste output here
```

</details>

<details>
<summary>Connection Test Results (<code>insight-plugin run -T tests/example.json --debug --jq</code>)</summary>

```
# Paste output here for the connection test of the plugin
# It doesn't matter which action/trigger you use, as long as -T flag is specified
```

</details>

<details>
<summary>Action/Trigger Test Results (<code>insight-plugin run -R tests/example.json --debug --jq</code>)</summary>

```
# Paste output here for all created/modified actions/triggers
```

</details>

### 🖼️ In-Product Verification (if applicable)

If you have access to an InsightConnect instance, please provide:
- [ ] Screenshot of job output with the plugin changes
- [ ] Screenshot of the changed connection, actions, or triggers input within the InsightConnect workflow builder

## ✅ Code Quality Checklist

Please review our [style guide](https://docs.rapid7.com/insightconnect/style-guide/) and check all that apply:
- [ ] Dependencies pinned in `Dockerfile` ([OS packages](https://docs.rapid7.com/insightconnect/style-guide/#dockerfile)) and `requirements.txt` ([Python packages](https://docs.rapid7.com/insightconnect/style-guide/#requirements.txt))
- [ ] `USER nobody` set in `Dockerfile` for least privileged account
- [ ] Uses [slim SDK images](https://docs.rapid7.com/insightconnect/sdk-guide/#sdk-guide) when possible (e.g., `rapid7/insightconnect-python-3-slim-plugin:{sdk-version-num}`)
- [ ] Uses [PluginException](https://docs.rapid7.com/insightconnect/error-handling-in-integrations/#plugin-exceptions) / [ConnectionTestException](https://docs.rapid7.com/insightconnect/error-handling-in-integrations#connection-exceptions) for errors
- [ ] Uses `self.logger` for [logging](https://docs.rapid7.com/insightconnect/sdk-guide/#logging)
- [ ] Changelog updated ([style guide](https://docs.rapid7.com/insightconnect/style-guide/#changelog))
- [ ] Work fully completed and functional

## 💬 Additional Notes
<!-- Screenshots, breaking changes, migration notes, or anything else reviewers should know -->

---

**Thanks for contributing! 🎉**
