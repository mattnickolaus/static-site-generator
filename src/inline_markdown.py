from src.textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        raw_text = old_node.text

        # Checks to see if Markdown delimiter appears twice
        delimiter_appears = 0
        for s in raw_text:
            if s == delimiter:
                delimiter_appears += 1
        if delimiter_appears % 2 != 0:
            raise Exception(f"Invalid Markdown Syntax: Missing the a matching '{delimiter}'")

        split_nodes = raw_text.split(delimiter)

        for i in range(len(split_nodes)):
            if split_nodes[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(split_nodes[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(split_nodes[i], text_type))

    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


