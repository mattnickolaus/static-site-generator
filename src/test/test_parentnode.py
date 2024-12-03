import unittest

from src.htmlnode import ParentNode, LeafNode

class TestLeafNode(unittest.TestCase):
    def setUp(self):
        # Leaf node examples
        self.leaf_with_tag = LeafNode("b", "Bold text")
        self.leaf_without_tag = LeafNode(None, "Normal text")

        # Parent node with nested children
        self.nest_paragraph = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

    def test_leaf_node_with_tag(self):
        """Test LeafNode with an HTML tag."""
        self.assertEqual(self.leaf_with_tag.to_html(), "<b>Bold text</b>")

    def test_leaf_node_without_tag(self):
        """Test LeafNode without an HTML tag."""
        self.assertEqual(self.leaf_without_tag.to_html(), "Normal text")

    def test_parent_node_with_children(self):
        """Test ParentNode with nested LeafNodes."""
        expected_output = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(self.nest_paragraph.to_html(), expected_output)

    def test_empty_parent_node(self):
        """Test ParentNode with no children."""
        empty_parent = ParentNode("div", [])
        self.assertEqual(empty_parent.to_html(), "<div></div>")

    def test_parent_node_without_tag(self):
        """Test ParentNode without a tag."""
        parent_without_tag = ParentNode(
            None,
            [LeafNode("b", "Bold text"), LeafNode(None, "Normal text")],
        )
        self.assertRaises(ValueError, parent_without_tag.to_html)

    def test_nested_parent_nodes(self):
        """Test ParentNode with nested ParentNodes."""
        nested_parent = ParentNode(
            "div",
            [
                ParentNode("span", [LeafNode("b", "Nested Bold")]),
                LeafNode(None, "Outside span"),
            ],
        )
        expected_output = "<div><span><b>Nested Bold</b></span>Outside span</div>"
        self.assertEqual(nested_parent.to_html(), expected_output)