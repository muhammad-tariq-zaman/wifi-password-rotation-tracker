import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import track

from datetime import date
NOW = date(2026, 11, 5)
def row(s, changed):
    return {"ssid": s, "last_changed": changed}

class TestRotation(unittest.TestCase):
    def test_rotate_due(self):
        self.assertEqual(track([row("Office", "2026-07-01")], NOW, 90)[0][3], "ROTATE DUE")
    def test_due_soon(self):
        self.assertEqual(track([row("Office", "2026-08-10")], NOW, 90)[0][3], "DUE SOON")
    def test_ok(self):
        self.assertEqual(track([row("Office", "2026-10-20")], NOW, 90)[0][3], "OK")
    def test_oldest_first(self):
        r = track([row("A", "2026-10-20"), row("B", "2026-07-01")], NOW, 90)
        self.assertEqual(r[0][0], "B")
