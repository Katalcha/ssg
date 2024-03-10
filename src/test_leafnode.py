import unittest

from leafnode import LeafNode
from parentnode import ParentNode

class TestLeafNode(unittest.TestCase):
    def test_to_html1(self):
        node = LeafNode("p", "Hello world!")
        expected = f"<p>Hello world!</p>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html2(self):
        node = LeafNode(None, "Hello world!")
        expected = f"Hello world!"
        self.assertEqual(node.to_html(), expected)

    def test_to_html3(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html4(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()
