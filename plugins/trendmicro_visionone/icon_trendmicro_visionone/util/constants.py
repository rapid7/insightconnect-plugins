import pytmv1

RESPONSE_MAPPING = {
    pytmv1.TaskAction.COLLECT_FILE.value: pytmv1.CollectFileTaskResp,
    pytmv1.TaskAction.ISOLATE_ENDPOINT.value: pytmv1.EndpointTaskResp,
    pytmv1.TaskAction.RESTORE_ENDPOINT.value: pytmv1.EndpointTaskResp,
    pytmv1.TaskAction.TERMINATE_PROCESS.value: pytmv1.TerminateProcessTaskResp,
    pytmv1.TaskAction.QUARANTINE_MESSAGE.value: pytmv1.EmailMessageTaskResp,
    pytmv1.TaskAction.DELETE_MESSAGE.value: pytmv1.EmailMessageTaskResp,
    pytmv1.TaskAction.RESTORE_MESSAGE.value: pytmv1.EmailMessageTaskResp,
    pytmv1.TaskAction.BLOCK_SUSPICIOUS.value: pytmv1.BlockListTaskResp,
    pytmv1.TaskAction.REMOVE_SUSPICIOUS.value: pytmv1.BlockListTaskResp,
    pytmv1.TaskAction.RESET_PASSWORD.value: pytmv1.AccountTaskResp,
    pytmv1.TaskAction.SUBMIT_SANDBOX.value: pytmv1.SandboxSubmissionStatusResp,
    pytmv1.TaskAction.ENABLE_ACCOUNT.value: pytmv1.AccountTaskResp,
    pytmv1.TaskAction.DISABLE_ACCOUNT.value: pytmv1.AccountTaskResp,
    pytmv1.TaskAction.FORCE_SIGN_OUT.value: pytmv1.AccountTaskResp,
}
