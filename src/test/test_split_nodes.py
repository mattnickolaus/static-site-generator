import unittest

from src.textnode import TextNode, TextType
from src.inline_markdown import split_nodes_delimiter

class TestTextToHtml(unittest.TestCase):
    def setUp(self):
        self.text_no_other = TextNode('This is just text', TextType.TEXT)
        self.single_bold = TextNode('This is **bold**', TextType.TEXT)
        self.single_bold2 = TextNode('This is also **bold** for another', TextType.TEXT)

        self.single_italics = TextNode('This is *italics* somethings else', TextType.TEXT)
        self.single_code = TextNode('This is a `code block`', TextType.TEXT)

        self.double_bold = TextNode('This is **bold** this is also **bold** right?', TextType.TEXT)
        self.double_italics = TextNode('This is *italics* somethings *else*', TextType.TEXT)
        self.double_code = TextNode('This is `code block` and `another`', TextType.TEXT)

        # output nodes for each
        self.text_no_other_out = [TextNode('This is just text', TextType.TEXT)]
        self.single_bold_out = [TextNode('This is ', TextType.TEXT),
                                TextNode('bold', TextType.BOLD)]
        self.single_italics_out = [TextNode('This is ', TextType.TEXT),
                                   TextNode('italics', TextType.ITALIC),
                                   TextNode(' somethings else', TextType.TEXT),]
        self.single_code_out = [TextNode('This is a ', TextType.TEXT),
                                TextNode('code block', TextType.CODE)]

        self.double_bold_out = [TextNode('This is ', TextType.TEXT),
                                TextNode('bold', TextType.BOLD),
                                TextNode('This is also ', TextType.TEXT),
                                TextNode('bold', TextType.BOLD),
                                TextNode(' for another', TextType.TEXT)]

    def test_split_nodes_single_bold(self):
        self.assertEqual(split_nodes_delimiter([self.single_bold], '**', TextType.BOLD),
                         self.single_bold_out)

    def test_split_nodes_single_italics(self):
        self.assertEqual(split_nodes_delimiter([self.single_italics], '*', TextType.ITALIC),
                         self.single_italics_out)

    def test_split_nodes_single_code(self):
        self.assertEqual(split_nodes_delimiter([self.single_code], '`', TextType.CODE),
                         self.single_code_out)

    def test_split_nodes_double_bold(self):
        self.assertEqual(split_nodes_delimiter([self.single_bold, self.single_bold2], '**', TextType.BOLD),
                         self.double_bold_out)

    def test_split_nodes_no_delimiter_in_text(self):
        self.assertEqual(split_nodes_delimiter([self.text_no_other], '**', TextType.BOLD),
                         self.text_no_other_out)

