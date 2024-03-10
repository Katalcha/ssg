import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode("div", "Hello, world!", None, {"class": "greeting", "href": "https://boot.dev"})
        expected = f' class="greeting" href="https://boot.dev"'
        self.assertEqual(node.props_to_html(), expected)

    def test_to_html_props2(self):
        node = HTMLNode("p", "Hewwo, wlord", None, {"id": "main-p", "class": "doge-blue"})
        expected = f' id="main-p" class="doge-blue"'
        self.assertEqual(node.props_to_html(), expected)

if __name__ == "__main__":
    unittest.main()
