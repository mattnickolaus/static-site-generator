import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        example_attributes = {"href": "http://example.com",
                              "target": "_blank"}
        link_node = HTMLNode(tag="a", value="link to:", props=example_attributes)
        expected_output = ' href="http://example.com" target="_blank"'
        self.assertEqual(link_node.props_to_html(), expected_output)


    def test_print_node(self):
        # <h1 class="main-title">Welcome to My Test Page</h1>
        h1_node = HTMLNode(tag="h1", value="Welcome to the Test", props={"class": "main-title"})
        h1_node_print = h1_node.__repr__()

        expected_output = "HTMLNode(h1, Welcome to the Test, None, {'class': 'main-title'})"
        self.assertEqual(h1_node_print, expected_output)



    def test_children_print(self):
        #        <nav>
        #             <ul>
        #                 <li><a href="#section1">Section 1</a></li>
        #                 <li><a href="#section2">Section 2</a></li>
        #             </ul>
        #         </nav>
        a1 = HTMLNode(tag="a", value="Section 1", props={"href": "#section1"})
        list_node1 = HTMLNode(tag="li", children=[a1])
        a2 = HTMLNode(tag="a", value="Section 2", props={"href": "#section2"})
        list_node2 = HTMLNode(tag="li", children=[a2])
        unordered_list_node = HTMLNode(tag="ul", children=[list_node1, list_node2])
        nav_node = HTMLNode(tag="nav", children=[unordered_list_node])

        a1_properties = unordered_list_node.children[0].children[0].props_to_html()
        expected_props = ' href="#section1"'
        self.assertEqual(a1_properties, expected_props)


    def test_nodes_equal(self):
        # <div class="gallery">
        #     <img src="image1.jpg" alt="Image 1" />
        #     <img src="image1.jpg" alt="Image 1" />
        # </div>
        img_node1 = HTMLNode(tag="img", props={"src": "image1.jpg", "alt": "Image 1"})
        img_node2 = HTMLNode(tag="img", props={"src": "image1.jpg", "alt": "Image 1"})
        div_node = HTMLNode(tag="div", children=[img_node1, img_node2], props={"class": "gallery"})

        img1_print = img_node1.__repr__()
        img2_print = img_node2.__repr__()
        self.assertEqual(img1_print, img2_print)

