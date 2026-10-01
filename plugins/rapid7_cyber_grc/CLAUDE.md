# Claude rules — Rapid7 Cyber GRC plugin

## Vendor name (reserved during testing)

`rapid7` is a **reserved vendor name** in InsightConnect (SOAR). A plugin tarball
whose `vendor` is `rapid7` **cannot be imported** into an InsightConnect instance
for testing — the UI rejects the upload with:

> Unable to upload. "rapid7 is a reserved vendor name, please reference this
> request ID when contacting support: ..."

### Rule
- **Keep `vendor: rapid7` committed** in `plugin.spec.yaml`. That is the merge-ready
  value, and keeping it committed avoids a stale `.CHECKSUM` (`insight-plugin` records
  a hash of the spec).
- **Do NOT hand-edit `vendor` for testing.** The vendor is rewritten automatically at
  **export time**. Build the test tarball with:

  ```sh
  make test-export
  # or override the placeholder:
  make test-export TEST_VENDOR=myname
  ```

  `test-export` temporarily rewrites `vendor:` to `$(TEST_VENDOR)` (default
  `rapid7lab`), builds and saves the image under that vendor, then restores the
  original spec — even if the build fails. It refuses to run with `TEST_VENDOR=rapid7`.

  Output: `./<TEST_VENDOR>_rapid7_cyber_grc_<version>.tar` — import this into SOAR.

### Why it matters
`vendor` in `plugin.spec.yaml` drives the Docker image tag (`<vendor>/<name>`), the
tarball name, and the exported `.tar` (see `Makefile`: `VENDOR`, `TEST_VENDOR`, `PKG`).
So the `vendor` value baked into the image at build time determines whether the
resulting tar is importable for testing.

### Merge-ready builds
- Use `make export` (uses committed `vendor: rapid7`) for the final artifact.
- Do not commit any built `.tar` (they are gitignored).

Note: `support: rapid7` is unrelated metadata and is not affected by this rule.
