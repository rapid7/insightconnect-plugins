import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from insightconnect_plugin_runtime.helper import clean
from .schema import Component, Input, NewAdvisoryInput, NewAdvisoryOutput, Output

# Custom imports below
import time
from datetime import datetime, timezone

POLL_INTERVAL_SECONDS = 30
STATE_SEEN_RHSA = "seen_rhsa"
STATE_CURSOR_DAY = "cursor_day"

CSAF_CATEGORY_TO_TYPE = {"csaf_security_advisory": "Security Advisory"}
CSAF_CATEGORY_DEFAULT_TYPE = "Security Advisory"

NOTE_CATEGORIES_ALLOWED = {"summary", "general", "description"}

REFERENCE_DESCRIPTION_BY_CATEGORY = {
    "self": "Advisory link",
    "external": "External reference",
}


class NewAdvisory(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super().__init__(
            name="new_advisory",
            description=Component.DESCRIPTION,
            input=NewAdvisoryInput(),
            output=NewAdvisoryOutput(),
        )

    def run(self, params: dict = {}) -> None:
        include_source = params.get(Input.INCLUDE_SOURCE, False)
        starting_after = params.get(Input.AFTER) or self._utc_today()

        self.load_state()
        cursor_day = self.state.get(STATE_CURSOR_DAY) or starting_after
        seen: set = set(self.state.get(STATE_SEEN_RHSA, []))

        self.logger.info(
            f"Polling Red Hat Security Data API from {cursor_day} "
            f"({len(seen)} advisories already emitted for this day)"
        )

        while self.run_trigger:
            # Snapshot the UTC day BEFORE the request so a midnight rollover mid-batch
            # cannot zero out `seen` while we still hold advisories from the previous day.
            day_at_poll = self._utc_today()

            try:
                advisories = self.connection.client.list_advisories(after=cursor_day)
            except PluginException as error:
                self.logger.error(f"Failed to list advisories: {error}")
                time.sleep(POLL_INTERVAL_SECONDS)
                continue

            released_day_by_rhsa = {
                raw.get("RHSA"): str(raw.get("released_on") or "")[:10] for raw in advisories if raw.get("RHSA")
            }

            for raw_advisory in advisories:
                rhsa = raw_advisory.get("RHSA")
                if not rhsa:
                    self.logger.warning(f"Advisory without RHSA ID; skipping: {raw_advisory}")
                    continue
                if rhsa in seen:
                    continue
                try:
                    advisory = self._process_advisory(raw_advisory, include_source=include_source)
                except Exception as error:
                    # Quarantine the record so we don't retry a poison advisory every poll cycle.
                    # KeyboardInterrupt / SystemExit still propagate because they derive from BaseException.
                    self.logger.error(f"Failed to process advisory {rhsa}: {error}", exc_info=True)
                    seen.add(rhsa)
                    continue
                self.send(clean(advisory))
                seen.add(rhsa)

            if day_at_poll != cursor_day:
                # Drop only RHSAs we can prove were released before the new day. Anything else
                # (unknown release day, missing from this batch, or released on/after day_at_poll)
                # stays in the seen-set — safer to skip a resend than to re-emit duplicates.
                self.logger.info(f"UTC day rolled from {cursor_day} to {day_at_poll}; pruning stale seen-set entries")
                seen = {
                    rhsa
                    for rhsa in seen
                    if not (released_day_by_rhsa.get(rhsa) and released_day_by_rhsa[rhsa] < day_at_poll)
                }
                cursor_day = day_at_poll

            self._persist_state(seen=seen, cursor_day=cursor_day)
            time.sleep(POLL_INTERVAL_SECONDS)

    def _persist_state(self, seen: set, cursor_day: str) -> None:
        self.state[STATE_SEEN_RHSA] = sorted(seen)
        self.state[STATE_CURSOR_DAY] = cursor_day
        if not self.state_file:
            return
        try:
            self._save_state()
        except PluginException as error:
            self.logger.warning(f"Could not persist trigger state: {error}")

    def _process_advisory(self, raw: dict, include_source: bool) -> dict:
        advisory = {
            Output.RHSA: raw.get("RHSA", ""),
            Output.CVES: raw.get("CVEs", []),
            Output.BUGZILLAS: list(dict.fromkeys(raw.get("bugzillas", []))),
            Output.SEVERITY: raw.get("severity"),
            Output.RELEASED_ON: raw.get("released_on"),
            Output.RELEASED_PACKAGES: raw.get("released_packages", []),
            Output.RESOURCE_URL: raw.get("resource_url"),
        }

        if not include_source:
            return advisory

        try:
            source = self.connection.client.get_advisory_document(advisory[Output.RHSA]) or {}
        except PluginException as error:
            self.logger.error(f"Failed to fetch advisory document for {advisory[Output.RHSA]}: {error}")
            return advisory

        document = source.get("document", {}) if isinstance(source, dict) else {}
        if document:
            advisory[Output.TITLE] = document.get("title")
            advisory[Output.TYPE] = CSAF_CATEGORY_TO_TYPE.get(document.get("category"), CSAF_CATEGORY_DEFAULT_TYPE)

            notes = [
                note.get("text", "")
                for note in document.get("notes") or []
                if note.get("category") in NOTE_CATEGORIES_ALLOWED and note.get("text")
            ]
            if notes:
                advisory[Output.NOTES] = "\n".join(notes)

            references = document.get("references") or []
            if references:
                advisory[Output.REFERENCES] = [self._render_reference(ref) for ref in references]
                advisory[Output.URL] = self._pick_advisory_url(references)

            publisher = document.get("publisher") or {}
            if publisher:
                advisory[Output.PUBLISHER] = {
                    "issuing_authority": publisher.get("issuing_authority"),
                    "contact_details": publisher.get("contact_details"),
                    "type": publisher.get("category"),
                }

        advisory[Output.SOURCE] = source
        return advisory

    @staticmethod
    def _render_reference(ref: dict) -> dict:
        url = ref.get("url")
        summary = ref.get("summary")
        category = ref.get("category")
        # Red Hat frequently sets `summary` to the URL itself or a bare Bugzilla ID —
        # substitute a category-based label so `description` carries real information.
        if not summary or summary == url:
            description = REFERENCE_DESCRIPTION_BY_CATEGORY.get(category, "Reference")
        else:
            description = summary
        return {"description": description, "url": url, "type": category}

    @staticmethod
    def _pick_advisory_url(references: list) -> str:
        self_urls = [ref.get("url", "") for ref in references if ref.get("category") == "self"]
        errata_url = next((url for url in self_urls if "/errata/" in url), "")
        return errata_url or (self_urls[0] if self_urls else "")

    @staticmethod
    def _utc_today() -> str:
        return datetime.now(timezone.utc).strftime("%Y-%m-%d")

    def test(self) -> dict:
        try:
            self.connection.client.test_connection()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(
                cause=error.cause,
                assistance=error.assistance,
                data=error.data,
            )
