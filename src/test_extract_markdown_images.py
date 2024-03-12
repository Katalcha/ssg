import unittest
from extract_markdown_images import extract_markdown_images

class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        test = extract_markdown_images("This is text with a python image ![python-img](https://i.imgur.com/zjjcJKZ.png)")
        expected = [("python-img", "https://i.imgur.com/zjjcJKZ.png")]
        self.assertListEqual(expected, test)

if __name__ == "__main__":
    unittest.main()
