import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code
)

bolded_text = "This is text with a **bolded** word"
bolded_text2 = "This is text with a **bolded** word and another **bolded** word"
bolded_text3 = "This is text with multiple **bolded words** and another **bolded** word"
italic_text = "This is text with an *italic* word"
code_text = "This is text with a `code` word"

md_bold = "**"
md_italic = "*"
md_code = "`"

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_delimiter_bold(self):
        node = TextNode(bolded_text, text_type_text)
        splitted_node = split_nodes_delimiter([node], md_bold, text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text), 
                TextNode("bolded", text_type_bold), 
                TextNode(" word", text_type_text)
            ], splitted_node
        )
    
    def test_delimiter_bold2(self):
        node = TextNode(bolded_text2, text_type_text)
        splitted_node = split_nodes_delimiter([node], md_bold, text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and another ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text)
            ], splitted_node
        )

    def test_delimiter_bold3(self):
        node = TextNode(bolded_text3, text_type_text)
        splitted_node = split_nodes_delimiter([node], md_bold, text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with multiple ", text_type_text),
                TextNode("bolded words", text_type_bold),
                TextNode(" and another ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text)
            ], splitted_node
        )
    
    def test_delimiter_italic(self):
        node = TextNode(italic_text, text_type_text)
        splitted_node = split_nodes_delimiter([node], md_italic, text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text)
            ], splitted_node
        )
    
    def test_delimiter_code(self):
        node = TextNode(code_text, text_type_text)
        splitted_node = split_nodes_delimiter([node], md_code, text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code", text_type_code),
                TextNode(" word", text_type_text)
            ], splitted_node
        )

if __name__ == "__main__":
    unittest.main()
