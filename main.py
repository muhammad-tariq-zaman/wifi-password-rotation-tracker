"""Track Wi-Fi password age per SSID against a rotation policy.

Usage: python3 main.py passwords.csv [--now 2026-11-05] [--rotation-days 90]
CSV columns: ssid,last_changed (ISO date).
ROTATE DUE past the rotation period, DUE SOON within 7 days of it,
otherwise OK. Soonest due first.
"""
import argparse, csv, sys
from datetime import date, timedelta

def track(rows, now, rotation_days):
    out = []
    for row in rows:
        changed = date.fromisoformat(row["last_changed"].strip())
        age = (now - changed).days
        if age > rotation_days:
            verdict = "ROTATE DUE"
        elif age > rotation_days - 7:
            verdict = "DUE SOON"
        else:
            verdict = "OK"
        out.append((row["ssid"], str(changed), age, verdict))
    return sorted(out, key=lambda r: -r[2])

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    parser.add_argument("--now", default=None)
    parser.add_argument("--rotation-days", type=int, default=90)
    args = parser.parse_args(argv)
    now = date.fromisoformat(args.now) if args.now else date.today()
    with open(args.path, newline="", encoding="utf-8") as f:
        for ssid, changed, age, verdict in track(list(csv.DictReader(f)), now, args.rotation_days):
            print(f"{ssid}: {verdict} (changed {changed}, {age} days ago)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
