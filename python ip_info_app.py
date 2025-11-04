
import argparse
import json
import sys
import requests
from typing import Optional, Dict

REQUEST_TIMEOUT = 6  # seconds

def fetch_ip(version: int = 4) -> Optional[str]:
    """Fetch public IP using ipify (v4 or v6)."""
    if version == 4:
        url = "https://api.ipify.org?format=json"
    elif version == 6:
        url = "https://api64.ipify.org?format=json"
    else:
        return None
    try:
        resp = requests.get(url, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
        return data.get("ip")
    except Exception as e:
        # print helpful debug to stderr, but return None so program continues
        print(f"[WARN] failed to fetch IPv{version}: {e}", file=sys.stderr)
        return None

def query_ip_api(ip: str) -> Dict:
    """Query ip-api.com (no key) for details."""
    # fields: status, query, country, countryCode, regionName, city, isp, as, timezone, lat, lon
    fields = "status,message,query,country,countryCode,regionName,city,isp,as,timezone,lat,lon"
    url = f"http://ip-api.com/json/{ip}?fields={fields}"
    resp = requests.get(url, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    return resp.json()

def query_ipapi_co(ip: str) -> Dict:
    """Query ipapi.co for details (no key for many endpoints)"""
    url = f"https://ipapi.co/{ip}/json/"
    resp = requests.get(url, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    return resp.json()

def normalize_result(provider: str, raw: Dict) -> Dict:
    """Normalize various API responses into a common dict for display."""
    out = {
        "ip": raw.get("query") or raw.get("ip") or raw.get("ip_address") or "",
        "status": raw.get("status", "success"),
        "country": raw.get("country") or raw.get("country_name") or "",
        "countryCode": raw.get("countryCode") or raw.get("country_code") or "",
        "region": raw.get("regionName") or raw.get("region") or raw.get("region_code") or "",
        "city": raw.get("city") or "",
        "isp": raw.get("isp") or raw.get("org") or raw.get("asn_org") or "",
        "asn": raw.get("as") or raw.get("asn") or raw.get("asn_org") or "",
        "timezone": raw.get("timezone") or raw.get("time_zone") or "",
        "lat": raw.get("lat") or raw.get("latitude") or "",
        "lon": raw.get("lon") or raw.get("longitude") or "",
        "provider_raw": provider
    }
    # ip-api returns {"status":"fail","message":"private range"} when private/reserved
    if out["status"] == "fail" and "message" in raw:
        out["error_message"] = raw.get("message")
    return out

def print_summary(rows):
    """Pretty print results in columns."""
    max_ip_len = max((len(r["ip"]) for r in rows if r.get("ip")), default=12)
    header = f"{'IP':{max_ip_len}}  {'ASN':20}  {'ISP':30}  {'Country (Code)':20}  {'Region/City':25}  {'TZ':20}"
    sep = "-" * len(header)
    print(header)
    print(sep)
    for r in rows:
        if r.get("status") == "fail":
            err = r.get("error_message", "unknown")
            print(f"{r.get('ip', ''):{max_ip_len}}  (error) {err}")
            continue
        asn = r.get("asn", "")[:20]
        isp = r.get("isp", "")[:30]
        country = f"{r.get('country','')[:16]} ({r.get('countryCode','')})"
        regioncity = f"{r.get('region','')[:16]}/{r.get('city','')[:8]}"
        tz = r.get('timezone','')[:20]
        print(f"{r.get('ip',''):{max_ip_len}}  {asn:20}  {isp:30}  {country:20}  {regioncity:25}  {tz:20}")

def main():
    parser = argparse.ArgumentParser(description="Public IPv4/IPv6 & geolocation prototype")
    parser.add_argument("--no-ipv6", action="store_true", help="skip IPv6 lookup")
    parser.add_argument("--provider", choices=["ip-api", "ipapi"], default="ip-api",
                        help="geolocation provider to use")
    parser.add_argument("--show-raw", action="store_true", help="print raw JSON responses")
    args = parser.parse_args()

    rows = []

    # IPv4
    ipv4 = fetch_ip(4)
    if ipv4:
        try:
            if args.provider == "ip-api":
                raw = query_ip_api(ipv4)
            else:
                raw = query_ipapi_co(ipv4)
            normalized = normalize_result(args.provider, raw)
            rows.append(normalized)
            if args.show_raw:
                print("\n[RAW IPv4 RESPONSE]\n", json.dumps(raw, indent=2))
        except Exception as e:
            print(f"[WARN] geolocation query for IPv4 failed: {e}", file=sys.stderr)
            rows.append({"ip": ipv4, "status": "fail", "error_message": str(e)})
    else:
        print("[INFO] IPv4 address not found.", file=sys.stderr)

    # IPv6
    if not args.no_ipv6:
        ipv6 = fetch_ip(6)
        if ipv6:
            try:
                if args.provider == "ip-api":
                    raw = query_ip_api(ipv6)
                else:
                    raw = query_ipapi_co(ipv6)
                normalized = normalize_result(args.provider, raw)
                rows.append(normalized)
                if args.show_raw:
                    print("\n[RAW IPv6 RESPONSE]\n", json.dumps(raw, indent=2))
            except Exception as e:
                print(f"[WARN] geolocation query for IPv6 failed: {e}", file=sys.stderr)
                rows.append({"ip": ipv6, "status": "fail", "error_message": str(e)})
        else:
            print("[INFO] IPv6 address not found (system or network may not have IPv6).", file=sys.stderr)

    if rows:
        print("\n=== Public IP Address Summary ===\n")
        print_summary(rows)
    else:
        print("No public IP information available.", file=sys.stderr)
        sys.exit(2)

if __name__ == "__main__":
    main()
