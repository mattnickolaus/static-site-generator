from src.textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)

        raw_text = old_node.text

        # Checks to see if Markdown delimiter appears twice
        delimiter_appears = 0
        for s in raw_text:
            if s == delimiter:
                delimiter_appears += 1
        if delimiter_appears % 2 != 0:
            raise Exception(f"Invalid Markdown Syntax: Missing the a matching '{delimiter}'")

        if delimiter not in raw_text:
            raise Exception(f"Delimiter not found:'{delimiter}'")
        split_nodes = raw_text.split(delimiter)
        text_nodes = split_nodes[0::2]
        edited_nodes = split_nodes[1::2]

        match delimiter:
            case "**":
                
            # case "*":

            # case "`":


