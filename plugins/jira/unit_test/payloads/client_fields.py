client_fields = [
{'id': 'statuscategorychangedate', 'key': 'statuscategorychangedate', 'name': 'Status Category Changed',
 'custom': False, 'orderable': False, 'navigable': True, 'searchable': True,
 'clauseNames': ['statusCategoryChangedDate'],
 'schema': {'type': 'datetime', 'system': 'statuscategorychangedate'}},
{'id': 'issuetype', 'key': 'issuetype', 'name': 'Issue Type', 'custom': False, 'orderable': True, 'navigable': True,
 'searchable': True, 'clauseNames': ['issuetype', 'type'], 'schema': {'type': 'issuetype', 'system': 'issuetype'}},
{'id': 'parent', 'key': 'parent', 'name': 'Parent', 'custom': False, 'orderable': False, 'navigable': True,
 'searchable': False, 'clauseNames': ['parent']},
{'id': 'timespent', 'key': 'timespent', 'name': 'Time Spent', 'custom': False, 'orderable': False,
 'navigable': True, 'searchable': False, 'clauseNames': ['timespent'],
 'schema': {'type': 'number', 'system': 'timespent'}},
{'id': 'project', 'key': 'project', 'name': 'Project', 'custom': False, 'orderable': False, 'navigable': True,
 'searchable': True, 'clauseNames': ['project'], 'schema': {'type': 'project', 'system': 'project'}},
{'id': 'customfield_10032', 'key': 'customfield_10032', 'name': 'Satisfaction', 'untranslatedName': 'Satisfaction',
 'custom': True, 'orderable': True, 'navigable': True, 'searchable': True,
 'clauseNames': ['cf[10032]', 'Satisfaction'],
 'schema': {'type': 'sd-feedback', 'custom': 'com.atlassian.servicedesk:sd-request-feedback', 'customId': 10032}},
{'id': 'fixVersions', 'key': 'fixVersions', 'name': 'Fix versions', 'custom': False, 'orderable': True,
 'navigable': True, 'searchable': True, 'clauseNames': ['fixVersion'],
 'schema': {'type': 'array', 'items': 'version', 'system': 'fixVersions'}},
{'id': 'customfield_10033', 'key': 'customfield_10033', 'name': 'Resolution', 'untranslatedName': 'Resolution',
 'custom': True, 'orderable': True, 'navigable': True, 'searchable': True,
 'clauseNames': ['cf[10033]', 'Resolution[Short text]'], 'scope': {'type': 'PROJECT', 'project': {'id': '10013'}},
 'schema': {'type': 'string', 'custom': 'com.atlassian.jira.plugin.system.customfieldtypes:textfield',
            'customId': 10033}},
{'id': 'aggregatetimespent', 'key': 'aggregatetimespent', 'name': 'Σ Time Spent', 'custom': False,
 'orderable': False, 'navigable': True, 'searchable': False, 'clauseNames': [],
 'schema': {'type': 'number', 'system': 'aggregatetimespent'}},
{'id': 'statusCategory', 'key': 'statusCategory', 'name': 'Status Category', 'custom': False, 'orderable': False,
 'navigable': True, 'searchable': True, 'clauseNames': ['statusCategory']},
{'id': 'customfield_10034', 'key': 'customfield_10034', 'name': 'Comment', 'untranslatedName': 'Comment',
 'custom': True, 'orderable': True, 'navigable': True, 'searchable': True,
 'clauseNames': ['cf[10034]', 'Comment[Short text]'], 'scope': {'type': 'PROJECT', 'project': {'id': '10013'}},
 'schema': {'type': 'string', 'custom': 'com.atlassian.jira.plugin.system.customfieldtypes:textfield',
            'customId': 10034}},
{'id': 'resolution', 'key': 'resolution', 'name': 'Resolution', 'custom': False, 'orderable': True,
 'navigable': True, 'searchable': True, 'clauseNames': ['resolution'],
 'schema': {'type': 'resolution', 'system': 'resolution'}},
{'id': 'customfield_10037', 'key': 'customfield_10037', 'name': 'Story Point', 'untranslatedName': 'Story Point',
 'custom': True, 'orderable': True, 'navigable': True, 'searchable': True,
 'clauseNames': ['cf[10037]', 'Story Point', 'Story Point[Short text]'],
 'scope': {'type': 'PROJECT', 'project': {'id': '10015'}},
 'schema': {'type': 'string', 'custom': 'com.atlassian.jira.plugin.system.customfieldtypes:textfield',
            'customId': 10037}},
{'id': 'customfield_10027', 'key': 'customfield_10027', 'name': 'Request participants',
 'untranslatedName': 'Request participants', 'custom': True, 'orderable': True, 'navigable': True,
 'searchable': True, 'clauseNames': ['cf[10027]', 'Request participants'],
 'schema': {'type': 'array', 'items': 'user', 'custom': 'com.atlassian.servicedesk:sd-request-participants',
            'customId': 10027}},
{'id': 'customfield_10028', 'key': 'customfield_10028', 'name': 'Story point estimate',
 'untranslatedName': 'Story point estimate', 'custom': True, 'orderable': True, 'navigable': True,
 'searchable': True, 'clauseNames': ['cf[10028]', 'Story point estimate'],
 'schema': {'type': 'number', 'custom': 'com.pyxis.greenhopper.jira:jsw-story-points', 'customId': 10028}},
{'id': 'customfield_10029', 'key': 'customfield_10029', 'name': 'Issue color', 'untranslatedName': 'Issue color',
 'custom': True, 'orderable': True, 'navigable': True, 'searchable': True,
 'clauseNames': ['cf[10029]', 'Issue color'],
 'schema': {'type': 'string', 'custom': 'com.pyxis.greenhopper.jira:jsw-issue-color', 'customId': 10029}},
{'id': 'resolutiondate', 'key': 'resolutiondate', 'name': 'Resolved', 'custom': False, 'orderable': False,
 'navigable': True, 'searchable': True, 'clauseNames': ['resolutiondate', 'resolved'],
 'schema': {'type': 'datetime', 'system': 'resolutiondate'}},
{'id': 'workratio', 'key': 'workratio', 'name': 'Work Ratio', 'custom': False, 'orderable': False,
 'navigable': True, 'searchable': True, 'clauseNames': ['workratio'],
 'schema': {'type': 'number', 'system': 'workratio'}},
{'id': 'issuerestriction', 'key': 'issuerestriction', 'name': 'Restrict to', 'custom': False, 'orderable': True,
 'navigable': False, 'searchable': True, 'clauseNames': [],
 'schema': {'type': 'issuerestriction', 'system': 'issuerestriction'}},
{'id': 'lastViewed', 'key': 'lastViewed', 'name': 'Last Viewed', 'custom': False, 'orderable': False,
 'navigable': True, 'searchable': False, 'clauseNames': ['lastViewed'],
 'schema': {'type': 'datetime', 'system': 'lastViewed'}},
{'id': 'watches', 'key': 'watches', 'name': 'Watchers', 'custom': False, 'orderable': False, 'navigable': True,
 'searchable': False, 'clauseNames': ['watchers'], 'schema': {'type': 'watches', 'system': 'watches'}},
{'id': 'thumbnail', 'key': 'thumbnail', 'name': 'Images', 'custom': False, 'orderable': False, 'navigable': True,
 'searchable': False, 'clauseNames': []},
{'id': 'created', 'key': 'created', 'name': 'Created', 'custom': False, 'orderable': False, 'navigable': True,
 'searchable': True, 'clauseNames': ['created', 'createdDate'],
 'schema': {'type': 'datetime', 'system': 'created'}},
{'id': 'priority', 'key': 'priority', 'name': 'Priority', 'custom': False, 'orderable': True, 'navigable': True,
 'searchable': True, 'clauseNames': ['priority'], 'schema': {'type': 'priority', 'system': 'priority'}},
{'id': 'customfield_10025', 'key': 'customfield_10025', 'name': 'Start date', 'untranslatedName': 'Start date',
 'custom': True, 'orderable': True, 'navigable': True, 'searchable': True,
 'clauseNames': ['cf[10025]', 'Start date', 'Start date[Date]'],
 'schema': {'type': 'date', 'custom': 'com.atlassian.jira.plugin.system.customfieldtypes:datepicker',
            'customId': 10025}},
{'id': 'labels', 'key': 'labels', 'name': 'Labels', 'custom': False, 'orderable': True, 'navigable': True,
 'searchable': True, 'clauseNames': ['labels'], 'schema': {'type': 'array', 'items': 'string', 'system': 'labels'}},
{'id': 'customfield_10026', 'key': 'customfield_10026', 'name': 'Request Type', 'untranslatedName': 'Request Type',
 'custom': True, 'orderable': True, 'navigable': True, 'searchable': True,
 'clauseNames': ['cf[10026]', 'Request Type'],
 'schema': {'type': 'sd-customerrequesttype', 'custom': 'com.atlassian.servicedesk:vp-origin', 'customId': 10026}},
{'id': 'customfield_10018', 'key': 'customfield_10018', 'name': 'Flagged', 'untranslatedName': 'Flagged',
 'custom': True, 'orderable': True, 'navigable': True, 'searchable': True,
 'clauseNames': ['cf[10018]', 'Flagged', 'Flagged[Checkboxes]'], 'schema': {'type': 'array', 'items': 'option',
                                                                            'custom': 'com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes',
                                                                            'customId': 10018}},
{'id': 'timeestimate', 'key': 'timeestimate', 'name': 'Remaining Estimate', 'custom': False, 'orderable': False,
 'navigable': True, 'searchable': False, 'clauseNames': ['remainingEstimate', 'timeestimate'],
 'schema': {'type': 'number', 'system': 'timeestimate'}},
{'id': 'aggregatetimeoriginalestimate', 'key': 'aggregatetimeoriginalestimate', 'name': 'Σ Original Estimate',
 'custom': False, 'orderable': False, 'navigable': True, 'searchable': False, 'clauseNames': [],
 'schema': {'type': 'number', 'system': 'aggregatetimeoriginalestimate'}},
{'id': 'versions', 'key': 'versions', 'name': 'Affects versions', 'custom': False, 'orderable': True,
 'navigable': True, 'searchable': True, 'clauseNames': ['affectedVersion'],
 'schema': {'type': 'array', 'items': 'version', 'system': 'versions'}},
{'id': 'issuelinks', 'key': 'issuelinks', 'name': 'Linked Issues', 'custom': False, 'orderable': True,
 'navigable': True, 'searchable': True, 'clauseNames': ['issueLink'],
 'schema': {'type': 'array', 'items': 'issuelinks', 'system': 'issuelinks'}},
{'id': 'assignee', 'key': 'assignee', 'name': 'Assignee', 'custom': False, 'orderable': True, 'navigable': True,
 'searchable': True, 'clauseNames': ['assignee'], 'schema': {'type': 'user', 'system': 'assignee'}},
{'id': 'updated', 'key': 'updated', 'name': 'Updated', 'custom': False, 'orderable': False, 'navigable': True,
 'searchable': True, 'clauseNames': ['updated', 'updatedDate'],
 'schema': {'type': 'datetime', 'system': 'updated'}},
{'id': 'status', 'key': 'status', 'name': 'Status', 'custom': False, 'orderable': False, 'navigable': True,
 'searchable': True, 'clauseNames': ['status'], 'schema': {'type': 'status', 'system': 'status'}},
{'id': 'components', 'key': 'components', 'name': 'Components', 'custom': False, 'orderable': True,
 'navigable': True, 'searchable': True, 'clauseNames': ['component'],
 'schema': {'type': 'array', 'items': 'component', 'system': 'components'}},
{'id': 'issuekey', 'key': 'issuekey', 'name': 'Key', 'custom': False, 'orderable': False, 'navigable': True,
 'searchable': False, 'clauseNames': ['id', 'issue', 'issuekey', 'key']},
{'id': 'timeoriginalestimate', 'key': 'timeoriginalestimate', 'name': 'Original estimate', 'custom': False,
 'orderable': False, 'navigable': True, 'searchable': False,
 'clauseNames': ['originalEstimate', 'timeoriginalestimate'],
 'schema': {'type': 'number', 'system': 'timeoriginalestimate'}},
{'id': 'description', 'key': 'description', 'name': 'Description', 'custom': False, 'orderable': True,
 'navigable': True, 'searchable': True, 'clauseNames': ['description'],
 'schema': {'type': 'string', 'system': 'description'}},
{'id': 'customfield_10010', 'key': 'customfield_10010', 'name': 'Sprint', 'untranslatedName': 'Sprint',
 'custom': True, 'orderable': True, 'navigable': True, 'searchable': True, 'clauseNames': ['cf[10010]', 'Sprint'],
 'schema': {'type': 'array', 'items': 'json', 'custom': 'com.pyxis.greenhopper.jira:gh-sprint', 'customId': 10010}},
{'id': 'customfield_10011', 'key': 'customfield_10011', 'name': 'Rank', 'untranslatedName': 'Rank', 'custom': True,
 'orderable': True, 'navigable': True, 'searchable': True, 'clauseNames': ['cf[10011]', 'Rank'],
 'schema': {'type': 'any', 'custom': 'com.pyxis.greenhopper.jira:gh-lexo-rank', 'customId': 10011}},
{'id': 'customfield_10012', 'key': 'customfield_10012', 'name': '[CHART] Date of First Response',
 'untranslatedName': '[CHART] Date of First Response', 'custom': True, 'orderable': True, 'navigable': True,
 'searchable': True,
 'clauseNames': ['[CHART] Date of First Response', '[CHART] Date of First Response[Date of first response]',
                 'cf[10012]'],
 'schema': {'type': 'datetime', 'custom': 'com.atlassian.jira.ext.charting:firstresponsedate', 'customId': 10012}},
{'id': 'customfield_10013', 'key': 'customfield_10013', 'name': '[CHART] Time in Status',
 'untranslatedName': '[CHART] Time in Status', 'custom': True, 'orderable': True, 'navigable': True,
 'searchable': True,
 'clauseNames': ['[CHART] Time in Status', '[CHART] Time in Status[Time in Status]', 'cf[10013]'],
 'schema': {'type': 'any', 'custom': 'com.atlassian.jira.ext.charting:timeinstatus', 'customId': 10013}},
{'id': 'customfield_10014', 'key': 'customfield_10014', 'name': 'Story Points', 'untranslatedName': 'Story Points',
 'custom': True, 'orderable': True, 'navigable': True, 'searchable': True,
 'clauseNames': ['cf[10014]', 'Story Points', 'Story Points[Number]'],
 'schema': {'type': 'number', 'custom': 'com.atlassian.jira.plugin.system.customfieldtypes:float',
            'customId': 10014}},
{'id': 'timetracking', 'key': 'timetracking', 'name': 'Time tracking', 'custom': False, 'orderable': True,
 'navigable': False, 'searchable': True, 'clauseNames': [],
 'schema': {'type': 'timetracking', 'system': 'timetracking'}},
{'id': 'customfield_10005', 'key': 'customfield_10005', 'name': 'Epic Name', 'untranslatedName': 'Epic Name',
 'custom': True, 'orderable': True, 'navigable': True, 'searchable': True,
 'clauseNames': ['cf[10005]', 'Epic Name'],
 'schema': {'type': 'string', 'custom': 'com.pyxis.greenhopper.jira:gh-epic-label', 'customId': 10005}},
{'id': 'customfield_10006', 'key': 'customfield_10006', 'name': 'Epic Status', 'untranslatedName': 'Epic Status',
 'custom': True, 'orderable': True, 'navigable': True, 'searchable': True,
 'clauseNames': ['cf[10006]', 'Epic Status'],
 'schema': {'type': 'option', 'custom': 'com.pyxis.greenhopper.jira:gh-epic-status', 'customId': 10006}},
{'id': 'security', 'key': 'security', 'name': 'Security Level', 'custom': False, 'orderable': True,
 'navigable': True, 'searchable': True, 'clauseNames': ['level'],
 'schema': {'type': 'securitylevel', 'system': 'security'}},
{'id': 'customfield_10007', 'key': 'customfield_10007', 'name': 'Epic Colour', 'untranslatedName': 'Epic Colour',
 'custom': True, 'orderable': True, 'navigable': True, 'searchable': True,
 'clauseNames': ['cf[10007]', 'Epic Colour'],
 'schema': {'type': 'string', 'custom': 'com.pyxis.greenhopper.jira:gh-epic-color', 'customId': 10007}},
{'id': 'customfield_10008', 'key': 'customfield_10008', 'name': 'Epic Link', 'untranslatedName': 'Epic Link',
 'custom': True, 'orderable': True, 'navigable': True, 'searchable': True,
 'clauseNames': ['cf[10008]', 'Epic Link'],
 'schema': {'type': 'any', 'custom': 'com.pyxis.greenhopper.jira:gh-epic-link', 'customId': 10008}},
{'id': 'attachment', 'key': 'attachment', 'name': 'Attachment', 'custom': False, 'orderable': True,
 'navigable': False, 'searchable': True, 'clauseNames': ['attachments'],
 'schema': {'type': 'array', 'items': 'attachment', 'system': 'attachment'}},
{'id': 'aggregatetimeestimate', 'key': 'aggregatetimeestimate', 'name': 'Σ Remaining Estimate', 'custom': False,
 'orderable': False, 'navigable': True, 'searchable': False, 'clauseNames': [],
 'schema': {'type': 'number', 'system': 'aggregatetimeestimate'}},
{'id': 'customfield_10009', 'key': 'customfield_10009', 'name': 'Parent Link', 'untranslatedName': 'Parent Link',
 'custom': True, 'orderable': True, 'navigable': True, 'searchable': True,
 'clauseNames': ['cf[10009]', 'Parent Link'],
 'schema': {'type': 'any', 'custom': 'com.atlassian.jpo:jpo-custom-field-parent', 'customId': 10009}},
{'id': 'summary', 'key': 'summary', 'name': 'Summary', 'custom': False, 'orderable': True, 'navigable': True,
 'searchable': True, 'clauseNames': ['summary'], 'schema': {'type': 'string', 'system': 'summary'}},
{'id': 'creator', 'key': 'creator', 'name': 'Creator', 'custom': False, 'orderable': False, 'navigable': True,
 'searchable': True, 'clauseNames': ['creator'], 'schema': {'type': 'user', 'system': 'creator'}},
{'id': 'subtasks', 'key': 'subtasks', 'name': 'Sub-tasks', 'custom': False, 'orderable': False, 'navigable': True,
 'searchable': False, 'clauseNames': ['subtasks'],
 'schema': {'type': 'array', 'items': 'issuelinks', 'system': 'subtasks'}},
{'id': 'reporter', 'key': 'reporter', 'name': 'Reporter', 'custom': False, 'orderable': True, 'navigable': True,
 'searchable': True, 'clauseNames': ['reporter'], 'schema': {'type': 'user', 'system': 'reporter'}},
{'id': 'aggregateprogress', 'key': 'aggregateprogress', 'name': 'Σ Progress', 'custom': False, 'orderable': False,
 'navigable': True, 'searchable': False, 'clauseNames': [],
 'schema': {'type': 'progress', 'system': 'aggregateprogress'}},
{'id': 'customfield_10000', 'key': 'customfield_10000', 'name': 'Development', 'untranslatedName': 'development',
 'custom': True, 'orderable': True, 'navigable': True, 'searchable': True,
 'clauseNames': ['cf[10000]', 'development'],
 'schema': {'type': 'any', 'custom': 'com.atlassian.jira.plugins.jira-development-integration-plugin:devsummarycf',
            'customId': 10000}},
{'id': 'customfield_10001', 'key': 'customfield_10001', 'name': 'Team', 'untranslatedName': 'Team', 'custom': True,
 'orderable': True, 'navigable': True, 'searchable': True, 'clauseNames': ['cf[10001]', 'Team', 'Team[Team]'],
 'schema': {'type': 'any', 'custom': 'com.atlassian.teams:rm-teams-custom-field-team', 'customId': 10001}},
{'id': 'customfield_10004', 'key': 'customfield_10004', 'name': 'Organizations',
 'untranslatedName': 'Organizations', 'custom': True, 'orderable': True, 'navigable': True, 'searchable': True,
 'clauseNames': ['cf[10004]', 'Organizations'], 'schema': {'type': 'array', 'items': 'sd-customerorganization',
                                                           'custom': 'com.atlassian.servicedesk:sd-customer-organizations',
                                                           'customId': 10004}},
{'id': 'customfield_10038', 'key': 'customfield_10038', 'name': 'Target start', 'untranslatedName': 'Target start',
 'custom': True, 'orderable': True, 'navigable': True, 'searchable': True,
 'clauseNames': ['cf[10038]', 'Target start'],
 'schema': {'type': 'date', 'custom': 'com.atlassian.jpo:jpo-custom-field-baseline-start', 'customId': 10038}},
{'id': 'customfield_10039', 'key': 'customfield_10039', 'name': 'Target end', 'untranslatedName': 'Target end',
 'custom': True, 'orderable': True, 'navigable': True, 'searchable': True,
 'clauseNames': ['cf[10039]', 'Target end'],
 'schema': {'type': 'date', 'custom': 'com.atlassian.jpo:jpo-custom-field-baseline-end', 'customId': 10039}},
{'id': 'environment', 'key': 'environment', 'name': 'Environment', 'custom': False, 'orderable': True,
 'navigable': True, 'searchable': True, 'clauseNames': ['environment'],
 'schema': {'type': 'string', 'system': 'environment'}},
{'id': 'duedate', 'key': 'duedate', 'name': 'Due date', 'custom': False, 'orderable': True, 'navigable': True,
 'searchable': True, 'clauseNames': ['due', 'duedate'], 'schema': {'type': 'date', 'system': 'duedate'}},
{'id': 'progress', 'key': 'progress', 'name': 'Progress', 'custom': False, 'orderable': False, 'navigable': True,
 'searchable': False, 'clauseNames': ['progress'], 'schema': {'type': 'progress', 'system': 'progress'}},
{'id': 'comment', 'key': 'comment', 'name': 'Comment', 'custom': False, 'orderable': True, 'navigable': False,
 'searchable': True, 'clauseNames': ['comment'], 'schema': {'type': 'comments-page', 'system': 'comment'}},
{'id': 'votes', 'key': 'votes', 'name': 'Votes', 'custom': False, 'orderable': False, 'navigable': True,
 'searchable': False, 'clauseNames': ['votes'], 'schema': {'type': 'votes', 'system': 'votes'}},
{'id': 'worklog', 'key': 'worklog', 'name': 'Log Work', 'custom': False, 'orderable': True, 'navigable': False,
 'searchable': True, 'clauseNames': [], 'schema': {'type': 'array', 'items': 'worklog', 'system': 'worklog'}}]
