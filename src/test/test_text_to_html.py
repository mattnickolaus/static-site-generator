import unittest

from src.htmlnode import LeafNode, text_node_to_html_node
from src.textnode import TextNode

class TestTextToHtml(unittest.TestCase):
    def setUp(self):
        # text, text_type, url=None
        self.text_node = TextNode("Normal Text", "text")
        self.text_no_tag = text_node_to_html_node(self.text_node)

        self.bold_node = TextNode("Bold Text", "bold")
        self.bold = text_node_to_html_node(self.bold_node)

        self.italic_node = TextNode("Italic Text", "italic")
        self.italic = text_node_to_html_node(self.italic_node)

        self.code_node = TextNode("Code Text", "code")
        self.code = text_node_to_html_node(self.code_node)

        self.link_node = TextNode("Click here", "link", "boot.dev")
        self.link = text_node_to_html_node(self.link_node)

        self.image_node = TextNode("Alt Image", "image", "image.jpg")
        self.image = text_node_to_html_node(self.image_node)

    def test_text_no_tag(self):
        expected_output = "Normal Text"
        self.assertEqual(self.text_no_tag.to_html(), expected_output)

    def test_bold(self):
        expected_output = "<b>Bold Text</b>"
        self.assertEqual(self.bold.to_html(), expected_output)

    def test_italic(self):
        expected_output = "<i>Italic Text</i>"
        self.assertEqual(self.italic.to_html(), expected_output)

    def test_code(self):
        expected_output = "<code>Code Text</code>"
        self.assertEqual(self.code.to_html(), expected_output)

    def test_link(self):
        expected_output = '<a href="boot.dev">Click here</a>'
        self.assertEqual(self.link.to_html(), expected_output)

    def test_image(self):
        expected_output = '<img src="image.jpg" alt="Alt Image"></img>'
        self.assertEqual(self.image.to_html(), expected_output)
