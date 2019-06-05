## Proposed Changes

Describe the proposed changes:

  -

## PR Requirements

Developers, verify you have completed the following items by checking them off:

### Functional Checklist
- [ ] Work fully completed
- [ ] Functional
  - [ ] Any new actions/triggers include JSON [test files](https://komand.github.io/python/style.html#tests) in the `tests/` directory created with `./run -c sample $action > tests/$action.json`
  - [ ] Tests should all pass unless it's a negative test. Negative tests have a naming convention of `tests/$action_bad.json`
  - [ ] Unsuccessful tests should fail by raising an exception causing the plugin to die and an object should be returned on successful test
  - [ ] Add functioning test results to PR, sanitize any output if necessary
    * Single action/trigger `./run -T tests/example.json -d -j`
    * All actions/triggers shortcut `./run -T all -d -j` (use PR format at end)
  - [ ] Add functioning run results to PR, sanitize any output if necessary
    * Single action/trigger `./run -R tests/example.json -d -j`
    * All actions/triggers shortcut `./run -R all -d -j` (use PR format at end)

### Assessment

You must validate your work to reviewers:

1. Run `make validate` and make sure everything passes
2. Run the assessment tool: `./run -A -R all -T all`. For single action validation: `./run -A -R tests/my_action.json -T tests/my_action.json`
3. Copy (`./run ... | pbcopy`) and paste the output in **a new post** on this PR.
4. Add UI screenshot of the workflow used for testing
5. Add UI screenshot of the job output used for testing
6. Add UI screenshot of the artifact (See rules in UI Checklist) used for testing
