# Contributing

Thank you for your interest in joining the InsightConnect developer community!! Please review our [Code of Conduct] before making contributions.

There are multiple ways to contribute beyond writing code. These include:

- [Submit bugs and feature requests] with detailed information about your issue or idea.
- [Help fellow users with open issues] or [help fellow committers test recent pull requests].
- [Report a security vulnerability in InsightConnect's plugins] to Rapid7.
- Submit an updated or brand new plugin!  We are always eager for new
  integrations or features. Don't know where to start? Check out the [developer documentation].

Here is a short list of dos and don'ts to make sure *your* valuable contributions actually make
it into production.  If you do not care to follow these rules, your contribution **will** be rejected. Sorry!

## Code Contributions

- **Do** read the [developer documentation]
- **Do** install [pre-commit](https://pre-commit.com/) to ensure your style is [Black](https://github.com/psf/black).
- **Do** stick to our [plugin style] guides.
- **Do** follow the [50/72 rule] for Git commit messages.
- **Do** license your code as MIT.
- **Do** create a [topic branch] to work on. This helps ensure users are aware of commits on the branch being considered for merge, allows for a location for more commits to be offered without mingling with other contributor changes, and allows contributors to make progress while a PR is still being reviewed.

### Pull Requests

- **Do** write "WIP" on your PR and/or open a [draft PR] if submitting unfinished code.
- **Do** target your pull request to the **master branch**.
- **Do** specify a descriptive title to make searching for your pull request easier e.g. "Okta: add Suspend User action".
- **Do** include [console output], especially the JSON output for new features and bug fixes.
- **Do** list [verification steps] so your tests are reproducible.
- **Do** [reference associated issues] in your pull request description.
- **Don't** leave your pull request description blank.
- **Don't** abandon your pull request. Being responsive helps us land your code faster.

#### Using the Contributor PR Template (External Contributors)

**If you're contributing from a fork**, please use our specialized contributor template that includes additional validation sections. Here's how:

1. When you click "Compare & Pull request" on GitHub after pushing your changes, you'll see a URL like:
   ```
   https://github.com/rapid7/insightconnect-plugins/compare/master...your-username:your-branch
   ```

2. Before clicking "Create pull request", add `?template=contrib.md` to the end of the URL:
   ```
   https://github.com/rapid7/insightconnect-plugins/compare/master...your-username:your-branch?template=contrib.md
   ```

3. Press Enter to reload the page with the contributor template pre-filled.

This template includes sections for plugin validation outputs, connection tests, and code quality checklists that help us review external contributions more efficiently.

#### New Features

- **Do** install validator dependencies necessary to run `make validate` to find and fix any errors or warnings that come up.
- **Do** include documentation showing sample run-throughs.
- **Don't** include more than one plugin per pull request.

#### Bug Fixes

- **Do** include reproduction steps in the form of [verification steps].
- **Do** link to any corresponding [Issues] in the format of `See #1234` in your commit description.

## Bug Reports

Please report vulnerabilities in Rapid7 software directly to security@rapid7.com.
For more on our disclosure policy and Rapid7's approach to coordinated disclosure, [head over here](https://www.rapid7.com/security).

When reporting issues:

- **Do** write a detailed description of your bug and use a descriptive title.
- **Do** include reproduction steps, stack traces, and anything that might help us fix your bug.
- **Don't** file duplicate reports; search for your bug before filing a new report.

If you have general requests or need additional guidance, reach out to the open source contribution owners at
`IntegrationAlliance@rapid7.com`.

Finally, **thank you** for taking the few moments to read this far! You're already way ahead of the
curve, so keep it up!

[Code of Conduct]:./CODE_OF_CONDUCT.md
[developer documentation]:https://docs.rapid7.com/insightconnect/getting-started/
[Submit bugs and feature requests]:https://github.com/rapid7/insightconnect-plugins/issues
[Report a security vulnerability in InsightConnect itself or its plugins]:https://www.rapid7.com/disclosure.jsp
[Help fellow users with open issues]:https://github.com/rapid7/insightconnect-plugins/issues
[help fellow committers test recent pull requests]:https://github.com/rapid7/insightconnect-plugins/pulls
[Python PEP8]:https://www.python.org/dev/peps/pep-0008/
[plugin style]:https://docs.rapid7.com/insightconnect/style-guide/
[50/72 rule]:http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html
[Report a security vulnerability in Metasploit itself]:https://www.rapid7.com/disclosure.jsp
[topic branch]:http://git-scm.com/book/en/Git-Branching-Branching-Workflows#Topic-Branches
[draft PR]:https://help.github.com/en/articles/about-pull-requests#draft-pull-requests
[console output]:https://help.github.com/articles/github-flavored-markdown#fenced-code-blocks
[verification steps]:https://help.github.com/articles/writing-on-github#task-lists
[reference associated issues]:https://github.com/blog/1506-closing-issues-via-pull-requests
[Issues]:https://github.com/rapid7/insightconnect-plugins/issues
