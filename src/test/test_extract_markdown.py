import unittest

from src.inline_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdownLinksandImages(unittest.TestCase):
    def setUp(self):
        self.image1 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.image1out = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                          ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

        self.link1 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.link1out = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

        self.image_weird = "This is an ![[image]](https://example.com)) that is formatted with extra () and []"
        self.image_weird_out = []

        self.link_weird = "This is an [link]]((https://example.com)) that is formatted with extra () and []"
        self.link_weird_out = []

    def test_image_text(self):
        self.assertEqual(extract_markdown_images(self.image1), self.image1out)

    def test_link_text(self):
        self.assertEqual(extract_markdown_links(self.link1), self.link1out)

    def test_extra_para_brackets(self):
        self.assertEqual(extract_markdown_images(self.image_weird), self.image_weird_out)
        self.assertEqual(extract_markdown_links(self.link_weird), self.link_weird_out)

    def test_wrong_type_extract(self):
        self.assertEqual(extract_markdown_links(self.image1), [])
        self.assertEqual(extract_markdown_images(self.link1), [])