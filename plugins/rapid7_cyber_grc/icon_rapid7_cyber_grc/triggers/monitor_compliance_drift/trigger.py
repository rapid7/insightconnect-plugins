import insightconnect_plugin_runtime
import time
from .schema import MonitorComplianceDriftInput, MonitorComplianceDriftOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException

from ...util.compliance import framework_scores, number

# The previous scores are kept in the SDK's trigger state (self.state), which the runtime
# loads from the plugin cache before run() starts and which survives the container
# restarting. Without it the first poll after a restart has no baseline to measure a
# fall against.
STATE_KEY = "scores"

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

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        control_set_id = params.get(Input.CONTROL_SET_ID)
        drop_threshold = params.get(Input.DROP_THRESHOLD)
        interval = params.get(Input.INTERVAL)
        minimum_compliance = params.get(Input.MINIMUM_COMPLIANCE)
        # END INPUT BINDING - DO NOT REMOVE

        while self.run_trigger:
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

    def _load(self):
        stored = self.state.get(STATE_KEY)
        # A missing or malformed baseline costs one poll with no baseline, which is far
        # better than the trigger refusing to start.
        return stored if isinstance(stored, dict) else {}

    def _save(self, frameworks):
        self.state[STATE_KEY] = {
            str(framework["control_set_id"]): {
                "compliance": framework["compliance"],
                "automated_controls_percentage": framework["automated_controls_percentage"],
            }
            for framework in frameworks
        }
        if not self.state_file:
            # The runtime only gives a trigger a state file when it knows the trigger ID.
            self.logger.warning("Could not persist the compliance scores: this trigger has no state file")
            return
        try:
            self._save_state()
        except Exception as error:  # A lost baseline only costs the next poll, so keep polling.
            self.logger.warning(f"Could not persist the compliance scores: {error}")
