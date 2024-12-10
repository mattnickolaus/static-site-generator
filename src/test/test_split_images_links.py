import unittest

from src.inline_markdown import split_nodes_image, split_nodes_link
from src.textnode import TextType, TextNode


class TestSplitNodesImagesLinks(unittest.TestCase):
    def setUp(self):
        self.image_node1 = [TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.TEXT,
        )]
        #    def __init__(self, text, text_type, url=None):
        self.image_node1_out = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
        ]

        self.image_node2 = [TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) and some more",
            TextType.TEXT,
        )]
        self.image_node2_out = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and some more", TextType.TEXT)
        ]

        self.nothing = [TextNode(
            "There's nothing here",
            TextType.TEXT,
        )]

        self.link_node1 = [TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )]
        self.link_node1_out = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
        ]

        self.link_node2 = [TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and more",
            TextType.TEXT,
        )]
        self.link_node2_out = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            TextNode(" and more", TextType.TEXT)
        ]

        self.link_node_back2back = [TextNode(
            "This is text with a links back to back [to boot dev](https://www.boot.dev)[to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )]
        self.link_node_back2back_out = [
            TextNode("This is text with a links back to back ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]

    def test_split_nodes_images(self):
        self.assertEqual(split_nodes_image(self.image_node1), self.image_node1_out)
        self.assertEqual(split_nodes_image(self.image_node2), self.image_node2_out)

    def test_split_nodes_links(self):
        self.assertEqual(split_nodes_link(self.link_node1), self.link_node1_out)
        self.assertEqual(split_nodes_link(self.link_node2), self.link_node2_out)
        self.assertEqual(split_nodes_link(self.link_node_back2back), self.link_node_back2back_out)

    def test_nothing_nodes(self):
        self.assertEqual(split_nodes_image(self.nothing), self.nothing)
        self.assertEqual(split_nodes_image(self.nothing), self.nothing)
