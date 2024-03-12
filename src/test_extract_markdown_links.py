import unittest
from extract_markdown_links import extract_markdown_links

test_content = "This is text with a boot.dev-link [boot.dev](https://boot.dev) and a freecodecamp.org-link [freecodecamp](https://www.freecodecamp.org)"

test_url_fcc = "https://www.freecodecamp.org"
test_alt_fcc = "freecodecamp"

test_url_bootdev = "https://boot.dev"
test_alt_bootdev = "boot.dev"

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        test = extract_markdown_links(test_content)
        expected = [(test_alt_bootdev, test_url_bootdev), (test_alt_fcc, test_url_fcc)]
        self.assertListEqual(expected, test)

if __name__ == "__main__":
    unittest.main()
