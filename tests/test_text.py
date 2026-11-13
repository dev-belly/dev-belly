"""Examples of corruption that must fail, and legitimate Unicode that must pass."""

import unittest

from scripts.check_text import findings


class TextQualityTests(unittest.TestCase):
    def test_chinese_and_mathematical_symbols_are_not_corruption(self):
        self.assertEqual(findings("利润增长 → 自由现金流；ΔFCF = ΔCFO − Δcapex。".encode(), ".md"), [])

    def test_bom_and_windows_newlines_are_valid(self):
        self.assertEqual(findings(b"\xef\xbb\xbf" + "中文\r\nEnglish\r\n".encode(), ".md"), [])

    def test_gbk_bytes_fail_instead_of_being_silently_guessed(self):
        self.assertTrue(findings("中文".encode("gbk"), ".md"))

    def test_broken_characters_and_nul_fail(self):
        for text in ("bad\ufffdtext", "cafÃ©", "itâ€™s", "bad\x00text", "bad\x81text", "bad\x85text"):
            with self.subTest(text=text):
                self.assertTrue(findings(text.encode(), ".md"))

    def test_standalone_html_declares_utf8(self):
        self.assertTrue(findings(b"<!doctype html><html><head></head></html>", ".html"))
        self.assertEqual(findings(b'<!doctype html><meta charset="UTF-8"><html></html>', ".html"), [])

    def test_partial_html_templates_need_no_document_header(self):
        self.assertEqual(findings("<section>中文片段</section>".encode(), ".html"), [])

    def test_vendor_script_literals_are_not_displayed_garbled_text(self):
        html = '<!doctype html><meta charset="utf-8"><script>const pattern=/\ufffd/;const magic="\x01";</script>'
        self.assertEqual(findings(html.encode(), ".html"), [])
        self.assertTrue(findings((html + "<p>\ufffd</p>").encode(), ".html"))

    def test_invalid_utf8_inside_a_script_still_fails(self):
        self.assertTrue(findings(b"<script>\xff</script>", ".html"))


if __name__ == "__main__":
    unittest.main()
