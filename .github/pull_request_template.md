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
- [ ] For size, use the [slim SDK images](https://docs.rapid7.com/insightconnect/sdk-guide/#sdk-guide) when possible: ``rapid7/insightconnect-python-3-38-slim-plugin:4`` and ``rapid7/insightconnect-python-3-38-plugin:4``
- [ ] For error handling, use of [PluginException](https://docs.rapid7.com/insightconnect/error-handling-in-integrations/#plugin-exceptions) and [ConnectionTestException](https://docs.rapid7.com/insightconnect/error-handling-in-integrations#connection-exceptions)
- [ ] For logging, use [self.logger](https://docs.rapid7.com/insightconnect/sdk-guide/#logging)
- [ ] For docs, use [changelog style](https://docs.rapid7.com/insightconnect/style-guide/#changelog)
- [ ] For docs, validate markdown with ``insight-plugin validate`` which calls ``icon_validate`` to lint ``help.md``

### Functional Checklist
- [ ] Work fully completed
- [ ] Functional
  - [ ] Any new actions/triggers include JSON [test files](https://docs.rapid7.com/insightconnect/style-guide/#tests) in the `tests/` directory created with `insight-plugin samples`
  - [ ] Tests should all pass unless it's a negative test. Negative tests have a naming convention of `tests/$action_bad.json`
  - [ ] Unsuccessful tests should fail by raising an exception causing the plugin to die and an object should be returned on successful test
  - [ ] Add functioning test results to PR, sanitize any output if necessary
    * Single action/trigger `insight-plugin run -T tests/example.json --debug --jq`
    * All actions/triggers shortcut `insight-plugin run -T all --debug --jq` (use PR format at end)
  - [ ] Add functioning run results to PR, sanitize any output if necessary
    * Single action/trigger `insight-plugin run -R tests/example.json --debug --jq`
    * All actions/triggers shortcut `insight-plugin run --debug --jq` (use PR format at end)

### Assessment

You must validate your work to reviewers:

1. Run `insight-plugin validate` and make sure everything passes
2. Run the assessment tool: `insight-plugin run -A`. For single action validation: `insight-plugin run tests/{file}.json -A`
3. Copy (`insight-plugin ... | pbcopy`) and paste the output in **a new post** on this PR
4. Add required screenshots from the In-Product Tests section
