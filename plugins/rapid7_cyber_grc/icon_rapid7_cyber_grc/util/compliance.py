# ControlSetMetrics keeps every calculation rather than overwriting the last one, so a
# control set has one row per run and only the newest carries the current score.
SORT_KEY = "dateCalculated"


def framework_scores(client, control_set_id=None):
    """Current compliance scores per framework, newest calculation first.

    Returns the scores and the IDs of the control sets that are in use but have never
    been scored, which is a state a caller usually wants to report rather than hide.

    An explicitly named control set is scored whatever its state: the caller asked for
    that one. Otherwise a retired framework would count towards a score for a framework
    nobody is being measured against any more.
    """
    # The action's Control Set ID defaults to 0, which means every framework in use.
    wanted_id = control_set_id or None

    # The control sets come first because they name each framework and say which are
    # still in use, and because the number of them bounds the work that follows.
    control_sets = client.list_records("ControlSets", select="id,name,enabled,isArchived")
    wanted = [
        record
        for record in control_sets
        if record.get("id") == wanted_id
        or (wanted_id is None and record.get("enabled") and not record.get("isArchived"))
    ]

    frameworks, unscored = [], []
    for control_set in wanted:
        metric = _newest_metric(client, control_set.get("id"))
        if not metric:
            unscored.append(control_set.get("id"))
            continue
        frameworks.append(
            {
                "control_set_id": control_set.get("id"),
                "name": control_set.get("name", ""),
                "compliance": number(metric.get("compliance")),
                "linked_controls_percentage": number(metric.get("linkedControlsPercentage")),
                "automated_controls_percentage": number(metric.get("automatedControlsPercentage")),
                "date_calculated": metric.get(SORT_KEY, ""),
            }
        )

    return frameworks, sorted(unscored)


def _newest_metric(client, control_set_id):
    """The most recent scoring of one control set, or None if it has never been scored.

    Asking per control set, for one row, is what keeps this affordable. The collection
    holds every calculation ever made for every framework: reading it whole meant paging
    tens of thousands of rows to use a handful of them, which on a tenant with real
    scoring history exhausts the API's rate limit before the read finishes.
    """
    metrics = client.list_records(
        "ControlSetMetrics",
        filter_=f"controlSetID eq {control_set_id}",
        order_by=f"{SORT_KEY} desc",
        top=1,
    )
    return metrics[0] if metrics else None


def number(value):
    """A score as a float, treating an absent or unreadable one as zero."""
    try:
        return round(float(value), 2)
    except (TypeError, ValueError):
        return 0.0
