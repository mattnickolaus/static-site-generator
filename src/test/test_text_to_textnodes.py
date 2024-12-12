import unittest

from src.inline_markdown import text_to_textnodes
from src.textnode import TextType, TextNode


class TestSplitNodeImageLink(unittest.TestCase):
    def setUp(self):
        self.line1 = "This is **text** with a *something* ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [to boot dev](https://www.boot.dev)"
        self.line1_out = [
            TextNode("This is ", TextType.TEXT, None),
            TextNode("text", TextType.BOLD, None),
            TextNode(" with a ", TextType.TEXT, None),
            TextNode("something", TextType.ITALIC, None),
            TextNode(" ", TextType.TEXT, None),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT, None),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev")
        ]

        self.line2 = "`code`**bold** with a *italic* [to youtube](https://www.youtube.com/@bootdotdev) and ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [to boot dev](https://www.boot.dev)"
        self.line2_out = [
            TextNode("code", TextType.CODE, None),
            TextNode("bold", TextType.BOLD, None),
            TextNode(" with a ", TextType.TEXT, None),
            TextNode("italic", TextType.ITALIC, None),
            TextNode(" ", TextType.TEXT, None),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            TextNode(" and ", TextType.TEXT, None),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT, None),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev")
        ]

        self.code_block = "```code block``` *italic* **bold**"
        self.code_block_out = [
            TextNode("code block", TextType.CODE, None),
            TextNode(" ", TextType.TEXT, None),
            TextNode("italic", TextType.ITALIC, None),
            TextNode(" ", TextType.TEXT, None),
            TextNode("bold", TextType.BOLD, None)
        ]

        self.line_multiple = "This **is** **text** **with** a *something* ![rick roll](https://i.imgur.com/aKaOqIh.gif), [image example](http://example.com) and this [to boot dev](https://www.boot.dev)"
        self.line_multiple_out = [
            TextNode("This ", TextType.TEXT, None),
            TextNode("is", TextType.BOLD, None),
            TextNode(" ", TextType.TEXT, None),
            TextNode("text", TextType.BOLD, None),
            TextNode(" ", TextType.TEXT, None),
            TextNode("with", TextType.BOLD, None),
            TextNode(" a ", TextType.TEXT, None),
            TextNode("something", TextType.ITALIC, None),
            TextNode(" ", TextType.TEXT, None),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(", ", TextType.TEXT, None),
            TextNode("image example", TextType.LINK, "http://example.com"),
            TextNode(" and this ", TextType.TEXT, None),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev")
        ]

    def test_normal_complex_lines(self):
        self.assertEqual(text_to_textnodes(self.line1), self.line1_out)
        self.assertEqual(text_to_textnodes(self.line2), self.line2_out)

    def test_code_block(self):
        self.assertEqual(text_to_textnodes(self.code_block), self.code_block_out)

    def test_line_multiple(self):
        self.assertEqual(text_to_textnodes(self.line_multiple), self.line_multiple_out)