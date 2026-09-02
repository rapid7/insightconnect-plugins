# InsightConnect Workflow Design: CVE Monitoring with IntelHub + Threat Command

## Customer Requirements Mapping

This document outlines how to build InsightConnect workflows using the **rapid7_intelhub** and **rapid7_intsights** (Threat Command) plugins to meet all 5 customer requirements.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         InsightConnect Workflow                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────┐    ┌──────────────────┐    ┌─────────────────────────┐   │
│  │  Scheduled   │───▶│  IntelHub Plugin │───▶│   Filter & Enrich       │   │
│  │   Trigger    │    │  (Search CVEs)   │    │   (Apply Watchlist)     │   │
│  └──────────────┘    └──────────────────┘    └───────────┬─────────────┘   │
│                                                           │                  │
│                      ┌────────────────────────────────────┘                  │
│                      ▼                                                       │
│  ┌──────────────────────────────────┐    ┌─────────────────────────────┐   │
│  │   Threat Command Plugin          │    │   State Management          │   │
│  │   (Get CVE Details + Add CVE)    │───▶│   (Track Status Changes)    │   │
│  └──────────────────────────────────┘    └───────────┬─────────────────┘   │
│                                                       │                      │
│                      ┌────────────────────────────────┘                      │
│                      ▼                                                       │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │   Notification & Automation Actions (Slack, Jira, SIEM, etc.)        │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Requirement 1: Dynamic, Version-Agnostic Watchlists

### Problem
Customer wants to track "Apache Struts" without selecting specific versions or ingesting assets.

### Solution
Use a **custom watchlist artifact** (JSON) + **IntelHub search** + **title/description pattern matching**.

### Workflow Components

```yaml
# Watchlist stored as workflow artifact or in a lookup table
watchlist:
  - name: "Apache Struts"
    patterns: ["struts", "apache struts"]
    added_date: "2026-02-20"  # For noise reduction (Req #5)
  - name: "Log4j"
    patterns: ["log4j", "log4shell"]
    added_date: "2024-12-01"
  - name: "OpenSSL"
    patterns: ["openssl"]
    added_date: "2026-01-15"
```

### Workflow Steps

1. **Scheduled Trigger** (every 15-60 min)
2. **IntelHub: Search CVEs** 
   - Filter: `cvss_score=high`, `exploitable=true` or `cisa_kev=true`
   - Get recent CVEs (last 24h based on published_date)
3. **Loop through CVEs**
4. **Pattern Match** against watchlist (Python script step)
   - Check if CVE title/description contains any watchlist pattern
5. **If match → Continue to enrichment**

### Example Python Script Step
```python
def match_watchlist(cve_title, cve_description, watchlist):
    """Check if CVE matches any watchlist item"""
    text = f"{cve_title} {cve_description}".lower()
    matches = []
    for item in watchlist:
        for pattern in item['patterns']:
            if pattern.lower() in text:
                matches.append(item['name'])
                break
    return matches
```

---

## Requirement 2: Deep Intel for New CVEs

### Problem
Customer needs more than NVD mirrors - wants Rapid7 analysis including exploitation status, PoC availability, threat actor attribution, zero-day confirmation.

### Solution
Combine **IntelHub** (for structured CVE data) + **Threat Command** (for deep threat intel).

### Data Sources

| Field | IntelHub Plugin | Threat Command Plugin |
|-------|-----------------|----------------------|
| Exploitable | ✅ `exploitable` filter | ✅ `exploitAvailability` |
| CISA KEV | ✅ `cisa_kev` filter | ❌ |
| PoC Available | ✅ (in CVE details) | ✅ `exploitAvailability` |
| Threat Actors | ✅ `threat_actor_count` | ✅ `relatedThreatActors` |
| Related Malware | ❌ | ✅ `relatedMalware` |
| Related Campaigns | ❌ | ✅ `relatedCampaigns` |
| IntSights Score | ❌ | ✅ `intsightsScore` |
| CVSS Score | ✅ `cvss_v3_base_score` | ✅ `cvssScore` |
| Dark Web Mentions | ❌ | ✅ `mentionsPerSource.DarkWeb` |

### Workflow Steps

1. **IntelHub: Search CVEs** with filters
2. **For each CVE:**
   - **IntelHub: Get CVE** (detailed info including EPSS, CVSS vectors)
   - **Threat Command: Get CVE by ID** (threat intel enrichment)
3. **Merge data** into unified alert object

### Example Enriched Output
```json
{
  "cve_id": "CVE-2025-12345",
  "title": "Apache Struts RCE Vulnerability",
  "sources": {
    "intelhub": {
      "cvss_v3_score": 9.8,
      "cvss_v3_severity": "Critical",
      "exploitable": true,
      "cisa_kev": true,
      "epss_score": 0.97,
      "threat_actor_count": 3
    },
    "threat_command": {
      "intsightsScore": 85,
      "exploitAvailability": true,
      "relatedThreatActors": ["APT28", "Lazarus"],
      "relatedMalware": ["Cobalt Strike"],
      "mentionsPerSource": {
        "DarkWeb": 15,
        "HackingForum": 8,
        "Exploit": 3
      },
      "firstMentionDate": "2025-01-10T00:00:00Z"
    }
  },
  "risk_assessment": {
    "actively_exploited": true,
    "poc_available": true,
    "threat_actor_attributed": true,
    "zero_day": false
  }
}
```

---

## Requirement 3: Alerts for Status Changes

### Problem
Customer wants notifications when a CVE's status changes (e.g., gets public exploit, added to CISA KEV).

### Solution
Implement **state tracking** with periodic comparison.

### State Tracking Fields
```json
{
  "cve_id": "CVE-2025-12345",
  "last_checked": "2026-02-20T10:00:00Z",
  "previous_state": {
    "exploitable": false,
    "cisa_kev": false,
    "exploit_availability": false,
    "threat_actor_count": 0
  },
  "current_state": {
    "exploitable": true,
    "cisa_kev": true,
    "exploit_availability": true,
    "threat_actor_count": 2
  }
}
```

### Workflow: Status Change Monitor

1. **Scheduled Trigger** (every 1-4 hours)
2. **Load tracked CVEs** from state store (artifact/database)
3. **For each tracked CVE:**
   - **IntelHub: Get CVE** 
   - **Threat Command: Get CVE by ID**
   - **Compare current vs previous state**
4. **If status changed:**
   - Generate change event with details
   - Send notification
   - Update state store

### Status Change Events to Track
```yaml
status_changes:
  - type: "EXPLOIT_PUBLISHED"
    condition: "previous.exploitable == false AND current.exploitable == true"
    severity: "CRITICAL"
    
  - type: "CISA_KEV_ADDED"
    condition: "previous.cisa_kev == false AND current.cisa_kev == true"
    severity: "CRITICAL"
    
  - type: "THREAT_ACTOR_ATTRIBUTED"
    condition: "previous.threat_actor_count == 0 AND current.threat_actor_count > 0"
    severity: "HIGH"
    
  - type: "POC_AVAILABLE"
    condition: "previous.exploit_availability == false AND current.exploit_availability == true"
    severity: "HIGH"
    
  - type: "DARK_WEB_MENTIONS"
    condition: "current.mentions.DarkWeb > previous.mentions.DarkWeb + 5"
    severity: "MEDIUM"
```

### Example Change Notification
```json
{
  "event_type": "CVE_STATUS_CHANGE",
  "cve_id": "CVE-2025-12345",
  "change_type": "CISA_KEV_ADDED",
  "timestamp": "2026-02-20T14:30:00Z",
  "previous_state": {
    "cisa_kev": false
  },
  "current_state": {
    "cisa_kev": true
  },
  "message": "CVE-2025-12345 has been added to CISA Known Exploited Vulnerabilities catalog",
  "recommended_action": "Immediate patching required within 2 weeks per BOD 22-01"
}
```

---

## Requirement 4: Automation-Ready API Metadata

### Problem
Downstream tools need structured, parseable metadata, not human-readable text.

### Solution
Both plugins return **structured JSON** that can be directly consumed by automation.

### IntelHub CVE Output Structure
```json
{
  "cve_id": "CVE-2025-12345",
  "cvss_v3_base_score": 9.8,
  "cvss_v3_severity": "Critical",
  "cvss_v3_vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
  "exploitable": true,
  "exploited_in_the_wild": true,
  "cisa_kev": true,
  "epss_score": 0.97,
  "epss_percentile": 0.99,
  "published_date": "2025-01-15T00:00:00",
  "modified_date": "2025-02-10T00:00:00",
  "threat_actor_count": 2,
  "campaign_count": 1
}
```

### Threat Command CVE Output Structure
```json
{
  "cveId": "CVE-2025-12345",
  "severity": "Critical",
  "intsightsScore": 92,
  "cvssScore": 9.8,
  "exploitAvailability": true,
  "relatedThreatActors": ["APT28", "Lazarus"],
  "relatedMalware": ["Cobalt Strike", "Mimikatz"],
  "relatedCampaigns": ["Operation Sunrise"],
  "mentionsPerSource": {
    "DarkWeb": 15,
    "HackingForum": 23,
    "Exploit": 5,
    "SocialMedia": 150
  },
  "vulnerabilityOrigin": ["NVD", "Vendor Advisory"],
  "cpe": [
    {
      "Value": "cpe:2.3:a:apache:struts:2.5.0:*:*:*:*:*:*:*",
      "VendorProduct": "Apache Struts"
    }
  ]
}
```

### Unified Output for Downstream Automation
```json
{
  "alert_id": "uuid-12345",
  "alert_type": "CVE_ALERT",
  "timestamp": "2026-02-20T14:30:00Z",
  
  "cve": {
    "id": "CVE-2025-12345",
    "title": "Apache Struts RCE"
  },
  
  "severity": {
    "cvss_score": 9.8,
    "cvss_severity": "Critical",
    "intsights_score": 92,
    "epss_score": 0.97
  },
  
  "exploitation": {
    "is_exploitable": true,
    "exploited_in_wild": true,
    "poc_available": true,
    "cisa_kev": true
  },
  
  "attribution": {
    "threat_actors": ["APT28", "Lazarus"],
    "malware": ["Cobalt Strike"],
    "campaigns": ["Operation Sunrise"]
  },
  
  "mentions": {
    "dark_web": 15,
    "hacking_forum": 23,
    "exploit_sites": 5
  },
  
  "affected_products": {
    "cpe": ["cpe:2.3:a:apache:struts:2.5.0:*:*:*:*:*:*:*"],
    "vendor_product": "Apache Struts",
    "watchlist_match": "Apache Struts"
  },
  
  "action_tags": [
    "CRITICAL_SEVERITY",
    "ACTIVELY_EXPLOITED",
    "CISA_KEV",
    "APT_ATTRIBUTED",
    "PATCH_IMMEDIATELY"
  ]
}
```

---

## Requirement 5: Noise Reduction for New Tech

### Problem
When adding new technology to watchlist, don't want historical CVE flood.

### Solution
Track **watchlist entry date** and filter CVEs by `published_date`.

### Watchlist with Date Filtering
```json
{
  "watchlist": [
    {
      "name": "Apache Struts",
      "patterns": ["struts", "apache struts"],
      "added_date": "2026-02-20T00:00:00Z",
      "alert_on_historical": false
    },
    {
      "name": "Log4j",
      "patterns": ["log4j"],
      "added_date": "2024-12-01T00:00:00Z",
      "alert_on_historical": true
    }
  ]
}
```

### Filtering Logic
```python
def should_alert(cve, watchlist_item):
    """Determine if CVE should trigger alert based on dates"""
    cve_published = parse_date(cve['published_date'])
    watchlist_added = parse_date(watchlist_item['added_date'])
    
    # Only alert on CVEs published AFTER watchlist item was added
    if not watchlist_item.get('alert_on_historical', False):
        if cve_published < watchlist_added:
            return False  # Skip historical CVE
    
    return True
```

### Workflow: New Tech Onboarding

1. **Add new technology to watchlist** with `added_date = now()`
2. **Optional: Backfill mode**
   - Set `alert_on_historical = true` temporarily
   - Run one-time backfill for last 90 days
   - Generate report (not alerts)
   - Set `alert_on_historical = false`
3. **Normal operation**: Only new CVEs after `added_date` trigger alerts

---

## Complete Workflow Implementation

### Workflow 1: CVE Discovery & Alerting (runs every 15 min)

```
┌─────────────────┐
│ Schedule Trigger│ (every 15 min)
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ IntelHub: Search CVEs               │
│ - cvss_score: high                  │
│ - exploitable: true                 │
│ - page_size: 50                     │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ Loop: For each CVE                  │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ Check: Already processed?           │
│ (lookup in state store)             │
└────────┬────────────────────────────┘
         │ No
         ▼
┌─────────────────────────────────────┐
│ Pattern Match: Check watchlist      │
│ (Python script)                     │
└────────┬────────────────────────────┘
         │ Match found
         ▼
┌─────────────────────────────────────┐
│ Date Filter: CVE published after    │
│ watchlist entry date?               │
└────────┬────────────────────────────┘
         │ Yes
         ▼
┌─────────────────────────────────────┐
│ IntelHub: Get CVE (full details)    │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ Threat Command: Get CVE by ID       │
│ (threat intel enrichment)           │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ Merge & Format: Create unified      │
│ alert object                        │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ Save State: Track CVE for status    │
│ change monitoring                   │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ Send Alert: Slack/Teams/Jira/SIEM   │
└─────────────────────────────────────┘
```

### Workflow 2: Status Change Monitor (runs every 2 hours)

```
┌─────────────────┐
│ Schedule Trigger│ (every 2 hours)
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ Load: Get all tracked CVEs from     │
│ state store                         │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ Loop: For each tracked CVE          │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ IntelHub: Get CVE                   │
│ Threat Command: Get CVE by ID       │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ Compare: Current vs Previous state  │
│ - exploitable changed?              │
│ - cisa_kev changed?                 │
│ - threat_actors added?              │
│ - exploit_availability changed?     │
└────────┬────────────────────────────┘
         │ Change detected
         ▼
┌─────────────────────────────────────┐
│ Generate: Status change event       │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ Update State: Save new state        │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ Send Alert: "CVE-XXXX now has       │
│ public exploit / added to CISA KEV" │
└─────────────────────────────────────┘
```

---

## Plugin Actions Summary

### rapid7_intelhub (New Plugin)

| Action | Use Case |
|--------|----------|
| **Search CVEs** | Find CVEs with filters (cvss, exploitable, cisa_kev, epss) |
| **Get CVE** | Get detailed CVE info by ID |

### rapid7_intsights (Threat Command)

| Action | Use Case |
|--------|----------|
| **Get CVE by ID** | Deep threat intel (actors, malware, mentions) |
| **Get CVE List** | List all tracked CVEs in account |
| **Add CVE** | Add CVE to tracking |
| **Delete CVE** | Remove CVE from tracking |
| **Get Indicator by Value** | Check if IOCs related to CVE are known threats |

---

## Sample InsightConnect Workflow JSON

Here's a simplified workflow structure for InsightConnect:

```json
{
  "name": "CVE Watchlist Monitor",
  "description": "Monitor CVEs matching technology watchlist with deep intel enrichment",
  "triggers": [
    {
      "type": "schedule",
      "interval": 900,
      "name": "Every 15 minutes"
    }
  ],
  "steps": [
    {
      "id": "search_cves",
      "plugin": "rapid7_intelhub",
      "action": "search_cves",
      "inputs": {
        "cvss_score": "high",
        "exploitable": true,
        "page_size": 50
      }
    },
    {
      "id": "loop_cves",
      "type": "loop",
      "items": "{{search_cves.cves}}",
      "steps": [
        {
          "id": "get_cve_detail",
          "plugin": "rapid7_intelhub",
          "action": "get_cve",
          "inputs": {
            "cve_id": "{{item.cve_id}}"
          }
        },
        {
          "id": "get_threat_intel",
          "plugin": "rapid7_intsights",
          "action": "get_cve_by_id",
          "inputs": {
            "cve_id": ["{{item.cve_id}}"]
          }
        },
        {
          "id": "send_alert",
          "plugin": "slack",
          "action": "post_message",
          "inputs": {
            "channel": "#security-alerts",
            "message": "New CVE Alert: {{item.cve_id}}"
          }
        }
      ]
    }
  ]
}
```

---

## Summary

| Requirement | Solution | Plugins Used |
|-------------|----------|--------------|
| 1. Dynamic Watchlists | Pattern matching on CVE title/description | IntelHub (search) + Python |
| 2. Deep Intel | Combine IntelHub + Threat Command data | Both |
| 3. Status Changes | State tracking + periodic comparison | Both |
| 4. Automation-Ready | Structured JSON output from both plugins | Both |
| 5. Noise Reduction | Filter by published_date vs watchlist added_date | IntelHub + Python |

Both plugins provide **structured, automation-ready JSON** that downstream tools can parse and act upon without human intervention.
