import unittest
from markdown_to_blocks import markdown_to_blocks

test_data_md1 = """
This is a **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""

test_data_md2 = """
This is a **bolded** paragraph with way too much new lines
My Function assures that these new lines get removed




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""

test_data_md3 = '''
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

class TestMarkDownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        test = markdown_to_blocks(test_data_md1)
        expected = [
            "This is a **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items"
        ]
        self.assertEqual(test, expected)

    def test_markdown_to_blocks_newlines(self):
        test = markdown_to_blocks(test_data_md2)
        expected = [
            "This is a **bolded** paragraph with way too much new lines\nMy Function assures that these new lines get removed",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items"
        ]
        self.assertEqual(test, expected)

    def test_markdown_to_blocks_newlines2(self):
        test = markdown_to_blocks(test_data_md3)
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

if __name__ == "__main__":
    unittest.main()
