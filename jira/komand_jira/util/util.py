import logging
import base64
from io import BytesIO
from komand.exceptions import PluginException


def normalize_comment(source, logger=logging.getLogger()):
    comment = source.raw
    author = normalize_user(source.author, logger=logger)
    comment["author"] = author
    return comment


def normalize_issue(issue, get_attachments=False, include_raw_fields=False, logger=logging.getLogger()):
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

    if issue.fields.description:
        description = issue.fields.description
    else:
        description = ""

    fields = {}
    if include_raw_fields:
        fields = issue.raw["fields"]

    attachment = []
    if get_attachments:
        for a in issue.fields.attachment:
            single_attachment = {'filename': a.filename, 'content': base64.standard_b64encode(a.get()).decode()}
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
        "labels": issue.fields.labels or [],
        "fields": fields,
    }

    logger.debug("Result issue: %s", output)

    return output


def normalize_user(user, is_cloud = False, logger=logging.getLogger()):
    output = {
        "display_name": user.displayName,
        "active": user.active,
        "email_address": user.emailAddress
    }
    if is_cloud:
        output["account_id"] = user.accountId
    else:
        output["name"] = user.name

    logger.debug("Result user: %s", output)

    return output


def look_up_project(_id, client, logger=logging.getLogger()):
    project_detail = client.projects()
    project_id_name = list(filter(lambda x: x.name == _id or x.key == _id, project_detail))

    if project_id_name:
        logger.debug("Project %s exists", project_id_name)
        return True
    return False


def add_attachment(connection, logger, issue, filename, file_bytes):
    try:
        data = base64.b64decode(file_bytes)
    except Exception as e:
        raise PluginException(cause='Unable to decode attachment bytes.',
                              assistance=f"Please provide a valid attachment bytes. Error: {str(e)}")
    attachment = BytesIO()
    attachment.write(data)
    output = connection.client.add_attachment(
        issue=issue,
        attachment=attachment,
        filename=filename)
    logger.debug('Attach issue has returned: %s', output)
    return output
