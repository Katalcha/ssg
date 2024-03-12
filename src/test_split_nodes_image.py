import unittest
from split_nodes_image import split_nodes_image
from textnode import (
    TextNode,
    text_type_text,
    text_type_image
)

test_textnode_content1 = "This is text with a python image ![Python Image](https://i.imgur.com/zjjcJKZ.png)"
test_textnode_content2 = "![Example.com Image](https://www.example.com/image.png)"
test_textnode_content3 = "This is text with a python image ![Python Image](https://i.imgur.com/zjjcJKZ.png) and a Go-lang-gopher image ![Go-Lang Gopher](https://i.imgur.com/3elNhQu.png)"

test_url_python_img = "https://i.imgur.com/zjjcJKZ.png"
test_url_examplecom_img = "https://www.example.com/image.png"
test_url_gopher_img = "https://i.imgur.com/3elNhQu.png"

class TestSplitNodesImage(unittest.TestCase):
    def test_split_nodes_image(self):
        test_data = TextNode(test_textnode_content1, text_type_text)
        test_nodes = split_nodes_image([test_data])
        expected = [
            TextNode("This is text with a python image ", text_type_text),
            TextNode("Python Image", text_type_image, test_url_python_img)
        ]
        self.assertListEqual(expected, test_nodes)

    def test_split_nodes_image_single_image(self):
        test_data = TextNode(test_textnode_content2, text_type_text)
        test_nodes = split_nodes_image([test_data])
        expected = [TextNode("Example.com Image", text_type_image, test_url_examplecom_img)]
        self.assertListEqual(expected, test_nodes)

    def test_split_nodes_multiple_images(self):
        test_data = TextNode(test_textnode_content3, text_type_text)
        test_nodes = split_nodes_image([test_data])
        expected = [
            TextNode("This is text with a python image ", text_type_text),
            TextNode("Python Image", text_type_image, test_url_python_img),
            TextNode(" and a Go-lang-gopher image ", text_type_text),
            TextNode("Go-Lang Gopher", text_type_image, test_url_gopher_img),
        ]
        self.assertListEqual(expected, test_nodes)

if __name__ == "__main__":
    unittest.main()
