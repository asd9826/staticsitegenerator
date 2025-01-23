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

def split_nodes_images(old_nodes):
        new_nodes = []
        #loop through the old nodes list
        for old_node in old_nodes:
            # if old node is not text type append and move to next node in old_nodes
            if old_node.text_type != TextType.TEXT:
                new_nodes.append(old_node)
                continue
            # extract the markdown image from the node
            original_text = old_node.text
            images = extract_markdown_images(original_text)
            # if the image tuple is empty append old_node to new_nodes list as is
            if len(images) == 0:
                new_nodes.append(old_node)
                continue
            for image in images:
                sections = original_text.split(f"![{image[0]}]({image[1]})",1)
                # if the section is not split into 2 raise an exception
                if len(sections)!= 2:
                    raise ValueError("Invalid Markdown: image section is not closed")
                # if the first section is not an empty string create a text node 
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0],TextType.TEXT))
                #create the text node for the image
                new_nodes.append(TextNode(image[0],TextType.IMAGE,image[1]))
                # if the section after the image is not an empty string create text node
                original_text = sections [1]
            if original_text != "":
                new_nodes.append(TextNode(sections[1],TextType.TEXT)) 
        return new_nodes
            

def split_nodes_links(old_nodes):
        new_nodes = []
        #loop through the old nodes list
        for old_node in old_nodes:
            # if old node is not text type append and move to next node in old_nodes
            if old_node.text_type != TextType.TEXT:
                new_nodes.append(old_node)
                continue
            # extract the markdown image from the node
            original_text = old_node.text
            links = extract_markdown_links(original_text)
            # if the image tuple is empty append old_node to new_nodes list as is
            if len(links) == 0:
                new_nodes.append(old_node)
                continue
            for link in links:
                sections = original_text.split(f"[{link[0]}]({link[1]})",1)
                # if the section is not split into 2 raise an exception
                if len(sections)!= 2:
                    raise ValueError("Invalid Markdown: link section is not closed")
                # if the first section is not an empty string create a text node 
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0],TextType.TEXT))
                #create the text node for the image
                new_nodes.append(TextNode(link[0],TextType.LINK,link[1]))
                # if the section after the image is not an empty string create text node
                original_text = sections[1]
            if original_text != "":
                new_nodes.append(TextNode(sections[1],TextType.TEXT)) 
        return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern,text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern,text)
    return matches

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes,"**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes,"*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_images(nodes)
    nodes = split_nodes_links(nodes)
    return nodes
