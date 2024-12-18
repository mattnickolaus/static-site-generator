import unittest

from src.block_markdown import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def setUp(self):
        self.block1 = """
        # This is a heading 

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""

        self.block1_out = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]

        self.block2 = """
# This is a heading

## Another heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

Paragraph ![image](image.com) with an image

* This is the first list item in a list block
* This is a list item
* This is another list item
"""

        self.block2_out = [
            "# This is a heading",
            "## Another heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "Paragraph ![image](image.com) with an image",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]

        self.block_with_extra_spaces = """
  # This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

 * This is the first list item in a list block
* This is a list item
* This is another list item
"""

        self.block_with_extra_spaces_out = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]

        self.block_with_extra_returns = """
# This is a heading



This is a paragraph of text. It has some **bold** and *italic* words inside of it.





* This is the first list item in a list block
* This is a list item
* This is another list item
"""

        self.block_with_extra_returns_out = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]

    def test_normal_markdown(self):
        self.assertEqual(markdown_to_blocks(self.block1), self.block1_out)
        self.assertEqual(markdown_to_blocks(self.block2), self.block2_out)

    def test_extra_spaces(self):
        self.assertEqual(markdown_to_blocks(self.block_with_extra_spaces), self.block_with_extra_spaces_out)

    def test_extra_returns(self):
        self.assertEqual(markdown_to_blocks(self.block_with_extra_returns), self.block_with_extra_returns_out)