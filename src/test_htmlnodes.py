import unittest
from htmlnodes import (HTMLNode, ParentNode, LeafNode)

test_htmlnode1 = ["div", "Hello, world!", {"class": "greeting", "href": "https://boot.dev"}]
test_htmlnode2 = ["p", "Hewwo, wlord!", {"id": "main-p", "class": "doge-blue"}]

test_parentnode1 = ["p", 
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"), 
        LeafNode("i", "italic text"), 
        LeafNode(None, "Normal text")
    ]]
test_parentnode2 = ["h2",
    [
        LeafNode("b", "Bold text"), 
        LeafNode(None, "Normal text"), 
        LeafNode("i", "italic text"), 
        LeafNode(None, "Normal text")
    ]]

test_leaf_node1 = ["p", "Hello world!"]
test_leaf_node2 = [None, "Hewwo, wlord!"]
test_leaf_node3 = ["span", "i am a child", "div"]
test_leaf_node4 = ["b", "i am a grandchild", "span", "div"]

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(test_htmlnode1[0], test_htmlnode1[1], None, test_htmlnode1[2])
        test = node.props_to_html()
        expected = f' class="greeting" href="https://boot.dev"'
        self.assertEqual(test, expected)

    def test_to_html_props2(self):
        node = HTMLNode(test_htmlnode2[0], test_htmlnode2[1], None, test_htmlnode2[2])
        test = node.props_to_html()
        expected = f' id="main-p" class="doge-blue"'
        self.assertEqual(test, expected)

class TestParentNode(unittest.TestCase):
    def test_to_html_many_children(self):
        node = ParentNode(test_parentnode1[0], test_parentnode1[1])
        test = node.to_html()
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(test, expected)

    def test_headings(self):
        node = ParentNode(test_parentnode2[0], test_parentnode2[1])
        test = node.to_html()
        expected = "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>"
        self.assertEqual(test, expected)

class TestLeafNode(unittest.TestCase):
    def test_to_html1(self):
        node = LeafNode(test_leaf_node1[0], test_leaf_node1[1])
        test = node.to_html()
        expected = f"<p>Hello world!</p>"
        self.assertEqual(test, expected)

    def test_to_html2(self):
        node = LeafNode(test_leaf_node2[0], test_leaf_node2[1])
        test = node.to_html()
        expected = f"Hewwo, wlord!"
        self.assertEqual(test, expected)

    def test_to_html3(self):
        child_node = LeafNode(test_leaf_node3[0], test_leaf_node3[1])
        parent_node = ParentNode(test_leaf_node3[2], [child_node])
        test = parent_node.to_html()
        expected = f"<div><span>i am a child</span></div>"
        self.assertEqual(test, expected)

    def test_to_html4(self):
        grandchild_node = LeafNode(test_leaf_node4[0], test_leaf_node4[1])
        child_node = ParentNode(test_leaf_node4[2], [grandchild_node])
        parent_node = ParentNode(test_leaf_node4[3], [child_node])
        test = parent_node.to_html()
        expected = f"<div><span><b>i am a grandchild</b></span></div>"
        self.assertEqual(test, expected)

if __name__ == "__main__":
    unittest.main()