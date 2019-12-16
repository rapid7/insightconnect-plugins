import komand
from .schema import HuntingInput, HuntingOutput


# Custom imports below


class Hunting(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='hunting',
            description='Looks for exposed secrets in the git commit history and branches',
            input=HuntingInput(),
            output=HuntingOutput())
        self.grr_api = None

    def run(self, params={}):
        self.grr_api = self.connection.grr_api
        flow_name = params.get('flow_name')
        administrative = ["Interrogate", "KeepAlive", "OnlineNotification"]
        browser = ["CacheGrep", "ChromeHistory", "FirefoxHistory"]
        collectors = ["ArtifactCollectorFlow", "DumpACPITable", "DumpFlashImage"]
        filesystem = ["FileFinder", "GetMBR", "ListVolumeShadowCopies"]
        registry = ["CollectRunKeyBinaries", "RegistryFinder"]
        if flow_name in administrative:
            self.administrative(flow_name)
        if flow_name in browser:
            self.brower(flow_name)
        if flow_name == "CheckRunner":
            self.checks(flow_name)
        if flow_name in collectors:
            self.collectors(flow_name)
        if flow_name in filesystem:
            self.filesystem(flow_name)
        if flow_name == "Netstat":
            self.network(flow_name)
        if flow_name == "ListProcesses":
            self.processes(flow_name)
        if flow_name in registry:
            self.registry(flow_name)

    def administrative(self, flow_name, params={}):
        flow_args = self.grr_api.types.CreateFlowArgs(flow_name)
        if flow_name == "Interrogate":
            flow_args.lightweight = True
            self.hunter_args()
        if flow_name == "KeepAlive":
            duration = params.get('duration')
            flow_args.duration = duration
            self.hunter_args()
        if flow_name == "OnlineNotification":
            email = params.get("email")
            flow_args.email = email
            self.hunter_args()

    def browser(self, flow_name, params={}):
        flow_args = self.grr_api.types.CreateFlowArgs(flow_name)
        if flow_name == "CacheGrep":
            check_chrome = params.get('check_chrome')
            check_firefox = params.get('check_firefox')
            data_regex = params.get('data_regex')
            grep_users = params.get('grep_users')
            pathtype = params.get('pathtype')
            if check_chrome:
                flow_args.check_chrome = True
            if check_firefox:
                flow_args.check_firefox = True
            flow_args.path_type = pathtype
            flow_args.data_regex = data_regex
            flow_args.grep_users = grep_users
            self.hunter_args()
        if flow_name == "ChromeHistory":
            get_archive = params.get('get_archive')
            history_path = params.get('history_path')
            path_type = params.get('pathtype')
            username = params.get('username')
            flow_args.get_archive = get_archive
            flow_args.username = username
            flow_args.history_path = history_path
            flow_args.path_type = path_type
            self.hunter_args()
        if flow_name == "FirefoxHistory":
            get_archive = params.get('get_archive')
            history_path = params.get('history_path')
            path_type = params.get('pathtype')
            username = params.get('username')
            flow_args.get_archive = get_archive
            flow_args.username = username
            flow_args.history_path = history_path
            flow_args.path_type = path_type
            self.hunter_args()

    def checks(self, flow_name, params={}):
        flow_args = self.grr_api.types.CreateFlowArgs(flow_name)
        if flow_name == "CheckRunner":
            max_findings = params.get('max_findings')
            only_cpe = params.get('only_cpe')
            only_label = params.get('only_label')
            only_os = params.get('only_os')
            restrict_checks = params.get('restrict_checks')
            flow_args.restrict_checks = restrict_checks
            flow_args.only_os = only_os
            flow_args.only_label = only_label
            flow_args.only_cpe = only_cpe
            flow_args.max_findings = max_findings
            self.hunter_args()

    def collectors(self, flow_name, params={}):
        flow_args = self.grr_api.types.CreateFlowArgs(flow_name)
        if flow_name == "ArtifactCollectorFlow":
            apply_parsers = params.get('apply_parsers')
            artifact_list = params.get('artifact_list')
            dependencies = params.get('dependencies')
            ignore_interpolation_errors = params.get('ignore_interpolation_errors')
            knowledge_base = params.get('knowledge_base')
            max_file_size = params.get('max_file_size')
            on_no_results_error = params.get('on_no_results_error')
            split_output_by_artifact = params.get('split_output_by_artifact')
            use_tsk = params.get('use_tsk')
            if ignore_interpolation_errors:
                flow_args.ignore_interpolation_errors = ignore_interpolation_errors
            if apply_parsers:
                flow_args.apply_parsers = apply_parsers
            if on_no_results_error:
                flow_args.on_no_results_error = on_no_results_error
            if split_output_by_artifact:
                flow_args.split_output_by_artifact = split_output_by_artifact
            if use_tsk:
                flow_args.use_tsk = use_tsk
            flow_args.dependencies = dependencies
            flow_args.artifact_list = artifact_list
            flow_args.knowledge_base = knowledge_base
            flow_args.max_file_size = max_file_size
            self.hunter_args()
        if flow_name == "DumpACPITable":
            component_version = params.get('component_version')
            logging = params.get('logging')
            table_signature_list = params.get('table_signature_list')
            flow_args.component_version = component_version
            flow_args.table_signature_list = table_signature_list
            flow_args.logging = logging
            self.hunter_args()
        if flow_name == "DumpFlashImage":
            chunk_size = params.get('chunk_size')
            component_version = params.get('component_version')
            log_level = params.get('log_level')
            notify_syslog = params.get('notify_syslog')
            if notify_syslog:
                flow_args.notify_syslog = notify_syslog
            flow_args.chunk_size = chunk_size
            flow_args.component_version = component_version
            flow_args.log_level = log_level
            self.hunter_args()

    def filesystem(self, flow_name, params={}):
        if flow_name == 'list_volume_shadow_copies':
            flow_args = self.grr_api.types.CreateFlowArgs(flow_name)
        if flow_name == 'FileFinder':
            flow_args = self.grr_api.types.CreateFlowArgs(flow_name)
            action = params.get('action')
            conditions = params.get('conditions')
            follow_links = params.get('follow_links')
            paths = params.get('paths')
            pathtype = params.get('pathtype')
            process_non_regular_files = params.get('process_non_regular_files')
            xdev = params.get('xdev')
            if action:
                flow_args.action = action
            if conditions:
                flow_args.conditions = conditions
            if follow_links:
                flow_args.follow_links = follow_links
            if paths:
                flow_args.ClearField("paths")
                flow_args.paths.append(paths)
            if pathtype:
                flow_args.pathtype = pathtype
            if process_non_regular_files:
                flow_args.process_non_regular_files = process_non_regular_files
            if xdev:
                flow_args.xdev = xdev
            self.hunter_args()
        if flow_name == 'length':
            length = params.get('length')
            flow_args.ClearField("length")
            flow_args.length.append(length)

    def hunter_args(self, params={}):
        hunt_name = params.get('hunt_name')
        description = params.get('description')
        priority = params.get('priority')
        notification_event = params.get('notification_event')
        queue = params.get('queue')
        cpu_limit = params.get('cpu_limit')
        network_bytes_limit = params.get('network_bytes_limit')
        client_limit = params.get('client_limit')
        expiry_time = params.get('expiry_time')
        client_rate = params.get('client_rate')
        crash_alert_email = params.get('crash_alert_email')
        hunt_runner_args = self.grr_api.types.CreateHuntRunnerArgs()
        if hunt_name:
            hunt_runner_args.hunt_name.append(hunt_name)
        if description:
            hunt_runner_args.description.append(description)
        if priority:
            hunt_runner_args.ClearField("priority")
            hunt_runner_args.priority.append(priority)
        if notification_event:
            hunt_runner_args.notification_event.append(notification_event)
        if queue:
            hunt_runner_args.ClearField("queue")
            hunt_runner_args.queue.append(queue)
        if cpu_limit:
            hunt_runner_args.cpu_limit.append(cpu_limit)
        if network_bytes_limit:
            hunt_runner_args.network_bytes_limit.append(network_bytes_limit)
        if client_limit:
            hunt_runner_args.ClearField("client_limit")
            hunt_runner_args.client_limit.append(client_limit)
        if expiry_time:
            hunt_runner_args.ClearField("expiry_time")
            hunt_runner_args.expiry_time.append(expiry_time)
        if client_rate:
            hunt_runner_args.client_rate.append(client_rate)
        if crash_alert_email:
            hunt_runner_args.ClearField("crash_alert_email")
            hunt_runner_args.crash_alert_email.append(crash_alert_email)
        self.output_plugins(hunt_runner_args)
        rule = self.hunt_runner_args.client_rule_set.rules.add()
        self.foreman(rule)
        rule.rule_type = rule.LABEL

    def foreman(self, rule, params={}):
        pass

    def output_plugins(self, hunt_runner_args, params={}):
        plugin_name = params.get('output_plugin_name')
        output_plugin = hunt_runner_args.output_plugin
        if plugin_name:
            output_plugin.plugin_name = plugin_name
        plugin_args = output_plugin.plugin_args
        if plugin_name == "EmailOutput":
            email_address = params.get('email_address')
            emails_limit = params.get('emails_limit')
            if email_address:
                plugin_args.email_address.append(email_address)
            if emails_limit:
                plugin_args.ClearField("emails_limit")
                plugin_args.emails_limit.append(emails_limit)
        if plugin_name == "BigQueryOutput":
            convert_values = params.get('convert_values')
            export_files_contents = params.get('export_files_contents')
            export_files_hashes = params.get('export_files_hashes')
            follow_urns = params.get('follow_urns')
            annotations = params.get('annotations')
            if convert_values:
                plugin_args.ClearField("convert_values")
                plugin_args.convert_values.append(convert_values)
            if export_files_contents or export_files_hashes or follow_urns or annotations:
                export_options = plugin_args.export_options
                if follow_urns:
                    export_options.ClearField("follow_urns")
                    export_options.follow_urns.append(follow_urns)
                if export_files_contents:
                    export_options.ClearField("export_files_contents")
                    export_options.export_files_contents.append(export_files_contents)
                if export_files_hashes:
                    export_options.ClearField("export_files_hashes")
                    export_options.export_files_hashes.append(export_files_hashes)
                for annotation in annotations:
                    export_options.annotations.append(annotation)
        return hunt_runner_args

    def network(self, flow_name, params={}):
        flow_args = self.grr_api.types.CreateFlowArgs(flow_name)
        listening_only = params.get('listening_only')
        if listening_only:
            flow_args.listening_only = listening_only

    def processes(self, flow_name, params={}):
        flow_args = self.grr_api.types.CreateFlowArgs(flow_name)
        if flow_name == 'list_processes':
            connection_states = params.get('connection_states')
            fetch_binaries = params.get('fetch_binaries')
            filename_regex = params.get('filename_regex')
            if connection_states:
                flow_args.connection_states = connection_states
            if fetch_binaries:
                flow_args.fetch_binaries = fetch_binaries
            if filename_regex:
                flow_args.filename_regex = filename_regex

    def registry(self, flow_name, params={}):
        if flow_name == 'CollectRunKeyBinaries':
            flow_args = self.grr_api.types.CreateFlowArgs(flow_name)
        if flow_name == 'RegistryFinder':
            flow_args = self.grr_api.types.CreateFlowArgs(flow_name)
            conditions = params.get('conditions')
            key_paths = params.get('key_paths')
            if conditions:
                flow_args.conditions = conditions
            if key_paths:
                flow_args.key_paths = key_paths

    def test(self):
        return {}
