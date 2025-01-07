from textnode import TextNode, TextType

def main():
    test_object = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(test_object)

main()