from src.htmlnode import HTMLNode, ParentNode
from src.inline_markdown import *
from src.textnode import *

# Accounts for white space before and after a \n (look at boot solution however to see if necessary)
def pre_strip_spaces(markdown):
    pre_split = markdown.split("\n")
    processed_string = ""
    for i in pre_split:
        text_stripped = i.strip()
        processed_string += text_stripped + "\n"

    return processed_string

def markdown_to_blocks(markdown):
    split = pre_strip_spaces(markdown).split("\n\n") # or you can take out the pre_strip_spaces and just include markdown
    edited_blocks = []
    for i in split:
        if i == "":
            continue
        edited_blocks.append(i.strip())
    return edited_blocks

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return "header"
    if block[0:3] == "```" and block[-3:] == "```":
        return "code"

    lines = block.split("\n")
    # no_blank_lines = list(filter(lambda line: line != "", lines))
    # ^ This is not needed as it is handled in the markdown_to_blocks func^

    # filters out lines in the list that contain >
    quote_filtered = list(filter(lambda line: line[0] == ">", lines))
    if lines == quote_filtered:
        return "quote"

    unordered_filtered = list(filter(lambda line: line[0:2] == "* " or line[0:2] == "- ", lines))
    if lines == unordered_filtered:
        return "unordered-list"

    line_number = 0
    ordered_filtered = []
    for line in lines:
        line_number += 1
        prefix = f"{line_number}. "
        if line[0:3] == prefix:
            ordered_filtered.append(line)
    if lines == ordered_filtered:
        return "ordered-list"

    return "paragraph"


def markdown_to_html_node(markdown):
    blocks_list = markdown_to_blocks(markdown)

    all_nodes = []
    for block in blocks_list:
        block_type = block_to_block_type(block)
        parent_node = create_html_parent_node_from_block(block, block_type)
        all_nodes.append(parent_node)
    return ParentNode(tag="div", children=all_nodes)


def create_html_parent_node_from_block(block, block_type):
    match block_type:
        case "header":
            # header -> <h1></h1> (will have to count the number of #)
            header_number = count_headers(block)
            prefix = header_number * "#" + " " # Prefix like "###" used to split
            header_block_value = block.split(prefix)[1] # It's always the second in the split list
            return ParentNode(tag=f"h{header_number}", children=text_to_children(header_block_value))
        case "code":
            code_child = code_block_processing_children(block)
            code_block = ParentNode(tag="code", children=code_child)
            return ParentNode(tag="pre", children=code_block)
        case "quote":
            quote_child = quote_block_processing_children(block)
            return ParentNode(tag="quoteblock", children=quote_child)
        case "ordered-list":
            ordered_child = ordered_block_processing_children(block)
            return ParentNode(tag="ol", children=ordered_child)
        case "unordered-list":
            unordered_list = unordered_block_processing_children(block)
            return ParentNode(tag="ul", children=unordered_list)
        case "paragraph":
            paragraph_child = paragraph_processing_children(block)
            return ParentNode(tag="p", children=paragraph_child)
        case _:
            raise ValueError("Invalid Block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_children.append(html_node)

    return html_children


def count_headers(header_markdown):
    header_prefix = header_markdown.split(" ")[0]
    count = 0
    for c in header_prefix:
        if c == '#':
            count += 1
    if count > 6:
        count = 6
    return count

def code_block_processing_children(block):
    text_between_code_markers = block.split("```")[1]
    code_children = text_to_children(text_between_code_markers)
    return code_children

def quote_block_processing_children(block):
    quote_lines = block.split("\n")

    quote_children = []
    for line in quote_lines:
        if line != "":
            content = line[2:]
            quote_children += text_to_children(content)
            quote_children += [LeafNode(tag="br", value="")]
    return quote_children

def unordered_block_processing_children(block):
    list_lines = block.split("\n")

    list_children = []
    for line in list_lines:
        if line != "":
            content = line[2:]
            list_element = ParentNode(tag="li", children=text_to_children(content))
            list_children.append(list_element)
    return list_children

def ordered_block_processing_children(block):
    includes_number_markers = block.split("\n")
    olist_children = []
    for line in includes_number_markers:
        if line != "":
            content = line[3:]
            list_element = ParentNode(tag="li", children=text_to_children(content))
            olist_children.append(list_element)
    return olist_children

def paragraph_processing_children(block):
    paragraph_lines = block.split("\n")
    paragraph_children = []
    for line in paragraph_lines:
        if line != "":
            paragraph_children += text_to_children(line)
            paragraph_children += [LeafNode(tag="br", value="")]
    return paragraph_children


