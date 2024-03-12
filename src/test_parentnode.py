import unittest
from parentnode import ParentNode
from leafnode import LeafNode

test_content1 = [
    "p",
    [
        LeafNode("b", "Bold text"), 
        LeafNode(None, "Normal text"), 
        LeafNode("i", "italic text"), 
        LeafNode(None, "Normal text")
    ]
]

test_content2 = [
    "h2",
    [
        LeafNode("b", "Bold text"), 
        LeafNode(None, "Normal text"), 
        LeafNode("i", "italic text"), 
        LeafNode(None, "Normal text")
    ]
]

class TestParentNode(unittest.TestCase):
    def test_to_html_many_children(self):
        node = ParentNode(test_content1[0], test_content1[1])
        test = node.to_html()
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(test, expected)

    def test_headings(self):
        node = ParentNode(test_content2[0], test_content2[1])
        test = node.to_html()
        expected = "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>"
        self.assertEqual(test, expected)

if __name__ == "__main__":
    unittest.main()