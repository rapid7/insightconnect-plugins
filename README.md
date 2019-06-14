# InsightConnect Plugins

We made a large number of our plugins open-source in order to benefit our customers, partners, and the greater community.
The integrations here include some new, some old, and many that need a little TLC. We'll continue to add more over time based on user requests and our own updates.
The full list of integrations is available on our [Marketplace](https://market.komand.com/).

If you have questions, reach out to us at `IntegrationAlliance@rapid7.com`.

### Table of Contents

1. [Getting Started](#getting-started)
2. [Example](#example)
3. [Plugin Support](#plugin-support)
4. [Contributing](#contributing)

### Getting Started

You can run and develop plugins from the command-line and then orchestrate them via [InsightConnect](https://www.rapid7.com/products/insightconnect/) or legacy Komand.

Plugins are stand-alone REST services that run within Docker containers. You can interact with them over HTTP via the REST service endpoints or stdin/stdout of the running container's process.

See our [developer documentation](https://komand.github.io/python/start.html) to learn how to build a plugin using our Python SDK. To learn more about a specific plugin, see the documentation in every plugin's `help.md` file.

Dependencies:

* [Python 3](https://www.python.org/download/releases/3.0/)
* [Make](https://www.gnu.org/software/make/)
* [Docker Engine](https://www.docker.com)
* InsightConnect [plugin tooling](https://komand.github.io/python/start.html)
* Optional: [jq](https://stedolan.github.io/jq/), [flake8](https://pypi.org/project/flake8/), [mdl](https://github.com/markdownlint/markdownlint) for the helper scripts in `tools/`.

### Example

![Make Menu](./imgs/menu.png)

Let's build and run a plugin from this repository.

We'll use the Dig plugin as an example. Dig is a command-line network utility for DNS.

```
$ cd dig
$ make
[*] Use ``make menu`` for available targets
[*] Including available Makefiles: ../tools/Makefiles/Colors.mk ../tools/Makefiles/Helpers.mk
--
[*] Building plugin image
docker build --pull -t rapid7/dig:1.0.1 .
Sending build context to Docker daemon  208.9kB
Step 1/14 : FROM komand/python-3-37-slim-plugin:3
2: Pulling from komand/python-3-37-slim-plugin
Digest: sha256:74c67981efc06a27c0e650bc0bc3a681c87bc193869a3316945480c26371f7f4
Status: Image is up to date for komand/python-3-37-slim-plugin:3
...
```

Now, let's create the runner script and then run the plugin:

```
$ make runner
[*] Use ``make menu`` for available targets
[*] Including available Makefiles: ../tools/Makefiles/Colors.mk ../tools/Makefiles/Helpers.mk
--
[*] Creating link to run.sh |

$ ./run.sh -R tests/search_by_domain.json -j

Running: cat tests/forward.json | docker run --rm   -i rapid7/dig:1.0.1  run | grep -- ^\{ | jq -r '.body | try(.log | split("\n") | .[]),.output'
rapid7/Dig:1.0.1. Step name: forward
Executing command /usr/bin/dig google.com A

{
  "status": "NOERROR",
  "fulloutput": "\n; <<>> DiG 9.12.3 <<>> google.com A\n;; global options: +cmd\n;; Got answer:\n;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 52959\n;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0\n\n;; QUESTION SECTION:\n;google.com.\t\t\tIN\tA\n\n;; ANSWER SECTION:\ngoogle.com.\t\t162\tIN\tA\t172.217.12.174\n\n;; Query time: 62 msec\n;; SERVER: 192.168.65.1#53(192.168.65.1)\n;; WHEN: Thu Apr 18 17:06:37 UTC 2019\n;; MSG SIZE  rcvd: 44\n\n",
  "question": "google.com",
  "all_answers": [
    "172.217.12.174"
  ],
  "last_answer": "172.217.12.174",
  "answer": "172.217.12.174",
  "nameserver": "192.168.65.1"
}
```

You can also run the plugin container in the background as a REST server:

```
$ ./run.sh -c http
Forwarding to port 10001
Running:  docker run --rm  -d  -p 10001:10001 -i rapid7/dig:1.0.1  http
d719d45e9238d407010e656209f11b30674c2a3dd39225e232685737b111cc2d
```

Let's run the equivalent of the previous example but with a web request:

```
$ curl -d @tests/forward.json http://127.0.0.1:10001/actions/forward
{
  "body": {
    "log": "rapid7/Dig:1.0.1. Step name: forward\nExecuting command /usr/bin/dig google.com A\n",
    "meta": {},
    "output": {
      "all_answers": [
        "172.217.9.78"
      ],
      "answer": "172.217.9.78",
      "fulloutput": "\n; <<>> DiG 9.12.3-P4 <<>> google.com A\n;; global options: +cmd\n;; Got answer:\n;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 59113\n;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0\n\n;; QUESTION SECTION:\n;google.com.\t\t\tIN\tA\n\n;; ANSWER SECTION:\ngoogle.com.\t\t162\tIN\tA\t172.217.9.78\n\n;; Query time: 46 msec\n;; SERVER: 192.168.65.1#53(192.168.65.1)\n;; WHEN: Fri Apr 19 16:45:20 UTC 2019\n;; MSG SIZE  rcvd: 44\n\n",
      "last_answer": "172.217.9.78",
      "nameserver": "192.168.65.1",
      "question": "google.com",
      "status": "NOERROR"
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}
```

You can generate sample JSON to use to test your plugin with the runner `run.sh`:

```
$ ./run.sh -c sample
Actions: [forward reverse]
Triggers: []
Sample requires sample name e.g. ``./run.sh -c sample <name>''

$ ./run.sh -c sample forward
Running:  docker run --rm   -i rapid7/dig:1.0.1  sample forward | jq '.'
{
  "body": {
    "action": "forward",
    "input": {
      "query": "A",
      "domain": "",
      "resolver": ""
    },
    "connection": null,
    "meta": {}
  },
  "version": "v1",
  "type": "action_start"
}
```

You can also generate all samples for a plugin with this shorthand: `./run.sh -c samples`

### Plugin Support

The following table shows which plugins are officially supported by Rapid7 developers (rapid7) and which ones are supported by our ecosystem of external developers or by Rapid7 as best-effort (community).

| Plugin                            | Status       |
| --------------------------------- | ------------ |
| abuseipdb                         | community  |
| active_directory_ldap             | rapid7    |
| anomali_threatstream              | community  |
| att_cybersecurity_alienvault_otx  | community  |
| awk                               | community  |
| azure_compute                     | community  |
| barracuda_waf                     | community  |
| base64                            | community  |
| basename                          | community  |
| bhr                               | community  |
| bitbucket                         | community  |
| blockade                          | community  |
| bluecoat_labs                     | community  |
| box                               | community  |
| cacador                           | community  |
| carbon_black_defense              | rapid7    |
| carbon_black_live_response        | rapid7    |
| carbon_black_protection           | rapid7    |
| carbon_black_response             | rapid7    |
| cef                               | community  |
| chaosreader                       | community  |
| checkdmarc                        | community  |
| checkpoint_sand_blast             | community  |
| cherwell                          | community  |
| cif                               | community  |
| cisco_cloudlock                   | rapid7    |
| cisco_firepower                   | rapid7    |
| cisco_ise                         | rapid7    |
| cisco_umbrella_enforcement        | rapid7    |
| cisco_umbrella_investigate        | rapid7    |
| cloudshark                        | community  |
| compression                       | community  |
| confluence                        | community  |
| cortex                            | community  |
| cortex_v2                         | community  |
| crits                             | community  |
| csv                               | community  |
| cuckoo                            | community  |
| datadog                           | community  |
| datetime                          | rapid7    |
| diff                              | community  |
| digitalocean                      | community  |
| dirname                           | community  |
| docker_engine                     | community  |
| domaintools                       | community  |
| dumbno                            | community  |
| duo_admin                         | rapid7    |
| duo_auth                          | rapid7    |
| elastalert                        | community  |
| elasticsearch                     | community  |
| eml                               | community  |
| extractit                         | community  |
| facebook_threat_exchange          | community  |
| finger                            | community  |
| fireeye_hx                        | community  |
| foremost                          | community  |
| freeipa                           | community  |
| ftp                               | community  |
| fullcontact                       | community  |
| geoip2precision                   | community  |
| get_url                           | community  |
| git                               | community  |
| github                            | community  |
| github_enterprise                 | community  |
| gitlab                            | community  |
| google_admin                      | community  |
| google_cloud_compute              | community  |
| google_cloud_pub_sub              | community  |
| google_directory                  | community  |
| google_docs                       | community  |
| google_drive                      | community  |
| google_safe_browsing              | community  |
| google_search                     | community  |
| google_sheets                     | community  |
| grafana                           | community  |
| graphite                          | community  |
| grr                               | community  |
| hashit                            | community  |
| haveibeenpwned                    | community  |
| hipchat                           | deprecated   |
| hippocampe                        | community  |
| html                              | community  |
| hybrid_analysis                   | community  |
| ibm_resilient_incident            | community  |
| idna                              | community  |
| ifconfig_co                       | community  |
| imperva_securesphere              | community  |
| influxdb                          | community  |
| infoblox                          | community  |
| ipify                             | community  |
| ipinfo                            | community  |
| ipintel                           | community  |
| ipstack                           | community  |
| jenkins                           | community  |
| jira                              | rapid7    |
| joe_sandbox                       | community  |
| json_edit                         | community  |
| kafka                             | community  |
| kolide                            | community  |
| lastpass_enterprise               | community  |
| logstash                          | community  |
| malwareconfig                     | community  |
| markdown                          | community  |
| math                              | community  |
| matplotlib                        | community  |
| mcafee_epo                        | community  |
| mcafee_esm                        | community  |
| microsoft_atp                     | community  |
| microsoft_atp_safe_links          | community  |
| mimecast                          | rapid7    |
| minfraud                          | community  |
| misp                              | community  |
| mxtoolbox_dns                     | community  |
| netmiko                           | community  |
| networktotal                      | community  |
| newrelic                          | community  |
| nfs                               | community  |
| nmap                              | community  |
| numverify                         | community  |
| okta                              | rapid7    |
| opendxl                           | community  |
| openphish                         | community  |
| openvas                           | community  |
| p0f                               | community  |
| pagerduty                         | community  |
| palo_alto_pan_os                  | rapid7    |
| paloalto_wildfire                 | rapid7    |
| passivetotal                      | community  |
| pastebin                          | community  |
| pdf_generator                     | community  |
| pdf_reader                        | community  |
| phabricator                       | community  |
| phishtank                         | community  |
| presto                            | community  |
| proofpoint_tap                    | community  |
| qradar                            | community  |
| qualys_pc_scan                    | community  |
| qualys_reports                    | community  |
| qualys_scap_scan                  | community  |
| qualys_ssl                        | community  |
| qualys_vm_scan                    | community  |
| rapid7_insightappsec              | rapid7    |
| rapid7_insightops                 | rapid7    |
| rapid7_insightvm                  | rapid7    |
| rapid7_metasploit                 | rapid7    |
| rapid7_tcell                      | rapid7    |
| rapid7_vulndb                     | rapid7    |
| recorded_future                   | rapid7    |
| red_canary                        | rapid7    |
| redhat_advisory                   | community  |
| redis                             | community  |
| request_tracker                   | community  |
| rest                              | community  |
| rpm                               | community  |
| rss                               | community  |
| salesforce                        | community  |
| samanage                          | community  |
| screenshot_machine                | community  |
| sentinelone                       | rapid7    |
| sentry                            | community  |
| shattered                         | community  |
| sleep                             | community  |
| smb                               | community  |
| smtp                              | community  |
| snortlabslist                     | community  |
| sophos_xg_firewall                | community  |
| splunk                            | rapid7    |
| sql                               | community  |
| sqlmap                            | community  |
| ssh                               | community  |
| statsd                            | community  |
| string                            | community  |
| subnet                            | community  |
| sumologic                         | community  |
| symantec_bcs                      | community  |
| syslog_forwarder                  | community  |
| syslog_listener                   | community  |
| tcpdump                           | community  |
| tcpxtract                         | community  |
| tenable_io                        | community  |
| tenable_nessus                    | community  |
| threat_connect                    | community  |
| threatq                           | community  |
| threatminer                       | community  |
| threatstack                       | community  |
| timers                            | community  |
| trufflehog                        | community  |
| try_bro                           | community  |
| twilio                            | community  |
| type_converter                    | rapid7    |
| typo_squatter                     | community  |
| uniq                              | community  |
| unshorten                         | community  |
| urlscan                           | community  |
| uuid                              | community  |
| virustotal_yara                   | community  |
| vmray                             | community  |
| vxstream_sandbox                  | community  |
| wazuh_ossec                       | community  |
| whois                             | community  |
| wordpress                         | community  |
| zendesk                           | community  |
| zenhub                            | community  |
| zeus_tracker                      | community  |

### Contributing

See our [contributing guide](./CONTRIBUTING.md).
