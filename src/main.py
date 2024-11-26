from textnode import TextNode

def main():
    bold_node = TextNode("This is a text node", "bold")
    print(bold_node)

    link_node = TextNode("This is a link node", "link", "https://www.boot.dev")
    print(link_node)


main()