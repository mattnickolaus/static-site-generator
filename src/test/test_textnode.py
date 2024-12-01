import unittest

from src.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_print(self):
        italics_node = TextNode("Italics Node", "italic")
        italics_out = italics_node.__repr__()
        self.assertEqual(italics_out, "TextNode(Italics Node, italic, None)")

        image_node = TextNode("Image Node", "image", "https://avatars.githubusercontent.com/u/97491556?v=4")
        image_out = image_node.__repr__()
        self.assertEqual(image_out, "TextNode(Image Node, image, https://avatars.githubusercontent.com/u/97491556?v=4)")

    def test_normal_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://github.com")
        node2 = TextNode("This is a link node", TextType.LINK, "https://github.com")
        self.assertEqual(node, node2)

    def test_url_with_wrong_type(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://github.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_link_without_value(self):
        node = TextNode("This is a link node", TextType.LINK)
        node2 = TextNode("This is a link node", TextType.LINK, None)
        self.assertEqual(node, node2)

    def test_equals_property(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertTrue(node.__eq__(node2))



if __name__ == "__main__":
    unittest.main()