
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
        


