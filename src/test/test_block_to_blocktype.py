import unittest

from src.block_markdown import markdown_to_blocks, block_to_block_type


class TestBlockToBlocktype(unittest.TestCase):
    def setUp(self):
        self.blocks = """
            > Hello
            > World
            > Something

            # Header block

            This is a paragraph

            ``` python
            print('Hello World')
            ```

            - This is 
            - an unordered list 

            * an this is also
            * an unordered list 

            1. This is 
            2. an ordered list 
            3. with three numbers
        """
        self.normal_blocks = markdown_to_blocks(self.blocks)

        self.odd_blocks = """
            ##### Header 5 (should be normal header)

            > Incorrect quote
            turns into paragraph

            -List with no space 
            -turns into paragraph

            *List with no space 
            *turns into paragraph

            1. incorrectly numbered
            2. list 
            4. turns into paragraph

            1.Also if 
            2.There are no
            3. Spaces
        """
        self.odd_blocks_list = markdown_to_blocks(self.odd_blocks)

    def test_normal_blocks(self):
        self.assertEqual(block_to_block_type(self.normal_blocks[0]), "quote")
        self.assertEqual(block_to_block_type(self.normal_blocks[1]), "header")
        self.assertEqual(block_to_block_type(self.normal_blocks[2]), "paragraph")
        self.assertEqual(block_to_block_type(self.normal_blocks[3]), "code")
        self.assertEqual(block_to_block_type(self.normal_blocks[4]), "unordered-list")
        self.assertEqual(block_to_block_type(self.normal_blocks[5]), "unordered-list")
        self.assertEqual(block_to_block_type(self.normal_blocks[6]), "ordered-list")

    def test_odd_blocks(self):
        self.assertEqual(block_to_block_type(self.odd_blocks_list[0]), "header")
        self.assertEqual(block_to_block_type(self.odd_blocks_list[1]), "paragraph")
        self.assertEqual(block_to_block_type(self.odd_blocks_list[2]), "paragraph")
        self.assertEqual(block_to_block_type(self.odd_blocks_list[3]), "paragraph")
        self.assertEqual(block_to_block_type(self.odd_blocks_list[4]), "paragraph")
        self.assertEqual(block_to_block_type(self.odd_blocks_list[5]), "paragraph")