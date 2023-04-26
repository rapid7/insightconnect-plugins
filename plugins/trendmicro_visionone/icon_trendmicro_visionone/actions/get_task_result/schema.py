# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieves an object containing the results of a response task in JSON format"


class Input:
    POLL = "poll"
    POLL_TIME_SEC = "poll_time_sec"
    TASK_ID = "task_id"
    

class Output:
    ACCOUNT = "account"
    ACTION = "action"
    AGENT_GUID = "agent_guid"
    CREATED_DATE_TIME = "created_date_time"
    DESCRIPTION = "description"
    ENDPOINT_NAME = "endpoint_name"
    EXPIRED_DATE_TIME = "expired_date_time"
    FILE_PATH = "file_path"
    FILE_SHA1 = "file_sha1"
    FILE_SHA256 = "file_sha256"
    FILE_SIZE = "file_size"
    FILENAME = "filename"
    ID = "id"
    IMAGE_PATH = "image_path"
    LAST_ACTION_DATE_TIME = "last_action_date_time"
    PASSWORD = "password"
    PID = "pid"
    RESOURCE_LOCATION = "resource_location"
    SANDBOX_TASK_ID = "sandbox_task_id"
    STATUS = "status"
    TASKS = "tasks"
    URL = "url"
    

class GetTaskResultInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "poll": {
      "type": "boolean",
      "title": "Poll",
      "description": "If script should wait until the task is finished before returning the result (enabled by default)",
      "order": 2
    },
    "poll_time_sec": {
      "type": "number",
      "title": "Poll Time In Seconds",
      "description": "Maximum time to wait for the result to be available",
      "order": 3
    },
    "task_id": {
      "type": "string",
      "title": "Task ID",
      "description": "taskId output from the collect command used to collect the file",
      "order": 1
    }
  },
  "required": [
    "poll",
    "task_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetTaskResultOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "account": {
      "type": "string",
      "title": "Account",
      "description": "User that triggered the response",
      "order": 7
    },
    "action": {
      "type": "string",
      "title": "Action",
      "description": "Command sent to the target",
      "enum": [
        "isolate",
        "restoreIsolate",
        "collectFile",
        "terminateProcess",
        "quarantineMessage",
        "restoreMessage",
        "deleteMessage",
        "block",
        "restoreBlock",
        "remoteShell",
        "runInvestigationKit",
        "runCustomScript",
        "submitSandbox",
        "dumpProcessMemory",
        "disableAccount",
        "enableAccount",
        "forceSignOut",
        "resetPassword"
      ],
      "order": 6
    },
    "agent_guid": {
      "type": "string",
      "title": "Agent GUID",
      "description": "Unique alphanumeric string that identifies an installed agent",
      "order": 8
    },
    "created_date_time": {
      "type": "string",
      "title": "Created Date Time",
      "description": "Timestamp in ISO 8601 format",
      "order": 2
    },
    "description": {
      "type": "string",
      "title": "Description",
      "description": "Task Description",
      "order": 5
    },
    "endpoint_name": {
      "type": "string",
      "title": "Endpoint Name",
      "description": "Endpoint name of the target endpoint",
      "order": 9
    },
    "expired_date_time": {
      "type": "string",
      "title": "Expired Date Time",
      "description": "The expiration date and time of the file",
      "order": 15
    },
    "file_path": {
      "type": "string",
      "title": "File Path",
      "description": "File path for the file that was collected",
      "order": 10
    },
    "file_sha1": {
      "type": "string",
      "title": "File SHA1",
      "description": "the fileSHA1 of the collected file",
      "order": 11
    },
    "file_sha256": {
      "type": "string",
      "title": "File SHA256",
      "description": "The fileSHA256 of the collected file",
      "order": 12
    },
    "file_size": {
      "type": "integer",
      "title": "File Size",
      "description": "The file size of the file collected",
      "order": 13
    },
    "filename": {
      "type": "string",
      "title": "Filename",
      "description": "File name of a response task target (\\u003c= 255)",
      "order": 17
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "Unique numeric string that identifies a response task",
      "order": 3
    },
    "image_path": {
      "type": "string",
      "title": "Image Path",
      "description": "File path of a process image",
      "order": 22
    },
    "last_action_date_time": {
      "type": "string",
      "title": "Last Action Date Time",
      "description": "Timestamp in ISO 8601 format",
      "order": 4
    },
    "password": {
      "type": "string",
      "title": "Password",
      "description": "The password of the file collected",
      "order": 16
    },
    "pid": {
      "type": "integer",
      "title": "PID",
      "description": "Unique numeric string that identifies an active process",
      "order": 21
    },
    "resource_location": {
      "type": "string",
      "title": "Resource Location",
      "description": "URL location of the file collected that can be used to download",
      "order": 14
    },
    "sandbox_task_id": {
      "type": "string",
      "title": "Sandbox Task ID",
      "description": "Unique alphanumeric string that identifies a task generated by the Sandbox Analysis App",
      "order": 20
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "The status of the command sent to the managing server. Possible task statuses; queued - The server queued the command due to a high volume of requests or because the Security Agent was offline; running - Trend Micro Vision One sent the command to the managing server and is waiting for a response; succeeded - The managing server successfully received the command; rejected - The server rejected the task. For automated response task only; waitForApproval - The task is pending approval. For automated response task only; failed - An error or time-out occurred when attempting to send the command to the managing server",
      "enum": [
        "queued",
        "running",
        "succeeded",
        "rejected",
        "waitForApproval",
        "failed"
      ],
      "order": 1
    },
    "tasks": {
      "type": "array",
      "title": "Tasks",
      "description": "Currently, it is only possible to apply tasks to one message in a mailbox or one message in several mailboxes",
      "items": {
        "type": "object"
      },
      "order": 18
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "Universal Resource Locator",
      "order": 19
    }
  },
  "required": [
    "action",
    "created_date_time",
    "last_action_date_time",
    "status"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
