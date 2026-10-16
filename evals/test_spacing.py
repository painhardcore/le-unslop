import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.check_spacing import spacing_errors

ROOT = Path(__file__).resolve().parents[1]


class SpacingTests(unittest.TestCase):
    def test_accepts_both_nonbreaking_spaces(self):
        for space in ("\u00a0", "\u202f"):
            with self.subTest(space=ascii(space)):
                text = f"Elle dit{space}: «{space}Bonjour{space}!{space}» Oui{space}; pourquoi{space}?"
                self.assertEqual(list(spacing_errors(text)), [])

    def test_rejects_ordinary_or_missing_spaces(self):
        for space in ("", " ", "\t"):
            for symbol in ":;!?»":
                with self.subTest(space=ascii(space), symbol=symbol):
                    text = f"Bonjour{space}{symbol}"
                    self.assertEqual(list(spacing_errors(text)), [(1, len(text), symbol)])
            with self.subTest(space=ascii(space), symbol="«"):
                self.assertEqual(list(spacing_errors(f"«{space}Bonjour")), [(1, 1, "«")])

    def test_reports_all_positions(self):
        self.assertEqual(list(spacing_errors("Bonjour!\n«Oui ?»")),
                         [(1, 8, "!"), (2, 1, "«"), (2, 6, "?"), (2, 7, "»")])

    def test_cli_exit_codes_and_read_only_behavior(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "prose.txt"
            command = [sys.executable, str(ROOT / "scripts/check_spacing.py"), str(path)]
            for text, expected_code in (("«\u00a0Bonjour\u00a0!\u00a0»", 0), ("Bonjour!", 1)):
                with self.subTest(text=text):
                    path.write_text(text, encoding="utf-8")
                    result = subprocess.run(command, capture_output=True, text=True)
                    self.assertEqual(result.returncode, expected_code, result.stderr)
                    self.assertEqual(bool(result.stdout), bool(expected_code))
                    self.assertEqual(path.read_text(encoding="utf-8"), text)
            path.unlink()
            missing = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(missing.returncode, 2)
            self.assertIn(str(path), missing.stderr)


if __name__ == "__main__":
    unittest.main()
