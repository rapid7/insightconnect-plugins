#!/usr/bin/env python3
"""
Local test script for rapid7_intelhub plugin
This version doesn't require insightconnect_plugin_runtime - just uses requests directly.

Usage: 
  export RAPID7_API_KEY='your-key'
  python3 test_local.py
"""
import os
import requests

# =============================================================================
# CONFIGURE YOUR API KEY AND REGION HERE
# =============================================================================
API_KEY = os.environ.get("RAPID7_API_KEY", "your-api-key-here")
REGION = "United States"  # Options: United States, Europe, Canada, Australia, Japan
# =============================================================================

REGION_MAP = {
    "United States": "us",
    "Europe": "eu",
    "Canada": "ca",
    "Australia": "au",
    "Japan": "ap",
}


def get_base_url(region):
    region_code = REGION_MAP.get(region, "us")
    return f"https://{region_code}.api.insight.rapid7.com/intelligencehub/intelligence-hub/v1"


def get_headers(api_key):
    return {
        "X-Api-Key": api_key,
        "Accept": "application/json",
        "Content-Type": "application/json",
    }


def test_connection(base_url, headers):
    """Test the connection"""
    print("\n" + "=" * 60)
    print("Testing Connection...")
    print("=" * 60)
    
    response = requests.get(
        f"{base_url}/cve",
        headers=headers,
        params={"page": 1, "page-size": 1},
        timeout=30,
    )
    
    if response.status_code == 200:
        print("✓ Connection successful!")
        return True
    else:
        print(f"✗ Connection failed: {response.status_code}")
        print(f"  Response: {response.text}")
        return False


def test_search_cves(base_url, headers, search="", page=1, page_size=5, cvss_score="", exploitable=None, epss_score="", cisa_kev=None, last_updated=""):
    """Test Search CVEs"""
    print("\n" + "=" * 60)
    filters = f"search='{search}'"
    if cvss_score:
        filters += f", cvss_score='{cvss_score}'"
    if exploitable is not None:
        filters += f", exploitable={exploitable}"
    if epss_score:
        filters += f", epss_score='{epss_score}'"
    if cisa_kev is not None:
        filters += f", cisa_kev={cisa_kev}"
    if last_updated:
        filters += f", last_updated='{last_updated}'"
    print(f"Testing Search CVEs ({filters})...")
    print("=" * 60)
    
    params = {
        "page": page,
        "page-size": page_size,
    }
    if search:
        params["search"] = search
    if cvss_score:
        params["cvss-score"] = cvss_score
    if exploitable is not None:
        params["exploitable"] = str(exploitable).lower()
    if epss_score:
        params["epss-score"] = epss_score
    if cisa_kev is not None:
        params["cisa-kev"] = str(cisa_kev).lower()
    if last_updated:
        params["last-updated"] = last_updated
    
    response = requests.get(
        f"{base_url}/cve",
        headers=headers,
        params=params,
        timeout=30,
    )
    
    if response.status_code == 200:
        data = response.json()
        cves = data.get("data", [])
        total = data.get("total_count", 0)
        print(f"✓ Found {len(cves)} CVEs (total: {total}):")
        for cve in cves:
            cve_id = cve.get("cve_id", "N/A")
            title = cve.get("title", "N/A")[:50] if cve.get("title") else "N/A"
            print(f"  - {cve_id}: {title}...")
        return cves
    else:
        print(f"✗ Search failed: {response.status_code}")
        print(f"  Response: {response.text}")
        return []


def test_get_cve(base_url, headers, cve_id):
    """Test Get CVE by ID"""
    print("\n" + "=" * 60)
    print(f"Testing Get CVE: {cve_id}...")
    print("=" * 60)
    
    response = requests.get(
        f"{base_url}/cve/{cve_id}",
        headers=headers,
        timeout=30,
    )
    
    if response.status_code == 200:
        cve = response.json()
        print(f"✓ CVE Found!")
        print(f"  ID: {cve.get('cve_id')}")
        print(f"  Title: {cve.get('title', 'N/A')}")
        print(f"  Severity: {cve.get('severity', 'N/A')}")
        print(f"  CVSS Score: {cve.get('cvss_score', 'N/A')}")
        print(f"  Published: {cve.get('published_date', 'N/A')}")
        desc = cve.get('description', 'N/A')
        if desc:
            print(f"  Description: {desc[:150]}...")
        return cve
    elif response.status_code == 404:
        print(f"✗ CVE {cve_id} not found")
        return None
    else:
        print(f"✗ Get CVE failed: {response.status_code}")
        print(f"  Response: {response.text}")
        return None


def main():
    if API_KEY == "your-api-key-here":
        print("ERROR: Please set your API key!")
        print("  export RAPID7_API_KEY='your-key'")
        print("  python3 test_local.py")
        return
    
    print("\n" + "#" * 60)
    print("# Rapid7 IntelHub Plugin - Local Test")
    print("#" * 60)
    
    base_url = get_base_url(REGION)
    headers = get_headers(API_KEY)
    
    print(f"\nUsing endpoint: {base_url}")
    
    # Test connection
    if not test_connection(base_url, headers):
        return
    
    # Test search CVEs with filters - high severity and exploitable
    cves = test_search_cves(base_url, headers, cvss_score="high", exploitable=True, page_size=5)
    
    # Test search with CISA KEV filter
    test_search_cves(base_url, headers, cisa_kev=True, page_size=3)
    
    # Test search by CVE ID pattern
    test_search_cves(base_url, headers, search="CVE-2024", page_size=3)
    
    # Test search with last_updated filter (useful for scheduled workflows)
    test_search_cves(base_url, headers, last_updated="last 72 hours", page_size=5)
    
    # Test get specific CVE
    if cves:
        cve_id = cves[0].get("cve_id")
        if cve_id:
            test_get_cve(base_url, headers, cve_id)
    
    print("\n" + "#" * 60)
    print("# All tests completed!")
    print("#" * 60 + "\n")


if __name__ == "__main__":
    main()
