import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def setUp(self):
        self.paragraph = LeafNode("p", "This is a paragraph.")
        self.link = LeafNode("a", "Click here", {"href": "https://www.google.com"})
        self.header = LeafNode("h1", "Main Header", {"class":"main_header"})

        self.no_tag = LeafNode(tag=None, value="No Tag")

        self.no_value = LeafNode(tag="p", value=None, props={"class":"no_value"})

    def test_init(self):
        self.assertEqual(self.paragraph.tag, "p")
        self.assertEqual(self.paragraph.value, "This is a paragraph.")

        self.assertEqual(self.link.tag, "a")
        self.assertEqual(self.link.props, {"href": "https://www.google.com"})

        self.assertEqual(self.header.tag, "h1")
        self.assertEqual(self.header.value, "Main Header")
        self.assertEqual(self.header.props, {"class":"main_header"})

        self.assertEqual(self.no_tag.tag, None)
        self.assertEqual(self.no_tag.value, "No Tag")

    def test_to_html(self):
        self.assertEqual(self.paragraph.to_html(), "<p>This is a paragraph.</p>")
        self.assertEqual(self.link.to_html(), '<a href="https://www.google.com">Click here</a>')
        self.assertEqual(self.header.to_html(), '<h1 class="main_header">Main Header</h1>')
        self.assertEqual(self.no_tag.to_html(), 'No Tag')

    def test_edge_cases(self):
        self.assertRaises(ValueError, self.no_value.to_html)



