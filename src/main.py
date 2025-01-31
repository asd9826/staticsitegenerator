from copystatic import copy_static
from generate_page import generate_page

import os
import shutil

stat_path = "./static/"
pub_path = "./public/"
from_path = "./content/index.md"
template_path = "./template.html"
dest_path = "./public/index.html"

def main():
    shutil.rmtree(pub_path)
    os.mkdir(pub_path)
    copy_static(stat_path,pub_path)
    generate_page(from_path,template_path,dest_path)


main()