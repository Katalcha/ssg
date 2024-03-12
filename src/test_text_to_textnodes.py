import unittest
from text_to_textnodes import text_to_textnodes
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)

test_textnode_content1 = "This is the bolded word **text** with an *italic* word beneath it and a `code block` and an ![Python Image](https://i.imgur.com/zjjcJKZ.png) and a [Boot.dev Link](https://boot.dev)"

test_url_python = "https://i.imgur.com/zjjcJKZ.png"
test_url_bootdev = "https://boot.dev"

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        nodes = text_to_textnodes(test_textnode_content1)
        expected = [
                TextNode("This is the bolded word ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word beneath it and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("Python Image", text_type_image, test_url_python),
                TextNode(" and a ", text_type_text),
                TextNode("Boot.dev Link", text_type_link, test_url_bootdev),
            ]
        self.assertListEqual(expected, nodes)

if __name__ == "__main__":
    unittest.main()
