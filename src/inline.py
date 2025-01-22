from textnode import TextNode,TextType
import re

def split_nodes_delimiter(old_nodes,delimiter, text_type):
    new_nodes = []
    # loop through the old_nodes list
    for old_node in old_nodes:
        #if node is not text_type return the node as is
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        #if the node is text type split the node text according to the delimiter
        split_node = old_node.text.split(delimiter)
        #check if there is a matching closing delimiter if not raise exception 
        if len(split_node)%2 == 0:
            raise Exception("Invalid Markdown, There is no matching closing delimiter")
        
        for i in range(len(split_node)):
            #Skip empty strings that result from leading/trailing delimiters 
            if split_node[i] == "" and (i == 0 or i == len(split_node)-1):
                continue
            # # Raise an exception for empty segments caused by consecutive delimiters inside the text
            if split_node[i] == "":
                raise Exception("Invalid Markdown: Empty segment between delimiters")
            # Every even index is plain text (TextType.TEXT), odd indices are delimited text (text_type)
            if i % 2 == 0:
                new_nodes.append(TextNode(split_node[i],TextType.TEXT))
            else:
                new_nodes.append(TextNode(split_node[i],text_type))
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern,text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern,text)
    return matches