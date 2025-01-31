import os
import shutil

def copy_static(src_path, dest_path):
    src_exist = os.path.exists(src_path)
    dest_exist = os.path.exists(dest_path)
    if src_exist == False:
        raise ValueError("Source directory does not exist")
    if dest_exist == False:
        raise ValueError("Destination directory does not exist")
    #delete the destination directory and remake it to ensure it is empty
    shutil.rmtree(dest_path)
    os.mkdir(dest_path)
    #get list of items in src directory
    items = os.listdir(src_path)
    for item in items:
        #create full paths for the source and dest directories
        current_src_path = os.path.join(src_path,item)
        current_dest_path = os.path.join(dest_path,item)
        #check if the src path is a file or directory
        if os.path.isfile(current_src_path):
            # handles case when the path leads to a file
            # copy the file from src to dest
            print(f"Copying file: {current_src_path}")
            shutil.copy(current_src_path,current_dest_path)
        else:
            #handles case when path leads to a directory
            #make the directory in the destination directory
            os.mkdir(current_dest_path)
            #recursively call function with the current src and dest
            print(f"Copying directory: {current_src_path}")
            copy_static(current_src_path,current_dest_path)