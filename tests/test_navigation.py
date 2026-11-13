"""Stable public fragments remain valid alongside native Chinese headings."""

import unittest

from scripts.check_profile import ProfileHTML, heading_anchors


class NavigationTests(unittest.TestCase):
    def test_explicit_fragment_and_chinese_heading_are_both_available(self):
        anchors = heading_anchors('<a id="selected-work"></a>\n\n## 三个代表作\n')
        self.assertTrue({"selected-work", "三个代表作"} <= anchors)

    def test_named_anchor_is_not_an_empty_navigation_target(self):
        parser = ProfileHTML()
        parser.feed('<a id="selected-work"></a><a href="README.en.md">English</a>')
        self.assertEqual(parser.references, ["README.en.md"])

    def test_empty_href_still_reaches_link_validation(self):
        parser = ProfileHTML()
        parser.feed('<a href="">Broken</a>')
        self.assertEqual(parser.references, [""])


if __name__ == "__main__":
    unittest.main()
