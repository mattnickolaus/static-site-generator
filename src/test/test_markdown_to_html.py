import unittest

from src.block_markdown import *

class TestMarkdownToHtml(unittest.TestCase):
    def setUp(self):
        self.normal_blocks = """
            > Hello *italic*
            > World

            ### Header block

            This is a paragraph
            This is also a paragraph but with **bold**
            And another *paragraph*

            ```
            print('Hello World')
            print('Something else')
            ```

            - This is [link](http://link.com)
            - an unordered list 

            * and *this* is also
            * and **unordered** list 

            1. This is 
            2. an *ordered* list 
            3. with three [numbers](http://number.com)
        """

        self.normal_blocks_out = """<quoteblock>Hello <i>italic</i><br>World<br></quoteblock>
<h3>Header block</h3>
<p>This is a paragraph<br>This is also a paragraph but with <b>bold</b><br>And another <i>paragraph</i><br></p>
<code>
print('Hello World')
print('Something else')
</code>
<ul><li>This is <a href="http://link.com">link</a></li><li>an unordered list</li></ul>
<ul><li>and <i>this</i> is also</li><li>and <b>unordered</b> list</li></ul>
<ol><li>This is</li><li>an <i>ordered</i> list</li><li>with three <a href="http://number.com">numbers</a></li></ol>
"""


    def gets_testable_html_output(self, block):
        html_string = ""
        div_node = markdown_to_html_node(block)
        for parent in div_node.children:
            if parent.tag == "pre":
                pre_children = parent.children
                # Note this completed ignores printing the pre tag in the output
                html_string += pre_children.to_html() + "\n"
            else:
                html_string += parent.to_html() + "\n"
                #                                   ^ this is to make it easier to read
        return html_string

    def test_normal_blocks(self):
        self.assertEqual(self.gets_testable_html_output(self.normal_blocks), self.normal_blocks_out)