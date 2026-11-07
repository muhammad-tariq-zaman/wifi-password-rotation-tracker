# wifi-password-rotation-tracker

Track Wi-Fi password age per SSID against a rotation policy (default 90 days): rotate-due, due-soon or OK, oldest change first, so no network password quietly goes stale.

## How to run

```sh
python3 main.py passwords.csv --now 2026-11-05 --rotation-days 90
```

## Example output

```
Office-WiFi: ROTATE DUE (changed 2026-07-01, 127 days ago)
Guest-WiFi: OK (changed 2026-10-20, 16 days ago)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
