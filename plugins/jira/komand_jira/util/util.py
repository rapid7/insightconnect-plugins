import logging
import base64
from jira import User
from jira.client import JIRA
from typing import Dict, Any, TYPE_CHECKING
import json

if TYPE_CHECKING:
    from komand_jira.util.api import JiraApi


def normalize_comment(source, is_cloud: bool = False, logger: logging.Logger = logging.getLogger()):
    if not is_cloud:
        comment = source.raw
        author = source.author
    else:
        comment = source
        author = source.get("author", {})

        # If comment body is in ADF format, convert it to plain text
        if body_object := comment.get("body", {}):
            comment["body"] = json.dumps(body_object)

    author = normalize_user(author, is_cloud, logger)
    comment["author"] = author
    return comment


def normalize_issue(  # pylint: disable=too-many-statements
    issue,
    get_attachments=False,
    include_raw_fields=False,
    logger=logging.getLogger(),
    is_cloud: bool = False,
    rest_client: "JiraApi" = None,
) -> Dict[str, Any]:
    if not is_cloud:
        url = issue.permalink().split(" - ", 1)[0]
        resolution = issue.fields.resolution.name if issue.fields.resolution else ""
        reporter = issue.fields.reporter.displayName if issue.fields.reporter else ""
        assignee = issue.fields.assignee.displayName if issue.fields.assignee else ""
        resolution_date = issue.fields.resolutiondate if issue.fields.resolutiondate else ""
        description = issue.fields.description if issue.fields.description else ""
        issue_id = issue.id
        issue_key = issue.key
        summary = issue.fields.summary
        status = issue.fields.status.name
        created_at = issue.fields.created
        updated_at = issue.fields.updated

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
    else:
        # For Jira Cloud API response
        fields = issue.get("fields", {})

        # URL - constructed from self
        url = issue.get("self", "") or ""

        # Summary
        issue_id = issue.get("id", "") or ""
        issue_key = issue.get("key", "") or ""
        summary = fields.get("summary", "") or ""
        created_at = fields.get("created", "") or ""
        updated_at = fields.get("updated", "") or ""

        # Status
        status_object = fields.get("status", {})
        status = status_object.get("name", "") or "" if status_object else ""

        # Resolution
        resolution_object = fields.get("resolution", {})
        resolution = resolution_object.get("name", "") or "" if resolution_object else ""

        # Reporter
        reporter_object = fields.get("reporter", {})
        reporter = reporter_object.get("displayName", "") or "" if reporter_object else ""

        # Assignee
        assignee_object = fields.get("assignee", {})
        assignee = assignee_object.get("displayName", "") or "" if assignee_object else ""

        # Resolution date
        resolution_date = fields.get("resolutiondate", "") or ""

        # Description - in Cloud it's an Atlassian Document Format (ADF) object
        if description_object := fields.get("description", {}):
            # Extract plain text from ADF if needed, or store the whole object
            description = str(description_object)
        else:
            description = ""

        # Labels
        labels = fields.get("labels", [])

        # Fields - raw
        if not include_raw_fields:
            fields = {}

        # Attachments
        attachment = []
        if get_attachments and rest_client:
            attachments = fields.get("attachment", [])
            for file in attachments:
                # In Cloud API, attachment is already a dict with these properties
                if "id" in file:
                    single_attachment = {
                        "filename": file.get("filename", ""),
                        "content": base64.standard_b64encode(
                            rest_client.get_attachment_content(file.get("id", ""))
                        ).decode(),
                    }
                    attachment.append(single_attachment)

    logger.debug(f"Source issue: {issue.raw if not is_cloud else issue}")

    output = {
        "attachments": attachment,
        "id": issue_id,
        "key": issue_key,
        "url": url,
        "summary": summary,
        "description": description,
        "status": status,
        "resolution": resolution,
        "reporter": reporter,
        "assignee": assignee,
        "created_at": created_at,
        "updated_at": updated_at,
        "resolved_at": resolution_date,
        "labels": labels,
    }

    if fields:
        output["fields"] = fields

    logger.debug("Result issue: %s", output)
    return output


def normalize_user(user: User, is_cloud: bool = False, logger: logging.Logger = logging.getLogger()) -> Dict[str, Any]:
    if not is_cloud:
        output = {
            "display_name": user.raw.get("displayName", ""),
            "active": user.raw.get("active", False),
            "email_address": user.raw.get("emailAddress", ""),
        }
        if is_cloud:
            output["account_id"] = user.raw.get("accountId", "")
        else:
            output["name"] = user.raw.get("name", "")
    else:
        output = {
            "display_name": user.get("displayName", ""),
            "active": user.get("active", False),
            "email_address": user.get("emailAddress", ""),
            "account_id": user.get("accountId", ""),
        }
    logger.debug(f"Result user: {output}")
    return output


def look_up_project(
    project_id: str,
    client: JIRA,
    rest_client: "JiraApi",
    logger: logging.Logger = logging.getLogger(),
    is_cloud: bool = False,
) -> bool:
    if not is_cloud:
        project_detail = client.projects()
        project_id_name = list(filter(lambda project: project_id in [project.name, project.key], project_detail))
    else:
        project_id_name = rest_client.get_project(project_id).get("values", [])
        logger.info(project_id_name)
    if project_id_name:
        logger.debug("Project %s exists", project_id)
        return True
    return False


def load_text_as_adf(input_text: str) -> Dict[str, Any]:
    """
    Converts plain text input into a simple Atlassian Document Format (ADF) structure.
    This is a basic implementation and may need to be expanded for more complex formatting.
    """

    try:
        return json.loads(input_text)
    except json.JSONDecodeError:
        # If not, we treat it as plain text and convert to ADF
        return {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": input_text,
                        }
                    ],
                }
            ],
        }
