

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
            block = block.strip()
            block_list.append(block)
    return block_list

