import logging
import base64
from insightconnect_plugin_runtime.exceptions import PluginException


def normalize_comment(source, is_cloud=False, logger=logging.getLogger()):
    comment = source.raw
    author = normalize_user(source.author, is_cloud, logger)
    comment["author"] = author
    return comment


def normalize_issue(issue, get_attachments=False, include_raw_fields=False, logger=logging.getLogger()):
    url = issue.permalink().split(" - ", 1)[0]

    resolution = issue.fields.resolution.name if issue.fields.resolution else ""
    reporter = issue.fields.reporter.displayName if issue.fields.reporter else ""
    assignee = issue.fields.assignee.displayName if issue.fields.assignee else ""
    resolution_date = issue.fields.resolutiondate if issue.fields.resolutiondate else ""
    description = issue.fields.description if issue.fields.description else ""

    try:
        labels = issue.fields.labels
    except AttributeError:
        labels = []

    fields = {}
    if include_raw_fields:
        fields = issue.raw["fields"]

    attachment = []
    if get_attachments:
        try:
            attachments = issue.fields.attachment
        except AttributeError:
            attachments = []
        for file in attachments:
            single_attachment = {
                "filename": file.filename,
                "content": base64.standard_b64encode(file.get()).decode(),
            }
            attachment.append(single_attachment)

    logger.debug("Source issue: %s", issue.raw)

    output = {
        "attachments": attachment,
        "id": issue.id,
        "key": issue.key,
        "url": url,
        "summary": issue.fields.summary,
        "description": description,
        "status": issue.fields.status.name,
        "resolution": resolution,
        "reporter": reporter,
        "assignee": assignee,
        "created_at": issue.fields.created,
        "updated_at": issue.fields.updated,
        "resolved_at": resolution_date,
        "labels": labels,
        "fields": fields,
    }

    logger.debug("Result issue: %s", output)

    return output


def normalize_user(user, is_cloud=False, logger=logging.getLogger()):
    output = {
        "display_name": user.displayName,
        "active": user.active,
        "email_address": user.emailAddress,
    }
    if is_cloud:
        output["account_id"] = user.accountId
    else:
        output["name"] = user.name

    logger.debug("Result user: %s", output)

    return output


def look_up_project(_id, client, logger=logging.getLogger()):
    project_detail = client.projects()
    project_id_name = list(filter(lambda x: x.name is _id or x.key is _id, project_detail))

    if project_id_name:
        logger.debug("Project %s exists", project_id_name)
        return True
    return False
