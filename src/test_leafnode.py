import unittest
from leafnode import LeafNode
from parentnode import ParentNode

test_content1 = "Hello world!"
test_content2 = "Hewwo, wlord!"
test_content3 = "i am a child"
test_content4 = "i am a grandchild"

test_tag1 = "p"
test_tag2 = None
test_tag3 = "span"
test_tag3_1 = "div"
test_tag4 = "b"
test_tag4_1 = "span"
test_tag4_2 = "div"

class TestLeafNode(unittest.TestCase):
    def test_to_html1(self):
        node = LeafNode(test_tag1, test_content1)
        test = node.to_html()
        expected = f"<p>Hello world!</p>"
        self.assertEqual(test, expected)

    def test_to_html2(self):
        node = LeafNode(test_tag2, test_content2)
        test = node.to_html()
        expected = f"Hewwo, wlord!"
        self.assertEqual(test, expected)

    def test_to_html3(self):
        child_node = LeafNode(test_tag3, test_content3)
        parent_node = ParentNode(test_tag3_1, [child_node])
        test = parent_node.to_html()
        expected = f"<div><span>i am a child</span></div>"
        self.assertEqual(test, expected)

    def test_to_html4(self):
        grandchild_node = LeafNode(test_tag4, test_content4)
        child_node = ParentNode(test_tag4_1, [grandchild_node])
        parent_node = ParentNode(test_tag4_2, [child_node])
        test = parent_node.to_html()
        expected = f"<div><span><b>i am a grandchild</b></span></div>"
        self.assertEqual(test, expected)

if __name__ == "__main__":
    unittest.main()
