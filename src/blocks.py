from htmlnode import ParentNode
from inline import text_to_textnodes
from textnode import text_node_to_html_node

def markdown_to_blocks(markdown):
    # Deal with multiple 
    while "\n\n\n" in markdown:
        markdown = markdown.replace("\n\n\n","\n\n")
    
    
    blocks = markdown.split("\n\n")
    block_list = []
    # Check each block to see if it is empty and skip if it is 
    for block in blocks:
        block = block.strip()
        if block != "":
            block_list.append(block)
    return block_list

def block_to_block_type(block):
    lines = block.split("\n")
    # check for heading
    if block.startswith(("# ","## ","### ","#### ","##### ","###### ")):
        return "heading"
    #check for code
    if len(lines)> 0 and (lines[0].startswith("```") and lines[-1].endswith("```")):
        return "code" 
    #check for quote
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">") and line.strip()!= "":
                return "paragraph"
        return "quote"
    #check for unordered list
    if block.startswith("* ") or block.startswith("- "):
        for line in lines:
            if not line.startswith("* ") and not line.startswith("- "):
                return "paragraph"
        return "unordered_list"
    #check for ordered list
    if block.startswith("1. "):
        #count variable
        i = 1
        #loop through all the lines and see if the line starts with a number
        for line in lines:
            if not line.startswith(f"{i}. "):
                return "paragraph"
            i += 1
        return "ordered_list"
    
    return "paragraph"

def markdown_to_html_node(markdown):
    # split the markdown into blocks
    blocks = markdown_to_blocks(markdown)
    children = []
    #loop over each block
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div",children)


#Create text_to_children function
def text_to_children(text):
    #create list of text nodes from 
    text_nodes = text_to_textnodes(text)
    children = []
    #loop through each of the text_nodes and create a html node and append to the children
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def block_to_html_node(block):
    #check block type and call appropriate function
    if block_to_block_type(block) == "heading":
        return heading_to_html_node(block)
    if block_to_block_type(block) == "code":
        return code_to_html_node(block)
    if block_to_block_type(block) == "quote":
        return quote_to_html_node(block)
    if block_to_block_type(block) == "unordered_list":
        return ulist_to_html_node(block)
    if block_to_block_type(block) == "ordered_list":
        return olist_to_html_node(block)
    if block_to_block_type(block) == "paragraph":
        return paragraph_to_html_node(block)
    raise ValueError("Invalid block type")

def paragraph_to_html_node(block):
    #Split the block into lines
    lines = block.split("\n")
    #join the lines into a paragraph
    paragraph = " ".join(lines)
    #create the children
    children = text_to_children(paragraph)
    return ParentNode("p",children)

def code_to_html_node(block):
    #ensure that the block is a code block else raise value error
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    # remove the ``` markers to access code block context
    code_content = block[3:-3].strip()
    children = text_to_children(code_content)
    code = ParentNode("code",children)
    return ParentNode("pre",[code])
    
def quote_to_html_node(block):
    lines = block.split("\n")
    # empty list to keep tack of all quote block contents
    new_lines = []

    for line in lines:
        # If line is empty/whitespace, add it as is
        if line.strip() == "":
            new_lines.append("")
        # If non-empty line doesn't start with >, it's invalid
        elif not line.startswith(">"):
            raise ValueError("Invalid quote block")
        # Otherwise process the quote content
        else:
            new_lines.append(line.strip(">").strip())

    quote_content = "\n".join(new_lines)
    children = text_to_children(quote_content)
    return ParentNode("blockquote",children)

def ulist_to_html_node(block):
    items = block.split("\n")
    new_items = []
    # loop through all the items in the list
    for item in items:
        if not item.startswith("* ") and not item.startswith("- "):
            raise ValueError("Invalid unordered list block")
        #access the list content
        ulist_content = item[2:]
        #Strip excessive whitespace
        ulist_content = ulist_content.strip()
        children = text_to_children(ulist_content)
        new_items.append(ParentNode("li", children))
    return ParentNode("ul",new_items)

def olist_to_html_node(block):
    items = block.split("\n")
    new_items = []
    for item in items:
        #Validate ordered list
        item = item.strip()
        if "." not in item:
            raise ValueError("Invalid ordered list block")
        period_index = item.index(".")

        try :
            int(item[:period_index])
        except:
            raise ValueError("Invalid ordered list block")
        
        #access the content 
        olist_content = item[period_index+1 :].strip()
        children = text_to_children(olist_content)
        new_items.append(ParentNode("li",children))
    return ParentNode("ol",new_items)

def heading_to_html_node(block):
    if not block.startswith("#"):
        raise ValueError("Invalid heading- no #")
    i = 0
    #check how many # characters in the heading
    for char in block:
        if char == "#":
            i += 1
        else:
            break
    if i>6:
        raise ValueError("Invalid heading- too many #")
    # Check for space after #'s
    parts = block.split(maxsplit = 1)
    if len(parts)!= 2:
        raise ValueError("Invalid heading - no content")
    heading_content = parts[1].strip()
    if not heading_content:
        raise ValueError("Invalid heading - no content")
    
    children = text_to_children(heading_content)
    return ParentNode(f"h{i}",children)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    
    raise ValueError("No h1 header")