import unittest
from md_to_md_blocks import (
    markdown_to_html_node,
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_ordered_list,
    block_type_unordered_list,
    block_type_quote
)

test_content_md_to_blocks1 = """
This is a **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
test_content_md_to_blocks2 = """
This is a **bolded** paragraph with way too much new lines
My Function assures that these new lines get removed




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
test_content_md_to_blocks3 = '''
This is a **bolded** paragraph with way too much new lines
My Function **assures** that *these* new lines get `removed`




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line




* This is a list
* with items




1. This is a numered list
2. with items

Here is a Link to freecodecamp [freecodecamp.org](https://freecodecamp.org)

And here is a Link to boot.dev [boot.dev](https://boot.dev)





And here is an image of Go-Langs mascot ![Go-Lang](https://imgur.com/3elNhQu)
'''
test_content_block_to_blocktype1 = "# This is a heading"
test_content_block_to_blocktype2 = "## This is a heading"
test_content_block_to_blocktype3 = "### This is a heading"
test_content_block_to_blocktype4 = "#### This is a heading"
test_content_block_to_blocktype5 = "##### This is a heading"
test_content_block_to_blocktype6 = "###### This is a heading"
test_content_block_to_blocktype7 = "```\ncode here\n```"
test_content_block_to_blocktype8 = "> quote\n> more quote\n> even more quote"
test_content_block_to_blocktype9 = "* list\n* items\n* more items"
test_content_block_to_blocktype10 = "1. list\n2. items\n3. more items"
test_content_block_to_blocktype11 = "this is a paragraph"
test_content_to_html1 = """
This is **bolded** paragraph
text in a p
tag here

"""
test_content_to_html2 = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""
test_content_to_html3 = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""
test_content_to_html4 = """
# this is an h1

this is paragraph text

## this is an h2
"""
test_content_to_html5 = """
> This is a
> blockquote block

this is paragraph text

"""

class TestMarkDownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        test = markdown_to_blocks(test_content_md_to_blocks1)
        expected = [
            "This is a **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items"
        ]
        self.assertEqual(test, expected)

    def test_markdown_to_blocks_newlines(self):
        test = markdown_to_blocks(test_content_md_to_blocks2)
        expected = [
            "This is a **bolded** paragraph with way too much new lines\nMy Function assures that these new lines get removed",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items"
        ]
        self.assertEqual(test, expected)

    def test_markdown_to_blocks_newlines2(self):
        test = markdown_to_blocks(test_content_md_to_blocks3)
        expected = [
            "This is a **bolded** paragraph with way too much new lines\nMy Function **assures** that *these* new lines get `removed`",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items",
            "1. This is a numered list\n2. with items",
            "Here is a Link to freecodecamp [freecodecamp.org](https://freecodecamp.org)",
            "And here is a Link to boot.dev [boot.dev](https://boot.dev)",
            "And here is an image of Go-Langs mascot ![Go-Lang](https://imgur.com/3elNhQu)"
        ]
        self.assertEqual(test, expected)

class TestBlockToBlockType(unittest.TestCase):    
    def test_block_to_block_type_headings(self):
        expected = block_type_heading
        test1 = block_to_block_type(test_content_block_to_blocktype1)
        test2 = block_to_block_type(test_content_block_to_blocktype2)
        test3 = block_to_block_type(test_content_block_to_blocktype3)
        test4 = block_to_block_type(test_content_block_to_blocktype4)
        test5 = block_to_block_type(test_content_block_to_blocktype5)
        test6 = block_to_block_type(test_content_block_to_blocktype6)

        self.assertEqual(test1, expected)
        self.assertEqual(test2, expected)
        self.assertEqual(test3, expected)
        self.assertEqual(test4, expected)
        self.assertEqual(test5, expected)
        self.assertEqual(test6, expected)

    def test_block_to_block_type_code(self):
        expected = block_type_code
        test = block_to_block_type(test_content_block_to_blocktype7)
        self.assertEqual(test, expected)

    def test_block_to_block_type_quote(self):
        expected = block_type_quote
        test = block_to_block_type(test_content_block_to_blocktype8)
        self.assertEqual(test, expected)

    def test_block_to_block_type_u_list(self):
        expected = block_type_unordered_list
        test = block_to_block_type(test_content_block_to_blocktype9)
        self.assertEqual(test, expected)

    def test_block_to_block_type_o_list(self):
        expected = block_type_ordered_list
        test = block_to_block_type(test_content_block_to_blocktype10)
        self.assertEqual(test, expected)

    def test_block_to_block_type_paragraph(self):
        expected = block_type_paragraph
        test = block_to_block_type(test_content_block_to_blocktype11)
        self.assertEqual(test, expected) 

class TestXToHTMLNode(unittest.TestCase):
    def test_single_paragraph(self):
        node = markdown_to_html_node(test_content_to_html1)
        test = node.to_html()
        expected = "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>"
        self.assertEqual(test, expected)

    def test_paragraphs(self):
        node = markdown_to_html_node(test_content_to_html2)
        test = node.to_html()
        expected = "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
        self.assertEqual(test, expected)

    def test_lists(self):
        node = markdown_to_html_node(test_content_to_html3)
        test = node.to_html()
        expected = "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>"
        self.assertEqual(test, expected)

    def test_headings(self):
        node = markdown_to_html_node(test_content_to_html4)
        test = node.to_html()
        expected = "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>"
        self.assertEqual(test, expected)

    def test_blockquote(self):
        node = markdown_to_html_node(test_content_to_html5)
        test = node.to_html()
        expected = "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>"
        self.assertEqual(test, expected)

if __name__ == "__main__":
    unittest.main()
