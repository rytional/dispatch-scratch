import unittest

from textstats import format_stats, stats, words


class TextStatsTest(unittest.TestCase):
    def test_words_lowercases_and_strips_punctuation(self):
        self.assertEqual(words("Hello, World! It's me."), ["hello", "world", "it's", "me"])

    def test_stats_counts(self):
        result = stats("a b a\nc a b\n", top=2)
        self.assertEqual(result["lines"], 2)
        self.assertEqual(result["words"], 6)
        self.assertEqual(result["unique_words"], 3)
        self.assertEqual(result["top_words"], [("a", 3), ("b", 2)])

    def test_empty_text(self):
        result = stats("")
        self.assertEqual(result["words"], 0)
        self.assertEqual(result["top_words"], [])

    def test_format_stats_includes_top_words(self):
        text = format_stats(stats("dispatch dispatch test", top=1))
        self.assertIn("words:        3", text)
        self.assertIn("2  dispatch", text)


if __name__ == "__main__":
    unittest.main()
