import unittest
from block_to_block_type import (
    block_to_block_type,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,
    block_type_paragraph
)

test_content_heading1 = "# This is a heading"
test_content_heading2 = "## This is a heading"
test_content_heading3 = "### This is a heading"
test_content_heading4 = "#### This is a heading"
test_content_heading5 = "##### This is a heading"
test_content_heading6 = "###### This is a heading"
test_content_code = "```\ncode here\n```"
test_content_quote = "> quote\n> more quote\n> even more quote"
test_content_u_list = "* list\n* items\n* more items"
test_content_o_list = "1. list\n2. items\n3. more items"
test_content_paragraph = "this is a paragraph"

class TestBlockToBlockType(unittest.TestCase):    
    def test_block_to_block_type_headings(self):
        expected = block_type_heading
        test1 = block_to_block_type(test_content_heading1)
        test2 = block_to_block_type(test_content_heading2)
        test3 = block_to_block_type(test_content_heading3)
        test4 = block_to_block_type(test_content_heading4)
        test5 = block_to_block_type(test_content_heading5)
        test6 = block_to_block_type(test_content_heading6)

        self.assertEqual(test1, expected)
        self.assertEqual(test2, expected)
        self.assertEqual(test3, expected)
        self.assertEqual(test4, expected)
        self.assertEqual(test5, expected)
        self.assertEqual(test6, expected)

    def test_block_to_block_type_code(self):
        expected = block_type_code
        test = block_to_block_type(test_content_code)
        self.assertEqual(test, expected)

    def test_block_to_block_type_quote(self):
        expected = block_type_quote
        test = block_to_block_type(test_content_quote)
        self.assertEqual(test, expected)

    def test_block_to_block_type_u_list(self):
        expected = block_type_unordered_list
        test = block_to_block_type(test_content_u_list)
        self.assertEqual(test, expected)

    def test_block_to_block_type_o_list(self):
        expected = block_type_ordered_list
        test = block_to_block_type(test_content_o_list)
        self.assertEqual(test, expected)

    def test_block_to_block_type_paragraph(self):
        expected = block_type_paragraph
        test = block_to_block_type(test_content_paragraph)
        self.assertEqual(test, expected)

if __name__ == "__main__":
    unittest.main()
