import insightconnect_plugin_runtime
import time
from .schema import MonitorComplianceDriftInput, MonitorComplianceDriftOutput, Input, Output, Component

# Custom imports below
import json
import os
from insightconnect_plugin_runtime.exceptions import PluginException
from pathlib import Path
from tempfile import gettempdir

from ...util.compliance import framework_scores, number

CACHE_FILE = "monitor_compliance_drift_cache.json"
# The directory the Dockerfile creates for the plugin cache, which InsightConnect backs
# with a volume that outlives the container because the plugin sets enable_cache. A score
# stored in the temporary directory instead would be lost whenever the container is
# rescheduled, and the first poll after that cannot report a fall it has no baseline for.
CACHE_DIR = Path("/workspace/cache")

DROP = "Drop"
BELOW_MINIMUM = "Below Minimum"


class MonitorComplianceDrift(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_compliance_drift",
            description=Component.DESCRIPTION,
            input=MonitorComplianceDriftInput(),
            output=MonitorComplianceDriftOutput(),
        )
        self.cache_path = self._cache_dir() / CACHE_FILE

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        control_set_id = params.get(Input.CONTROL_SET_ID)
        drop_threshold = params.get(Input.DROP_THRESHOLD)
        interval = params.get(Input.INTERVAL)
        minimum_compliance = params.get(Input.MINIMUM_COMPLIANCE)
        # END INPUT BINDING - DO NOT REMOVE

        self.logger.info(f"Storing the previous compliance scores in {self.cache_path}")

        while True:
            try:
                frameworks, unscored = framework_scores(self.connection.client, control_set_id)
            except PluginException as error:
                # A trigger that raises stops polling for good, and a rate limit or a
                # restart of the API should not take the workflow down with it. The
                # stored scores mean the next successful poll still has its baseline.
                self.logger.error(
                    f"Reading the compliance scores failed, retrying in {abs(interval)} seconds. "
                    f"{error.cause} {error.assistance}"
                )
                time.sleep(abs(interval))
                continue

            if unscored:
                self.logger.info(
                    f"{len(unscored)} control set(s) have no scores in Cyber GRC yet and cannot be watched: "
                    f"{', '.join(str(set_id) for set_id in unscored)}"
                )

            previous = self._load()
            drifts = self._drifts(frameworks, previous, abs(drop_threshold), abs(minimum_compliance))
            self._save(frameworks)

            if drifts:
                self.logger.info(f"Emitting {len(drifts)} framework(s) whose compliance score has fallen")
                self.send({Output.DRIFTS: drifts, Output.COUNT: len(drifts)})
            else:
                self.logger.info(f"No compliance drift across {len(frameworks)} framework(s)")

            time.sleep(abs(interval))

    def _drifts(self, frameworks, previous, drop_threshold, minimum_compliance):
        """The frameworks worth waking a workflow for, worst fall first."""
        drifts = []
        for framework in frameworks:
            was = previous.get(str(framework["control_set_id"]))
            # With no stored score there is no fall to measure, so treat the current
            # score as the baseline. That leaves the floor as the only thing that can
            # report on the first poll, which is what stops a fresh trigger from
            # announcing every framework it has just learned about.
            before = number(was.get("compliance")) if was else framework["compliance"]
            change = round(framework["compliance"] - before, 4)

            if was and change < 0 and -change >= drop_threshold:
                reason = DROP
            elif (
                minimum_compliance
                and framework["compliance"] < minimum_compliance
                # Only on the way past the floor. A framework parked below it would
                # otherwise be reported again on every single poll, for ever.
                and (not was or before >= minimum_compliance)
            ):
                reason = BELOW_MINIMUM
            else:
                continue

            drifts.append(
                {
                    "control_set_id": framework["control_set_id"],
                    "name": framework["name"],
                    "reason": reason,
                    "previous_compliance": before,
                    "current_compliance": framework["compliance"],
                    "compliance_change": change,
                    "previous_automated_controls_percentage": (
                        number(was.get("automated_controls_percentage"))
                        if was
                        else framework["automated_controls_percentage"]
                    ),
                    "current_automated_controls_percentage": framework["automated_controls_percentage"],
                    "date_calculated": framework["date_calculated"],
                }
            )

        return sorted(drifts, key=lambda drift: drift["compliance_change"])

    @staticmethod
    def _cache_dir():
        """The persistent cache directory, falling back to a temporary one.

        The fallback matters when the trigger runs outside the plugin container, such as
        under the unit tests, where /workspace/cache does not exist.
        """
        if CACHE_DIR.is_dir() and os.access(CACHE_DIR, os.W_OK):
            return CACHE_DIR
        return Path(gettempdir())  # nosec

    def _load(self):
        try:
            stored = json.loads(self.cache_path.read_text())
        except (OSError, ValueError):
            # An unreadable or corrupt cache costs one poll with no baseline, which is
            # far better than the trigger refusing to start.
            return {}
        return stored if isinstance(stored, dict) else {}

    def _save(self, frameworks):
        cache = {
            str(framework["control_set_id"]): {
                "compliance": framework["compliance"],
                "automated_controls_percentage": framework["automated_controls_percentage"],
            }
            for framework in frameworks
        }
        try:
            self.cache_path.write_text(json.dumps(cache))
        except OSError as error:
            # A lost cache only costs the next poll its baseline, so keep polling.
            self.logger.warning(f"Could not persist the compliance scores: {error}")
