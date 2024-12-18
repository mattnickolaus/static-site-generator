
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

