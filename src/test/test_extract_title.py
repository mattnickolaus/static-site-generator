import unittest

from src.generate_static import extract_title

class TestExtractTitle(unittest.TestCase):
    def setUp(self):
        self.markdown1 = "# Hello"
        self.markdown1_out = "Hello"

        self.markdown2 = "# Hello       "
        self.markdown2_out = "Hello"

        self.markdown3 = """# Title
        Here's a paragraph
        
        - list
        """
        self.markdown3_out = "Title"

        self.markdown4 = """# Title
        Here's a paragraph

        - list
        # Title 2
        """
        self.markdown4_out = "Title"

        self.markdown5 = """This should raise exception
        
        Title
        
        Here's a paragraph

        - list
        > Title 2
        """

    def test_extract_title_single_line(self):
        self.assertEqual(extract_title(self.markdown1), self.markdown1_out)
        self.assertEqual(extract_title(self.markdown2), self.markdown2_out)

    def test_extract_title_multiple_lines(self):
        self.assertEqual(extract_title(self.markdown3), self.markdown3_out)
        self.assertEqual(extract_title(self.markdown4), self.markdown4_out)

    def test_extract_title_exception(self):
        self.assertRaises(Exception, extract_title, self.markdown5)