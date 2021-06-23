## Proposed Changes

### Description

Describe the proposed changes:

  -

## PR Requirements

Developers, verify you have completed the following items by checking them off:

### Testing

#### Unit Tests

Review our documentation on [generating](https://docs.rapid7.com/insightconnect/unit-test-generation) and [writing](https://docs.rapid7.com/insightconnect/unit-test-primer) plugin unit tests

- [ ] Unit tests written for any new or updated code

#### In-Product Tests

If you are an InsightConnect customer or have access to an InsightConnect instance, the following in-product tests should be done:

- [ ] Screenshot of job output with the plugin changes
- [ ] Screenshot of the changed connection, actions, or triggers input within the InsightConnect workflow builder

### Style

Review the [style guide](https://docs.rapid7.com/insightconnect/style-guide/)

- [ ] For dependencies, pin [OS package](https://docs.rapid7.com/insightconnect/style-guide/#dockerfile) and [Python package](https://docs.rapid7.com/insightconnect/style-guide/#requirements.txt) versions
- [ ] For security, set least privileged account with ``USER nobody`` in the ``Dockerfile`` when possible
- [ ] For size, use the [slim SDK images](https://docs.rapid7.com/insightconnect/sdk-guide/#sdk-guide) when possible: ``komand/python-3-37-slim-plugin`` and ``komand/python-3-37-plugin``
- [ ] For error handling, use of [PluginException](https://docs.rapid7.com/insightconnect/error-handling-in-integrations/#plugin-exceptions) and [ConnectionTestException](https://docs.rapid7.com/insightconnect/error-handling-in-integrations#connection-exceptions)
- [ ] For logging, use [self.logger](https://docs.rapid7.com/insightconnect/sdk-guide/#logging)
- [ ] For docs, use [changelog style](https://docs.rapid7.com/insightconnect/style-guide/#changelog)
- [ ] For docs, validate markdown with ``make validate`` which calls ``mdl`` to lint ``help.md``

### Functional Checklist
- [ ] Work fully completed
- [ ] Functional
  - [ ] Any new actions/triggers include JSON [test files](https://docs.rapid7.com/insightconnect/style-guide/#tests) in the `tests/` directory created with `icon-plugin run -c sample $action > tests/$action.json`
  - [ ] Tests should all pass unless it's a negative test. Negative tests have a naming convention of `tests/$action_bad.json`
  - [ ] Unsuccessful tests should fail by raising an exception causing the plugin to die and an object should be returned on successful test
  - [ ] Add functioning test results to PR, sanitize any output if necessary
    * Single action/trigger `icon-plugin run -T tests/example.json --debug --jq`
    * All actions/triggers shortcut `icon-plugin run -T all --debug --jq` (use PR format at end)
  - [ ] Add functioning run results to PR, sanitize any output if necessary
    * Single action/trigger `icon-plugin run -R tests/example.json --debug --jq`
    * All actions/triggers shortcut `icon-plugin run -R all --debug --jq` (use PR format at end)

### Assessment

You must validate your work to reviewers:

1. Run `make validate` and make sure everything passes
2. Run the assessment tool: `icon-plugin run -A -R all -T all`. For single action validation: `icon-plugin run -A -R tests/my_action.json -T tests/my_action.json`
3. Copy (`icon-plugin ... | pbcopy`) and paste the output in **a new post** on this PR
4. Add required screenshots from the In-Product Tests section
