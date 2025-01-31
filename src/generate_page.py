
from blocks import markdown_to_html_node, extract_title
import os

def generate_page(from_path,template_path,dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Open the from_path file and read its contents
    from_file = open(from_path,"r")
    from_contents = (from_file.read())
    from_file.close()
    # Open the template file and read its contents
    template_file = open(template_path,"r")
    template_contents = (template_file.read())
    template_file.close()
    # Convert the markdown file to html
    node = markdown_to_html_node(from_contents)
    html = node.to_html()
    title =  extract_title(from_contents)

    template_contents = template_contents.replace("{{ Title }}", title)
    template_contents = template_contents.replace("{{ Content }}", html)

    #Create directories of they do not exist
    os.makedirs(os.path.dirname(dest_path),exist_ok=True)

    #open the dest file and write the replaced title and contents to the dest file
    dest_file = open(dest_path, "w")
    dest_file.write(template_contents)
    dest_file.close()




