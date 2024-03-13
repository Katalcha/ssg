import unittest
from md_lines_to_text_nodes import (
    text_to_textnodes,
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    extract_markdown_images,
    extract_markdown_links
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)

test_content_text_to_textnodes = ["This is the bolded word **text** with an *italic* word beneath it and a `code block` and an ![Python Image](https://i.imgur.com/zjjcJKZ.png) and a [Boot.dev Link](https://boot.dev)", "https://i.imgur.com/zjjcJKZ.png", "https://boot.dev"]

test_content_split_nodes_delimiter1 = ["This is text with a **bolded** word", "**"]
test_content_split_nodes_delimiter2 = ["This is text with a **bolded** word and another **bolded** word", "**"]
test_content_split_nodes_delimiter3 = ["This is text with multiple **bolded words** and another **bolded** word", "**"]
test_content_split_nodes_delimiter4 = ["This is text with an *italic* word", "*"]
test_content_split_nodes_delimiter5 = ["This is text with a `code` word", "`"]

test_content_split_nodes_image1 = ["This is text with a python image ![Python Image](https://i.imgur.com/zjjcJKZ.png)", "https://i.imgur.com/zjjcJKZ.png"]
test_content_split_nodes_image2 = ["![Example.com Image](https://www.example.com/image.png)", "https://www.example.com/image.png"]
test_content_split_nodes_image3 = ["This is text with a python image ![Python Image](https://i.imgur.com/zjjcJKZ.png) and a Go-lang-gopher image ![Go-Lang Gopher](https://i.imgur.com/3elNhQu.png)", "https://i.imgur.com/zjjcJKZ.png", "https://i.imgur.com/3elNhQu.png"]

test_content_split_nodes_link = ["This is text with a link to boot.dev [boot.dev](https://boot.dev) and another link to boot.devs blog [boot.dev blog](https://blog.boot.dev) with text that follows", "https://boot.dev", "https://blog.boot.dev"]

test_content_extract_markdown_images = ["This is text with a python image ![python-img](https://i.imgur.com/zjjcJKZ.png)", "python-img", "https://i.imgur.com/zjjcJKZ.png"]

test_content_extract_markdown_links = ["This is text with a boot.dev-link [boot.dev](https://boot.dev) and a freecodecamp.org-link [freecodecamp](https://www.freecodecamp.org)", "boot.dev", "https://boot.dev", "freecodecamp", "https://www.freecodecamp.org"]

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        nodes = text_to_textnodes(test_content_text_to_textnodes[0])
        expected = [
                TextNode("This is the bolded word ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word beneath it and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("Python Image", text_type_image, test_content_text_to_textnodes[1]),
                TextNode(" and a ", text_type_text),
                TextNode("Boot.dev Link", text_type_link, test_content_text_to_textnodes[2]),
            ]
        self.assertListEqual(expected, nodes)

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_delimiter_bold(self):
        node = TextNode(test_content_split_nodes_delimiter1[0], text_type_text)
        test = split_nodes_delimiter([node], test_content_split_nodes_delimiter1[1], text_type_bold)
        expected = [
            TextNode("This is text with a ", text_type_text), 
            TextNode("bolded", text_type_bold), 
            TextNode(" word", text_type_text)
        ]
        self.assertListEqual(test, expected)
    
    def test_delimiter_bold2(self):
        node = TextNode(test_content_split_nodes_delimiter2[0], text_type_text)
        test = split_nodes_delimiter([node], test_content_split_nodes_delimiter2[1], text_type_bold)
        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("bolded", text_type_bold),
            TextNode(" word and another ", text_type_text),
            TextNode("bolded", text_type_bold),
            TextNode(" word", text_type_text)
        ]
        self.assertListEqual(test, expected)

    def test_delimiter_bold3(self):
        node = TextNode(test_content_split_nodes_delimiter3[0], text_type_text)
        test = split_nodes_delimiter([node], test_content_split_nodes_delimiter3[1], text_type_bold)
        expected = [
            TextNode("This is text with multiple ", text_type_text),
            TextNode("bolded words", text_type_bold),
            TextNode(" and another ", text_type_text),
            TextNode("bolded", text_type_bold),
            TextNode(" word", text_type_text)
        ]
        self.assertListEqual(test, expected)
    
    def test_delimiter_italic(self):
        node = TextNode(test_content_split_nodes_delimiter4[0], text_type_text)
        test = split_nodes_delimiter([node], test_content_split_nodes_delimiter4[1], text_type_italic)
        expected = [
            TextNode("This is text with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word", text_type_text)
        ]
        self.assertListEqual(test, expected)
    
    def test_delimiter_code(self):
        node = TextNode(test_content_split_nodes_delimiter5[0], text_type_text)
        test = split_nodes_delimiter([node], test_content_split_nodes_delimiter5[1], text_type_code)
        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code", text_type_code),
            TextNode(" word", text_type_text)
        ]
        self.assertListEqual(test, expected)

class TestSplitNodesImage(unittest.TestCase):
    def test_split_nodes_image(self):
        test_data = TextNode(test_content_split_nodes_image1[0], text_type_text)
        test_nodes = split_nodes_image([test_data])
        expected = [
            TextNode("This is text with a python image ", text_type_text),
            TextNode("Python Image", text_type_image, test_content_split_nodes_image1[1])
        ]
        self.assertListEqual(expected, test_nodes)

    def test_split_nodes_image_single_image(self):
        test_data = TextNode(test_content_split_nodes_image2[0], text_type_text)
        test_nodes = split_nodes_image([test_data])
        expected = [TextNode("Example.com Image", text_type_image, test_content_split_nodes_image2[1])]
        self.assertListEqual(expected, test_nodes)

    def test_split_nodes_multiple_images(self):
        test_data = TextNode(test_content_split_nodes_image3[0], text_type_text)
        test_nodes = split_nodes_image([test_data])
        expected = [
            TextNode("This is text with a python image ", text_type_text),
            TextNode("Python Image", text_type_image, test_content_split_nodes_image3[1]),
            TextNode(" and a Go-lang-gopher image ", text_type_text),
            TextNode("Go-Lang Gopher", text_type_image, test_content_split_nodes_image3[2]),
        ]
        self.assertListEqual(expected, test_nodes)

class TestSplitNodesLink(unittest.TestCase):
    def test_split_links(self):
        test_data = TextNode(test_content_split_nodes_link[0], text_type_text)
        test_nodes = split_nodes_link([test_data])
        expected = [
            TextNode("This is text with a link to boot.dev ", text_type_text),
            TextNode("boot.dev", text_type_link, test_content_split_nodes_link[1]),
            TextNode(" and another link to boot.devs blog ", text_type_text),
            TextNode("boot.dev blog", text_type_link, test_content_split_nodes_link[2]),
            TextNode(" with text that follows", text_type_text)
        ]
        self.assertListEqual(expected, test_nodes)

class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        test = extract_markdown_images(test_content_extract_markdown_images[0])
        expected = [(test_content_extract_markdown_images[1], test_content_extract_markdown_images[2])]
        self.assertListEqual(expected, test)

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        test = extract_markdown_links(test_content_extract_markdown_links[0])
        expected = [(test_content_extract_markdown_links[1], test_content_extract_markdown_links[2]), (test_content_extract_markdown_links[3], test_content_extract_markdown_links[4])]
        self.assertListEqual(expected, test)

if __name__ == "__main__":
    unittest.main()
