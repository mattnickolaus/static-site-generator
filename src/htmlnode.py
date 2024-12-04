from src.textnode import TextNode, TextType

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html must be implemented in subclass")

    def props_to_html(self):
        if self.props is None:
            return ""
        return "".join(map(lambda x: f' {x[0]}="{x[1]}"', self.props.items()))

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")
        if self.children is None:
            raise ValueError("All parent nodes must have children")
        return f"<{self.tag}{self.props_to_html()}>{''.join(map(lambda child: child.to_html(), self.children))}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

# text, text_type, url=None
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT.value:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD.value:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC.value:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE.value:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK.value:
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        case TextType.IMAGE.value:
            return LeafNode(tag="img", value="", props={"src": text_node.url, "alt":text_node.text})
        case _:
            raise Exception("Not a valid text type")
