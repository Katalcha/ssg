import unittest
from extract_markdown_images import extract_markdown_images

test_content = "This is text with a python image ![python-img](https://i.imgur.com/zjjcJKZ.png)"
test_url = "https://i.imgur.com/zjjcJKZ.png"
test_alt = "python-img"

class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        test = extract_markdown_images(test_content)
        expected = [(test_alt, test_url)]
        self.assertListEqual(expected, test)

if __name__ == "__main__":
    unittest.main()
