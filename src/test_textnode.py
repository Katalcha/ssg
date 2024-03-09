import unittest

from textnode import (
    TextNode, 
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)

test_url_bootev = "https://www.boot.dev"
test_url_freecodecamp= "https://www.freecodecamp.org"
text_content = "This is a text node"
text_content_false = "node text a is This"

class TestTextNode(unittest.TestCase):
    def test_eq_true(self):
        node = TextNode(text_content, text_type_bold)
        node2 = TextNode(text_content, text_type_bold)
        self.assertEqual(node, node2)

    def test_eq_text_type_false(self):
        node = TextNode(text_content, text_type_link)
        node2 = TextNode(text_content, text_type_italic)
        self.assertNotEqual(node, node2)

    def test_eq_content_false(self):
        node = TextNode(text_content, text_type_code)
        node2 = TextNode(text_content_false, text_type_code)
        self.assertNotEqual(node, node2)

    def test_eq_content_and_text_type_false(self):
        node = TextNode(text_content, text_type_image)
        node2 = TextNode(text_content_false, text_type_text)
        self.assertNotEqual(node, node2)

    def test_eq_when_none_false(self):
        node = TextNode(text_content, text_type_bold)
        node2 = TextNode(None, None)
        self.assertNotEqual(node, node2)

    def test_eq_when_both_none_true(self):
        node = TextNode(None, None)
        node2 = TextNode(None, None)
        self.assertEqual(node, node2)

    def test_eq_url_true(self):
        node = TextNode(text_content, text_type_bold, test_url_bootev)
        node2 = TextNode(text_content, text_type_bold, test_url_bootev)
        self.assertEqual(node, node2)

    def test_eq_url_false(self):
        node = TextNode(text_content, text_type_text, test_url_bootev)
        node2 = TextNode(text_content, text_type_text, test_url_freecodecamp)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        expected = TextNode(text_content, text_type_code, test_url_bootev)
        self.assertEqual(f"TextNode({text_content}, {text_type_code}, {test_url_bootev})", repr(expected))

if __name__ == "__main__":
    unittest.main()
