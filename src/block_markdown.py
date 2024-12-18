
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
    if block[0] == "#":
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