import pytmv1

RESPONSE_MAPPING = {
    pytmv1.TaskAction.COLLECT_FILE.value[0]: pytmv1.CollectFileTaskResp,
    pytmv1.TaskAction.ISOLATE_ENDPOINT.value[0]: pytmv1.EndpointTaskResp,
    pytmv1.TaskAction.RESTORE_ENDPOINT.value[0]: pytmv1.EndpointTaskResp,
    pytmv1.TaskAction.TERMINATE_PROCESS.value[0]: pytmv1.TerminateProcessTaskResp,
    pytmv1.TaskAction.QUARANTINE_MESSAGE.value[0]: pytmv1.EmailMessageTaskResp,
    pytmv1.TaskAction.DELETE_MESSAGE.value[0]: pytmv1.EmailMessageTaskResp,
    pytmv1.TaskAction.RESTORE_MESSAGE.value[0]: pytmv1.EmailMessageTaskResp,
    pytmv1.TaskAction.BLOCK_SUSPICIOUS.value[0]: pytmv1.BlockListTaskResp,
    pytmv1.TaskAction.REMOVE_SUSPICIOUS.value[0]: pytmv1.BlockListTaskResp,
    pytmv1.TaskAction.RESET_PASSWORD.value[0]: pytmv1.AccountTaskResp,
    pytmv1.TaskAction.SUBMIT_SANDBOX.value[0]: pytmv1.SandboxSubmitUrlTaskResp,
    pytmv1.TaskAction.ENABLE_ACCOUNT.value[0]: pytmv1.AccountTaskResp,
    pytmv1.TaskAction.DISABLE_ACCOUNT.value[0]: pytmv1.AccountTaskResp,
    pytmv1.TaskAction.FORCE_SIGN_OUT.value[0]: pytmv1.AccountTaskResp,
}
