import unittest
from extract_markdown_links import extract_markdown_links

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        test = extract_markdown_links(
            "This is text with a boot.dev-link [boot.dev](https://boot.dev) and a freecodecamp.org-link [freecodecamp](https://www.freecodecamp.org)"
        )
        expected = [("boot.dev", "https://boot.dev"), ("freecodecamp", "https://www.freecodecamp.org")]
        self.assertListEqual(expected, test)

if __name__ == "__main__":
    unittest.main()
