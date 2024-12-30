from src.textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        raw_text = old_node.text
        # print(raw_text)

        # Checks to see if Markdown delimiter appears twice
        delimiter_appears = 0
        for s in raw_text:
            if s == delimiter:
                delimiter_appears += 1
        if delimiter_appears % 2 != 0:
            raise Exception(f"Invalid Markdown Syntax: Missing the a matching '{delimiter}'")

        split_nodes = []
        sections = raw_text.split(delimiter)

        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)

    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


# 3.5
def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text

        list_of_image_contents = extract_markdown_images(original_text)

        if list_of_image_contents == []:
            new_nodes.append(old_node)
            continue

        for image_alt, image_link in list_of_image_contents:
            sections = original_text.split(f"![{image_alt}]({image_link})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text

        list_of_link_contents = extract_markdown_links(original_text)

        if list_of_link_contents == []:
            new_nodes.append(old_node)
            continue

        for link_text, link_url in list_of_link_contents:
            sections = original_text.split(f"[{link_text}]({link_url})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text):
    text_node_start = [TextNode(text, TextType.TEXT)]
    bold_nodes = split_nodes_delimiter(text_node_start, "**", TextType.BOLD)
    italic_nodes = split_nodes_delimiter(bold_nodes, "*", TextType.ITALIC)
    code_nodes = split_nodes_delimiter(italic_nodes, "`", TextType.CODE)

    link_nodes = split_nodes_link(code_nodes)
    image_nodes = split_nodes_image(link_nodes)
    return image_nodes


