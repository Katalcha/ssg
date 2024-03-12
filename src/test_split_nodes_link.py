import unittest
from split_nodes_link import split_nodes_link
from textnode import (
    TextNode,
    text_type_text,
    text_type_link
)

test_textnode_content1 = "This is text with a link to boot.dev [boot.dev](https://boot.dev) and another link to boot.devs blog [boot.dev blog](https://blog.boot.dev) with text that follows"

test_url_bootdev = "https://boot.dev"
test_url_bootdev_blog = "https://blog.boot.dev"

class TestSplitNodesLink(unittest.TestCase):
    def test_split_links(self):
        test_data = TextNode(test_textnode_content1, text_type_text)
        test_nodes = split_nodes_link([test_data])
        expected = [
            TextNode("This is text with a link to boot.dev ", text_type_text),
            TextNode("boot.dev", text_type_link, test_url_bootdev),
            TextNode(" and another link to boot.devs blog ", text_type_text),
            TextNode("boot.dev blog", text_type_link, test_url_bootdev_blog),
            TextNode(" with text that follows", text_type_text)
        ]
        self.assertListEqual(expected, test_nodes)

if __name__ == "__main__":
    unittest.main()
