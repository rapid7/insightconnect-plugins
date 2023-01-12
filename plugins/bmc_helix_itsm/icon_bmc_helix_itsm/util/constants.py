class IncidentRequest:
    FIRST_NAME = "First_Name"
    LAST_NAME = "Last_Name"
    DESCRIPTION = "Description"
    IMPACT = "Impact"
    URGENCY = "Urgency"
    STATUS = "Status"
    REPORTED_SOURCE = "Reported Source"
    SERVICE_TYPE = "Service_Type"
    INSTANCE_ID = "InstanceId"
    ENTRY_ID = "Entry ID"
    STATUS_REASON = "Status_Reason"
    RESOLUTION = "Resolution"


class ProblemRequest:
    SITE_GROUP = "Site Group"
    REGION = "Region"
    SITE = "Site"
    DESCRIPTION = "Description"
    COMPANY = "Company"
    LAST_NAME = "Last Name"
    FIRST_NAME = "First Name"
    URGENCY = "Urgency"
    IMPACT = "Impact"
    INVESTIGATION_DRIVER = "Investigation Driver"
    COORDINATOR_SUPPORT_COMPANY = "Support Company Pblm Mgr"
    COORDINATOR_SUPPORT_ORGANIZATION = "Support Organization Pblm Mgr"
    COORDINATOR_GROUP = "Support Group Name Requester"
    COORDINATOR = "Problem Manager Login"
    ASSIGNEE_SUPPORT_COMPANY = "Assigned Support Company"
    ASSIGNEE_SUPPORT_ORGANIZATION = "Assigned Support Organization"
    ASSIGNEE_GROUP = "Assigned Group Pblm Mgr"
    ASSIGNEE = "Assignee Pblm Mgr"
    Z1D_ACTION = "z1D_Action"


class TaskRequest:
    SUMMARY = "Summary"
    ROOT_REQUEST_INSTANCE_ID = "RootRequestInstanceID"
    ROOT_REQUEST_NAME = "RootRequestName"
    ROOT_REQUEST_FORM_NAME = "RootRequestFormName"
    ROOT_REQUEST_MODE = "RootRequestMode"
    NOTES = "Notes"
    TASK_TYPE = "TaskType"
    TASK_NAME = "TaskName"
    PRIORITY = "Priority"
    LOCATION_COMPANY = "Location Company"


class BmcResponse:
    LOCATION = "Location"
    VALUES = "values"


class IncidentResponse(BmcResponse):
    ENTRIES = "entries"
    INCIDENT_NUMBER = "Incident Number"
    ENTRY_ID = "Entry ID"
    LINKS = "_links"
    WORKLOG_LINKS = "assoc-HPD:INC:Worklog"
    WORKLOG_LINK_HREF = "href"
    WORKLOG_VALUES = "values"


class TaskResponse(BmcResponse):
    TASK_ID = "Task ID"


class ProblemResponse(BmcResponse):
    PROBLEM_ID = "Problem Investigation ID"


class Parameters:
    def get_all_parameters(self):
        return [
            getattr(self, name)
            for name in dir(self)
            if not name.startswith("_") and isinstance(getattr(self, name), str)
        ]


class Incident(Parameters):
    ENTRY_ID = "Entry ID"
    SUBMITTER = "Submitter"
    SUBMIT_DATE = "Submit Date"
    ASSIGNEE = "Assignee"
    ASSIGNED_GROUP = "Assigned Group"
    ASSIGNED_SUPPORT_COMPANY = "Assigned Support Company"
    ASSIGNED_ORGANIZATION_COMPANY = "Assigned Support Organization"
    OWNER = "Owner"
    OWNER_GROUP = "Owner Group"
    OWNER_SUPPORT_COMPANY = "Owner Support Company"
    OWNER_ORGANIZATION_COMPANY = "Owner Support Organization"
    LAST_MODIFIED_BY = "Last Modified By"
    LAST_MODIFIED_DATE = "Last Modified Date"
    LAST_RESOLVED_DATE = "Last Resolved Date"
    CLOSED_DATE = "Closed Date"
    STATUS = "Status"
    STATUS_REASON = "Status_Reason"
    STATUS_HISTORY = "Status History"
    DESCRIPTION = "Description"
    RESOLUTION = "Resolution"
    INCIDENT_NUMBER = "Incident Number"
    URGENCY = "Urgency"
    IMPACT = "Impact"
    PRIORITY = "Priority"
    REPORTED_SOURCE = "Reported Source"
    REPORTED_DATE = "Reported Date"
    TIME_ZONE = "Time Zone"
    STATUS_REASON = "Status_Reason"


class Worklog(Parameters):
    WORK_LOG_ID = "Work Log ID"
    SUBMITTER = "Submitter"
    SUBMIT_DATE = "Submit Date"
    ASSIGNED_TO = "Assigned To"
    LAST_MODIFIED_BY = "Last Modified By"
    LAST_MODIFIED_DATE = "Last Modified Date"
    STATUS = "Status"
    DESCRIPTION = "Description"
    WORK_LOG_SUBMIT_DATE = "Work Log Submit Date"
    WORK_LOG_SUBMITTER = "Work Log Submitter"
    INCIDENT_NUMBER = "Incident Number"
    WORK_LOG_TYPE = "Work Log Type"
    VIEW_ACCESS = "View Access"
    SECURE_WORK_LOG = "Secure Work Log"
    WORK_LOG_DATE = "Work Log Date"
    WORK_LOG_ACTION_STATUS = "WorkLog Action Status"
    ASSIGN_WORK_LOG_FLAG = "Assign WorkLog Flag"
    WORK_LOG_ACTION_COMPLETED = "WorkLog Action Completed"


class IncidentStatus(Parameters):
    RESOLVED = "Resolved"
    PENDING = "Pending"
