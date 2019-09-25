import logging


def normalize_comment(source, logger=logging.getLogger()):
    comment = source.raw
    author = normalize_user(source.author, logger=logger)
    comment["author"] = author
    return comment


def normalize_issue(issue, include_raw_fields=False, logger=logging.getLogger()):

    url = issue.permalink().split(" - ", 1)[0]

    if issue.fields.resolution:
        resolution = issue.fields.resolution.name
    else:
        resolution = ""

    if issue.fields.reporter:
        reporter = issue.fields.reporter.displayName
    else:
        reporter = ""

    if issue.fields.assignee:
        assignee = issue.fields.assignee.displayName
    else:
        assignee = ""

    if issue.fields.resolutiondate:
        resolution_date = issue.fields.resolutiondate
    else:
        resolution_date = ""

    fields = {}
    if include_raw_fields:
        fields = issue.raw["fields"]

    attachment = []
    for a in issue:
        file = a.get()
        single_attachment = {'filename': a.filename,'content': file}
        attachment.append(single_attachment)

    logger.debug("Source issue: %s", issue.raw)

    output = {
        "id": issue.id,
        "key": issue.key,
        "url": url,
        "summary": issue.fields.summary,
        "description": issue.fields.description,
        "status": issue.fields.status.name,
        "resolution": resolution,
        "reporter": reporter,
        "assignee": assignee,
        "created_at": issue.fields.created,
        "updated_at": issue.fields.updated,
        "resolved_at": resolution_date,
        "labels": issue.fields.labels or [],
        "fields": fields,
        "attachment": attachment
    }

    logger.debug("Result issue: %s", output)

    return output


def normalize_user(user, logger=logging.getLogger()):
    output = {
        "name": user.name,
        "email_address": user.emailAddress,
        "display_name": user.displayName,
        "active": user.active,
    }

    logger.debug("Result user: %s", output)

    return output
