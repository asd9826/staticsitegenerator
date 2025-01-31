from copystatic import copy_static

import os
import shutil

src_path = "/home/asd98/workspace/github.com/asd9826/staticsitegenerator/static/"
dest_path = "/home/asd98/workspace/github.com/asd9826/staticsitegenerator/public/"

def main():
    copy_static(src_path,dest_path)


main()