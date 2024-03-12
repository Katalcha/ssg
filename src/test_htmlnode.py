import unittest
from htmlnode import HTMLNode

test_content1 = "Hello, world!"
test_content2 = "Hewwo, wlord!"

test_tag1 = "div"
test_tag2 = "p"

test_props1 = {"class": "greeting", "href": "https://boot.dev"}
test_props2 = {"id": "main-p", "class": "doge-blue"}

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(test_tag1, test_content1, None, test_props1)
        test = node.props_to_html()
        expected = f' class="greeting" href="https://boot.dev"'
        self.assertEqual(test, expected)

    def test_to_html_props2(self):
        node = HTMLNode(test_tag2, test_content2, None, test_props2)
        test = node.props_to_html()
        expected = f' id="main-p" class="doge-blue"'
        self.assertEqual(test, expected)

if __name__ == "__main__":
    unittest.main()
